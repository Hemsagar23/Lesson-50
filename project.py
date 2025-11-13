file = open("project.txt", "r")

print("1. Read full content")
print("2. Read first line")
print("3. Read all lines")
print("4. Read first 20 characters")

choice = input("Enter choice (1-4): ")

if choice == "1":
    print(file.read())
elif choice == "2":
    print(file.readline())
elif choice == "3":
    print(file.readlines())
elif choice == "4":
    print(file.read(20))
else:
    print("Invalid choice.")

file.close()
