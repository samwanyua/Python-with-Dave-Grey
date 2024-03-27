def hello(name, lang):
    greetings = {
        "English": "Hello",
        "Spanish": "Hola",
        "German": "Hallo",
        "Swahili": "Jambo",
    }
    msf = f"{greetings[lang]} {name}"
    print(msf)

if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(
        description="Provides personal greetings."
    )

    parser.add_argument(
        "-n", "--name", metavar="name", 
        required=True, help="The name of the person to greet"
    )

    parser.add_argument(
        "-l", "--lang", metavar="language",
        required=True, choices=["English","Spanish","German", "Swahili" ],
        help="The language of the greeting."
    )
    args = parser.parse_args()

    hello(args.name, args.lang)