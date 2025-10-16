# list comprehension
# names = ["Mohit","Nia","Mukesh","Goku","Bheem"]

# filtered_names = [name for name in names if not name.startswith("M")]
# print(filtered_names)


#set comprehension

# names = ["Mohit","Nia","Mukesh","Goku","Bheem","Mohit"]

# unique_names = {name for name in names if name.startswith("Moh")}
# print(unique_names)


# user_fav_colours = {
#     "Pranjal":["Red","Green","Yellow"],
#     "Mia":["Red","Green","Magenta"],
#     "Nick":["Orange","Cyan","Purple"]
# }

# unique_colours = {colour for colours in user_fav_colours.values() for colour in colours}
# print(unique_colours)



#dict comprehension

# user_salary = {
#     "Nia":20000,
#     "Mia":30000,
#     "Nick":10000,
# }

# salary_in_usd = {name:salary/80 for name,salary in user_salary.items()}

# print(salary_in_usd)


#Generator comprehension

savings =[100,200,300,400]
total_savings = sum(saving for saving in savings if saving>200)
print(total_savings)