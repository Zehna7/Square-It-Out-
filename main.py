start, end = int(input("Enter the start: ")), int(input("Enter the end: "))

squares = [i**2 for i in range(start, end + 1)]
odd_squares = [x for x in squares if x % 2]
even_squares = [x for x in squares if x % 2 == 0]

print("Odd squares are:", odd_squares)
print("Even squares are:", even_squares)