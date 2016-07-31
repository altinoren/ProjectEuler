even_sum = 2

first = 1
second = 2
third = 3

while third < 4000000:
    if third % 2 == 0:
        even_sum = even_sum + third
    first = second
    second = third
    third = first + second

print(even_sum)