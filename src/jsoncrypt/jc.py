import argparse, json
from sys import stdout, stdin
from jsoncrypt.jsoncrypt import JSONCrypt as jc

parser = argparse.ArgumentParser(description='Encrypt or decrypt JSON data.')
parser.add_argument('--cmd', type=str, choices=['enc', 'dec'], required=True, help='Command to execute')
parser.add_argument('--infile', type=str, help='Input file path for JSON to encrypt')
parser.add_argument('--outfile', type=str, help='Output file path for encrypted JSON')
parser.add_argument('--json', type=str, help='JSON string to encrypt or decrypt')
parser.add_argument('--secret', type=str, help='Secret key for encryption/decryption')
args = parser.parse_args()

def __start__():
    """
    Main function to handle command line arguments and execute the appropriate command.
    """
    if args.cmd == 'enc':
        
        # Assumes that the JSON data is passed as a string
        data = args.json
        
        # if a file is passed as input, read the JSON data from the file
        if args.infile:
            with open(args.infile, 'r') as file:
                data = file.read()
        elif args.json is None:
            with stdin as file:
                data = file.read()
        
        # Encrypt the JSON data
        jcObject = jc(data=json.loads(data), secret=args.secret)
        
        # Retrieve the encrypted JSON object
        encrypted_json = jcObject.enc_json

        # writes the encrypted JSON to output, if '-' or 'stdout' is passed
        # the output is written to stdout
        if args.outfile:
            with open(args.outfile, 'w') as file:
                file.write(json.dumps(encrypted_json))
        else:
            with stdout as file:
                file.write(json.dumps(encrypted_json))

    elif args.cmd == 'dec':

        # Decrypt the JSON data
        if not args.json and not args.infile:
            raise ValueError("Either --json or --infile must be provided for decryption.")

        if args.infile:
            with open(args.infile, 'r') as file:
                enc_json = file.read()
        else:
            enc_json = args.json

        # Initialize the JSONCrypt object
        encObj = jc(enc_json=enc_json, secret=args.secret)

        # Retrieve the decrypted JSON object
        decrypted_json = encObj.data
        
        # writes the decrypted JSON to output, if '-' or 'stdout' is passed
        # the output is written to stdout
        if args.outfile:
            with open(args.outfile, 'w') as file:
                file.write(json.dumps(decrypted_json, indent=4))
        else:
            with open('-', 'w') as file:
                file.write(json.dumps(decrypted_json, indent=4))
