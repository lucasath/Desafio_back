# Documentação da API

Documentação de uso da API.

Api criada para solicitação de um cartão de crédito e analise de crédito.

## Como Usar

Para subir o ambiente de desenvolvimento é necessario possuir:

- Python3.6+
- Django3
- Virtualenv Ou Pipenv


Primeiro é necessario preparar o ambiente do projeto

Criando o ambiente da virtualenv

```bash
$ virtualenv --python=python3.8 venv
```

Ative a sua env ou pipenv

```bash
$ source venv/bin/activate
```

Instalando as dependencias do projeto

```bash
(venv)$ pip install -r requirements.txt
```

Agora é necessario adicionar variaveis de ambiente

```bash
(venv)$ export DEBUG="True"
(venv)$ export SECRET_KEY="mysecretkey"
```

Rodando as migrates do django para preparar o seu banco local

```bash
(venv)$ python manage.py migrate
```

Para executar os testes
```bash
(venv)$ python manage.py test
```

Se estiver tudo certo agora é so rodar o projeto
```bash
(venv)$ python manage.py runserver
```


Pronto! agora o ambiente está instalado.

## ENDPOINTS

- [**GET**](#Listar): /api/solicitacoes/
- [**POST**](#Enviar): /api/solicitacoes/
- [**DELETE**](#Deletar): /api/solicitacoes/


## Enviar uma Solicitação

### Enviar

- Endpoint: **/api/solicitacoes/**
- Allowed method: POST

Para enviar uma solicitação deve se enviar os dados a seguir:

*POST*:

Corpo da requisição: JSON

Exemplo:

```JSON
{
	"nome":"joao",
	"renda": "2500",
	"endereco":{
		"pais":"Brasil",
		"estado":"PI",
		"cidade":"Teresina",
		"cep":"64000000",
		"bairro":"Centro",
		"rua":"Joaquim nelson",
		"numero":"2502"
	}
}
```

Resposta:

*status_code*: 201

## Listar Solicitações

### Listar

- Endpoint: **/api/solicitacoes/**
- Allowed method: GET

Para listar todas as solicitações.

Resposta:

*status_code*: 200

## Listar Solicitações por id

- Endpoint: **/api/solicitacoes/`{id}`**
- Allowed method: GET

Para listar todas as solicitações:

Para listar uma solicitação por id deve se adicionar o id referente a solicitação.

Resposta:

*status_code*: 200

## Deletar Solicitações

### Deletar

- Endpoint: **/api/solicitacoes/`{id}`**
- Allowed method: DELETE

Para deletar uma solicitação:

Deve se enviar uma request com o Metodo DELETE passando o id da solictitação na url no campo `{id}`.

Resposta:

*status_code*: 204

