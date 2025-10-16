# def print_details(name,salary):
#     print(f"{name}: {type(salary)}")

# print_details("Happy",20000)
# print_details("Hap",10000)

# name = "Happy"
# def update_name():
#     name = "Mia"
#     def update2():
#        nonlocal name
#        name = "Nanako"
#     update2()
#     print(name)    

# print(name)    

# update_name()


# def print_participants(*male,**female):
#     print("Male",male)
#     print("Fale",female)

# print_participants("Jack","James","John",name="Mia",name2 ="Nia")


users = ["Happy","Soney","Helly","Mia"]

print(list(filter(lambda name: name.startswith("H"),users)))