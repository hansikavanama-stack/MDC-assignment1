#3. Generate a dictionary containing numbers and their squares
n = int(input("Enter a number: "))

dictionary = {}

for i in range(1, n + 1):
    dictionary[i] = i * i

print(dictionary)
