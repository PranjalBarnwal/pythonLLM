#Objects (Concept of Mutable vs Immutable)

# amount = 1
# print(f"The sugar is {amount}")
# print(f"The sugar is {id(amount)}")

# destination = set()
# destination.add("Manali")
# print(f"Destination set is {destination} and the id is {id(destination)}")
# destination.add("Delhi")
# print(f"Destination set is {destination} and the id is {id(destination)}")

#Numbers

# quantity = 2
# litre = 3
# # total = quantity + litre
# # total = quantity / litre
# # total = quantity // litre
# # total = quantity % litre
# # total = quantity ** litre
# # print(f"total is {total}")

# billion = 1_000_000_000
# print(f"printing very large no., {(billion)}")


#Boolean

# is_True = True #True is treated as 1 for calculation
# count = 0
# print(is_True+count)

# print(f"Is it true, {bool(count)}")



# Logical Operators(and, or, not)

# is_Male = False
# is_Young = True

# can_jump = is_Male and is_Young
# print(can_jump)


# Floating Numbers

# long_decimal = 1.9999999999
# print(type(long_decimal))




#Strings

# name = "Pranjal"
# print(name[0:5:2])


#Tuples

# name = ("Happy","Honey","Bill")
# (n1,n2,n3) = name
# print(n1,n2)

# if("Happy" in name):
#     print("True")
# print(type(name))

#Mutable Datatypes

#List
# names = ["Mia","Emily","Jack"]
# names2 = ["Honey","Pandey"]

# names.append("Happy")

# names.remove("Mia")

# names.extend(names2)
# names2.insert(1,"Bill")

# popped = names2.pop()
# names2.reverse()
# names.sort()
# print(max(names))


#Operator Overloading

# name = ["Happy","Pranjal"]
# name2 = 2

# print(name*name2)

#Set

# name = {"Bill","Mia","Gill","Bill"}
# name2 = {"Dill","Rill","Mia"}
# print(name - name2)
# print(name | name2)
# print(name & name2)
# print(type(name))



# Dictionary

user = dict(name="Happy",role="Admin")
print(user)
print(type(user))

user2={}
user2["name"] = "Mia"
user2["role"] = "User"
user2["isAdmin"] = False

print(user2.keys())
print(user2.values())
# del user2["role"]
# print("isAdmin" in user2)