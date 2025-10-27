from cli.cli import CLI


def main():
    """
    Punto de entrada del juego cuando se ejecuta `python -m`.
    """
    interfaz = CLI()
    interfaz.iniciar_juego()


if __name__ == "__main__":
    main()
