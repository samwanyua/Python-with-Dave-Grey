import argparse

parser = argparse.ArgumentParser(
    description="Provides personal greetings."
)

parser.add_argument(
    "-n", "--name", metavar="name", 
    required=True, help="The name of the person to greet"
)

args = parser.parse_args()

msf = f"Hello {args.name}"
print(msf)