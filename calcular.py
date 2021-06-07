from random import randint

class Calcular():
    def __init__(self, dificuldade: int) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1: int = self.gerar_valor
        self.__valor2: int = self.gerar_valor
        self.__operacao: int = randint(1,3)
        self.__resultado: int = self.gerar_resultado
    
    @property
    def valor1(self) -> int:
        return self.__valor1
    
    @property
    def valor2(self) -> int:
        return self.__valor2
    
    @property
    def resultado(self) -> int:
        return self.__resultado

    @property
    def gerar_valor(self) -> int:

        if self.__dificuldade == 1:
            return randint(0,10)

        elif self.__dificuldade == 2:
            return randint(0,100)

        elif self.__dificuldade == 3:
            return randint(0,150)

        elif self.__dificuldade == 4:
            return randint(0,200)

        else:
            return randint(0,1000)

    @property
    def gerar_resultado(self) -> int:
        if self.operacao == 'Somar':
            return self.__valor1 + self.__valor2
        elif self.operacao == 'Subtrair':
            return self.__valor1 - self.__valor2
        else:
            return self.__valor1 * self.__valor2
        
    @property
    def operacao(self) -> str:
        if self.__operacao == 1:
            return 'Somar'
        elif self.__operacao == 2:
            return 'Subtrair'
        else:
            return 'Multiplicar'
    
    @property
    def op_simbolo(self) -> str:
        if self.operacao == 'Somar':
            return '+'
        elif self.operacao == 'Subtrair':
            return '-'
        else:
            return '*'
    @property
    def mostra_calc(self):
        print(f'Qual o Resultado {self.valor1} {self.op_simbolo} {self.valor2} = ?')

    def resposta(self, resp: int) -> bool:
        if resp == self.resultado:
            return True
        return False


    def __str__(self) -> str:
        return f'Dificuldade: {self.__dificuldade}\nValor 1: {self.valor1}\nValor 2: {self.valor2}\nOperação: {self.operacao}\nResultado: {self.gerar_resultado}'


if __name__ == "__main__":
    calc: Calcular = Calcular(1)
    print(calc)
