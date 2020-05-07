# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 22:38:36 2020

@author: elber
"""

pares = []

for x in range(101):
  if x % 2 == 0:
      pares.append(x)

print(pares)
print("====================================")

pares = [par for par in range(101) if par % 2 == 0]

print(pares);

print("====================================")

def soma_e_produto(x, y):
    return (x+y), (x*y)

sp = soma_e_produto(2, 3)
s,p = soma_e_produto(2, 3)

print(sp)
print(s,p)

print("=============Ocorrencias=======================")

unicas = [];
ocorrencias = {}

document = list(open("palavras.txt").read().lower().split())

total = len(document)

for p in document:
    if p not in unicas:
        unicas.append(p)
    
    ocorrencias.update({p: ocorrencias.get(p) + 1 if p in ocorrencias else 1 })
        
print("total de", total, "palavras")
print("total de plavras unicas: ",len(unicas))
print(ocorrencias)

print("=============Ordenação=======================")

stop_words = set()

#ordenar em ordem crescente
ordem = [palavra for palavra in sorted(ocorrencias.items(), key=lambda \
            chave_valor:chave_valor[1], reverse=True)[:3]]

#print("ordem",ordem)
    
maiores = dict(ordem).keys()

for m in maiores:
    stop_words.add(m)
    
#ordenar em ordem decrescente
ordem = [palavra for palavra in sorted(ocorrencias.items(), key=lambda \
        chave_valor:chave_valor[1], reverse=False)[:3]]
    
#print("ordem",ordem) / dict cast para conjunto
menores = dict(ordem).keys()

for m in menores:
    stop_words.add(m)
    
print("stop_words: ", stop_words,"\n")

todos_sem_stop_words = [palavra for palavra in document \
                        if palavra not in stop_words]
    
conjunto = set()
for item in todos_sem_stop_words:
    conjunto.add(item)

print("lista de todos menos stop_keywords:", conjunto)
print("Lista de todos menos stop_keywords:",todos_sem_stop_words)

