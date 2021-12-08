user1=input("Enter your Name :")
user2=input("Enter your Love Name :")
love=user1+user2
name=love
t=name.count('t')
r=name.count('r')
u=name.count('u')
e=name.count('e')
num1= t + r + u + e
l=name.count('l')
o=name.count('o')
v=name.count('v')
e=name.count('e')
num2 = l + o + v + e
total=int(str(num1) + str(num2))
print(total)
if total < 10 or total > 80:
    print('your score is',+total, 'you are together like a coke and mentos ')
if total < 10 or total > 40:
    print('your score is', +total, 'you are alright together')
else:

    print('your score is',+total,'you are not match')