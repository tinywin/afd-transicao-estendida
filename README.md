# Função de Transição Estendida em AFD

Repositório da disciplina **Linguagens Formais e Autômatos (LFA)** – UFT.

## Sobre

Este projeto implementa a **função de transição estendida** `δ(q, w)` de um **Autômato Finito Determinístico (AFD)** em Python.

A função recebe um estado inicial e uma palavra de entrada, e retorna o estado final após processar todos os símbolos da palavra.

Também verifica se a palavra termina em um **estado de aceitação**, com base no AFD fornecido pelo exercício.

## Exemplo de saída
Palavra 'ab' termina em: q3 → rejeita
Palavra 'aba' termina em: q6 → aceita

## Aluna

- **Nome:** Laura Barbosa Henrique  
- **E-mail:** laura.henrique@mail.uft.edu.br

## Como executar
No terminal/bash, execute o seguinte comando:

```bash
python lfa_laura_070425.py
