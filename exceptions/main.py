# names = ["Nick","Nia","Mia"]

# try:
#     print(names[1])
# except IndexError:
#     print("Index not accessible")



# def handle_humans(human):
    
#     if(human!="animal"):
#         print("Human found")
#     else:
#         raise ValueError("Non Humans not allowed")
    

# handle_humans("Happy")    
# handle_humans("animal")    


class CustomError(Exception):
    pass

num=5 
if(num<10):
    raise CustomError("num less than 10 is not allowed")