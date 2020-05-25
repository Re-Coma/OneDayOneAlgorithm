package bfs;

import java.util.LinkedList;

public class Graph {
	protected int size;
	protected LinkedList<Integer> adjList[]; //인접 리스트
	/*
	   adjList[i] --> i번째 노드
	   adjList[i].get[j] --> i번째 노드에 인접한 j
	*/

	// constructor
	public Graph(int maxSize){
		// over 2
		this.size = maxSize;
		this.adjList = new LinkedList[maxSize];

		for(int i = 0; i < this.size; i++)
			this.adjList[i] = new LinkedList();
	}
	public void setAdjNode(int startNode, int endNode) {
		this.adjList[startNode].add(endNode);
		this.adjList[endNode].add(startNode);
	}
}
