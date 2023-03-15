class programa:
    def __init__(self, Nome, Ano, Genero):
        self._Nome = Nome.title()
        self.Ano = Ano
        self.Genero = Genero.title()
        self._like = 0

    @property
    def like (self):
        return self._like

    def darlike(self):
        self._like += 1

    @property
    def Nome(self):
        return self._Nome

    @Nome.setter
    def Nome(self, Novo_Nome):
        self._Nome = Novo_Nome.title()

    def __str__(self):
        return f"Programa: {self._Nome}, ano: {self.Ano}, genero: {self.Genero}, likes: {self._like}"

class Filme (programa):
    def __init__(self, Nome, Ano, Genero, Duracao):
        super().__init__(Nome, Ano, Genero)
        self.Duracao = Duracao
    def __str__(self):
        return f"Filme: {self._Nome}, ano: {self.Ano}, genero: {self.Genero}, likes: {self._like}, duracao: {self.Duracao}"


class Serie (programa):
    def __init__(self, Nome, Ano, Genero, Temporadas):
        super().__init__(Nome, Ano, Genero)
        self.Temporadas = Temporadas
    def __str__(self):
        return f"Filme: {self._Nome}, ano: {self.Ano}, genero: {self.Genero}, likes: {self._like}, Temporadas: {self.Temporadas}"

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)



Matrix = Filme("Matrix", 1999, "Sci-Fi", 120)
Matrix.darlike()
Matrix.darlike()

idm = Filme("The Conjuring", 2013, "Terror", 140)
idm.darlike()

Flash = Serie("Flash", 2013, "Super-Herois", 8)
Flash.darlike()
Flash.darlike()

Wednesday = Serie("wednesday", 2022, "Adolescente", 1)
Flash.darlike()


playlist = [Matrix, idm, Flash, Wednesday]
netflix = Playlist("Netflix - ", playlist)

print(f'Tamanho da Playlist {len(netflix)}')

for programa in netflix.listagem:
   print(programa)