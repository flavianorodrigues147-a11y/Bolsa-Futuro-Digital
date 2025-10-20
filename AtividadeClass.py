# Sistema de Biblioteca
# Autor: Flaviano Rodrigues

class Livro:
    # nao preciso passar o disponivel pq ele sempre vai ser true quando criar o livro
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True  # para saber se o livro esta disponivel ou nao

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False  # se o livro estiver disponivel, ele empresta
            return True  # se o livro for emprestado, ele retorna true
        return False  # se o livro nao estiver disponivel, ele nao empresta

    def devolver(self):
        self.disponivel = True  # devolve o livro, ou seja, torna ele disponivel

    def exibir_info(self):
        # verifica se o livro esta disponivel ou nao

        if self.disponivel:
            status = "Sim"  # se estiver disponivel, status é sim
        else:
            status = "Não"
        return print(f"Título: {self.titulo}, Autor: {self.autor}, Disponível: {status}")


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []  # lista de livros emprestados pelo usuario

    def emprestar_livro(self, livro):
        if livro.emprestar():  # tenta emprestar o livro
            # adiciona o livro na lista de emprestados
            self.livros_emprestados.append(livro)
            return True
        return False  # se nao conseguir emprestar, retorna false

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:  # verifica se o livro esta na lista de emprestados
            livro.devolver()  # devolve o livro
            # remove o livro da lista de emprestados
            self.livros_emprestados.remove(livro)
            return True
        return False  # se o livro nao estiver na lista, retorna false

    def listar_livros(self):
        for livro in self.livros_emprestados:
            livro.exibir_info()


class Biblioteca:
    def __init__(self, nome):
        self.livros = []
        self.nome = nome

    def adicionar_livro(self, livro):
        self.livros.append(livro)  # adiciona um livro na biblioteca

    def listar_livros_disponiveis(self):
        for livro in self.livros:
            if livro.disponivel:  # verifica se o livro esta disponivel
                livro.exibir_info()

    def buscar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:  # verifica se o titulo do livro bate
                return livro
        return None


livro = Livro("1984", "George Orwell")
livro.exibir_info()
livro.emprestar()
livro.exibir_info()
livro.devolver()

usuario = Usuario("Alice")
usuario.emprestar_livro(livro)

biblioteca = Biblioteca("Biblioteca Central")
biblioteca.adicionar_livro(livro)
biblioteca.listar_livros_disponiveis()

