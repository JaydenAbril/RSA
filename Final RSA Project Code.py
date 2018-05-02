def RSA():
  leave = True
  encrypted_message = ''
  decrypted_message = ''
  while leave == True:
    print ("Do you want to encrypt, decrypt or leave?")
    inpot = input()

    if inpot == "encrypt":
      print ("What is your e value?")
      evalue = input()
      print ("What is your n value?")
      nvalue = input()
      print ("What is your message?")
      message = input()
      for x in message:
        numerize = ord(x)
        encrypt = pow(numerize, int(evalue), int(nvalue))
        denumerize = chr(encrypt)
        encrypted_message += denumerize
      print (encrypted_message)
      
    if inpot == "decrypt":
      print ("What is your d value?")
      dvalue = input()
      print("What is your n value?")
      nvalue = input()
      print("What is the message?")
      message = input()
      for t in message:
         numerize = ord(t)
         decrypt = pow(numerize, int(dvalue), int(nvalue))
         denumerize = chr(decrypt)
         decrypted_message += denumerize
      print (decrypted_message)
        
    if inpot == "leave":
      break
      
RSA()
      

    
    
    
    
