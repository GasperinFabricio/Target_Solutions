package sintaxes_variaveis_e_fluxo;

public class Fibonacci {

	/*
	 * 
	 * 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor
	 * sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8,
	 * 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado
	 * um número, ele calcule a sequência de Fibonacci e retorne uma mensagem
	 * avisando se o número informado pertence ou não a sequência.
	 *
	 * IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua
	 * preferência ou pode ser previamente definido no código;
	 */
	static int recursiveFibo(int i) {
		if(i == 0 || i == 1) {
			return 1;
		} else {
			return recursiveFibo(i - 2) + recursiveFibo(i - 1);
		}
	}
	static int getFibo(int selectedNumber) {
		boolean check = false;
		for(int i = 0; i < 100; i++) {
			int fiboNum = recursiveFibo(i);
			if(fiboNum == selectedNumber) {
				System.out.println("O número escolhido pertence à sequência " + (i + 1) + " de Fibonacci. ");
				check = true;
			}
		}
		if (!check) {
				System.out.println("Não pertence à sequência Fibonacci.");
			}
		return 0;
		
	}
	
	public static void main(String[] args) {
		int selectedNumber = 8;
		
		getFibo(selectedNumber);
		
	}

}
