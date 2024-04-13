phone_number = "123-456-7890"

# for i in phone_number:
#     if i == "-":
#         continue
#     else:
#         print(i, end="")

# print("")

# for i in phone_number:
#     if i == "0":
#         pass
#         print("hello")
#     elif i == "-":
#         pass
#     elif phone_number[int(i)] == len(phone_number) - 2:
#         print(i)
#     else:
#         print(i, end="")

for index, digit in enumerate(phone_number):
    if digit == "0":
        pass
        print("hello")
    elif digit == "-":
        pass
    elif index == len(phone_number) - 2:
        print(digit)
    else:
        print(digit, end="")

 