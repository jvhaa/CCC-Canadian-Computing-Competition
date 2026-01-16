# Read the number of interested people
num_people = int(input())

# Initialize a list to keep track of the count of interested people for each day
count_per_day = [0] * 5

# Read the availability for each person and update the count per day
for _ in range(num_people):
    availability = input()
    for day, status in enumerate(availability):
        if status == 'Y':
            count_per_day[day] += 1

# Find the maximum count of interested people
max_count = max(count_per_day)

# Find the days with the maximum count
best_days = [str(day + 1) for day, count in enumerate(count_per_day) if count == max_count]

# Print the days with the maximum count
print(','.join(best_days))
