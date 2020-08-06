#include "heap.h"
#include <stdlib.h>
int heap_init(struct heap* _h)
{
	register int i = 0;
	if(_h == NULL) return 0;
	_h->size = 0;
	for(i = 0; i <= MAX_SIZE; i++)
		_h->data[i] = -1;
	return 1;
}

int heap_add(struct heap* _h, const int _new_data)
{
	register int i = 0;
	register int data_buf = 0;

	int idx = _h->size + 1;
	if(idx > MAX_SIZE)
		return 0;

	// set idx
	_h->data[idx] = _new_data;
	while(idx > 1)
	{
		int parent_idx = idx/2;
		if(_h->data[idx] > _h->data[parent_idx])
		{
			// swap
			data_buf = _h->data[parent_idx];
			_h->data[parent_idx] = _h->data[idx];
			_h->data[idx] = data_buf;
			// change index
			idx = parent_idx;

			continue;
		}
		else
			break;
	}

	_h->size++;
	return 1;
}
int heap_pop(struct heap* _h)
{
	int poped_data;
	int idx = 1;

	if(_h->size == 0)
		return -1;
	// set data
	poped_data = _h->data[1];
	_h->data[1] = _h->data[_h->size];	
	_h->data[_h->size] = -1;
	_h->size--;


	// loop
	while(idx < _h->size)
	{
		int target_idx = 0;
		if(_h->data[idx*2] >= _h->data[idx*2+1])
			target_idx = idx*2;
		else
			target_idx = idx*2+1;
		if(_h->data[idx] < _h->data[target_idx]) //swap
		{
			int tmp = _h->data[idx];
			_h->data[idx] = _h->data[target_idx];
			_h->data[target_idx] = tmp;
			idx = target_idx;
			continue;
		}
		else
			break;



	}

	return poped_data;
}
