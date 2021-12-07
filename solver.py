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


def getMaxProfit(tasks):
    dp = [len(tasks) + 1][1440 + 1]
    for t in range(0, 1440 + 1):
        dp[0][t] = 0

    # Go through every igloo/task
    for i in range(1, len(tasks) + 1):
        # Go through every t 0->1440 inclusive
        for t in range(0, 1441):
            startTime = t - tasks[i - 1].get_duration()
            if startTime < 0:
                dp[i][t] = dp[i - 1][t]
            else:
                potentialProfit = tasks[i].get_late_benefit(max(0, t - tasks[i - 1].get_deadline()))
                dp[i][t] = max(dp[i-1][t], potentialProfit + dp[i - 1][t])
    return dp

    


# Here's an example of how to run your solver.
# if __name__ == '__main__':
#     for size in os.listdir('inputs/'):
#         if size not in ['small', 'medium', 'large']:
#             continue
#         for input_file in os.listdir('inputs/{}/'.format(size)):
#             if size not in input_file:
#                 continue
#             input_path = 'inputs/{}/{}'.format(size, input_file)
#             output_path = 'outputs/{}/{}.out'.format(size, input_file[:-3])
#             print(input_path, output_path)
#             tasks = read_input_file(input_path)
#             output = solve(tasks)
#             write_output_file(output_path, output)