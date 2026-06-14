from quantum_logic import rodar_rodada_quantica
import time

def jogar():
    print("=" * 40)
    print("  BEM-VINDO AO QUANTUM FLIP (MOEDA QUÂNTICA)  ")
    print("=" * 40)
    print("Você está jogando contra um Computador Quântico.")
    print("Regras: A moeda começa em CARA. Quem terminar com CARA ganha.")
    print("-" * 40)

    # Decisão do Humano
    print("O Computador Quântico já fez a jogada dele (em superposição!).")
    print("Sua vez: Você quer virar a moeda ou manter?")
    print("[ 0 ] Manter a moeda como está")
    print("[ 1 ] Virar a moeda")
    
    escolha = int(input("Escolha (0 ou 1): "))
    
    print("\nO Computador Quântico faz sua última jogada...")
    time.sleep(1)
    print("Medindo o estado final da moeda...\n")
    time.sleep(1)
    
    resultado = rodar_rodada_quantica(escolha)
    
    if resultado == '0':
        print("💡 Resultado: CARA!")
        print("🤖 O Computador Quântico GANHOU! (Como sempre...)")
    else:
        print("💡 Resultado: COROA!")
        print("🎉 Você GANHOU! (Você quebrou as leis da física quântica?)")

if __name__ == "__main__":
    jogar()
