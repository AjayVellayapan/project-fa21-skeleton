from parse import read_input_file, write_output_file
import os

def solve(tasks):
    """
    Args:
        tasks: list[Task], list of igloos to polish
    Returns:
        output: list of igloos in order of polishing  
    """
    possible = {}
    for i in tasks:
    	d = i.get_duration();
    	dead = i.get_deadline();
    	ide = i.get_task_id();

    	for j in range(d, 1440):
    		toAdd = {start: j - d, end: j, profit: i.get_late_benefit(max(0, j - end)), ID: ide}
    		possible.push(toAdd)

    


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