from __future__ import print_function

def recursive_unique_stair_climbs(step_sizes, steps):
    if steps < 0:
        return 0
    if steps == 0:
        return 1
    if steps in step_sizes:
        return 1 + sum(recursive_unique_stair_climbs(step_sizes, steps-s)
                for s in step_sizes if s < steps)
    return sum(recursive_unique_stair_climbs(step_sizes, steps-s)
            for s in step_sizes if s < steps)

def opt_unique_stair_climbs(step_size, steps):
    dp = [0 for _ in range(steps+1)]
    dp[0] = 1

    for i in range(steps+1):
        dp[i] += 1 if i in step_sizes else 0
        dp[i] += sum(dp[i-s] for s in step_sizes if i-s > 0)

    return dp[-1]

if __name__ == '__main__':
    step_sizes = [1,2]
    steps = 4

    assert recursive_unique_stair_climbs(step_sizes, steps) == 5
    assert opt_unique_stair_climbs(step_sizes, steps) == 5
