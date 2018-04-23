encrypted_message = ''
decrypted_message = ''
LUT_encryption = dict()
LUT_decryption = dict()

def encrypt(e,n):
    encrypted_message = ''
    LUT_encryption = dict()
    message = raw_input("")
    for x in message:
        if x in LUT_encryption:
            encrypted_message += LUT_encryption[x]
        else:
            numerize = ord(x)
            encrypt = pow(numerize, e, n)
            denumerize = unichr(encrypt)
            encrypted_message += denumerize
            LUT_encryption[x] = denumerize

    print encrypted_message
    
