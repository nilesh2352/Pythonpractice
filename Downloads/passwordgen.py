letters = [ 'a' ,'b', 'c', 'd' ,'e']
num = ['1','2','3','4','5']
sy =['!','@','#','$', '%']

nr_letters= int(input("how many letter you want\n"))
nr_num = int(input("how many num you want\n"))
nr_sy = int(input("how many sy you want\n"))

import random2
pass_list = []
for char in range(1,nr_letters +1):
  pass_list.append(random2.choice(letters))

for char in range(1,nr_num + 1):
 pass_list.append(random2.choice(num))

for char in range(1,nr_sy +1):
 pass_list.append(random2.choice(sy))

print(pass_list)
random2.shuffle(pass_list)

print(pass_list)

password = ""
for char in pass_list:
  password += char
print(f"Your password is :{password}")

      

