import x


def func_global() -> None:
    print(f"Estou em: {__name__} - {__file__.split('/')[-1]}")


x.func_global()
func_global()
print()
print(globals())
