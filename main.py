from Crypto.Cipher import AES

# helper function:
def string_to_bytes(item):
    """
    encode string to bytes using utf-8
    """
    if isinstance(item, str):
        return item.encode("utf-8", errors="strict")
    raise TypeError("Only string can be passed to string_to_bytes function")

def bytes_to_string(item):
    """
    decode bytes to string using utf-8
    """
    if isinstance(item, bytes):
        return item.decode("utf-8", errors="strict")
    raise TypeError("Only bytes object cna be passed to bytes_to_string function")

def load_key():
    """
    load key.bin
    """
    file = open("key.bin", "rb")
    key = file.read()
    file.close()
    return key


def encrypt(secret_code, key):
    """
    encrypt secret_code and save it in encrypted.bin using key
    """
    # Can be in other AES modes
    cipher = AES.new(key, AES.MODE_EAX)
    # MAC tag is used for checking content not changed
    ciphertext, tag = cipher.encrypt_and_digest(string_to_bytes(secret_code))
    file_out = open("encrypted.bin", "wb")
    [file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]
    file_out.close()

def decrypt(key):
    """
    read encrypted.bin, return the decrypted string using key
    """
    file_in = open("encrypted.bin", "rb")
    # nonce and tag are 16 bytes long, so they are 16 and 16, ciphertext is the rest, represented by -1
    nonce, tag, ciphertext = [file_in.read(x) for x in (16, 16, -1)]
    # let's assume that the key is somehow available again
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    return bytes_to_string(data)

if __name__ == "__main__":
    secret_code = "This \n" \
                  "should be \n" \
                  "encrypted" # has to be a string in this case
    key = load_key()
    encrypt(secret_code, key)
    import time
    start_time = time.time()
    print(decrypt(key))
    print("--- %s seconds ---" % (time.time() - start_time))