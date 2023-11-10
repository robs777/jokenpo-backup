import random

from time import sleep


# Função Principal

def main():    
    while True:
        print("-="*15)
        print("Jokenpo")
        print("-="*15)
        print("Vamos jogar?")
        us_digit= input("digite sim ou não: ")
        print("-"*30)

        if  us_digit == "sim":
           modo_jogo()
            
        elif us_digit == "não":
            print("Que pena, nos vemos em breve!")
            break
        
        else:
            print(f"opção {us_digit} invalida. Digite apenas sim ou não")
      

# Menu modo de jogo

def modo_jogo():
    while True:
        print ("Normal (1)")
        print("Necessito de confiança (2)")
        print("A soberba precede a queda (3)")

        jogador = input("Escolha o modo do jogo: ")
        if jogador == "1":
            return modo_jogo1()
        elif jogador == "2":
            return modo_jogo2()
        elif jogador == "3":
            return modo_jogo3()     
        else:
            print ("Escolha inválida. Por favor digite 1, 2 ou 3")

# Modos de Jogo

def modo_jogo1():
    j = obter_escolha_usuario()
    c = gerar_escolha_computador()
    determinar_vencedor(j,c)
    print("-"*30)
    jogar_novamente()

def modo_jogo2():
    j = obter_escolha_usuario2()
    c = gerar_escolha_computador2(j)
    print("-"*30)
    print("Escolha do computador:" + c)
    determinar_vencedor2()
    print("-"*30)
    jogar_novamente()

def modo_jogo3():
    j = obter_escolha_usuario3()
    c = gerar_escolha_computador3(j)
    print("-"*30)
    print("Escolha do computador:" + c)
    determinar_vencedor3()
    print("-"*30)
    jogar_novamente()

# Funções do Modo de Jogo 1

def obter_escolha_usuario():
    while True:
        print("-"*30)
        jogador = input("Escolha: pedra (1), papel(2) ou tesoura(3): ")

        if jogador == "1":
            return "pedra"
        elif jogador == "2":
            return "papel"
        elif jogador == "3":
            return "tesoura"
        else:
            print ("Escolha inválida. Por favor digite 1, 2 ou 3")

def gerar_escolha_computador():
    print("-"*30)
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO")

    jogo = ["Pedra", "Papel", "Tesoura"]
    computador = random.randint(0,2)    
    print ("Escolha do computador:{}".format(jogo[computador]))
    return computador

def determinar_vencedor(j, c):
    if j == "pedra":
        if c == 0:
            print ("Empate")
        elif c == 1:
            print ("O computador ganhou")
        elif c == 2:
            print("Parabéns. Você ganhou")
            
    elif j == "papel":
        if c == 0:
            print ("Parabéns. Você ganhou")
        elif c == 1:
            print ("Empate")
        elif c == 2:
            print("O computador ganhou")
    
    elif j == "tesoura":
        if c == 0:
            print ("O computador ganhou")
        elif c == 1:
            print ("Parabéns. Você ganhou")
        elif c == 2:
            print("Empate")

# Jogar novamente

def jogar_novamente():
    while True:
        print("Deseja jogar novamente?")
        jogador = input("Digite sim ou não: ")
        print("-"*30)
        if jogador == "sim":
            return modo_jogo()
        
        elif jogador == "não":
            return print("Que pena, nos vemos em breve!"), exit() 
        else:
            print ("Escolha inválida. Por favor digite sim ou não")

        
# Funções do Modo de Jogo 2

def obter_escolha_usuario2():
    while True:
        print("-"*30)
        jogador = input("Escolha: pedra (1), papel(2) ou tesoura(3): ")
        if jogador == "1":
            return "pedra"
        elif jogador == "2":
            return "papel"
        elif jogador == "3":
            return "tesoura"
        else:
            print ("Escolha inválida. Por favor digite 1, 2 ou 3")

def gerar_escolha_computador2(jogador):
    print("-"*30)
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO")

    if jogador == "pedra":
        return "Tesoura"
    
    elif jogador == "papel":
        return "Pedra"
    
    elif jogador == "tesoura":
        return "Papel"
    
def determinar_vencedor2():
    print("Parabens Campeão. Você ganhou.")

# Funções do Modo de Jogo 3

def obter_escolha_usuario3():
    while True:
        print("-"*30)
        jogador = input("Escolha: pedra (1), papel(2) ou tesoura(3): ")
        if jogador == "1":
            return "pedra"
        elif jogador == "2":
            return "papel"
        elif jogador == "3":
            return "tesoura"
        else:
            print ("Escolha inválida. Por favor digite 1, 2 ou 3")
    
def gerar_escolha_computador3(jogador):
    print("-"*30)
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO")

    if jogador == "pedra":
        return "Papel"

    elif jogador == "papel":
        return "Tesoura"
    
    elif jogador == "tesoura":
        return "Pedra"

def determinar_vencedor3():
    print("Senta e chora que você perdeu.") 

# Main

if __name__=="__main__":
    main()