import java.util.Scanner;

public class CalculadoraComOpcao {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String operador = scanner.nextLine();

        if (!operador.equals("+") && !operador.equals("-") && !operador.equals("*") && !operador.equals("/")) {
            System.out.println("ENTRADA INVALIDA");
        } else {
            double num1 = scanner.nextDouble();
            double num2 = scanner.nextDouble();

            if (operador.equals("+")) {
                System.out.println("RESULTADO: " + (num1 + num2));
            } else if (operador.equals("-")) {
                System.out.println("RESULTADO: " + (num1 - num2));
            } else if (operador.equals("*")) {
                System.out.println("RESULTADO: " + (num1 * num2));
            } else if (operador.equals("/")) {
                if (num2 == 0.0) {
                    System.out.println("ERRO");
                } else {
                    System.out.println("RESULTADO: " + (num1 / num2));
                }
            } else {
                System.out.println("ENTRADA INVALIDA");
            }
        }

        //scanner.close();
    }
}
