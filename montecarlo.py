import random

#Check if the point (x, y) is inside the quarter circle.
def in_circle(x, y):
    return (x*x + y*y) <= (0.5*0.5)

# Initialize variables
true_count = 0
total_count = 0
num = 1

for _ in range(7):
    num *= 10  # Update the sample count at the beginning
    count = 0  # Counter for the while loop

    while count < num:
        x = random.random() - 0.5
        y = random.random() - 0.5
        if in_circle(x, y):
            true_count += 1
        total_count += 1
        count += 1

    approx_pi = 4 * true_count / total_count
    print('{:>15d}{:>13s}{:>9d}{:>13s}{:>12.9f}'.format(num, "円の内側の数：", true_count, "πの近似値：", approx_pi))
