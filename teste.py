# Escopo global

def show_namespace() -> None:
    # Escopo local
    module_namespace = globals()
    print("Conteúdo de globals():", module_namespace)

    # Note que 'function_namespace' não aparecerá no locals() se chamado antes dela
    function_namespace = locals()
    print("Conteúdo de locals():", function_namespace)


if __name__ == "__main__":
    show_namespace()
    