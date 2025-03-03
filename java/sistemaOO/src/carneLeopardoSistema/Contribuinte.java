package carneLeopardoSistema;

import java.util.Objects;

public class Contribuinte {
	private String cpf;
	private String nome;
	private String contato;
	private Tributo[] tributos;
    private int totalTributos; 
	
	
	public String getCpf() {
		return cpf;
	}
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public String getContato() {
		return contato;
	}
	public void setContato(String contato) {
		this.contato = contato;
	}
	
	
	public Contribuinte(String cpf, String nome) {
		if(cpf == null || cpf.trim().isEmpty() || nome == null || nome.trim().isEmpty()) {
			throw new IllegalArgumentException("Valor inválido");
		}
		this.cpf = cpf;
		this.nome = nome;
		this.tributos = new Tributo[10];
		this.totalTributos = 0;
		//this.contato = contato;
	}
	
	
	public void adicionarTributos(Tributo tributo) {
		if(totalTributos < tributos.length) {
			tributos[totalTributos] = tributo;
            totalTributos++;
		}else {
			throw new IllegalStateException("O contribuinte já tem o máximo de tributos permitidos.");
		}
		
	}
	// Método para adicionar tributo
//	public void adicionarTributo(Tributo tributo) {
//	    if (quantidadeTributos >= 10) {
//	        throw new IllegalStateException("Contribuinte já possui 10 tributos.");
//	    }
//	    this.tributos[quantidadeTributos] = tributo;
//	    quantidadeTributos++;
//	}
//	
	// Método para pagar tributos
	public void pagarTributos() {
	    for (int i = 0; i < totalTributos; i++) {
	        tributos[i].pagar(); // Marca tributo como pago
	    }
	}

	// Método para calcular total pago por ano
	public double totalPago(int ano) {
	    double total = 0;
	    for (int i = 0; i < totalTributos; i++) {
	        if (tributos[i].getAno() == ano && tributos[i].isStatus()) {
	            total += tributos[i].getValorTributacao();
	        }
	    }
	    return total;
	}

	// Método para gerar extrato
	public String extratoTributos() {
	    StringBuilder extrato = new StringBuilder("Extrato de tributos:\n");
	    for (int i = 0; i < totalTributos; i++) {
	        extrato.append(tributos[i].toString()).append("\n");
	    }
	    return extrato.toString();
	}

	
	
	
	@Override
	public int hashCode() {
		return Objects.hash(cpf);
	}
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (!(obj instanceof Contribuinte))
			return false;
		Contribuinte other = (Contribuinte) obj;
		return Objects.equals(cpf, other.cpf);
	}
	@Override
	public String toString() {
		return "Contribuinte: " + nome + " - CPF: " + cpf + " - Contato: " + contato + "||\n";
	}
	
	
	
	
	

}
