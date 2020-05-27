function getPi(pattern) { //pi값 구하기

	var curPoint = 0; // pattern을 순회하는 커서
	var equalPoint = 0; // 일치할 때마다 증가하는 커서

	// 리턴할 pi 배열
	var piArr = new Array();

	// init pi array
	for(var i = 0; i < pattern.length; i++ )
		piArr[i] = 0;
	
	for(curPoint  = 1; curPoint < pattern.length; curPoint++) {

		while((equalPoint > 0) && (pattern[equalPoint] != pattern[curPoint]))
		// 계속 패턴이 일치하다가 갑자기 일치가 안되는 경우, 
		// 일치할 때 까지 equalPoint를 내린다
			equalPoint = piArr[equalPoint- 1];

		if(pattern[equalPoint] == pattern[curPoint])  {
			// 패턴 일치
			equalPoint++;
			piArr[curPoint] = equalPoint;
		}
	}
	return piArr;
}

function kms(targetString, pattern) {

	var indexList = new Array(); //패턴과 일치한 시작 인덱스 지점

	// pattern pi Array
	var patternPiArr = getPi(pattern);

	// pattern cursor
	var patPoint = 0;


	for(var strPoint = 0; strPoint < targetString.length; strPoint++)
	{
		while((patPoint > 0) && (targetString[strPoint] != pattern[patPoint]))
		// 일치하지 않는 경우 getPi와 똑같은 방향으로 patPoint 감소
			patPoint = patternPiArr[patPoint- 1];
		if(targetString[strPoint] == pattern[patPoint])
		{
			// 전부다 일치
			if(patPoint == (pattern.length - 1))
			{
				indexList.push( strPoint - (pattern.length - 1));
				patPoint = patternPiArr[patPoint];
			} else {
				patPoint++;
			}
		}
	}
	return indexList;
}

// Test Function --> read test.txt to string
function getStringFromFile(fileRoot) {
	var fs = require('fs');

	var data = fs.readFileSync(fileRoot).toString();
	return data;
}

// Test Code
var fileData = getStringFromFile('test.txt');
var indexList = kms(fileData, 'banana');
console.log(indexList);
