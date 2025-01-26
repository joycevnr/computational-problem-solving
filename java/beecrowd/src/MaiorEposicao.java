import java.util.Scanner;

public class MaiorEposicao {
	public static void main(String[] args) {
		 //int[] valores = new Array[100];
        Scanner sc = new Scanner(System.in);
        
        int maior = 0;
        int posicao = -1;
        
        for(int i = 0; i < 5; i++){
            int x = sc.nextInt();
            if(x > maior){
                maior = x;
                posicao = i;
            }
        }
        System.out.println(maior);
        System.out.println(posicao+1);
    }
}
