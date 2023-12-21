import re


class Part:
    def __init__(self, x, m, a, s) -> None:
        self.x = x
        self.m = m
        self.a = a
        self.s = s
    def sum(self):
        return self.x + self.m + self.a + self.s

class Workflow:
    def __init__(self, actions_parameters) -> None:
        self.actions_parameters = actions_parameters
    def perform(self, part: Part) -> str:
        for elem, comparison_sign, num, excepted_result in self.actions_parameters:
            result = action_function(part, elem, comparison_sign, num, excepted_result)
            if result is None:
                continue
            else:
                return result

def action_function(part, elem, comparison_sign, num, result):
    if elem == None and comparison_sign == None and num == None:
        return result
    
    if elem == 'x' and comparison_sign == '<':
        function_result = result if part.x < num else None
    elif elem == 'x' and comparison_sign == '>':
        function_result = result if part.x > num else None
    elif elem == 'm' and comparison_sign == '<':
        function_result = result if part.m < num else None
    elif elem == 'm' and comparison_sign == '>':
        function_result = result if part.m > num else None
    elif elem == 'a' and comparison_sign == '<':
        function_result = result if part.a < num else None
    elif elem == 'a' and comparison_sign == '>':
        function_result = result if part.a > num else None
    elif elem == 's' and comparison_sign == '<':
        function_result = result if part.s < num else None
    else:
        function_result = result if part.s > num else None
    
    return function_result


def covert_to_workflow(workflow_as_string):
    match_outside = re.match(r'(\w+){(.+)}', workflow_as_string)
    name = match_outside.group(1)
    rules = match_outside.group(2)
    rules = rules.split(',')
    actions_parameters = []
    for rule in rules:
        match_rule = re.match(r'(\w+)(<|>)(\d+):(\w+)', rule)
        if match_rule:
            comparison_elem = match_rule.group(1)
            comparison_sign = match_rule.group(2)
            comparison_num = int(match_rule.group(3))
            comparison_result = match_rule.group(4)

            action_parameters = (comparison_elem, comparison_sign, comparison_num, comparison_result)
        else:
            action_parameters = (None, None, None, rule)
        actions_parameters.append(action_parameters)
    return (name, Workflow(actions_parameters))

def convert_to_part(part_as_string):
    match_part = re.match(r'{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}', part_as_string)
    x = int(match_part.group(1))
    m = int(match_part.group(2))
    a = int(match_part.group(3))
    s = int(match_part.group(4))
    return Part(x, m, a, s)

def count_combinations(workflows, curr_workflow, minx, maxx, minm, maxm, mina, maxa, mins, maxs):
    if minx <= 0 or maxx <= 0 or minm <= 0 or maxm <= 0 or mina <= 0 or maxa <= 0 or mins <= 0 or maxs <= 0:
        return 0
    if curr_workflow == 'A':
        return (maxx - minx + 1) * (maxm - minm + 1) * (maxa - mina + 1) * (maxs - mins + 1)
    if curr_workflow == 'R':
        return 0
    
    result = 0
    for (elem, sign, num, expected) in workflows[curr_workflow].actions_parameters:
        if (elem is None) and (sign is None) and (num is None):
            result += count_combinations(workflows, expected, minx, maxx, minm, maxm, mina, maxa, mins, maxs)
        elif elem == 'x' and sign == '<':
            result += count_combinations(workflows, expected, minx, min(maxx, num-1), minm, maxm, mina, maxa, mins, maxs)
            minx = max(num, minx)
        elif elem == 'x' and sign == '>':
            result += count_combinations(workflows, expected, max(minx, num+1), maxx, minm, maxm, mina, maxa, mins, maxs)
            maxx = min(num, maxx)
        elif elem == 'm' and sign == '<':
            result += count_combinations(workflows, expected, minx, maxx, minm, min(maxm, num-1), mina, maxa, mins, maxs)
            minm = max(num, minm)
        elif elem == 'm' and sign == '>':
            result += count_combinations(workflows, expected, minx, maxx, max(minm, num+1), maxm, mina, maxa, mins, maxs)
            maxm = min(num, maxm)
        elif elem == 'a' and sign == '<':
            result += count_combinations(workflows, expected, minx, maxx, minm, maxm, mina, min(maxa, num-1), mins, maxs)
            mina = max(num, mina)
        elif elem == 'a' and sign == '>':
            result += count_combinations(workflows, expected, minx, maxx, minm, maxm, max(mina, num+1), maxa, mins, maxs)
            maxa = min(num, maxa)
        elif elem == 's' and sign == '<':
            result += count_combinations(workflows, expected, minx, maxx, minm, maxm, mina, maxa, mins, min(maxs, num-1))
            mins = max(num, mins)
        elif elem == 's' and sign == '>':
            result += count_combinations(workflows, expected, minx, maxx, minm, maxm, mina, maxa, max(num+1, mins), maxs)
            maxs = min(num, maxs)
        
    return result
    




with open('Day19/input.in', 'r') as file:
    lines = file.read().splitlines()

workflows_as_strings = []
parts_as_strings = []
is_blank_met = False
for line in lines:
    if line == '':
        is_blank_met = True
        continue

    if is_blank_met:
        parts_as_strings.append(line)
    else:
        workflows_as_strings.append(line)

workflows = {}
for workflow_as_string in workflows_as_strings:
    name, workflow = covert_to_workflow(workflow_as_string)
    workflows[name] = workflow

parts = [convert_to_part(x) for x in parts_as_strings]

print(count_combinations(workflows, 'in', 1, 4000, 1, 4000, 1, 4000, 1, 4000))