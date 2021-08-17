import string

def dataEncryption(data):
    keyLoader=open('HL_Engine\HL_Crypto\key.txt','r')
    key=keyLoader.read()
    dataModel=[]
    ASCER=(string.printable)
    for i in ASCER:
        dataModel.append(i)
    keyModel=str(key)
    Position_Generator=[]
    Data=str(data)
    for i in Data:
        #print(i)
        if(i in Data):
            Position=dataModel.index(i)
            Position_Generator.append(Position)
    encrypt=[]
    stringer=""
    for i in Position_Generator:        
        data=keyModel[i]
        encrypt.append(data)        
    encrypted=stringer.join(encrypt)    
    return(encrypted)


def dataDecryption(data):
    data=str(data)
    dataModel=[]
    ASCER=(string.printable)
    for i in ASCER:
        dataModel.append(i)
    keyLoader=open('HL_Crypto/key.txt','r')
    key=keyLoader.read()
    keyModel=str(key)
    decrypt=[]
    decryption=[]
    stringer=""
    for i in data:
        if(i in keyModel):
            position=keyModel.index(i)
            decrypt.append(position)
    for i in decrypt:
        decode=dataModel[i]
        decryption.append(decode)

    decrypted=stringer.join(decryption)
    return(decrypted)
        

        