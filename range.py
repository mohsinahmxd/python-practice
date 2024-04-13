import time

# num_range = range(1, 6)
# for num in num_range:
#     print(num)
#     time.sleep(1)

# print("Countdown done!")

# for num in range(4, 17, 2): # 3rd arg is the step
#     print(num)

rows = int(input("How many rows "))
columns = int(input("How many columns "))
symbol = (input("Please choose a symbol "))

for row in range(0, rows):
    for column in range(0, columns):
        print(symbol, end="")
    print()