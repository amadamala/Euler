import java.util.Vector;
import com.amadamala.timer.*;
 
public class Pairs {
 
	public static void main(String[] args) {
		int sum=0;
		Vector<Integer> pairs = new Vector<Integer>();
		for(int tal=1; tal<10000;tal++) {
			if(p(p(tal)) == tal && p(tal) < 10000 && tal != p(tal))
				if(!pairs.contains(tal)) {
					pairs.add(tal);
				}
		}
		for(int l=0;l<pairs.size();l++)
			sum+=pairs.elementAt(l);
		System.out.println("Sum: " + sum);
	}
 
	static long p(long n) {
		long sum=0;
		for(int m=1;m<n;m++){
			if(n%m == 0)
				sum+=m;
		}
		return sum;
	}
}