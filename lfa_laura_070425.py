# Aluna: Laura Barbosa Henrique
# Matrícula: 2022216981
# Linguagem: Python 3

afd = {
    'q0': {'a': 'q1', 'b': 'q0'},
    'q1': {'a': 'q2', 'b': 'q3'},
    'q2': {'a': 'q4', 'b': 'q5'},
    'q3': {'a': 'q6', 'b': 'q7'},
    'q4': {'a': 'q4', 'b': 'q5'},
    'q5': {'a': 'q6', 'b': 'q7'},
    'q6': {'a': 'q2', 'b': 'q3'},
    'q7': {'a': 'q1', 'b': 'q0'}
}

finais = {'q4', 'q5', 'q6', 'q7'}  # estados finais com borda dupla

def delta(afd, estado, palavra):
    for simbolo in palavra:
        estado = afd[estado][simbolo]
    return estado

palavras = ['ab', 'aba', 'abab', 'aab', 'bbb', 'ababab']

for p in palavras:
    estado_final = delta(afd, 'q0', p)
    resultado = 'aceita' if estado_final in finais else 'rejeita'
    print(f"Palavra '{p}' termina em: {estado_final} → {resultado}")