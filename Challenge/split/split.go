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


	log.Print("start: "+target)
	// delimiter가 2개 이상이면 알파벳 순으로 sort정렬
	if len(delimiterList) >= 2 {
		sort.Strings(delimiterList)
	}
	log.Print(delimiterList)

	// delimiter 리스트를 rune slice로 변환
	for _, v := range delimiterList {
		delimiterListRune = append(delimiterListRune, []rune(v))
	}

	cursor := 0
	for cursor < len(targetRune) {
		
		// Start Search
		dCursor := 0
		cdIndexList := []int{}	// Delimiter 후보군
		
		// 값이 delimiter 앞글자 보다 더 작으면 같은 값을 찾을 때 까지 skip
		for (dCursor < len(delimiterListRune)) && (targetRune[cursor] > delimiterListRune[dCursor][0]) {
			dCursor += 1
		}

		// 해당 위치에 같은 값을 골라 cdIndexList에 저장
		for (dCursor < len(delimiterListRune)) && (targetRune[cursor] == delimiterListRune[dCursor][0]) {
			cdIndexList = append(cdIndexList, dCursor)
			dCursor += 1
		}

		// 못찾았으면 큐에 글자를 추가하고 커서넘기기
		if len(cdIndexList) == 0 {
			runeQueue = append(runeQueue, targetRune[cursor])
			cursor += 1
			continue
		} else if len(cdIndexList) == 1 &&  len(delimiterListRune[cdIndexList[0]]) == 1 {
			// Delimiter 하나를 검색했는데 이 Delimiter의 길이가 1이면 result에 데이터를 push하고
			// 맨 위로 다시 돌아간다.
			if len(runeQueue) >= 1 {
				result = append(result, string(runeQueue))
				runeQueue = nil
			}
			if doRemainDelimiter {
				result = append(result, delimiterList[cdIndexList[0]])
			}
			cursor += 1
			continue

		} else {
			strLength :=  1 //검색 대상 문자열
			cursor += 1

			for cursor < len(targetRune) && len(cdIndexList) >= 1 {

				strLength += 1
				dlCursor := 0 // Delmiter Select Cursor
				
				newCdIdxList := []int{}

				// 이전 길이의 Delimiter 추가
				
				if len(delimiterListRune[cdIndexList[dlCursor]]) < strLength-1 {
					dlCursor += 1
				}
				if len(delimiterListRune[cdIndexList[dlCursor]]) == strLength-1 {
					newCdIdxList = append(newCdIdxList, cdIndexList[dlCursor])
					
					dlCursor += 1
				}
				log.Print(newCdIdxList)
				
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
				log.Print(newCdIdxList)
				log.Print(cursor)
				log.Print("======================")

				
				// newCdIdxList의 길이가 하나밖에 없다 == 같은 길이대의 Delimiter가 없다
				if len(newCdIdxList) == 1 {
					if len(delimiterListRune[newCdIdxList[0]]) == strLength-1 {
						log.Print("down")
						cdIndexList = newCdIdxList
						break
					} else {
						cdIndexList = newCdIdxList
						cursor += 1
						continue
					}
				} else if len(newCdIdxList) > 1 {
					// 두개 이상인 경우 아직 더 찾아봐야 하므로 cursor 카운터 1올리고 다시 순환
					cdIndexList = newCdIdxList
					cursor += 1
				} else {
					break
				}
			}

			if len(runeQueue) >= 1 {
				result = append(result, string(runeQueue))
				runeQueue = nil
			}
			if doRemainDelimiter && len(cdIndexList) >= 1 {
				result = append(result, delimiterList[cdIndexList[len(cdIndexList)-1]])
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