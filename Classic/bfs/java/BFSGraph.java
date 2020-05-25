package bfs;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Iterator;
import bfs.Graph;

public class BFSGraph extends Graph {
	public BFSGraph(int size) {
		super(size);
	}

	public LinkedList<Integer> bfs(int startNode) {

		// 방문된 리스트
		int currentNode = startNode;
		boolean visitedNodeList[] = new boolean[this.size];
		LinkedList<Integer> readyQueue = new LinkedList();	
		LinkedList<Integer> result = new LinkedList();

		// start Node Setting
		visitedNodeList[startNode] = true;
		readyQueue.add(startNode);
		result.add(startNode);

		while(readyQueue.size() != 0) {
			currentNode = readyQueue.poll();

			// adjusmemt Nodes
			Iterator<Integer> adjNodes = this.adjList[currentNode].listIterator();	
			while(adjNodes.hasNext()) {
				
				// get nodes from adj node list
				int targetNode = adjNodes.next();

				// if node is not yet searched
				if(!visitedNodeList[targetNode]) {
					visitedNodeList[targetNode] = true;
					// add node to queue
					readyQueue.add(targetNode);
					result.add(targetNode);
				}
			}
		}
		return result;
	}
}
