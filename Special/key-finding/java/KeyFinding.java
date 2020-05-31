import java.util.ArrayList;
import java.lang.Math;

public class Main {
	
	/**
	  Data Setting
	  Key
		0 = B#, C
		1 = C#, Db
		2 = D
		3 = D#, Eb
		4 = E, Fb
		5 = E#, F
		6 = F#, Gb
		7 = G
		8 = G#, Ab
		9 = A
		10 = A#, Bb
		11 = B, Cb
	Octave Range = -6 ~ +6
	Duration Range = 1/64 ~ 4
	 **/

	public enum KEY {

		C(0), B_SHARP(0),
		C_SHARP(1), D_FLAT(1),
		D(2),
		D_SHARP(3), E_FLAT(3),
		E(4), F_FLAT(4),
		E_SHARP(5), F(5),
		F_SHARP(6), G_FLAT(6),
		G(7),
		G_SHARP(8), A_FLAT(8),
		A(9),
		A_SHARP(10), B_FLAT(10),
		B(11), C_FLAT(11);

		public int val;
		KEY(int val) {
			this.val = val;
		}

	}

	static class Note {
	/*
	   음표 클래스 (예외처리 제외)
	   @param
			int key; 음높이
			int octave; 옥타브 높이
			float duration; 음표 길이

		@function
		 generator(int key, int octave, float duration);
		 getKey, getOctave, getDuration
		 setKey(int key), setOctave(int octave), setDuration(float duration);
	*/
		private int key;
		private int octave;
		private float duration;

		public Note(int key, int octave, float duration) {
			this.key = key;
			this.octave = octave;
			this.duration = duration;
		}
		public int getKey() { return this.key; }
		public int getOctave() { return this.octave; }
		public float getDuration() { return this.duration; }

		public void setKey(int key) { this.key = key; }
		public void setOctave(int octave) { this.octave = octave; }
		public void setDuration(float duration) { this.duration = duration; }
			
	}
	static class Chord {
		/*
		   코드 클래스(Maj, Min만)
		*/
		private int key;
		private boolean isMajor;

		public Chord(int key, boolean isMajor) {
			this.key = key;
			this.isMajor = isMajor;
		}
		public int getKey() { return this.key; }
		public boolean getIsMajor() { return this.isMajor; }

		public void setKey(int key) { this.key = key; }
		public void setIsMajor(boolean isMajor) { this.isMajor = isMajor; }
	}

	// 메이저 마이너 테이블
	public static double[] majorTable = {6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88};
	public static double[] minorTable = {6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17};

	static public Chord findKey(ArrayList<Note> melody) {
		// Algorithm
		
		// C부터 B 까지 12음계의 분포도 조사
		double[] melodyHistogram = new double[12];

		for(Note note : melody)
			melodyHistogram[note.getKey()] = note.getDuration();


		// Get Avg from majorTable and minorTable
		double majorTableAvg = 0.0;
		double minorTableAvg = 0.0;
		double melodyHistogramAvg = 0.0;

		for(int i = 0; i < 12; i++)
			majorTableAvg += majorTable[i];
		majorTableAvg /= 12;

		for(int i = 0; i < 12; i++)
			minorTableAvg += minorTable[i];
		minorTableAvg /= 12;

		// get Avg melody histogram
		for(int i = 0; i < 12; i++)
			melodyHistogramAvg += melodyHistogram[i];
		melodyHistogramAvg /= 12;

		// 메이저 마이너 상관계수
		double majorCoefficientTable[] = new double[12];
		double minorCoefficientTable[] = new double[12];

		// 메이저부터 구하기
		for(int i = 0; i < 12; i++) {

			double value = 0.0;
			// 피어슨 상관계수 공식 참고
			// value = a/ (b*c)^(1/2)
			double a = 0.0;
			double b = 0.0;
			double c = 0.0;

			for(int j = 0; j < 12; j++) {
				a += ((melodyHistogram[(i+j)%12] - melodyHistogramAvg) * (majorTable[j] - majorTableAvg));
				b += Math.pow((melodyHistogram[(i+j)%12] - melodyHistogramAvg), 2);
				c += Math.pow((majorTable[j] - majorTableAvg), 2);
			}
			value = a/( Math.sqrt(b*c));
			majorCoefficientTable[i] = value;
		}

		// 마이너 구하기
		for(int i = 0; i < 12; i++) {
			double value = 0.0;
			double a = 0.0;
			double b = 0.0;
			double c = 0.0;

			for(int j = 0; j < 12; j++) {
				a += ((melodyHistogram[(i+j)%12] - melodyHistogramAvg) * (minorTable[j] - minorTableAvg));
				b += Math.pow((melodyHistogram[(i+j)%12] - melodyHistogramAvg), 2);
				c += Math.pow((minorTable[j] - minorTableAvg), 2);
			}
			value = a/(Math.sqrt(b*c));
			minorCoefficientTable[i] = value;
		}

		// 최대값 구하기
		double max = majorCoefficientTable[0];
		int maxIndex = 0;
		for(int i = 1; i < 12; i++) {
			if(max < majorCoefficientTable[i]) {
				maxIndex = i;
				max = majorCoefficientTable[i];
			}
		}

		double majMaxValue = max;
		// Major
		Chord maxMajor = new Chord(maxIndex, true);

		// 마이너 최대값 구하기
		max = minorCoefficientTable[0];
		maxIndex = 0;
		for(int i = 1; i < 12; i++) {
			if(max < minorCoefficientTable[i]) {
				maxIndex = i;
				max = minorCoefficientTable[i];
			}
		}


		// PrintResult
		System.out.println("=====Major===== =====Minor====");
		for(int i = 0; i < 12; i++) {
			System.out.println(String.format("%d: %.8f\t | %d:  %.8f", 
						i, majorCoefficientTable[i], i, minorCoefficientTable[i]));
		}

		double minMaxValue = max;
		Chord maxMinor = new Chord(maxIndex, false);

		if(minMaxValue > majMaxValue)
			return maxMinor;
		else
			return maxMajor;
	}

	static public void main(String[] args) {

		// Melody List
		ArrayList<Main.Note> melody = new ArrayList<>();

		// Melody input
		melody.add(new Main.Note(Main.KEY.G.val, 2, 1));
		melody.add(new Main.Note(Main.KEY.G.val, 2, 1));
		melody.add(new Main.Note(Main.KEY.A.val, 2, 1));
		melody.add(new Main.Note(Main.KEY.B.val, 2, 1));
		melody.add(new Main.Note(Main.KEY.G.val, 2, 1));
		melody.add(new Main.Note(Main.KEY.B.val, 2, 1));
		melody.add(new Main.Note(Main.KEY.A.val, 2, 1));
		melody.add(new Main.Note(Main.KEY.D.val, 2, 1));

		Chord result = findKey(melody);
		if(result.getIsMajor())
			System.out.println("Major");
		else
			System.out.println("Minor");

		System.out.println(result.getKey());

	}
}
