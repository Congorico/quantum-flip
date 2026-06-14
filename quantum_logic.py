from qiskit import QuantumCircuit, assemble, Aer
from qiskit.visualization import plot_bloch_multivert

def rodar_rodada_quantica(escolha_humano):
    # Cria um circuito com 1 qubit e 1 bit clássico
    qc = QuantumCircuit(1, 1)
    
    # 1º Turno do Computador Quântico: Coloca a moeda em Superposição (Hadamard)
    qc.h(0)
    
    # 2º Turno do Humano: Se escolher 'virar' (1), aplica a porta X (NOT).
    # Se escolher 'manter' (0), não faz nada (porta Identity).
    if escolha_humano == 1:
        qc.x(0)
    else:
        qc.id(0)
        
    # 3º Turno do Computador Quântico: Aplica outra Hadamard para garantir a vitória
    qc.h(0)
    
    # Medição
    qc.measure(0, 0)
    
    # Executa o simulador
    simulador = Aer.get_backend('qasm_simulator')
    resultado = simulador.run(qc, shots=1).result()
    contagem = resultado.get_counts()
    
    # Retorna o resultado ('0' para Cara, '1' para Coroa)
    return list(contagem.keys())[0]
