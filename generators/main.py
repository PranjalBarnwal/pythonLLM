# def get_name():
#     yield "Happy"
#     yield "Mia"
#     yield "Nia"

# name = get_name()
# print(name)    
# print(next(name))    
# print(next(name))    
# print(next(name))    



# def infinite_count():
#     count=1
#     while True:
#         yield count
#         count+=1    

# counter = infinite_count()

# for i in range(5):
#     print(next(counter))


# def get_name():
#     print("Looking for a name")
#     name = yield
#     while True:
#         print(name)
#         name = yield

# name_yielder = get_name()
# next(name_yielder) #start the generator
# name_yielder.send("Nick")        
# name_yielder.send("Mia")        



#Decorators

