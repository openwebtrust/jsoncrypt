# JSONCrypt Usage

## Introduction

This document provides detailed usage instructions for the JSONCrypt library. JSONCrypt is a JSON encryption tool created by the Open Web Trust Community. It allows you to easily encrypt and decrypt your JSON dict objects into a serializable JSON format.

## The JSONCrypt Format

JSONCrypt uses JSON to represent the encrypted data with the following structure (GCM, SIV, and ChaCha20Poly1305):

```json
{
    "algorithm": "str", // The algorithm used for encryption (e.g., 'AES'),
    "encryption-mode": "int", // The encryption mode used (e.g., AES.GCM_MODE)
    "nonce": "bytes", // The nonce used with AEAD ciphers (GCM, SIV, and ChaCha20Poly1305)
    "data" : "bytes", // The cleartext data that needs to be encrypted
    "tag": "bytes" // The tag used with AEAD ciphers (GCM, SIV, and ChaCha20Poly1305)
}

When using the `AES.CBC_MODE` for encryption, the JSON format does not contain the nonce and tag and
introduces the `iv` as follows:

```json
{
    "algorithm": str, // The algorithm used for encryption (e.g., 'AES'),
    "encryption-mode": int, // The encryption mode used (e.g., AES.CBC_MODE)
    "iv": bytes, // The initialization vector used with CBC mode
    "data" : bytes // The cleartext data that needs to be encrypted
}
```

Where the options are:

* `algorithm` (str): The algorithm used for encryption (e.g., 'AES').
* `encryption-mode` (str): The encryption mode used (e.g., Crypto.AES.GCM_MODE, Crypto.AES.CBC_MODE).
* `nonce` (bytes): The nonce used with AEAD ciphers (meaningful only for GCM, SIV, and ChaCha20Poly1305).
* `iv` (bytes): The initialization vector (only used with CBC mode).
* `data` (bytes): The cleartext data that needs to be encrypted (bytes).
* `tag` (bytes): The tag used with AEAD ciphers (bytes).

## CLI Tool (jc)

The `jc` command-line interface (CLI) tool is a simple command-line utility that allows you to encrypt
and decrypt JSON data using the JSONCrypt library. It provides a convenient way to use the library without
writing any code.

### Encrypting JSON Data

To encrypt JSON data using the `jc` CLI tool, you can use the following command:

```shell
$ jc --cmd enc --json '{"key": "value"}' --secret 'test' --outfile 'encrypted.json'
```

This command will encrypt the JSON data `{"key": "value"}` using the secret `test` and save the
encrypted data to the file `encrypted.json`. The `--cmd` option specifies the command to run (in
this case, `enc` for encryption), the `--json` option specifies the JSON data to encrypt, and the
`--secret` option specifies the secret key to use for encryption. The `--outfile` option specifies
the output file where the encrypted data will be saved.


Alternatively, you can use the `--infile` option to specify an input file containing the JSON data
to encrypt. For example:

This command will read the JSON data from the file `input.json`, encrypt it using the secret `test`, and
save the encrypted data to the file `encrypted.json`. The `--infile` option specifies the input file
containing the JSON data to encrypt.

### Decrypting JSON Data

To decrypt JSON data using the `jc` CLI tool, you can use the following command:

```bash
$ jc --cmd 'dec' --json '<json_data>' --secret '<value>' --outfile '<output>'
```

This command will decrypt the JSON data `{"key": "value"}` using the secret `test` and save the
decrypted data to the file `decrypted.json`. The `--cmd` option specifies the command to run (in
this case, `dec` for decryption), the `--json` option specifies the JSON data to decrypt, and the
`--secret` option specifies the secret key to use for decryption. The `--outfile` option specifies
the output file where the decrypted data will be saved.

Alternatively, you can use the `--infile` option to specify an input file containing the JSON data
to decrypt.

```bash
$ jc --cmd dec --infile 'encrypted.json' --secret 'test' --outfile 'decrypted.json'
```

#### Examples

```shell
$ jc --cmd dec --json '{"algorithm": "AES", "encryption-mode": 11, "nonce": "51nbhCgIlQFnnCz1EcNaDw==", "data": "T8KDMcQPVcrq72bbBaDdRQ==", "tag": "-pJGDF5eOy2g9-2kT1mcbA=="}' --secret 'test' --outfile 'decrypted.json'
```

```shell
$ jc --cmd dec --infile 'encrypted.json' --secret 'test' --outfile 'decrypted.json'
```


## Encrypting Data

To encrypt data using JSONCrypt, you can initialize a new `JSONCrypt` object and pass the `data` argument
to the initializer. The `data` argument should be a dictionary object (JSON) that you want to encrypt. You
the encryption parameters to use parameters sets that are different from the default.

```python
from jsoncrypt.jsoncrypt import JSONCrypt as jc

# Initialize the JSONCrypt object
encObj = jc(data={'key': 'value'}, secret='secret_master_key')

# Retrieve the encrypted JSON object
encrypted_json = jc.enc_json
```

## Decrypting Data

To decrypt data using JSONCrypt, you first need to initialize a new `JSONCrypt` object. The data to be
decrypted can be passed to the initializer either in a binary format (`enc_data`) or in jsoncrypt format
(`enc_json`). The `enc_json` argument carries a JSON object with the structure described above.

Like the encryption, you can also use the `secret` argument to specify the master key used for decryption.

```python
from jsoncrypt.jsoncrypt import JSONCrypt as jc

# Initialize the JSONCrypt object
encObj = jc(enc_json=encrypted_json, secret='secret_master_key')

# Retrieve the decrypted JSON object
decrypted_json = encObj.data
```
