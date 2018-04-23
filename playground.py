import time

n = 52993
e = 6977
d = 51873

message = 'Hello World!'
encrypted_message = ''
decrypted_message =''
start = time.time()

#########Encryption#########
for x in message:
    numerize = ord(x)
    encrypt = pow(numerize, e, n)
    denumerize = unichr(encrypt)
    encrypted_message += denumerize

print encrypted_message
    
#########Decryption#########
for t in encrypted_message:
    numerize = ord(t)
    decrypt = pow(numerize, d, n)
    denumerize = chr(decrypt)
    decrypted_message += denumerize
    
print decrypted_message
end = time.time()

print(end - start)

encrypted_message2 = ''
decrypted_message2 = ''
LUT_encryption = dict()
LUT_decryption = dict()


start = time.time()
#########Encryption v2#########
for x in message:
    if x in LUT_encryption:
        encrypted_message2 += LUT_encryption[x]
    else:
        numerize = ord(x)
        encrypt = pow(numerize, e, n)
        denumerize = unichr(encrypt)
        encrypted_message2 += denumerize
        LUT_encryption[x] = denumerize

print encrypted_message2



end = time.time()

print(end - start)






















