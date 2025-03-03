package testes;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import carneLeopardoSistema.Contribuinte;

class ContribuinteTest {
	private Contribuinte contribuinte;


	@BeforeEach
	void setUp() {
		contribuinte = new Contribuinte("21", "Maria");
	}


	@Test
	void test() {
		fail("Not yet implemented");
	}

}
