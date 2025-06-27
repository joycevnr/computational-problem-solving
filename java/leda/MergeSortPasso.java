package leda;

import java.util.Arrays;
import java.util.Scanner;

public class MergeSortPasso {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] entrada = sc.nextLine().split(" ");
        int[] array = new int[entrada.length];

        // Converte de String para int.
        for (int i = 0; i < entrada.length; i++) {
            array[i] = Integer.parseInt(entrada[i]);
        }

        // Imprime o array inicial
        System.out.println(Arrays.toString(array));

        // Inicia o processo de ordenação recursiva.
        mergeSort(array, 0, array.length - 1);
    }

    /**
     * Ordena o array recursivamente usando a estratégia "dividir para conquistar".
     */
    public static void mergeSort(int[] array, int inicio, int fim) {
        // Caso recursivo: só divide se o sub-array tiver mais de 1 elemento.
        if (inicio < fim) {
            // Calcula o índice do meio para a divisão.
            int meio = inicio + (fim - inicio) / 2;

            // Ordena a metade da esquerda.
            mergeSort(array, inicio, meio);

            // Ordena a metade da direita.
            mergeSort(array, meio + 1, fim);

            // Junta (merge) as duas metades ordenadas.
            merge(array, inicio, meio, fim);

            // Imprime o resultado da junção (sub-array ordenado).
            System.out.println(Arrays.toString(Arrays.copyOfRange(array, inicio, fim + 1)));

        } else {
            // Caso base: sub-array de 1 elemento. Imprime e retorna.
            System.out.println(Arrays.toString(Arrays.copyOfRange(array, inicio, fim + 1)));
        }
    }

    /**
     * Junta dois sub-arrays ordenados (`inicio..meio` e `meio+1..fim`).
     */
    public static void merge(int[] array, int inicio, int meio, int fim) {
        // Cria um array auxiliar com a cópia do trecho a ser ordenado.
        int[] helper = Arrays.copyOfRange(array, inicio, fim + 1);
        int meioHelper = meio - inicio;

        // Define os ponteiros para as duas metades e para o array original.
        int i = 0;              // i: ponteiro da metade esquerda (no helper)
        int j = meioHelper + 1; // j: ponteiro da metade direita (no helper)
        int k = inicio;         // k: ponteiro de escrita no array original

        // Compara elementos das duas metades e copia o menor para o array original.
        while (i <= meioHelper && j < helper.length) {
            if (helper[i] <= helper[j]) {
                array[k++] = helper[i++];
            } else {
                array[k++] = helper[j++];
            }
        }

        // Copia os elementos restantes da primeira metade, se houver.
        while (i <= meioHelper) {
            array[k++] = helper[i++];
        }

        // Copia os elementos restantes da segunda metade, se houver.
        while (j < helper.length) {
            array[k++] = helper[j++];
        }
    }
}