import sys
from collections import deque

class Campeonato:
    def __init__(self):
        self.jogadores = {}
        self.times = {}
        self.confrontos = deque()

    def cadastrar_jogador(self, nome, idade, posicao):
        if nome not in self.jogadores:
            self.jogadores[nome] = {'idade': idade, 'posicao': posicao, 'time': None}
            print(f"Jogador {nome} cadastrado com sucesso.")
        else:
            print("Jogador já cadastrado.")

    def montar_time(self, nome_time, jogadores):
        if nome_time not in self.times:
            jogadores_validos = []
            for jogador in jogadores:
                if jogador not in self.jogadores:
                    print(f"Jogador {jogador} não cadastrado e não será adicionado ao time.")
                elif self.jogadores[jogador]['time'] is not None:
                    print(f"Jogador {jogador} já está no time {self.jogadores[jogador]['time']} e não será adicionado ao time {nome_time}.")
                else:
                    jogadores_validos.append(jogador)
            self.times[nome_time] = jogadores_validos
            for jogador in jogadores_validos:
                self.jogadores[jogador]['time'] = nome_time
            print(f"Time {nome_time} montado com sucesso com os jogadores: {', '.join(jogadores_validos)}.")
        else:
            print("Time já existe.")

    def realizar_confronto(self, time1, time2):
        if time1 in self.times and time2 in self.times:
            self.confrontos.append((time1, time2))
            print(f"Confronto entre {time1} e {time2} agendado.")
        else:
            print("Um ou ambos os times não existem.")

    def listar_jogadores(self):
        for jogador, info in self.jogadores.items():
            print(f"Nome: {jogador}, Idade: {info['idade']}, Posição: {info['posicao']}, Time: {info['time']}")

    def listar_confrontos(self):
        for confronto in self.confrontos:
            print(f"Confronto: {confronto[0]} vs {confronto[1]}")

def main():
    campeonato = Campeonato()
    
    while True:
        print("\nMenu:")
        print("1. Cadastrar Jogador")
        print("2. Montar Time")
        print("3. Realizar Confronto")
        print("4. Listar Jogadores")
        print("5. Listar Confrontos")
        print("6. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            nome = input("Nome do jogador: ")
            idade = int(input("Idade do jogador: "))
            posicao = input("Posição do jogador: ")
            campeonato.cadastrar_jogador(nome, idade, posicao)
        elif escolha == '2':
            nome_time = input("Nome do time: ")
            jogadores = input("Nomes dos jogadores (separados por vírgula): ").split(',')
            campeonato.montar_time(nome_time, [j.strip() for j in jogadores])
        elif escolha == '3':
            time1 = input("Nome do primeiro time: ")
            time2 = input("Nome do segundo time: ")
            campeonato.realizar_confronto(time1, time2)
        elif escolha == '4':
            campeonato.listar_jogadores()
        elif escolha == '5':
            campeonato.listar_confrontos()
        elif escolha == '6':
            print("Saindo do sistema.")
            sys.exit()
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

