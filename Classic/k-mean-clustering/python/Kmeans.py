import math
import random

class Kmeans:
	""" 2차원 뿐만 아니라 다차원도 가능 """

	def __init__(self, dimension, init_data_list):
		self.dimension = dimension

		# format of init_data_list
		# [ [1,2,3], [4,5,6], [7,8,9] ]
		for point in init_data_list:
			if len(point) != self.dimension:
				raise Exception("length of one list must be equal to dimension")
		self.data_list = init_data_list


	def add_data(self, new_data):
		if len(new_data) != self.dimension:
			raise Exception("length of data must be equal to dimension")


	def initialize(self, size):
		"""In This Function
		There is atom functions for make k-means

		initialize: make random data of cluster point

		@param : size --> number of how many make cluster
		return type: [[float, float] .... ]"""

		initialize_data_list = []

		# get point of maximun amd minimum
		max_min_list = []

		# make empty max_min_data
		# index 0 is x, index 1 is y...
		for i in range(0, self.dimension):
			init_data = [0, 0]
			max_min_list.append(init_data)

		# set max, min data
		for one_data in self.data_list:
			for idx in range(0, len(one_data)):

				# check min
				if one_data[idx] < max_min_list[idx][0]:
					max_min_list[idx][0] = one_data[idx]

				# check max
				elif one_data[idx] > max_min_list[idx][1]:
					max_min_list[idx][1] = one_data[idx]

		# make random 
		for i in range(0, size):
			ran_point = []
			for dim in range(0, self.dimension):
				ran_data = \
					random.uniform( max_min_list[dim][0], max_min_list[dim][1] )
				ran_point.append(ran_data)
			initialize_data_list.append(ran_point)
				
		return initialize_data_list
	
	def expectation(self, cluster_data_list):
		""" cluster point 
			@param: cluster_data_list = cluster data list

			return: cluster table --> [ [a1, a2, a3], [b1, b2...] ...]
		"""
		cluster_table = []
		# make empty list
		for idx in range(0, len(cluster_data_list)):
			cluster_table.append([])

		for point in self.data_list:

			min_idx = 0
			min_len = 0
			
			# check length about cluster_data_list and point
			for idx in range(0, len(cluster_data_list)):
				cur_len = 0

				# get length
				for dim in range(0, len(cluster_data_list[idx])):
					cur_len += (point[dim] - cluster_data_list[idx][dim]) ** 2

				if idx == 0:
					min_len = cur_len
				# check length
				elif cur_len < min_len:
					min_len = cur_len
					min_idx = idx

			# save index of pointer to cluster table
			cluster_table[min_idx].append(point) 

		return cluster_table
					
	
	def maximization(self, cluster_data_list, \
					cluster_table):
		"""
			update cluster pointes
			@param
				cluster_data_list
				cluster_table: get from expectation
			return updated cluster_data_list
		"""
		updated_cluster_data_list = []

		# get length and insert to updated cluster data list
		for idx in range(0, len(cluster_table)):
			updated_point = []
			# calcaulate average per dimension
			for dim in range(0, self.dimension):
				dim_avg = 0
				for num in range(0, len(cluster_table[idx])):
					dim_avg += cluster_table[idx][num][dim]

				# get avg
				dim_avg = dim_avg / len(cluster_data_list[idx])
				
				# save_at updated point
				updated_point.append(dim_avg)
			updated_cluster_data_list.append(updated_point)
		return updated_cluster_data_list

	def __call__(self, cluster_size):
		""" process function """

		# init cluster data
		cluster_data_list = self.initialize(cluster_size)

		# save to buffer for checing equal
		def copy_cluster_data(src):
			buf = []
			for idx in range(0, len(src)):
				point = []
				for dim in range(0, len(src[idx])):
					point.append(src[idx][dim])
				buf.append(point)

			return buf

		def is_this_equal(prev_cluster, cur_cluster):
			for idx in range(0, len(prev_cluster)):
				for dim in range(0, self.dimension):
					if prev_cluster[idx][dim] != cur_cluster[idx][dim]:
						return False
			return True

			
		# first copy
		cluster_data_buf_list = copy_cluster_data(cluster_data_list)

		# first expectation and maximization
		expectation_table = self.expectation(cluster_data_list)

		# first maximization
		cluster_data_list = self.maximization(cluster_data_list, expectation_table)

		while is_this_equal(cluster_data_buf_list, cluster_data_list) == False:
			cluster_data_buf_list = cluster_data_list
			# expectation
			expectation_table = self.expectation(cluster_data_list)
			# maximization
			cluster_data_list = self.maximization(cluster_data_list, expectation_table)

		return (cluster_data_list, expectation_table)

		
