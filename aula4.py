#!/usr/bin/env python
#-*- coding: utf-8 -*-

#usando funcoes

#importando da pasta python

from python.biblioteca import *

print('Convites Vips\n')
nome = raw_input('Nome: ')
print('Convite gerado para %s: ' % (gera_nome_convite(nome)))
