import java.lang.Integer;

public class Problem24 {
	private static int count = 0;
    // print N! permutation of the characters of the string s (in order)
    public  static void perm1(String s) { perm1("", s); }
    private static void perm1(String prefix, String s) {
        int N = s.length();
        if (N == 0) {
			count++;
			if(count == 1000000) {
				System.out.println("millionth lex:: " + prefix);
				System.exit(0);
			}
		}
        else {
            for (int i = 0; i < N; i++)
               perm1(prefix + s.charAt(i), s.substring(0, i) + s.substring(i+1, N));
        }

    }


    // swap the characters at indices i and j
    private static void swap(char[] a, int i, int j) {
        char c;
        c = a[i]; a[i] = a[j]; a[j] = c;
    }



    public static void main(String[] args) {
       int N = 10;
       String alphabet = "0123456789";
       String elements = alphabet.substring(0, N);
       perm1(elements);
       System.out.println();
    }
}