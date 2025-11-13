file = open('Codingal.txt', 'r')
print("reading first line.......")
print(file.readline())
file.close()

file = open('Codingal.txt', 'r')
print("Reading multiple lines......")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file = open('Codingal.txt', 'r')
print("Looping through the lines......")
for line in file:
    print(line)
file.close()

file = open('Codingal.txt', 'r')
print("Looping through the lines......")
for f in file.readlines():
    print(f)
file.close()