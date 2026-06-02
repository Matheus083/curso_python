# # Variavéis livres + nonlocal(locals, globals).
# def out(x):
#     a = x
#     def inn():
#         # print(locals()) # Variáveis locais da função inn.
#         print(inn.__code__.co_freevars)  # Variáveis livres da função inn.
#         return a
#     return inn

# inn = out(10)
# inn2 = out(20)

# print(inn())  # 10
# print(inn2()) # 20
# print(globals()) # Variáveis globais do módulo.

def concatenate(string_start):
    end_value = string_start

    def inside(value_to_concatenate):
        nonlocal end_value
        end_value += value_to_concatenate
        return end_value
    return inside

c = concatenate('a')
print(c('b'))
print(c('c'))
print(c('d'))
