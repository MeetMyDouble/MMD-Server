import crypt
from hmac import compare_digest as compare_hash



def encryptPassword(password):
    return crypt.crypt(password)

def comparePassword(plainText, hashed):
    return compare_hash(hashed, crypt.crypt(plainText, hashed))