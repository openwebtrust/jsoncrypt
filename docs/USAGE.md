# JsonCrypt Usage

## Introduction

This document provides detailed usage instructions for the JsonCrypt library. JsonCrypt is a JSON encryption tool created by the Open Web Trust Community. It allows you to easily encrypt and decrypt your JSON dict objects into a serializable JSON format.

## The JsonCrypt Format

JsonCrypt uses JSON to represent the encrypted data with the following structure (GCM, SIV, and ChaCha20Poly1305):

```json
{
    'algorithm': str, // The algorithm used for encryption (e.g., 'AES'),
    'encryption-mode': int, // The encryption mode used (e.g., AES.GCM_MODE)
    'nonce': bytes, // The nonce used with AEAD ciphers (GCM, SIV, and ChaCha20Poly1305)
    'data' : bytes, // The cleartext data that needs to be encrypted
    'tag': bytes // The tag used with AEAD ciphers (GCM, SIV, and ChaCha20Poly1305)
}

When using the `AES.CBC_MODE` for encryption, the JSON format does not contain the nonce and tag and
introduces the `iv` as follows:

```json
{
    'algorithm': str, // The algorithm used for encryption (e.g., 'AES'),
    'encryption-mode': int, // The encryption mode used (e.g., AES.CBC_MODE)
    'iv': bytes, // The initialization vector used with CBC mode
    'data' : bytes // The cleartext data that needs to be encrypted
}

Where the options are:

* `algorithm` (str): The algorithm used for encryption (e.g., 'AES').
* `encryption-mode` (str): The encryption mode used (e.g., Crypto.AES.GCM_MODE, Crypto.AES.CBC_MODE).
* `nonce` (bytes): The nonce used with AEAD ciphers (meaningful only for GCM, SIV, and ChaCha20Poly1305).
* `iv` (bytes): The initialization vector (only used with CBC mode).
* `data` (bytes): The cleartext data that needs to be encrypted (bytes).
* `tag` (bytes): The tag used with AEAD ciphers (bytes).

## Encrypting Data

To encrypt data using JsonCrypt, you can initialize a new `JsonCrypt` object and pass the `data` argument
to the initializer. The `data` argument should be a dictionary object (JSON) that you want to encrypt. You
the encryption parameters to use parameters sets that are different from the default.

```python

from jsoncrypt import JsonCrypt

# Initialize the JsonCrypt object
jc = JsonCrypt(data={'key': 'value'}, secret='secret_master_key')

# Retrieve the encrypted JSON object
encrypted_json = jc.enc_json
```

## Decrypting Data

To decrypt data using JsonCrypt, you first need to initialize a new `JsonCrypt` object. The data to be
decrypted can be passed to the initializer either in a binary format (`enc_data`) or in jsoncrypt format
(`enc_json`). The `enc_json` argument carries a JSON object with the structure described above.

Like the encryption, you can also use the `secret` argument to specify the master key used for decryption.

```python
from jsoncrypt import JsonCrypt

# Initialize the JsonCrypt object
jc = JsonCrypt(enc_json=encrypted_json, secret='secret_master_key')

# Retrieve the decrypted JSON object
decrypted_json = jc.data
```
