public class Main {

	static private int getMinValue(int... values) {
		boolean isFirst = true;
		int tmp = 0;

		for(int value : values) {
			if(isFirst) {
				tmp = value;	
				isFirst = false;
			} else {
				if(tmp > value)
					tmp = value;
			}
		}
		return tmp;
	}

	static public int levenstein(String str01, String str02) {

		int[][] levList = new int[str01.length() + 1][str02.length() + 1];
		/*
		   X {} e x a m p l e
		   {} 
		   e
		   x
		   a
		   m
		*/
		if( (str01.isEmpty()) || (str02.isEmpty()) )
			return -1;

		// initialize
		for(int i = 0; i <= str01.length(); i++)
			levList[i][0] = i;
		for(int i = 0; i <= str02.length(); i++)
			levList[0][i] = i;

		// cacluate
		for(int i = 1; i <= str01.length(); i++) {
			for(int j = 1; j <= str02.length(); j++) {
				// equal
				if( str01.charAt(i-1) == str02.charAt(j-1) )
					levList[i][j] = levList[i-1][j-1];
				// nonequal
				else {
					// get minumum from (i, j-1), (i-1, j), (j-1, i-1)
					levList[i][j] = getMinValue(levList[i][j-1], levList[i-1][j], levList[i-1][j-1]) + 1;
				}
			}
		}

		for(int i = 0; i <= str01.length(); i++) {
			for(int j = 0; j <= str02.length(); j++) {
				System.out.printf("%d ", levList[i][j]);
			}
			System.out.println("");
		}

		return levList[str01.length()][str02.length()];
	}

	public static void main(String args[]) {
		System.out.println(levenstein("microsoft", "ncsoft"));
	}
} 
