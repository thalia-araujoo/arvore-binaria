class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def insere(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._insere_recursivamente(self.raiz, valor)

    def _insere_recursivamente(self, no_atual, valor):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)
            else:
                self._insere_recursivamente(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            if no_atual.direita is None:
                no_atual.direita = No(valor)
            else:
                self._insere_recursivamente(no_atual.direita, valor)

    def busca(self, valor):
        return self._busca_recursivamente(self.raiz, valor)

    def _busca_recursivamente(self, no_atual, valor):
        if no_atual is None:
            return False
        if valor == no_atual.valor:
            return True
        if valor < no_atual.valor:
            return self._busca_recursivamente(no_atual.esquerda, valor)
        return self._busca_recursivamente(no_atual.direita, valor)

    def altura(self):
        return self._calcula_altura(self.raiz)

    def _calcula_altura(self, no_atual):
        if no_atual is None:
            return 0
        altura_esquerda = self._calcula_altura(no_atual.esquerda)
        altura_direita = self._calcula_altura(no_atual.direita)
        return max(altura_esquerda, altura_direita) + 1

    def nos_internos(self):
        return self._conta_nos_internos(self.raiz)

    def _conta_nos_internos(self, no_atual):
        if no_atual is None:
            return 0
        if no_atual.esquerda or no_atual.direita:
            return 1 + self._conta_nos_internos(no_atual.esquerda) + self._conta_nos_internos(no_atual.direita)
        return 0

    def folhas(self):
        return self._conta_folhas(self.raiz)

    def _conta_folhas(self, no_atual):
        if no_atual is None:
            return 0
        if not no_atual.esquerda and not no_atual.direita:
            return 1
        return self._conta_folhas(no_atual.esquerda) + self._conta_folhas(no_atual.direita)


# Exemplo de uso:
if __name__ == "__main__":
    arvore = ArvoreBinaria()
    numeros = [11, 5, 17, 3, 7, 12, 20]

    for numero in numeros:
        arvore.insere(numero)

    print("Árvore Binária Criada!")
    print("Raiz:", arvore.raiz.valor)
    print("Altura:", arvore.altura())
    print("Nós Internos:", arvore.nos_internos())
    print("Folhas:", arvore.folhas())

    numero_busca = 12
    if arvore.busca(numero_busca):
        print(f"{numero_busca} está presente na árvore.")
    else:
        print(f"{numero_busca} não está presente na árvore.")
