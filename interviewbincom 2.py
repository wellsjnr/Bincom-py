
import re
from collections import Counter
import statistics
import psycopg2
import random

# Extract colors from HTML data
html_data = """
... (insert the HTML data here)
"""

colors = re.findall(r'\b\w+\b', html_data)
colors = [color for color in colors if color.upper() in ['RED', 'GREEN', 'BLUE', 'YELLOW', 'BROWN', 'PINK', 'ORANGE', 'CREAM', 'WHITE', 'BLACK']]

# 1. Mean color
mean_color = statistics.mean([1 if color == 'RED' else 0 for color in colors])
print("Mean color:", mean_color)

# 2. Most worn color
most_worn_color = Counter(colors).most_common(1)[0][0]
print("Most worn color:", most_worn_color)

# 3. Median color
median_color = statistics.median([1 if color == 'RED' else 0 for color in colors])
print("Median color:", median_color)

# 4. BONUS: Variance of colors
variance_colors = statistics.variance([1 if color == 'RED' else 0 for color in colors])
print("Variance of colors:", variance_colors)

# 5. BONUS: Probability of choosing red
probability_red = Counter(colors)['RED'] / len(colors)
print("Probability of choosing red:", probability_red)

# 6. Save colors and frequencies in PostgreSQL database
conn = psycopg2.connect(
    dbname="your_database",
    user="your_username",
    password="your_password",
    host="your_host",
    port="your_port"
)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS colors (color TEXT, frequency INTEGER)")
color_frequencies = Counter(colors)
for color, frequency in color_frequencies.items():
    cur.execute("INSERT INTO colors VALUES (%s, %s)", (color, frequency))
conn.commit()
conn.close()

# 7. BONUS: Recursive searching algorithm
def recursive_search(lst, target):
    if len(lst) == 0:
        return False
    elif lst[0] == target:
        return True
    else:
        return recursive_search(lst[1:], target)

numbers = [1, 2, 3, 4, 5]
target = 3
print("Recursive search result:", recursive_search(numbers, target))

# 8. Generate random 4-digit binary number and convert to base 10
binary_number = ''.join(random.choice('01') for _ in range(4))
decimal_number = int(binary_number, 2)
print("Random binary number:", binary_number)
print("Decimal equivalent:", decimal_number)

# 9. Sum of first 50 Fibonacci numbers
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci_sum = sum(fibonacci(i) for i in range(50))
print("Sum of first 50 Fibonacci numbers:", fibonacci_sum)
