import app.config.settings as configuraciones


def main():
    print(configuraciones.DEBUG)
    print(configuraciones.get_settings())


if __name__ == "__main__":
    main()
