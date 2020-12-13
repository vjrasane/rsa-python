from get_keypair import get_keypair

bits=1024

def chunk(string, chunks):
  result = []
  for i in range(0, len(string), chunks):
    result.append(string[i : i + chunks])
  return result

def encrypt(plaintext, public_key):
  key, n = public_key
  return [pow(ord(char), key, n) for char in plaintext]

def decrypt(ciphertext, private_key):
  key, n = private_key
  return "".join([chr(pow(char, key, n)) for char in ciphertext])

def pass_message_through(message):
  public_key, private_key = get_keypair(bits)
  ciphertext = encrypt(message, public_key)
  plaintext = decrypt(ciphertext, private_key)
  return plaintext

print(pass_message_through("ENCRYPT THIS"))