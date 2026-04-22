namespace_global = globals()
um_nome = "um_nome (GLOBAL)"

# # print(id(um_nome), id(namespace_global["um_nome"]))
# print(dir(__builtins__))


def func_global(sou_local: str) -> None:
    um_nome = "um_nome (LOCAL)"
    outro_nome = "outro_nome (LOCAL)"
    print("LOCALS (namespace da função)")
    print(locals())
    print()


# func_global("arg (local)")
# print()

# print("GLOBALS (namespace do módulo)")
# print(globals())
