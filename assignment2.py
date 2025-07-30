# odd even tester
a=int(input('Enter a Number:'))
if a%2==0:
    print(a,'is an even number')
else:
    print(a,'is an odd number')

#sum of 1 to 50
b=0
for i in range(51):
    b=i+b

print('sum from 1 to 50 is:',b)