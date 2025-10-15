# kettle_boiled = False
# if kettle_boiled:
#     print("Make Chai")


# snack = input("Which snack?")
# if snack.lower() in ["samosa","cookies"]:
#     print("order confirm")
# else:
#     print("Unavailable")    

# size = input("Preferred coffee size?").lower()
# if size=="small":
#     print("MRP 10")
# elif size=="medium":
#     print("MRP 20")
# elif size=="large":
#     print("MRP 30")
# else:
#     print("Invalid size")

# order_amount = int(input("Enter order amount: "))
# if(order_amount>300):
#     print("Delivery is free")
# else:
#     order_amount+=30
#     print("Delivery fee added")


# order_amount += 30 if order_amount<=300 else 0
# print(f"Order amount: {order_amount}")


seat_type = input("Select form sleeper, AC, luxury: ").lower()

match seat_type:
    case "sleeper":
        print("Bad experience")
    case "ac":
        print("Good experience")
    case "luxury":
        print("Hole found in wallet")
    case _:
        print("Invalid selection")

