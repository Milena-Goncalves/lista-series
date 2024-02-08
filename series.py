import pandas as pd

seriesDoc = pd.read_csv('data.csv')  # Abre e lê o ficheiro csv
print("Séries já inseridas: \n")
print(f"{seriesDoc}\n")

STREAMS = ['Amazon Prime', 'HBO Max', 'Viki',
           'Disney+', 'Youtube', 'Netflix', 'Crunchyroll']

# Criação da Classe Série


class Serie:
    def __init__(self, titulo, genero, nota):
        self.titulo = titulo
        self.genero = genero
        self.nota = nota

# Insere as Séries no documento csv
    def InserirSerie():

        # Criação de um dicionário vazio
        series = {'Titulo': [],
                  'Genero': [],
                  'Nota': []
                  }

        inserir = input(
            "\nQuer inserir mais séries? Se sim, digite 'sim' ou 's'\n")

        # Entrada das informações do utilizador
        while (inserir == "sim" or inserir == "s"):

            titulo = input("Qual série deseja inserir?\n")

            genero = input("Qual a gênero da série inserida?\n")

            nota = input("Qual nota você dá para a série?\n")

            series['Titulo'].append(f'{titulo}')
            series['Genero'].append(f'{genero}')
            series['Nota'].append(f'{nota}')

            inserir = input("Quer continuar a inserir séries?\n")

        else:
            # Converte o dicionário series em um DataFrame
            series = pd.DataFrame(series)
            # Exporta DataFrames para o ficheiro csv
            series.to_csv('data.csv', mode='a', index=False, header=False)
            pass

            seriesDoc = pd.read_csv('data.csv')  # Abre e lê o ficheiro csv
            print(seriesDoc)

    # Informar as melhores notas
    def MelhoresNotas(nota):
        seriesDoc = pd.read_csv('data.csv')

        valor = str(type(nota))
        if 'int' in valor:

            if (nota >= 0 and nota <= 10):

                if (nota >= 8 and nota <= 10):
                    print("\n\nEstas são as séries com as melhores notas!")
                    # Filtra as séries com o valor da nota maior ou igual a nota solicitada
                    MaiorNota = seriesDoc[seriesDoc['Nota'] >= nota]
                    print(MaiorNota)
                elif (nota <= 8 and nota >= 5):
                    print("\n\nEstas são as séries com notas medianas!")
                    MaiorNota = seriesDoc[seriesDoc['Nota'] < nota]
                    print(MaiorNota)
                elif (nota < 5 and nota >= 0):
                    print("\n\nEstas são as séries com as notas mais baixas!")
                    MaiorNota = seriesDoc[seriesDoc['Nota'] < nota]
                    print(MaiorNota)

        else:
            raise ValueError(
                "Valor da nota inválido! Insira um valor numérico entre 0 e 10!")

    # Retorna os gêneros mais assistidos
    def Generos_Mais_Assistidos():
        seriesDoc = pd.read_csv('data.csv')
        print("\n")
        # Contabiliza a frequência que ocorre o mesmo valor
        print(seriesDoc['Genero'].value_counts())

    # Descreve a série solicitada
    def descricao(self):
        print(
            f"Nome da série: {self.titulo} \nGénero da série: {self.genero} \nNota da série: {self.nota}")

    # Solicita ao utilizador dados que queira inserir
    def serie_preferida():
        titulo = input("Qual sua série preferida?\n")

        genero = input("Qual a gênero da sua série preferida?")

        nota = input("Qual nota você dá para a série?")

        seriePreferida = Serie(titulo, genero, nota)

        seriePreferida.descricao()
    # Mostra o stream preferido

    def stream_preferido(stream):
        print(
            f"\nStream preferida: {stream}")

# Criação da classe remove_stream para remover um stream da Lista STREAM


class remove_stream:

    def remove_stream(s):
        valor = str(type(s))
        if 'list' in valor:

            while 'Netflix' in s:
                s.remove('Netflix')
            return s

        else:
            raise ValueError(
                "É possível apenas remover séries com variáveis do tipo lista. Tente novamente!")


serie = Serie("The Last of Us", "Sobrevivencia", 10)

# Insere as Séries no documento csv
Serie.InserirSerie()


# Informar as melhores notas
Serie.MelhoresNotas(5)

# Retorna os gêneros mais assistidos
Serie.Generos_Mais_Assistidos()

# Descreve a série solicitada
Serie.descricao(serie)

# Mostra o stream preferido
Serie.stream_preferido("HBO Max")

# Remove Stream
print(STREAMS)
remove_stream.remove_stream(STREAMS)
print(STREAMS)
