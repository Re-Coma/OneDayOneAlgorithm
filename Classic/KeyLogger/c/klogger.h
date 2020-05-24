/*
   방향키는 <> 대체, 백스페이스는 -로 대체 (백준 5397번 기준)
*/

// Stack Data
struct char_stack_data 
{
	char data;
	struct char_stack_data* next_link;
	struct char_stack_data* prev_link;
};

struct char_stack 
{
	struct char_stack_data* start_head;
	struct char_stack_data* end_head;
	int length; //길이
};

// Stack Functions;
void char_stack_init(struct char_stack* stack); 
void char_stack_push(struct char_stack* stack, char data); 
char char_stack_pop(struct char_stack* stack);

// 데이터 정보
struct klog_info 
{
	char* inputed_str; // 입력된 문자열
	struct char_stack ready_stack; //결과 문자열로 출력될 스택
	struct char_stack back_stack; // prev Stack

};

// keylogger Functions
void klog_info_init(struct klog_info* klogger);
void klog_info_push_str(struct klog_info* klogger, char* new_str);
char* klog_info_reslove(struct klog_info* klogger);
char* klog_info_process(char* str);
