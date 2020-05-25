package bfs;
import bfs.Graph;
import java.util.LinkedList;
public class Main {
	public static void main(String[] args) {

		BFSGraph g = new BFSGraph(6);

		g.setAdjNode(0, 1);
		g.setAdjNode(0, 2);
		g.setAdjNode(1, 2);
		g.setAdjNode(1, 3);
		g.setAdjNode(3, 4);
		g.setAdjNode(2, 5);

		LinkedList<Integer> result = g.bfs(3);
		
		for(int i = 0; i < result.size(); i++)
			System.out.println(result.get(i));

	}
}
