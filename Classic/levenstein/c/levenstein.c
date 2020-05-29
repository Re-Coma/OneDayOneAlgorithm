#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>
#include <stdarg.h>
#include <string.h>

// 가장 작은 정수 찾기
int get_min_value(int a, int b, int c)
{
	int tmp = a;
	if(tmp > b)
	{
		tmp = b;
		if(tmp > c)
			tmp = c;
	}
	else
	{
		if(tmp > c)
			tmp = c;
	}
	return tmp;
}

int levenstein(const char* str01, const char* str02)
{
	register int i = 0, j = 0;
	int lev_list[strlen(str01) + 1][strlen(str02) + 1];


	//initialize

	for(i = 0; i <= strlen(str01); i++)
		for(j = 0; j <= strlen(str02); j++)
			lev_list[i][j] = 0;

	for(i = 0; i <= strlen(str01); i++)
		lev_list[i][0] = i;
	for(i = 0; i <= strlen(str02); i++)
		lev_list[0][i] = i;

	//calculate
	for(i = 1; i <= strlen(str01); i++)
	{
		for(j = 1; j <= strlen(str02); j++)
		{
			//equal
			if(str01[i-1] == str02[j-1])
				lev_list[i][j] = lev_list[i-1][j-1];
			//nonequal
			else
				lev_list[i][j] = get_min_value(lev_list[i-1][j], lev_list[i][j-1], lev_list[i-1][j-1]) + 1;
		}
	}

	// print 
	for(i = 0; i <= strlen(str01); i++)
	{
		for(j = 0; j <= strlen(str02); j++)
			printf("%d ", lev_list[i][j]);
		printf("\n");
	}

	return lev_list[strlen(str01)][strlen(str02)];
}

int main(void)
{

	char str01[100] = {0, };
	char str02[100] = {0, };

	printf("str01: ");
	fgets(str01, 100, stdin);

	printf("str02: ");
	fgets(str02, 100, stdin);

	str01[strlen(str01) - 1] = '\0';
	str02[strlen(str02) - 1] = '\0';

	printf("01: %s\n", str01);
	printf("02: %s\n", str02);
	printf("result: %d\n", levenstein(str01, str02));
	return 0;
}
