from itertools import product

# Define the denominations and their counts
denominations = [20, 10, 5, 1]
max_counts = [3, 5, 2, 5]


# Function to check if a combination sums to the target amount
def valid_combination(combo, target=100):
    return sum(denom * count for denom, count in zip(denominations, combo)) == target


# Generate all possible combinations of counts within the max counts
possible_combinations = product(*(range(count + 1) for count in max_counts))

# Filter valid combinations and sort each combination to avoid duplicates
valid_combinations = set(map(tuple, map(sorted, filter(valid_combination, possible_combinations))))
# Print all valid combinations
for combo in valid_combinations:
    print(combo)

# Print the number of valid combinations
print(f"Number of combinations: {len(valid_combinations)}")
