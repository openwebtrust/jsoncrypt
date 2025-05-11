import argparse, json
from sys import stdout, stdin
from jsoncrypt.jsoncrypt import JSONCrypt as jc

# Builds the command line argument parser
parser = argparse.ArgumentParser(description='Encrypt or decrypt JSON data.')
parser.add_argument('-cmd', type=str, choices=['enc', 'dec'], required=True, help='Command to execute')
parser.add_argument('-json', type=str, help='JSON string to encrypt or decrypt')
parser.add_argument('-infile', type=str, help='Input file path for JSON to encrypt')
parser.add_argument('-outfile', type=str, help='Output file path for encrypted JSON')
parser.add_argument('-secret', type=str, help='Secret key for encryption/decryption')
parser.add_argument('-pretty', action='store_true', help='Pretty print JSON output')

# Parses the command line arguments
args = parser.parse_args()

def __start__():
    """
    Main function to handle command line arguments and execute the appropriate command.
    """

    # Check for valid options for JSON and INFILE
    if not args.json and not args.infile:
        raise ValueError("Either --json or --infile must be provided for decryption.")
    elif args.json and args.infile:
        raise ValueError("Only one of --json or --infile can be provided for decryption.")
    
    # By default, let's assume we have a JSON parameter
    data = args.json
    
    # if a file is passed as input, read the JSON data from the file
    if args.infile:
        with open(args.infile, 'r') as file:
            data = file.read()
    elif args.json is None:
        with stdin as file:
            data = file.read()
                
    # Encrypt or decrypt the JSON data based on the command
    if args.cmd == 'enc':       
        
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
                if args.pretty:
                    file.write(json.dumps(encrypted_json, indent=4))
                    file.write("\n")
                else:
                    file.write(json.dumps(encrypted_json))

    elif args.cmd == 'dec':

        # Initialize the JSONCrypt object
        encObj = jc(enc_json=json.loads(data), secret=args.secret)

        # Retrieve the decrypted JSON object
        decrypted_json = encObj.data
        
        # writes the decrypted JSON to output, if '-' or 'stdout' is passed
        # the output is written to stdout
        if args.outfile:
            with open(args.outfile, 'w') as file:
                file.write(json.dumps(decrypted_json))
        else:
            with stdout as file:
                if args.pretty:
                    file.write(json.dumps(decrypted_json, indent=4))
                    file.write("\n")
                else:
                    file.write(json.dumps(decrypted_json))
