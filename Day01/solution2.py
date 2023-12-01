import re

templates = {}

templates['1'] = 1
templates['one'] = 1

templates['2'] = 2
templates['two'] = 2

templates['3'] = 3
templates['three'] = 3

templates['4'] = 4
templates['four'] = 4

templates['5'] = 5
templates['five'] = 5

templates['6'] = 6
templates['six'] = 6

templates['7'] = 7
templates['seven'] = 7

templates['8'] = 8
templates['eight'] = 8

templates['9'] = 9
templates['nine'] = 9


def get_calibration_value(word):
    all_finded_templates = []
    for template, value in templates.items():
        finded_templates = [(match.start(), value) for match in re.finditer(template, word)]
        all_finded_templates.extend(finded_templates)
    begin = min(all_finded_templates, key=lambda x: x[0])[1]
    end = max(all_finded_templates, key=lambda x: x[0])[1]
    return begin*10 + end





with open('input', 'r') as plik:
    wyrazy = plik.read().splitlines()

print([match.start() for match in re.finditer('two', wyrazy[0])])

wyniki = [get_calibration_value(x) for x in wyrazy]

print(wyniki)
print(sum(wyniki))
