package split

import "fmt"
import "sort"
import "log"

func split(target string, delimiterList []string, doRemainDelimiter bool) []string {
	/*
		@param
			target: 대상 문자열
			delimiter:  기준 문자열 리스트
			doRemainDelimiter: 

		@return
			result: 분해된 문자열 리스트
	*/
	targetRune := []rune(target)	// target를 rune Slice로 변환
	delimiterListRune := [][]rune{} // delmiiterList를 run Slice로 변환

	result := []string{}	// 분해된 문자열보관
	runeQueue := []rune{}	// Delimiter에서 제외된 문자들을 넣는 큐
							// for문에서 Delimiter를 만나면 queue를 비워서 result에 복사한다.
	
	log.Print("Start: "+target)

	// delimiter가 2개 이상이면 알파벳 순으로 sort정렬
	if len(delimiterList) >= 2 {
		sort.Strings(delimiterList)
	}

	// delimiter 리스트를 rune slice로 변환
	for _, v := range delimiterList {
		delimiterListRune = append(delimiterListRune, []rune(v))
	}

	cursor := 0
	for cursor < len(targetRune) {
		
		// Start Search
		dCursor := 0
		cdIndexList := []int{}	// Delimiter 후보군

		// targetRune의 cursor인덱스에 있는 rune 값과 delimiterListRune에 있는 요소들의 
		// 맨 앞글자가 같은 지 찾기
		for dCursor < len(delimiterListRune) {
			// 첫 글자 값이 delimiter 쪽이 더 높으면 더 이상 search할 이유가 없으므로 
			// break
			if targetRune[cursor] < delimiterListRune[dCursor][0] {
				break
			} else if targetRune[cursor] > delimiterListRune[dCursor][0] {
				// 값이 delimiter 앞글자 보다 더 작으면 같은 값을 찾을 때 까지 skip
				for (dCursor < len(delimiterListRune)) && (targetRune[cursor] > delimiterListRune[dCursor][0]) {
					dCursor += 1
				}
			} else {
				
				// 일치 할 경우
				for (dCursor < len(delimiterListRune)) && (targetRune[cursor] == delimiterListRune[dCursor][0]) {
					cdIndexList = append(cdIndexList, dCursor)
					dCursor += 1
				}
			}
		}


		// 못찾았으면 큐에 글자를 추가하고 커서넘기기
		if len(cdIndexList) == 0 {
			runeQueue = append(runeQueue, targetRune[cursor])
			cursor += 1
			continue
		} else if len(cdIndexList) == 1 &&  len(delimiterListRune[cdIndexList[0]]) == 1 {
			// 하나밖에 없는데 이게 또 글자 길이가 하나밖에 업음
			// Pass
			// runeQueue에 들어있는 데이터 result에 추가
			if len(runeQueue) >= 1 {
				result = append(result, string(runeQueue))
				runeQueue = nil
			}
			if doRemainDelimiter {
				result = append(result, delimiterList[cdIndexList[0]]);
			}
			cursor += 1

		} else {
			// index List에 2개 이상 남아있을 경우
			strLength :=  1 //검색 대상 문자열
			cursor += 1

			for cursor < len(targetRune) && len(cdIndexList) > 1 {

				strLength += 1
				dlCursor := 0 // Delmiter Select Cursor
				
				newCdIdxList := []int{}

				// 이전 길이의 Delimiter 추가
				for len(delimiterListRune[cdIndexList[dlCursor]]) < strLength-1 {
					dlCursor += 1
				}
				newCdIdxList = append(newCdIdxList, cdIndexList[dlCursor])
				dlCursor += 1
				
				for dlCursor < len(cdIndexList) &&
					targetRune[cursor] > delimiterListRune[cdIndexList[dlCursor]][strLength-1] {
					// 값이 같은 걸 계속 찾을 때 까지 진행
					dlCursor += 1
				}
				for dlCursor < len(cdIndexList) &&
					targetRune[cursor] == delimiterListRune[cdIndexList[dlCursor]][strLength-1] {
					newCdIdxList = append(newCdIdxList, cdIndexList[dlCursor])
					dlCursor += 1
				}

				// newCdIdxList의 길이가 하나밖에 없다 == 같은 길이대의 Delimiter가 없다
				// 더이상 찾을 수 없으므로 for문 끝내기
				if len(newCdIdxList) == 1 {
					cdIndexList = newCdIdxList
					break
				} else {
					// 두개 이상인 경우 아직 더 찾아봐야 하므로 cursor 카운터 1올리고 다시 순환
					cdIndexList = newCdIdxList
					cursor += 1
				}
			}
			if len(runeQueue) >= 1 {
				result = append(result, string(runeQueue))
				runeQueue = nil
			}
			if doRemainDelimiter {
				result = append(result, delimiterList[cdIndexList[0]])
			}
		}
	}
	// 남아있는 데이터 체크
	if len(runeQueue) >= 1 {
		result = append(result, string(runeQueue))
	}
	return result
}
func printSplitedArray(target []string) {
	for _, v := range target {
		fmt.Printf("%s:", v)
	}
	fmt.Println("")
}