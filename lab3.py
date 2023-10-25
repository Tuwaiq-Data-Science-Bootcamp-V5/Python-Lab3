print("QUESTION 1:")

for element in range(45,210):
    if element==205:
        print(element)
        break;
    if element!=100:
        print(element)

print("QUESTION 2:")
while True:
    answer = input("what is the product of 7 * 24 ?")
    if answer=="168":
        print("Correct!")
        break
    else:
        print("Wrong! Try Again.")
