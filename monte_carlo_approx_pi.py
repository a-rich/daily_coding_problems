from __future__ import print_function
import random

def monte_carlo_approx_pi(points):
    inside = outside = 0.0
    for _ in range(points):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1:
            inside += 1
            outside += 1
        else:
            outside += 1

    return 4 * (inside/outside)

if __name__ == '__main__':
    print(monte_carlo_approx_pi(1000000))
