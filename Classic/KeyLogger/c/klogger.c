#include <stdlib.h>
#include <malloc.h>
#include <string.h>

#include "klogger.h"
// stack functions
void char_stack_init(struct char_stack* stack) 
{
	stack = (struct char_stack*)malloc(sizeof(struct char_stack));
	memset(stack, 0, sizeof(struct char_stack));
	stack->length = 0;
}
void char_stack_push(struct char_stack* stack, char data)
{
	// make stack data
	struct char_stack_data* new_data = 
		(struct char_stack_data*)malloc(sizeof(struct char_stack_data));
	memset(new_data, 0, sizeof(struct char_stack_data));
	new_data->data = data;
	
	//push on the stack
	if(stack->length == 0)
	{
		stack->start_head = stack->end_head = new_data;
	} 
	else
	{
		stack->end_head->next_link = new_data;
		new_data->prev_link = stack->end_head;
		stack->end_head = new_data;
	}
	stack->length++;
}
char char_stack_pop(struct char_stack* stack)
{
	if(stack->length == 0)
		return 0;
	else
	{
		char poped_data = stack->end_head->data;
		if(stack->length == 1)
		{
			struct char_stack_data* deleted_data = 
				stack->end_head;
			stack->end_head = NULL;
			stack->start_head = NULL;
			free(deleted_data);
		}
		else
		{
			struct char_stack_data* deleted_data = 
				stack->end_head;
			stack->end_head->prev_link->next_link = NULL;
			stack->end_head = stack->end_head->prev_link;
			free(deleted_data);

		}
		stack->length--;
		return poped_data;
	}
}

// Keylogger Functions
void klog_info_init(struct klog_info* klogger)
{
	klogger = (struct klog_info*)malloc(sizeof(struct klog_info));
	memset(klogger, 0, sizeof(struct klog_info));

	char_stack_init(&(klogger->ready_stack));
	char_stack_init(&(klogger->back_stack));
}
void klog_info_push_str(struct klog_info* klogger, char* new_str)
{
	int length = strlen(new_str);
	register int counter = 0;
	klogger->inputed_str = (char*)malloc(length);

	for(counter = 0; counter < length; counter++)
		klogger->inputed_str[counter] = new_str[counter];
}
char* klog_info_reslove(struct klog_info* klogger)
{
	register int counter = 0;
	char* result_str = NULL;

	// checking string
	for(counter < 0; counter < strlen(klogger->inputed_str); counter++)
	{
		switch(klogger->inputed_str[counter])
		{
			case '>': // one step

				if(klogger->back_stack.length != 0)
					char_stack_push(
						&(klogger->ready_stack),
						char_stack_pop(&(klogger->back_stack))
					);
				break;

			case '<': // prev step
				if(klogger->ready_stack.length != 0)
					char_stack_push(
						&(klogger->back_stack),
						char_stack_pop(&(klogger->ready_stack))
					);
				break;

			case '-': // back space
				char_stack_pop(&(klogger->ready_stack));
				break;

			case 0: // ingore null data
				break;
			case '\n':
				break;
			default:
				char_stack_push(&(klogger->ready_stack), klogger->inputed_str[counter]);
				break;
		}
	}

	// merge string
	for(counter = 0; counter < klogger->back_stack.length; counter++)
		char_stack_push(&(klogger->ready_stack), 
				char_stack_pop(&(klogger->back_stack))
		);
	result_str = (char*)malloc(klogger->ready_stack.length + 1);
	memset(result_str, 0, klogger->ready_stack.length + 1);
	result_str[klogger->ready_stack.length] = '\0';

	for(counter = klogger->ready_stack.length - 1; counter >= 0; counter--) {
		result_str[counter] = char_stack_pop(&(klogger->ready_stack));
	}
	return result_str;
}
char* klog_info_process(char* str)
{
	struct klog_info klogger;
	klog_info_init(&klogger);
	klog_info_push_str(&klogger, str);
	return klog_info_reslove(&klogger);
}


