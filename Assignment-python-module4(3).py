numbers = []
while True:
    s = input("Enter a number (empty to quit): ")
    if s == "":
        break
    numbers.append(float(s))

if numbers:  # only print if we have at least one number
    print("Smallest:", min(numbers))
    print("Largest:", max(numbers))
else:
    print("No numbers entered.")
