# JSONCrypt Project

This project provides a simple and secure way to encrypt and decrypt JSON data using strong (quantum-resistant) symmetric encryption. It is designed to be easy to use and integrate into your existing systems.

The guiding principles of this project are:

* **Simplicity**: The library is designed to be easy to use and understand, with a simple API that allows you to encrypt and decrypt JSON data with minimal effort.
* **Security**: The library uses strong encryption algorithms and key management practices to ensure the security of your data.
* **Crypto-Agility**: The library is designed to be flexible and extensible, allowing you to customize the encryption and decryption process to meet your specific needs.
* **Quantum-Resistance**: The library uses encryption algorithms that are resistant to attacks from quantum computers, ensuring the long-term security of your data.
* **Open Source**: The library is open source and freely available for anyone to use and contribute to. We welcome contributions from the community and encourage you to get involved in the project.
* **Community-Driven**: The library is developed and maintained by the Open Web Trust Community, a group of passionate developers and security experts dedicated to improving the security of the web.

## Introduction

This is a JSON encryption tool created by the Open Web Trust Community. It is a simple
library that allows you to easily encrypt and decrypt your JSON dict objects into a
serializable JSON format.

The output is a JSON string that can be easily stored or transmitted and contains all the
necessary information to decrypt the data later. The library uses a symmetric encryption
algorithm to encrypt the data, which means that the same key is used for both encryption
and decryption. The key is derived from a password using a key derivation function (KDF)
based on the bcrypt algorithm and SHA3-512 hash function.

## Installation

To install the JSONCrypt package, you need to have Python 3.6 or higher installed on your system. You can install the JSONCrypt package using pip:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install .
```

For development installation, you might want to use an editable install. Use the `-e` flag for development:

```
python3 -m venv .venv
. .venv/bin/activate
pip install -e .
```

## Usage

Please see the [USAGE.md](docs/USAGE.md) file for detailed usage instructions.

## Support

If you have any questions or need help with the JSONCrypt package, please contact us at
jsoncrypt-support {@} openwebtrust.org, or visit our website at [www.openwebtrust.org](https://www.openwebtrust.org).

## Acknowledgements

This project is supported by the Open Web Trust Community. We would like to thank all our
contributors for their help and support.

## Contributing

Please see the [CONTRIBUTING.md](docs/CONTRIBUTING.md) file for information on how to contribute
to this project.

Thank you for using JSONCrypt!
