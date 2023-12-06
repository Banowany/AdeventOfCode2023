class Converter:
    def __init__(self) -> None:
        self.mapping_ranges = []
    def add_mapping_range(self, mapping_range):
        self.mapping_ranges.append(mapping_range)
    
    def get_common_range(self, range1, range2):
        begin = max(range1[0], range2[0])
        end = min(range1[0] + range1[1] - 1, range2[0] + range2[1] - 1)
        if end - begin >= 0:
            return (begin, end - begin + 1)
        else:
            return None
    
    def translate_range(self, range, mapping_range):
        how_far = range[0] - mapping_range[1]
        return (mapping_range[0] + how_far, range[1])
    
    def get_before_range(self, orginal_range, common_range):
        how_far_from_begin = common_range[0] - orginal_range[0]
        if how_far_from_begin > 0:
            return (orginal_range[0], how_far_from_begin)
        else:
            return None

    def get_after_range(self, orginal_range, common_range):
        how_far_from_end = (orginal_range[0] + orginal_range[1] - 1) - (common_range[0] + common_range[1] - 1)
        if how_far_from_end == 0:
            return None
        else:
            return (common_range[0] + common_range[1], how_far_from_end)

    def convert(self, ranges):
        #range -> przed common, common, po common
        # jesli istnieje common
        translated_ranges = []
        for mapping_range in self.mapping_ranges:
            tmp_ranges = []
            for range in ranges:
                common_range = self.get_common_range(range, (mapping_range[1], mapping_range[2]))
                if common_range is None:
                    tmp_ranges.append(range)
                else:
                    translated_range = self.translate_range(range, mapping_range)
                    translated_ranges.append(translated_range)
                    before_range = self.get_before_range(range, common_range)
                    after_range = self.get_after_range(range, common_range)
                    if before_range is not None:
                        tmp_ranges.append(before_range)
                    if after_range is not None:
                        tmp_ranges.append(after_range)
            ranges = tmp_ranges
        translated_ranges.extend(ranges)
        return translated_ranges
                    



        

with open('Day05/example.in', 'r') as file:
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
        converter.add_mapping_range(range)

for converter in converters:
    paired_seeds_with_range = converter.convert(paired_seeds_with_range)

print(min(paired_seeds_with_range, key=lambda x: x[0]))
