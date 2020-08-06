#define MAX_SIZE 128
struct heap
{
	int size;
	int data[MAX_SIZE + 1];
};

int heap_init(struct heap* _h);
int heap_add(struct heap* _h, const int _new_data);
int heap_pop(struct heap* _h);
