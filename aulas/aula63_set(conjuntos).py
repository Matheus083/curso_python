# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set1 = set('Geek University')
# set2 = {'Matheus', 'Maria', 'João'}
# print(set1)
# print(set2)

# set(iterável) ou {1, 2, 3}
# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
# l1 = [1, 2, 3, 4, 5, 5, 5, 6]
# s1 = set(l1)
# l2 = list(s1)
# print(s1)
# print(l2)
# s1 = {1,2,3}
# print(s1)

# Métodos úteis:
# add, update, clear, discard
# s1 = set()
# s1.add(1)
# s1.add(2)
# s1.add(3)
# s1.update(('Geek University', 177))
# # s1.clear()
# s1.discard(3)
# print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}
s3 = s1 | s2 # s1.union(s2)
s4 = s1 & s2 # s1.intersection(s2)
s5 = s1 - s2 # s1.difference(s2) - Itens presentes apenas no set da esquerda
s6 = s1 ^ s2 # s1.symmetric_difference(s2) - Itens que não estão em ambos
print(s3)
print(s4)
print(s5)
print(s6)
