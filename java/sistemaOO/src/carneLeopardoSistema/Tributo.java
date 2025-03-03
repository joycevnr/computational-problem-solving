package carneLeopardoSistema;

import java.util.Objects;

public class Tributo {
	private int codigo;
	private String descricao;
	private double valorTributacao;
	private int ano;
	private double percentual;
	private boolean status;
	
	
	public int getCodigo() {
		return codigo;
	}
	public String getDescricao() {
		return descricao;
	}
	public void setDescricao(String descricao) {
		this.descricao = descricao;
	}
	public double getValorTributacao() {
		return valorTributacao;
	}
	public void setValorTributacao(double valorTributacao) {
		this.valorTributacao = valorTributacao;
	}
	public int getAno() {
		return ano;
	}
	public void setAno(int ano) {
		this.ano = ano;
	}
	public double getPercentual() {
		return percentual;
	}
	public void setPercentual(double percentual) {
		this.percentual = percentual;
	}
	public boolean isStatus() {
		return status;
	}
	public void setStatus(boolean status) {
		this.status = status;
	}
	public Tributo(int codigo, String descricao, double valorTributacao, int ano) {
		this.codigo = codigo;
		this.descricao = descricao;
		this.valorTributacao = valorTributacao;
		this.ano = ano;
		this.percentual = 1;
		this.status = false;
	}
	
	public double calculaValorTributacao() {
		return valorTributacao * percentual;
	}
	
	public void pagar() {
	    this.status = true;
	}

	@Override
	public int hashCode() {
		return Objects.hash(codigo);
	}
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (!(obj instanceof Tributo))
			return false;
		Tributo other = (Tributo) obj;
		return codigo == other.codigo;
	}
	@Override
	public String toString() {
		return "| Tributo " + codigo + " " + descricao + " – Valor: R$" + valorTributacao
				+ "; Ano Base: " + ano + "|";
	}
	
	
	
	
	

}
