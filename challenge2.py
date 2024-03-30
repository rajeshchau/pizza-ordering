#Given:
#Menu: small pizza(s):$15 medium pizza(m):$20 large pizza(l):$25
#Add pepperoni for small pizza(y or n) = +$2
#Add pepperoni for medium pizza(y or n) =+$3
#add chesse on any pizza =$1

print("Thanks for choosing python pizza deliveries!")
size = input("Enter the size of pizza:")
add_pepperoni = input("Wants Pepperoni in small pizza(y or n):")
add_pepperoni_m = input("Wants Pepperoni in medium pizza(y or n):")
extra_cheese = input("Wants Extra cheese in pizza (y or n):")

bill= 0

if size =="s":
    bill = 15
elif size == "m":
    bill = 20
elif size == "l":
    bill = 25
else:
    print("no pizza is ordered !")
    
if add_pepperoni == "y":
    bill +=2
elif add_pepperoni_m == "y":
    bill +=3
elif extra_cheese == "y":
    bill +=1
    
else:
    print("the bill not found!")
    
print(f"the total bill of pizza {bill}")

