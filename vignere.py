a=input("Enter Plain text : ")
key=input("Enter key : ")
encrypt=""
k=0
for i in range(len(a)):
    if(len(key)<len(a)):
        if(i==len(key)-1):
            encrypt=encrypt+ chr((((ord(a[i])-97)+(ord(key[k])-97))%26)+65)
            print(key[k])
            k=0          
            continue
        else:
            encrypt=encrypt+ chr((((ord(a[i])-97)+(ord(key[k])-97))%26)+65)
            print(key[k])       
        k=k+1       
    else:
        encrypt=encrypt+ chr((((ord(a[i])-97)+(ord(key[i])-97))%26)+65)

       
print(encrypt)