package carneLeopardoSistema;

public class CarneLeopardoSistema {
	private final int TAMANHO = 100;
	private Contribuinte[] contribuinte;
	private Tributo[] tributos;
	private int contatorTributos;
	private int contatorContribuintes;


	public CarneLeopardoSistema() {
		this.contribuinte = new Contribuinte[TAMANHO];
		this.tributos = new Tributo[TAMANHO];
		this.contatorTributos = 0;
	}

	public String cadastrarContribuinte(String cpf, String nome) {
		for (Contribuinte c : contribuinte) {
			if (c != null && c.getCpf().equals(cpf)) {
				throw new IllegalArgumentException("Contribuinte já cadastrado!");
			}
		}
		if(contatorContribuintes < TAMANHO) {
			contribuinte[contatorContribuintes] = new Contribuinte(cpf, nome);
			contatorContribuintes++;
		}

		//	    for(int i = 0; i < TAMANHO; i++) {
		//	    	if(contribuinte[i] == null) {
		//	    		contribuinte[i] = new Contribuinte(cpf, nome);
		//	            return contribuinte[i].toString();
		//	    	}
		//	    }//outra opção é add um contator, aí coloco ele com o valor de 0, verifico sempre se ele é menor que o limite, e se for add mais um ao cadastrar
		throw new IllegalStateException("Limite de contribuintes atingido!");

	}

	//	public String[] listarContribuintes() {
	//		String lista = "";
	//		if(contribuinte.length > 0) {
	//			lista += contribuinte.toString();
	//		}
	//		return lista;
	//	}

	public int cadastrarTributo(int codigo, String descricao, double valor, int ano) {
		if(codigo < 1 || codigo > 60) {
			throw new IndexOutOfBoundsException("A faixa disponível\n"
					+ "para códigos tributários é de 1 a 60!");
		}
		for(Tributo t: tributos) {
			if(t != null && codigo == t.getCodigo()) {
				throw new IllegalArgumentException("O código já está sendo utilizado por outro tributo!");
			}
		}
		if(contatorTributos <= TAMANHO) {
			tributos[contatorTributos] = new Tributo(codigo, descricao, valor, ano);
			contatorTributos++;
			return codigo;
		}
		throw new IllegalStateException("Limite de tributos atingido!");

	}

	public String listarTributos() {
		return contribuinte.toString();

	}

	public double reajustrarTributo(int codigo, int ano, double percentual) {
		for(Tributo t: tributos) {
			if(t != null && t.getCodigo() == (codigo)) {
				t.setAno(ano);
				t.setPercentual(percentual);
				return t.getValorTributacao();
			}
		}
		throw new IllegalArgumentException("Tributo não encontrado.");		
	}
	
	//achei + complexo esse método
	public String atribuirTributoAoContribuinte(int codigo, String cpf) {
		// Encontrar o contribuinte no array
		Contribuinte contribuinteA = null;
		for (int i = 0; i < contatorContribuintes; i++) {
			if (contribuinte[i] != null && contribuinte[i].getCpf().equals(cpf)) {
				contribuinteA = contribuinte[i];
				break;
			}
		}
		if (contribuinte == null) {
			return "Erro: Contribuinte não encontrado.";
		}

		// Encontrar o tributo no array
		Tributo tributo = null;
		for (int i = 0; i < contatorTributos; i++) {
			if (tributos[i] != null && tributos[i].getCodigo() == codigo) {
				tributo = tributos[i];
				break;
			}
		}
		if (tributo == null) {
			return "Erro: Tributo não encontrado.";
		}

		// Atribuir o tributo ao contribuinte
		try {
			contribuinteA.adicionarTributos(tributo);
			//contribuinte.adicionarTributos(tributo);
			return "Tributo " + codigo + " atribuído ao contribuinte " + cpf;
		} catch (IllegalStateException e) {
			return "Erro: O contribuinte já atingiu o limite de tributos.";
		}
	}

	public String pagarTributo(String cpf) {
	    for (int i = 0; i < contribuinte.length; i++) {
	        if (contribuinte[i] != null && contribuinte[i].getCpf().equals(cpf)) {
	            contribuinte[i].pagarTributos();
	            return "Todos os tributos do contribuinte " + cpf + " foram pagos.";
	        }
	    }
	    return "Erro: Contribuinte não encontrado.";
	}


	public String emitirExtratoDeTributos(String cpf) {
	    for (int i = 0; i < contribuinte.length; i++) {
	        if (contribuinte[i] != null && contribuinte[i].getCpf().equals(cpf)) {
	            return contribuinte[i].extratoTributos();
	        }
	    }
	    return "Erro: Contribuinte não encontrado.";
	}


	public double totalPagoEmTributos(String cpf, int ano) {
	    for (int i = 0; i < contribuinte.length; i++) {
	        if (contribuinte[i] != null && contribuinte[i].getCpf().equals(cpf)) {
	            return contribuinte[i].totalPago(ano);
	        }
	    }
	    return 0.0; // Se o contribuinte não for encontrado, retorna 0.
	}








}
