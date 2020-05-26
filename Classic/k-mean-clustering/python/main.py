from Kmeans import Kmeans
import random

def make_random_data(size, dimension, _max, _min):
	""" Make random data by dimension"""
	ran_list = []
	for i in range(0, size):
		ran_data = []	
		for d in range(0, dimension):
			ran_data.append(random.uniform(_min, _max))
		ran_list.append(ran_data)
	return ran_list


if __name__ == "__main__":
	DIMENSION = 2
	DATA_SIZE =10 
	k = Kmeans(DIMENSION, \
			make_random_data(DATA_SIZE, DIMENSION, -10, 4) + make_random_data(20, DIMENSION, 8, 14))
	result = k(2)
	print(result[0])
