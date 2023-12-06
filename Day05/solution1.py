class Converter:
    def __init__(self) -> None:
        self.ranges = []
    def add_range(self, range):
        self.ranges.append(range)
    def convert(self, num):
        for range in self.ranges:
            diff = num - range[1]
            if diff >= 0 and diff < range[2]:
                return range[0] + diff
        return num

with open('Day05/input.in', 'r') as file:
    lines = file.read().splitlines()

seeds = [int(x) for x in lines[0].split()]
lines = lines[1:]
converters = []

for line in lines:
    if line == '':
        converter = Converter()
        converters.append(converter)
    else:
        splitted_line = line.split()
        range = (int(splitted_line[0]), int(splitted_line[1]), int(splitted_line[2]))
        converter.add_range(range)

for converter in converters:
    seeds = [converter.convert(x) for x in seeds]

print(min(seeds))
