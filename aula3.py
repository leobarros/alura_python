#!/usr/bin/python
#-*- coding: utf-8 -*-

#listas
#tuplas e dicionarios

tipos_convite = ['vip', 'normal', 'meia', 'cortesia']
tipos_convite.append('penetra')

print(tipos_convite)

#usando tuplas
convite_fixo = ('vip', 60, 'normal', 40, 'meia', 30, 'cortesia', 0)
print('Convites vip: ')
print(convite_fixo[0:2])

#dicionario
convite_com_preco = {'vip' : 60, 'normal' : 40, 'meia' : 30, 'cortesia' : 0}

print(convite_com_preco)

#consultando a entrada meia

print('Meia: ' + str(convite_com_preco['meia']))

#chaves do dicionario
print(convite_com_preco.keys())

#valores do dicionario
print(convite_com_preco.values())
