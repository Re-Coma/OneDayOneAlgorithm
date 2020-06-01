#include <iostream>
#include <vector>
#include <stack>
#include <list>


using namespace std;

class graph
{
private:
	int size; // max size
	vector<vector<bool>> adj_list; //adjusment list
	/*
	   Example
		1 --> 2, 3, 4
		2 --> 1, ...
	*/
	bool all_searched(vector<bool>& visited)
	{
		for(int i = 0; i < visited.size(); i++)
			if(visited[i] == false)
				return false;
		return true;
	}
public:
	graph(const int size)
	{
		this->size = size;
		for(int i = 0; i < size; i++)
			this->adj_list.push_back(vector<bool>(size, false));
	}
	// 연결
	void connect_node(const int node, const int target_node)
	{
		this->adj_list[node][target_node] = true;
		this->adj_list[target_node][node] = true;
	}
	void dfs(const int start_node)
	{
		list<int> visited_to_print; // 결과 출력용
		vector<bool> visited = vector<bool>(this->size, false);
		stack<int, list<int>> visited_stack; //현재 방문한 노드
		// 이 stack은 backtracking할 때마다 가장 맨 앞에 있는 노드를  pop 한다
		int current_node = -1;

		// first
		visited_stack.push(start_node);
		visited[start_node] = true;
		visited_to_print.push_back(start_node);

		// start
		while((!visited_stack.empty()) && !all_searched(visited))
		{
			current_node = visited_stack.top();
			// 인접한 노드  중에 선택
			int next_node = -1;
			for(int i = 0; i < this->adj_list[current_node].size(); i++)
			{
				if(this->adj_list[current_node][i] == true)
				{
					int target_node = i;
					if(!visited[target_node]) //방문 안한 경우
					{
						//방문 안한 노드로 이동
						next_node = target_node;
						visited_stack.push(next_node);
						visited[next_node] = true;
						visited_to_print.push_back(next_node);
						break;
					}
				}
			}
			if(next_node == -1)
				visited_stack.pop();
		}


		// print result
		for(list<int>::iterator iter = visited_to_print.begin();
				iter != visited_to_print.end();
				iter++)
			cout << *iter << " ";
		cout << endl;
	}
};

int main(void)
{
	graph g = graph(5);

	g.connect_node(0, 1);
	g.connect_node(0, 2);
	g.connect_node(1, 2);
	g.connect_node(2, 3);
	g.connect_node(3, 4);
	g.connect_node(0, 4);
	g.connect_node(2, 4);
	g.dfs(0);

	return 0;
}
