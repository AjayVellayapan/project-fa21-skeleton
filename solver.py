from parse import read_input_file, write_output_file
import os

def solve(tasks):
    """
    Args:
        tasks: list[Task], list of igloos to polish
    Returns:
        output: list of igloos in order of polishing  
    """
    postProcessArray = getMaxProfit(tasks)
    result = []
    goThrough(postProcessArray, result, len(tasks) - 1, 1440, tasks)
    return result


def getMaxProfit(tasks):
    dp = [([0] * 1441) for _ in range(len(tasks) + 1)]
    for t in range(0, 1440 + 1):
        dp[-1][t] = 0

    # Go through every igloo/task
    for i in range(len(tasks)):
        # Go through every t 0->1440 inclusive
        for t in range(0, 1441):
            startTime = t - tasks[i].get_duration()
            if startTime < 0:
                dp[i][t] = dp[i - 1][t]
            else:
                potentialProfit = tasks[i].get_late_benefit(max(0, t - tasks[i].get_deadline()))
                dp[i][t] = max(dp[i-1][t], potentialProfit + dp[i - 1][t])
    return dp

def goThrough(dp, res, i, t, tasks):

    if i == -1:
        return
    if dp[i-1][t] == dp[i][t]:
        goThrough(dp, res, i-1, t, tasks)
    else:
        newT = min(t, tasks[i].get_deadline()) - tasks[i].get_duration
        goThrough(dp, res, i - 1, newT, tasks)
        res.append(i)
       




# Here's an example of how to run your solver.
if __name__ == '__main__':
    for size in os.listdir('inputs/'):
        if size not in ['small', 'medium', 'large']:
            continue
        for input_file in os.listdir('inputs/{}/'.format(size)):
            if size not in input_file:
                continue
            input_path = 'inputs/{}/{}'.format(size, input_file)
            output_path = 'outputs/{}/{}.out'.format(size, input_file[:-3])
            print(input_path, output_path)
            tasks = read_input_file(input_path)
            output = solve(tasks)
            write_output_file(output_path, output)