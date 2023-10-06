import pilha 

def criar(num:int):
    pino = pilha.pilha(num)
    
    for i in range(num):
        pino.empilha(num-i)
    return pino

def mover(A:pilha.pilha, B:pilha.pilha):
     B.empilha(A.data[-1])
     A.desempilha()

class hanoi:
    def __init__(self, num:int):
        self.num = num
        self.inicial = criar(num) 
        self.auxiliar = pilha.pilha(num)
        self.final = pilha.pilha(num)
        self.passos =  0

    def mov_disc(self, mov:int):
        if mov != 0 and self.passos % mov == 0 and self.passos != 2 ** self.num - 1:
            print(self.inicial.data.tolist(), "pino inicial\n", self.auxiliar.data.tolist(), "pino auxiliar\n", self.final.data.tolist(), "pino final\n", "Passos =", self.passos)
            input("favor pressionar [ENTER] para continuar")
            return
        else:
            return

    def resolver(self, Mov = 0 ):    
        print(self.inicial.data.tolist(), "pino inicial\n", self.auxiliar.data.tolist(), "pino auxiliar\n", self.final.data.tolist(), "pino final\n", "Passos =", self.passos)
        input("favor pressionar [ENTER] para continuar")
        def resolver_inter(M, n = self.num, A = self.inicial, B= self.auxiliar, C=self.final):
            if n == 1:
                mover(A, C)
                self.passos += 1
                self.mov_disc(M)
            else:
                resolver_inter(M, n-1, A, C, B)
                mover(A, C)
                self.passos += 1
                self.mov_disc(M)
                resolver_inter(M, n-1, B, A, C)
        resolver_inter(Mov)
        print(self.inicial.data.tolist(), "pino inicial\n", self.auxiliar.data.tolist(), "pino auxiliar\n", self.final.data.tolist(), "pino final\n", "Passos =", self.passos)
        return
