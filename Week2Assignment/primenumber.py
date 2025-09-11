
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

middle_five = prime_numbers[2:7]
print(middle_five)

count = 0
every_second_prime=[]
while(count < len(prime_numbers)):
    every_second_prime.append(prime_numbers[count])
    count += 2
print(every_second_prime)

last_three_prime = prime_numbers[-3:]
print(last_three_prime)

count=len(prime_numbers) - 1
reverse_order = []
while(count >= 0):
    reverse_order.append(prime_numbers[count])
    count = count - 1
print(reverse_order)

descending_sort = sorted(prime_numbers, reverse=True)
print(descending_sort)