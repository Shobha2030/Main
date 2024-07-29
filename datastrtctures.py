s = 'Aa, Bb - A a B C'
dic1={}
for i in s:
    if i in dic1 and i.isalpha():
        dic1[i]+=1
    elif i not in dic1 and i.isalpha():
        dic1[i]=1
    else:
        pass
print(dic1)
