a = int(input())
b = int(input())

b1 = b%10
fst = b1*a
b2 = (b%100 - b1)/10
sec = int(b2*a)
b3 = int(b/100)
thd = b3*a

fourth = int(thd*100 + sec*10 + fst)

print(fst)
print(sec)
print(thd)
print(fourth)