import java.util.ArrayList;
public class Problem21 {
	public static final int LIMIT = 10000;
	public static void main(String[] args) {
		allProperDivisors(LIMIT);
	}
	private static void allProperDivisors(int LIMIT) {
		int[] dict = new int[LIMIT + 1];
		for (int i=2; i <= LIMIT ; i++)   	// for 0, 1 sum of proper divisors is 0
			dict[i] = properDivisors(i);
		System.out.println("sum of amicable numbers:: " + sumOfAmicablePairs(dict));
	}
	private static int properDivisors(int n) {
		int sum=1;    						// '1' is proper divisor for all numbers
		for (int i = 2; i <= Math.sqrt(n); i++) {
				if(n % i != 0) 
					continue;
				if( i != (n/i) ) {
					sum += (i + (n/i) );	
					continue;
				}
				sum += i;
		}
		return sum;
	}
	private static int sumOfAmicablePairs(int[] a) {
		int sum = 0;
		for(int i=2; i < a.length; i++) {
			if(a[i] > LIMIT)
				continue;

			if(i == a[a[i]] && (i != a[i])) { // it shouldn't be the same number. eg.6
				System.out.println(i + "::" + a[i]);
				sum += (a[i] + i);			// add the pair
				a[i] = 0;					// don't add other number in pair twice
			}
		}
		return sum;
	}
}