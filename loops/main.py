# for i in range(1,11):
#     print(i)


# names = ["Mia","Nia","Emily","Jack"]
# for name in names:
#     print(f"Hello {name}")

# menu = ["Rice","Roti","Tofu","Jalebi"]
# print(list(enumerate(menu,start=1)))
# for idx, item in enumerate(menu,start=1):
#     print(f"Item is {item}")

# names = ["Mia","Nia","Emily","Jack"]
# salary = ["10000","20000","30000","40000"]

# for name, s in zip(names,salary):
#     print(f"{name} gets ${s}")

# Walrus Operator

base = 5
if (sum := 50-base):
    print(sum)