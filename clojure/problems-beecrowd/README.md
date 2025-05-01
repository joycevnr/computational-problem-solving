# README - Execução de Scripts Clojure

Este repositório contém soluções de problemas do Beecrowd escritas em Clojure. Os arquivos estão no formato de **flat scripts** (sem namespaces) para testes rápidos, mas também é possível organizar como projeto com **Clojure CLI** ou **Leiningen**.

---

## 1. Pré-requisitos

- **Clojure CLI** instalado (comando `clojure`).
    - O Clojure CLI é a ferramenta oficial para executar scripts, gerenciar dependências e automatizar builds em Clojure.
- Opcionalmente, **rlwrap** para edição de linha e histórico no REPL (comando `clj`).

**Instalação do rlwrap (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install rlwrap
```

---
## 2. Resumo dos comandos

| Modo                  | Comando                                         | Quando usar                        |
|-----------------------|-------------------------------------------------|------------------------------------|
| Flat script           | `clojure -M src/arquivo.clj`                    | Sem namespace, teste rápido        |
| Flat script           | `clj    -M src/arquivo.clj`                     | Mesmo que acima, com `rlwrap` REPL |
| Namespace + CLI       | `clojure -M -m meu-namespace.core`              | Projeto organizado com namespace   |
| Leiningen             | `lein run -m meu-namespace.core`                | Projeto com build/deps Gerenciados |

obs.: **Executar script flat sem `-main`** add no final do arquivo?

   ```bash
   echo "2.00" | clojure -M -i src/1002_area_circulo.clj -e "(-main)"
   ;;-i arquivo.clj carrega o arquivo (define a função).
   ;; -e "(–main)" executa a expressão que chama sua função principal.
   ;; basicamente chamo no comando o main
   ```

## 3. Estrutura de arquivos (“flat scripts”)

```bash
problems-beecrowd/
└── src/
    ├── 1002_area_circulo.clj   # flat script exemplo
    ├── 1003_soma_simples.clj   # outro flat script
    └── ...                    # demais soluções
```
---

## 4. Execução de qualquer script (genérico para todos os testes)

### 4.1. Usando `echo` (pipe de entrada)

```bash
# envia a entrada e executa o script
echo "<entrada>" | clojure -M src/<arquivo>.clj
# Exemplo para o problema 1002 (raio = 2.00):
echo "2.00" | clojure -M src/1002_area_circulo.clj
# A saída será: A=12.5664
```

### 4.2. Digitando a entrada manualmente

```bash
clojure -M src/<arquivo>.clj
# digite o valor quando o programa pausar e pressione Enter
```

### 4.3. Usando o launcher `clj`

```bash
echo "<entrada>" | clj -M src/<arquivo>.clj
```
> Se aparecer aviso sobre `rlwrap`, basta ignorar ou instalar o rlwrap. Não afeta a execução.

---

## 5. Organização avançada (namespaces, Clojure CLI e Leiningen)

### 5.1. Clojure CLI com namespaces

1. Estrutura de diretórios conforme namespace:
   ```bash
   problems-beecrowd/
   └── src/
       └── meu_namespace/
           └── core.clj    # namespace: meu-namespace.core
   ```
2. No topo de `core.clj`:
   ```clojure
   (ns meu-namespace.core)
   (:gen-class)

   (defn -main []
     (let [dados (read-line)]
       ;; processa dados
       (println dados)))
   ```
3. Executar via Clojure CLI:
   ```bash
   echo "<entrada>" | clojure -M -m meu-namespace.core
   ```
    - `-M` carrega o classpath padrão.
    - `-m <namespace>` invoca a função `-main`.

### 5.2. Leiningen (opcional)

1. Crie um `project.clj` na raiz:
   ```clojure
   (defproject problems-beecrowd "0.1.0-SNAPSHOT"
     :dependencies [[org.clojure/clojure "1.10.3"]]
     :main meu-namespace.core)
   ```
2. Mantenha o layout em `src/meu_namespace/core.clj`.
3. Execute:
   ```bash
   lein run -m meu-namespace.core
   ```

---

Com este README você pode rodar **qualquer** arquivo em `src/`, seja no formato flat script ou em projetos organizados com namespaces.

