slovo = input('Введите слово из маленьких латинских букв: ')
e=slovo.count('e')
a=slovo.count('a')
i=slovo.count('i')
u=slovo.count('u')
o=slovo.count('o')

x = e+a+i+u+o
print("всего гласных",x)
print("всего согласных",len(slovo)-x)

if (e==0):
    print (" e - False")
else:
    print("e=",e)

if (u==0):
    print (" u - False")
else:
    print("u=",u)

if (o==0):
    print (" o - False")
else:
    print("o=",o)

if (a==0):
    print (" a - False")
else:
    print("a=",a)

if (i==0):
    print (" i - False")
else:
    print("i=",i)