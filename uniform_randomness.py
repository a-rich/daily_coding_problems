import random
import matplotlib.pyplot as plt

def rand5():
    return random.randint(1,5)

def rand7():
    num = 5*rand5() + rand5()-5
    if num < 22:
        return num % 7 + 1
    return rand7()

if __name__ == '__main__':
    nums = [rand7() for _ in range(100000)]
    plt.hist(nums, bins=7, density=True)
    plt.show()
