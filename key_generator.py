from Crypto.Random import get_random_bytes

def generate_key():
    """
    Return a random byte string of length 16.
    """
    key = get_random_bytes(16)
    return key


def save_key(key):
    """
    save the key in a key.bin file
    """
    file = open("key.bin", "wb")
    file.write(key)
    file.close()


if __name__ == "__main__":
    generated_key = generate_key()
    save_key(generated_key)
