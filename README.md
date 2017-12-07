# Easydata.edu


### requirements

	javabridge==1.0.15
	matplotlib==2.1.0
	numpy==1.13.3
	pandas==0.20.3
	pyparsing==2.2.0
	python-dateutil==2.6.1
	request==0.0.18
	six==1.11.0
	subprocess32==3.2.7

### rode o projeto

1. Prepare o ambiente virtual
	
	$ pyvenv venv
	$ source venv/bin/activate

2. Instale os pacotes
	
	$ pip install -r requirements.txt

3. Rode os script 

### weka

	$ git clone https://github.com/fracpete/python-weka-wrapper3
	$ cd python-weka-wrapper3
	$ python setup.py install

### explicação dos arquivos

- data-handler.py: script que trata os dados e gera o arquivo final
- data-explorer.py: script para obter informaçoes sobre os dados
- requirements.txt: bibliotecas necessarias para rodas os scripts
- data/
    - Dados_Enem.csv: arquivo passado pela professora Elizabel com informações sobre o Enem
    - Dados_Cotas.csv: arquivo com informaçoes das matriculos dos componentes curriculares 2017.1
    - Dados_Cep.csv: arquivo com informações sobre o cep
    - final-data.csv: arquivo final gerado pelo data-handler.py
- graph/
	- boxplot_media_final.png
	- boxplot_nota_enem.png
	- boxplot_numero_total_faltas.png
	- media_final.png
	- nota_enem.png
	- numero_total_faltas.png
	- situacao.png
- weka/
	- apriori.txt 	

### mudanças feitas nos dados

- separação das colunas de ; para ,
- valores decimais identificados com . e não ,
- removel colunas: 'unidade', 'nota', 'reposicao', 'faltas_unidade'
- ...

### informações sobre os dados

#### colunas

- id: Identificador do registro de um aluno em um componente curricular [id gerado por nós].
- id_discente: Identificador do discente da matrícula.
- sexo: Sexo dos estudantes.
- nota_enem: Nota do enem.
- cotista: Se o estudante é cotista ou não.
- cep: CEP do estudante matriculado.
- descrição: ?.
- id_turma: Identificador da turma do discente.
- id_curso: Identificador do curso do discente.
- media_final: Média final do discente.
- numero_total_faltas: Quantidade total de faltas.
- situacao: Situação da matrícula [APROVADO, APROVADO POR NOTA, DESISTENCIA, CANCELADO, EXCLUIDA, TRANCADO, INDEFERIDO] .


### possibilidades de analise

- Média da nota de cotistas e não cotistas
- Faltas de cotistas e não cotistas
- Situação mais frequente entre cotistas e não cotistas
- Quantas vezes cada Situação acontece entre cotistas e não cotistas
- ...