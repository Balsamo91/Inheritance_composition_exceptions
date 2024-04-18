# import sys

# user_input = int(input("provide a birth year: "))

# try:
#     age = 2024 - user_input
# except Exception as e:
#     print(f"Calculation failed! Reason: {e} ")
#     sys.exit(1)

# print(f"Your age is: {age}")

####################################################

# import sys

# while True:
#     try:
#         user_input = int(input("provide a birth year: "))
#         # break
#     except ValueError:
#         print("\nYou need to provide a number!\n")
#     except Exception as e:
#         print(f"Program failed! reason: {e}")
#         sys.exit(1)
#     else:
#         print("This works fine!")
#         break
# age = 2024 - user_input
# print(f"Your age is: {age}")
        




import sys

while True:
    try:
        user_input = int(input("provide a birth year: "))
        # break
    except ValueError:
        print("\nYou need to provide a number!\n")
    except Exception as e:
        print(f"Program failed! reason: {e}")
        sys.exit(1)
    else:
        print("This works fine!")
        break
    finally:
        print("\nFinally is used and it will always works!\n")


age = 2024 - user_input
print(f"Your age is: {age}")
        
