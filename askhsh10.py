list = []
import fileinput
with fileinput.input() as f:
    for line in f:
        for x in line:
            list.append('{0:07b}'.format(ord(x)))
#print(list)

for i in range(0,len(list)):
    bit = list[i]
    bit = bit[0]+bit[1]+bit[5]+bit[6]
    list[i] = bit

#print(list)

num_list = []

n = len(list)

while(n % 8):
    list.append('{0:04b}'.format(0))
    n += 1

for i in range(0,n,4):
    str = list[i]+list[i+1]+list[i+2]+list[i+3]
    num = int(str,2)
    num_list.append(num)

size = len(num_list)
two = 0
three = 0
five = 0
seven = 0

for num in num_list:
    if num % 2 == 0 :
        two += 1
    if num % 3 == 0 :
        three += 1
    if num % 5 == 0 :
        five += 1
    if num % 7 == 0 :
        seven += 1
    

print("divided by two {}%".format(two/size*100))
print("divided by three {}%".format(three/size*100))
print("divided by five {}%".format(five/size*100))
print("divided by seven{}%".format(seven/size*100))