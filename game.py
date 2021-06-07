from calcular import Calcular

def start(pontos):
    pontos: int = 0
    jogar(pontos)

def jogar(pontos: int):
    dificuldade: int = int(input('Qual o nivel de dificuldade [1, 2, 3 e 4]: '))
    calc: Calcular = Calcular(dificuldade)
    calc.mostra_calc
    resultado: int = int(input('Resultado: '))
    if calc.resposta(resultado):
        print('Resposta correta!')
        pontos += 1
    else:
        print('Resposta incorreta!')
        pontos -= 1
    print(f'Você tem {pontos} Ponto(s)')
    continuar: int = int(input('Deseja continuar? [1 - Sim / 0 - Não]: '))
    if continuar:
        jogar(pontos)
    else:
        print('obrigado por participar, Volte sempre!')
    



if __name__ == "__main__":
    start(0)