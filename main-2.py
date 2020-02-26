#Check Whether character is alphabet or not
def checkcharacter(ch):
    if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):  
        print("Character is Alphabet")
    else:
        print("Character is not Alphabet")
        
ch = input("Enter The Character")
checkcharacter(ch)