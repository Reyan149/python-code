
limit = int(input("Enter limit: "))
total_sum = 0
start = 1

while start <= limit:
    total_sum += total_sum + start
    start += 1

print(f"The sum of numbers from 1 to {limit} is: {total_sum}")