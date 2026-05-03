# 📘 Anotações SQL

## 📑 Índice

[Normalização de Dados](#normalização-de-dados)

[1FN Atomicidade](#1fn-atomicidade)

[2FN Dependência](#2fn-dependência)

[3FN Transitividade](#3fn-transitividade)

[Consultas Avançadas](#consultas-avançadas)

[JOIN](#join)

[INNER JOIN](#inner-join)

[LEFT JOIN](#left-join)

[RIGHT JOIN](#right-join)

[FULL JOIN](#full-join)

[Índices](#índices)

[Comando EXPLAIN](#comando-explain)

# Normalização de Dados 

A normalização de dados garante boas práticas na estruturação de tabelas, evitando redundância e inconsistência.

Ela é baseada em três formas normais principais:

## 1FN Atomicidade

📌 Regra:
Cada coluna deve conter valores indivisíveis (atômicos).

📍 Exemplo:

❌ Errado:

Endereço = "Rua X, 123, São Paulo, SP, Brasil"

✅ Correto:

Rua | Número | Cidade | Estado | País

💡 Objetivo: padronização e facilidade de consulta.

## 2FN Dependência

📌 Regra:
Todas as colunas devem depender totalmente da chave primária.

⚠️ Problema comum:

Dependência parcial (quando uma coluna depende só de parte da chave)

💡 Objetivo: evitar redundância em tabelas com chave composta.

## 3FN Transitividade

📌 Regra:
Colunas não-chave devem depender apenas da chave primária, e não de outras colunas.

📍 Exemplo:

❌ Errado:

ID → Cidade → Estado

✅ Correto:

ID → Cidade
Cidade → Estado (em outra tabela)

💡 Objetivo: eliminar dependências indiretas.

# Consultas Avançadas

# JOIN

📌 Definição:
Permite combinar dados de múltiplas tabelas relacionadas.

## INNER JOIN

📌 Retorna:
Apenas registros com correspondência em ambas as tabelas.

INNER JOIN tabela2 
ON tabela1.coluna = tabela2.coluna;

💡 Resumo: interseção entre tabelas.

## LEFT JOIN

📌 Retorna:
Todos os dados da tabela da esquerda + correspondências da direita.

➡️ Sem correspondência → NULL

LEFT JOIN tabela2 
ON tabela1.coluna = tabela2.coluna;

💡 Resumo: “traz tudo da esquerda”.

## RIGHT JOIN

📌 Retorna:
Todos os dados da tabela da direita + correspondências da esquerda.

➡️ Sem correspondência → NULL

RIGHT JOIN tabela2 
ON tabela1.coluna = tabela2.coluna;

💡 Resumo: “traz tudo da direita”.

## FULL JOIN

📌 Retorna:
Todos os registros de ambas as tabelas.

➡️ Sem correspondência → NULL

FULL JOIN tabela2 
ON tabela1.coluna = tabela2.coluna;

💡 Resumo: união completa.

# Índices

📌 Definição:
Índices aceleram consultas ao permitir acesso rápido aos dados.

🧠 Analogia com Excel

## Sem índice:

Busca linha por linha (Ctrl + F / PROCV exato)

## Com índice:

Dados organizados (ex: ordem alfabética)
Busca ocorre apenas em uma parte específica
⚠️ Trade-off

✔️ Vantagem:

Consultas (SELECT) muito mais rápidas

❌ Desvantagem:

Operações de escrita ficam mais lentas:

INSERT

UPDATE

DELETE

## 🛠️ Comando para Criação de índice

CREATE INDEX nome_indice
ON tabela1 (coluna1);

## Comando EXPLAIN

📌 Função:
Mostra detalhes técnicos da execução de uma query.

📊 Informações retornadas:

Quantidade de linhas lidas;

Uso de índices;

Tipo de varredura (scan);

Estratégia de execução;

💡 Comando:

OBS: Deve-se inserir o EXPLAIN sempre antes da query

EXPLAIN SELECT * FROM tabela1;

👉 Essencial para análise de performance.