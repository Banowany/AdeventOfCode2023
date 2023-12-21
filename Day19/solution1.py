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

accepted = []
for part in parts:
    workflow_result = workflows['in'].perform(part)
    while workflow_result != 'A' and workflow_result != 'R':
        workflow_result = workflows[workflow_result].perform(part)
    if workflow_result == 'A':
        accepted.append(part)

print(sum([part.sum() for part in accepted]))