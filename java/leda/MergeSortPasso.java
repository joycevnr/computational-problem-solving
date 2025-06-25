package leda;
import java.util.Scanner;

public class MergeSortPasso {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String entrada = sc.nextLine();
        String[] elementos = entrada.split(" ");
        int[] lista = new int[elementos.length];

        for (int i = 0; i < elementos.length; i++) {
            lista[i] = Integer.parseInt(elementos[i]);
        }
        mergeSort(lista, 0, lista.length);
    }

    public void mergeSort(int[] v, int ini, int fim){
        if(ini < fim){
            int meio = (ini + fim) / 2;
            mergeSort(v, ini, meio);
            mergeSort(v, meio+1, fim);
            merge(v, ini, fim);
        }
    }



    public void merge(int[] v, int ini, int fim){
        int[] helper = new int[v.length];

        for(int i = 0; i < v.length; i++){
            helper[i] = v[i];
        }
        int i = ini; //primeira metade
        int meio = (ini + fim) / 2; //pivot
        int k = ini; //posições do array
        int j = ini + 1;//segunda metade
        while(ini <= meio && j <= fim) {
            if(helper[i] <= helper[j])
                v[k++] = helper[i++];
            else
                v[k++] = helper[j++];
        }
        while(ini <= meio){//add o restante da primeira parte se sobrar
            v[k++] = helper[i++];
        }
    }
}
