#include "heap.h"
#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int main(void)
{

	register int i = 0;
	struct heap h;
	heap_init(&h);

	srand((unsigned int)time(NULL));

	for(int i = 0; i < 50; i++)
		heap_add(&h, rand()%100);
	for(int i = 2; i < 51; i++)
		printf("%d ", heap_pop(&h));
	printf("\n");

	return 0;
}
