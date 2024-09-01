import random
print("choose your password complexity: \n1. SuperStrong \n2. Strong \n3. Medium \n4. Weak")
lower="qwertyuiopasdfghjklzxcvbnm"
#print(len(lower))
upper="QWERTYUIOPASDFGHJKLZXCVBNM"
#print(len(upper))
num="1234567890"
spchr="!@#$%^&*()~[]}{<>?/"
bum=lower+upper
all=lower + upper + spchr + num
gum=lower+upper+num
types=input("Enter your password complexity: ")
m=types.lower()
length=int(input("Enter the length of your password: "))
if m=="weak":
    password="".join(random.sample(num,length))
    print(f"your {types} password is :{password}")
elif m=="medium":
    password = "".join(random.sample(bum, length))
    print(f"your {types} password is :{password}")
elif m=="strong":
    password = "".join(random.sample(gum, length))
    print(f"your {types} password is :{password}")
elif m=="superstrong" or m=="super strong":
    password="".join(random.sample(all,length))
    print(f"your {types} password is :{password}")
else:
    print("invalid option")
