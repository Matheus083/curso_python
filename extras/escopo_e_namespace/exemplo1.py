# nome definido no escopo global (módulo)
um_nome = "um_nome (GLOBAL)"


# nome definido no escopo global (módulo)
def func_global(sou_local: str) -> None:
    # Escopo local (função e seus parâmetros)

    # `um_nome` no escopo local é OUTRA VARIÁVEL (sem relação outro escopo)
    um_nome = "um_nome (LOCAL)"  # nome definido no escopo local
    outro_nome = "outro_nome (LOCAL)"  # nome definido no escopo local

    # Parâmetros de funções também são do escopo local da função
    print(f"Dentro da função: {um_nome}, {outro_nome}, {sou_local}")


# ISSO NÃO FUNCIONA
# print(outro_nome, sou_local)

# Isso é injetado automaticamente pelo Python no escopo global
print("Nome do módulo:", __name__)
print("Arquivo do módulo:", __file__)
print("Documentação do módulo:", __doc__)
print()  # apenas uma quebra de linha

func_global("arg (local)")
# Saída - Dentro da função: um_nome (LOCAL), outro_nome (LOCAL), arg (local)

print(f"Fora da função: {um_nome}")  # Acessa a variável GLOBAL
# Saída - Fora da função: um_nome (GLOBAL)
