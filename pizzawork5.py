dict ={
    'small pizza':{'name':'RS','price':150},
    'medium pizza':{'name':'RS','price':200},
    'large pizza':{'name':'RS','price':250},
    'pepperoni small pizza':{'name':'RS','price':20},
    'pepperoni medium or large pizza':{'name':'RS','price':30},
    'extra cheese':{'name':'RS','price':10}
     }
for i in dict.keys():
    print(i + ' : ', dict[i]['name'] + ' : ' + str(dict[i]['price']))
sum=[]
dic={}
total=[]
while True:
    user=input("Enter your choice:")
    condition=input("Do you want to add toppings [yes / no ?]")
    dic[user]=dict[user]
    if condition == 'no':
        break
amount=[]
for j in dic.keys():
    amount.append(dic[j]['price'])

bill=0
for k in amount:
    bill=bill+k
print(' ')
print('Total Amount= RS',bill)








