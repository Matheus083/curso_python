um_nome = "um_nome (global)"


def func_global(sou_local: str) -> None:
    um_nome = "um_nome (local)"
    outro_nome = "outro_nome (local)"
    print("locals (namespace da função)")
    print("dir", dir())
    print("vars", vars())
    print()


# func_global("arg (local)")
# print()

print("globals (namespace do módulo)")
print("dir", dir())
print("vars", vars())
