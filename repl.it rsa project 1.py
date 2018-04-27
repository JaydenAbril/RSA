def encrypt(e,n):
    encrypted_message = ''
    LUT_encryption = dict()
    message = input("")
    for x in message:
        if x in LUT_encryption:
            encrypted_message += LUT_encryption[x]
        else:
            numerize = ord(x)
            encrypt = pow(numerize, e, n)
            denumerize = chr(encrypt)
            encrypted_message += denumerize
            LUT_encryption[x] = denumerize

    print (encrypted_message)
    
def decrypt(d,n):
    decrypted_message = ''
    LUT_decryption = dict()
    decrypted_message = input("")
    for t in decrypted_message:
       if t in LUT_decryption:
            decrypted_message += LUT_decryption[t]
       else: 
           numerize = ord(t)
           decrypt = pow(numerize, d, n)
           denumerize = chr(decrypt)
           decrypted_message += denumerize
    
    print (decrypted_message)
    
    variable = input
    while 
      print ("Do you want to encrypt, decrypt, or exit?")
      if input = encrypt
        print ("what is your e value?"): input("")
        print ("What is your n value?"): input("")
        
       elif:
        input = decrypt
        print ("what is your d value?"): input("")
              ("What is your n value?"): input("")
        print ("Program Complete")
