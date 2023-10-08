import array

class pilha:
    def __init__(self, max:int = 100, tipo:str = 'f'):
        self.data = array.array(tipo)
        self.max = max
        self.len= 0
        

    def pilha_esta_cheia(self):
        return self.len == self.max
    
    def pilha_esta_vazia(self):
        return self.len == 0 
    
    def tamanho(self):
        return self.len
    
    def empilha(self, item):
        if self.len == self.max:
            raise Exception("PilhaCheiaErro")
        
        else:
            try:
                self.data.append(item)
                self.len += 1
            except:
                raise Exception("TipoErro")
    
    def desempilha(self):
        if self.len == 0:
            raise Exception("PilhaVaziaErro")
        
        else:
            self.data.pop()
            self.len += -1

    def troca(self):
        if self.len <2:
            print("requer ao menos dois elementos")
        
        else:
            ultimo = self.data.pop()
            penultimo = self.data.pop()
            self.data.append(ultimo)
            self.data.append(penultimo)

