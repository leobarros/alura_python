# -*- coding: utf-8 -*-

def cadastrar(nomes):
    nome = raw_input('Digite o nome: ')
    nomes.append(nome)

def listar(nomes):
    for nome in nomes:
        print nome

def menu():
    nomes = []
    escolha = ''

    while (escolha != '0'):
        print '\n1 - Cadastrar nome\n2 - Listar\n0 - Sair\n'
        escolha = raw_input('Escolha uma opção: ')

        if (escolha == '1'):
            cadastrar(nomes)
        if (escolha == '2'):
            print('\nListando nomes')
            listar(nomes)

menu()
