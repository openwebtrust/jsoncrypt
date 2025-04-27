import json

from jsoncrypt import jsoncrypt
from jsoncrypt.jsoncrypt import JSONCrypt as jc

# Test the jsoncrypt module
def test_jsoncrypt():
    
    secret = "password1234"
    
    # Test the encryption and decryption of a simple dictionary
    data = {"name": "Alice", "age": 30, "city": "New York"}
    
    # Builds the JSONCrypt object with the data and password
    # and retrieves the JSON object with the encrypted data
    jcObject = jc(data=data, secret=secret)
    enc_json = jcObject.enc_json
    
    # Retrieves the JSON object with the encrypted data
    dec_data = jcObject.data
    
    # Asserts that the original data and decrypted data are the same
    # by comparing the two dictionaries key/value pairs
    assert set(data.items()) == set(dec_data.items()), \
        f"Expected {data}, but got {dec_data}"
    
    # Loads the encrypted JSON into a new JSONCrypt object
    # by passing the encrypted JSON and the secret to the
    # constructor. The .data property actually decrypts and
    # returns the original data that is kept encrypted in
    # the JSON object.
    dec_data_new = jc(enc_json=enc_json, secret=secret).data
    print(dec_data_new)
    
    # Asserts that the original data and decrypted data have
    # the same key/value pairs, but the order may be different
    assert set(data.items()) == set(dec_data_new.items()), \
        f"Expected {data}, but got {dec_data_new}"
    
    
    