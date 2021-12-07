from parse import read_input_file, write_output_file
import os

def solve(tasks):
    """
    Args:
        tasks: list[Task], list of igloos to polish
    Returns:
        output: list of igloos in order of polishing  
    """
    possible = []
    for i in tasks:
        dead = i.get_deadline()
        dur = i.get_duration()
        ide = i.get_task_id()
        for n in range(dead, dead + 10):
            points = i.get_late_benefit(n - dead)
            toAdd = {'tid': ide, 'start': n - dur, 'end': n}
            rate = points/dur
            possible.append((rate, toAdd))

    possible.sort(key=lambda x: x[0], reverse=True)

    answer = []
    spaces = [-1] * 1440

    for t in possible:
        d = t[1]
        if d['tid'] in answer:
            continue
        x = spaces[d['start'] : d['end']]
        if all(elm == -1 for elm in x):
            answer.append(d['tid'])
            spaces[d['start'] : d['end']] = [d['tid']] * (d['end'] - d['start'])
        else:
            count = (d['end'] - d['start'])
            removal = []
            for i in range(0, d['start']):
                if spaces[i] == -1:
                    removal.append(i)
                if (len(removal) == count):
                    break
            if (len(removal) == count):
                for x in range(count):
                    spaces[(removal[x] - x):d['end']] = spaces[(removal[x]+1-x):d['end']] + [0]
                answer.append(d['tid'])
                spaces[d['start'] : d['end']] = [d['tid']] * (d['end'] - d['start'])

    resy = []
    for i in spaces:
        if i > 0 and i not in resy:
            resy.append(i)

    return resy




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
