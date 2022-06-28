from lab11.regex import Regex


def main():
    # Extracting zip with our log file
    Regex.extract()

    print("-------------------------------------")

    # Searching needed info using regex
    Regex.regex()


if __name__ == '__main__':
    main()
