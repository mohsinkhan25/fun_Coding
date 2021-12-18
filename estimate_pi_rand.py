# This problem will have a random function that will output a uniform random number between 0 and 1.
# Find pi (Sounds funny right?!)

# number of points in circle / number of points overall = pi*r^2/ (2*r)^2
# Since the radius of the circle is 1, it becomes easier to estimate pi
# pi = 4*number points in circle / number of points overall

# The parameter n is the number of points we will use in the grid to estimate pi, error is less and less with more total_points

import random

def approximate_pi(n):
    '''This function returns an estimate for pi using 'n' as many points, like a circular riemann summ of some sort'''
    circle_points = 0
    total_points = 0
    for _ in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        dist = x**2 + y**2
        if dist < 1:
            circle_points += 1
        total_points += 1

    return (4 * circle_points) / total_points

while True:
    try:
        num_points = int(input('Enter an integer for the number of points used to estimate pi: '))
        break
    except:
        print('Invalid input! Enter a positive integer.')
print(approximate_pi(num_points))
help(approximate_pi)
