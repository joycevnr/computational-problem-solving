import java.util.Scanner;

public class MaiorQueMedia {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
 
        String linha = scanner.nextLine();
        String[] palavras = linha.split(" ");
        int[] numeros = new int[palavras.length];

        int soma = 0;
        for (int i = 0; i < palavras.length; i++) {
            numeros[i] = Integer.parseInt(palavras[i]);
            soma += numeros[i];
        }
        
        double media = soma / (double) numeros.length;
        
        String resultado = "";
        for (int num : numeros) {
            if (num > media) {
                resultado += num + " ";
            }
        }
        
        System.out.println(resultado.trim());
    }
}
