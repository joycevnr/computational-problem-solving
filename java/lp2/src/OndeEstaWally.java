import java.util.Scanner;

/**
 * Laboratorio de Programacao 2 - Lab 1
 * 
 * @joycevnr 
 */

public class OndeEstaWally {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        while (true) {
            String ultimoNomeValido = "?";

            String linha = scanner.nextLine();

            String[] nomes = linha.split(" ");

            for (String nome : nomes) {
                if (nome.length() == 5 ) {
                    ultimoNomeValido = nome;
                }
            }
            if (ultimoNomeValido.equals("wally")) {
                break;
            }else System.out.println(ultimoNomeValido);
        }
    }
}
