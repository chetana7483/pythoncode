n = int(input())
spaces = n - 1
stars = 1
for row in range(1, n + 1):
  for space in range(spaces):
      print(" ", end = " ")
  spaces -= 1
   for star in range(stars):
      print("*", end = " ")
  stars += 2
  print()
 stars -= 4
spaces = 1




for row in range(1, n):
  for space in range(spaces):
      print(" ", end = " ")
  spaces += 1
   for star in range(stars):
      print("*", end = " ")
  stars -= 2
  print()

Pattern-Twenty solution

