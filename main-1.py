#Check Whether alphabet is vowel or constant
def checkalphabetvowel(ch):
    if(ch=='a' or ch=='A'or ch=='e' or ch=='E' or ch=='I' or ch=='i' or ch=='o' or ch=='O' or ch=='u' or ch=='U'):
        print("No is vowel")
    else:
        print("Alphabet is constant")
ch = input("Enter The Alphabet")
checkalphabetvowel(ch)