# Documentação da API

Documentação de uso da API.

Api criada para solicitação de um cartão de crédito e analise de crédito.

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