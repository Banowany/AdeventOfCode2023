class Converter:
    def __init__(self) -> None:
        self.ranges = []
    def add_range(self, range):
        self.ranges.append(range)
    def convert(self, num_ranges):
        waiting = num_ranges
        converted = []
        for range in self.ranges:
            tmp = []
            for wait_nr in waiting:
                min_common = max(range[1], wait_nr[0])
                max_common = min(range[1] + range[2], wait_nr[0] + wait_nr[1])
                length = max_common - min_common
                if length > 0:
                    #common_range = (min_common, length)
                    converted_range = (range[0] + (min_common - range[1]), length)
                    converted.append(converted_range)
                    if wait_nr[0] < min_common:
                        tmp.append((wait_nr[0], min_common - wait_nr[0]))
                    if max_common < wait_nr[0] + wait_nr[1]:
                        tmp.append((max_common, wait_nr[0] + wait_nr[1] - max_common))
                else:
                    tmp.append(wait_nr)
            waiting = tmp
        
        converted.extend(waiting)
        return converted

with open('Day05/input.in', 'r') as file:
    lines = file.read().splitlines()

seeds_with_range = [int(x) for x in lines[0].split()]
paired_seeds_with_range = [(seeds_with_range[i], seeds_with_range[i+1]) for i in range(0, len(seeds_with_range), 2)]
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
    paired_seeds_with_range = converter.convert(paired_seeds_with_range)

print(min(paired_seeds_with_range, key=lambda x: x[0]))
