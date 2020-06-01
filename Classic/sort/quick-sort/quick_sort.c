#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <malloc.h>

#define MAX_SIZE 256

struct data_list
{
	int list[MAX_SIZE];
	int size;
};

/* BackEnd Modules  */
void init_data_list(struct data_list* list)
{
	memset(list->list, 0, sizeof(int) * MAX_SIZE); 
	list->size = 0;
}
// add data
int add_data(struct data_list* list, int new_data) 
{
	if( list->size == MAX_SIZE-1)
		return -1;
	else
	{
		list->list[list->size] = new_data;
		list->size++;
		return 0;
	}
}
// print data
void print_data(struct data_list* list)
{
	register int i = 0;
	for(i = 0; i < list->size; i++)
		printf("%d ", list->list[i]);
	printf("\n");
}
// sort algorithm
int make_partition(struct data_list* list, int left, int right)
{
	int pivot = 0;
	int tmp = 0;

	int low = left;
	int high = right;

	// set pivot
	pivot = list->list[left];

	// low high가 교차할 때 까지 반복한다
	while(low < high)
	{
		// low 계산 시작 pivot보다 큰 값이 나올 때 까지의 건너띄기
		while(low <= right && list->list[low] < pivot)
			low++;
		// right 계산 시작
		while(right >= left && list->list[high] > pivot)
			high--;

		if(low < high)
		{
			// swap
			tmp = list->list[low];
			list->list[low] = list->list[high];
			list->list[high] = tmp;
		}
	}
	// 교차 후에
	// high를 pivot 설정
	return high;
}
void quick_sort(struct data_list* list, int left, int right)
{
	// 정렬 대상의 데이터 갯수가 2 이상이어야 작동
	if(left<right) {
		
		int pivot = make_partition(list, left, right);

		// 양쪽으로 나눠서 퀵 소트
		quick_sort(list, left, pivot-1);
		quick_sort(list, pivot+1, right);
	}

}

// ui
void UI(void)
{
	printf("=== Command list ===\n");
	printf("-1: sort\n");
	printf("-2: print\n");
	printf("else: add data\n");
}


/* FrontEnd Modules  */
// input interface
void interface(struct data_list* list, int* cmd)
{
	UI();
	printf(">>> ");
	scanf("%d", cmd);

}


int main(void)
{
	// init buffer;
	int cmd = 0;
	struct data_list list;

	init_data_list(&list);

	while(1)
	{
		interface(&list, &cmd);
		printf("%d\n", cmd);

		switch(cmd)
		{
			case -1: // quick sort
					quick_sort(&list, 0, list.size-1);
				break;
			case -2: // print data
				print_data(&list);
				break;
			default: // add data
				add_data(&list, cmd);
				break;
		}
	}


	return 0;
}

