# Read input
river_length = int(input())
num_animals = int(input())

# Initialize a list to store occupied river segments
occupied_segments = []

# Read and store the segments occupied by animals
for _ in range(num_animals):
    start, end = map(int, input().split())
    occupied_segments.append((start, end))

# Sort the occupied segments by their start positions
occupied_segments.sort()

# Initialize variables to keep track of the longest unoccupied segment
max_unoccupied_length = 0
current_start = 0

# Iterate through the occupied segments to find the longest unoccupied segment
for start, end in occupied_segments:
    if start > current_start:
        max_unoccupied_length = max(max_unoccupied_length, start - current_start)
    current_start = max(current_start, end)

# Check if there's unoccupied river at the end
if current_start < river_length:
    max_unoccupied_length = max(max_unoccupied_length, river_length - current_start)

# Print the result
print(max_unoccupied_length)
