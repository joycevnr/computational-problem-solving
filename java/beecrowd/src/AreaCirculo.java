import java.util.Locale;
import java.util.Scanner;

public class AreaCirculo {
	public static void main(String[] args) {
		final double PI = 3.14159;
		Locale.setDefault(Locale.US); //SE O S.O ESTIVER EM BRA
		Scanner scanner = new Scanner(System.in);
		
		double raio = scanner.nextDouble();
		double area = PI * (Math.pow(raio, 2));
		
		System.out.printf("A=%.4f%n", area);
		
		scanner.close();
		
	}
}