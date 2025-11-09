f=input("Send a message")
result=""
for ch in f:
    if(ch.islower()):
        num_ch = ord(ch)-97
        result += chr(122-num_ch)

    elif (ch.isupper()):
        num_ch = ord(ch)-65
        result += chr(90-num_ch)
    else:
        result+=ch
# print(result) 





with open("secret.txt","w") as f:
    f.write(result)

with open("secret.txt","r") as f:
    atbash = f.read()
    new = "" 
    for ch in atbash:
        if(ch.islower()):
            num_ch = ord(ch)-97
            new += chr(122-num_ch)

        elif (ch.isupper()):
            num_ch = ord(ch)-65
            new += chr(90-num_ch)
        else:
            new+=ch
print(new) 
        

""""exe 2"""

with open("mixed_stories.txt","r") as f:
    count=0
    for line in f:
        print(count,line.strip())
        count+=1
        if count % 2 == 0:
           with open("story_A.txt","a") as f:
               f.write(line) 
        if count % 2 != 0:
           with open("story_B.txt","a") as f:
               f.write(line)        