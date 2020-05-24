#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <malloc.h>

#include "klogger.h"

#define MAX_BUFFER	128

int main(void)
{
	// Data
	char input[MAX_BUFFER];
	register int counter = 0;

	//test
	struct klog_info key_logger;

	// interface
	while(1)
	{
		memset(input, 0, MAX_BUFFER);
		printf(">>> ");
		fgets(input, MAX_BUFFER, stdin);
		if(strlen(input) >= 1)
			printf("%s\n", klog_info_process(input));

	}
	return 0;
}
