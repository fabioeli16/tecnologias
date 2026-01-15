from app.config.settings import DEBUG, get_settings
import requests


def main():
    print(DEBUG)
    print(get_settings())

if __name__ == "__main__":
    main()
