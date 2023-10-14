a = int(input())
if a>=90 and a<=100 :
    result = 'A'
elif a<=89 and a>=80 :
    result = 'B'
elif a<=79 and a>=70 :
    result = 'C'
elif a<=69 and a>=60 :
    result = 'D'
else:
    result = 'F'

print(result)