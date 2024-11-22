import java.util.Scanner;

/**
 * Laboratorio de Programacao 2 - Lab 1
 * 
 * @joycevnr
 */

public class ResultadosDeProva {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int maior = -1;
        int menor = 1001;
        int soma = 0;
        int contador = 0;
        int acima = 0;
        int abaixo = 0;

        while (true) {

            String linha = scanner.nextLine();

            if (linha.equals("-")) {
                break;
            }

            String[] dados = linha.split(" ");
            int nota = Integer.parseInt(dados[1]);

            soma += nota;
            contador++;

            // maior e menor nota
            if (nota > maior) {
                maior = nota;
            }
            if (nota < menor) {
                menor = nota;
            }

            // alunos acima e abaixo de 700
            if (nota >= 700) {
                acima++;
            } else {
                abaixo++;
            }
        }
        // Média
        int mediaTruncada = (int) (soma / contador);

        // resultados
        System.out.println("maior: " + maior);
        System.out.println("menor: " + menor);
        System.out.println("media: " + mediaTruncada);
        System.out.println("acima: " + acima);
        System.out.println("abaixo: " + abaixo);

    }
}
