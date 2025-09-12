# Zander size limit check
zander_length = int(input("Enter the length of the zander in centimeters: "))

if zander_length < 42:
    difference = 42 - zander_length
    print(f"Release the fish back into the lake. It is {difference} cm below the size limit.")
else:
    print("The fish meets the size limit.")


