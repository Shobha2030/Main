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


d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'d': 100, 'e': 200, 'f': 300}
d3 = {'f': 30, 'g': 40}

d1.update(d2)

dd=[j for i,j in d1.items()]
dd.extend([j for i,j in d3.items()])
dd1=[i for i,j in d1.items()]
dd1.extend([i for i,j in d3.items()])
print(dd)
print(dd1)


grades = {
    'John': [90, 95, 98],
    'Eric': [86, 84, 92],
    'Michael': [90, 89, 85]
}

exam = {
    'Eric': 99,
    'John': 100
}

'''{
    'John': [100, 90, 95, 98],
    'Eric': [99, 86, 84, 92],
    'Michael': [None, 90, 89, 85]
}'''

for i,j in grades.items():
    if i in exam:
        grades[i].append(exam[i])
    else:
        grades[i].append("None")
print(grades) 


#Write some code that generates an m x n multiplication table.

#For example if m=3 and n=4 your output should look something like:

for i in range(1,5):
    for j in range(1,5):
        print(f"{i}*{j}={j}")
        i=i*1
        if j ==4:
            print(f"-------------")
            break;
        
