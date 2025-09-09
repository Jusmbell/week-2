import numpy as np


# update/add code below ...
def ways(n):
    ways_list = []  # List to store each way as a tuple
    # Try every possible number of nickels from 0 up to n//5
    for nickels in range(n // 5 + 1):
        pennies = n - 5 * nickels  # Remaining cents must be pennies
        if pennies >= 0:
            ways_list.append((pennies, nickels))  # Add the tuple to the list
    # Print each way
    for way in ways_list:
        print(way)
    # Print the total number of ways
    print("Total ways:", len(ways_list))
    return len(ways_list)
    # Example usage:
ways(12)

def lowest_score(names, scores):
    # Find the index of the lowest score
    idx = np.argmin(scores)
    return names[idx]

def sort_names(names, scores):
    # Get indices that would sort scores in descending order
    sorted_indices = np.argsort(scores)[::-1]
    # Return names and scores sorted by descending score
    return list(zip(names[sorted_indices], scores[sorted_indices]))

# Example usage:
names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
scores = np.array([99, 71, 85, 62, 91])

print('Lowest score:', lowest_score(names, scores))
print('Sorted names and scores:', sort_names(names, scores))