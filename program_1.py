# Eliya Statema
# 3/21/25
# Initials

print("This program will print your initials.")

def main():
    full_name = input("Enter your full name: ")

    name = full_name.split()

    for string in name:
        print(string[0].upper(), sep=" ", end="")
        print(".", sep="", end="")

if __name__ == "__main__":
    main()