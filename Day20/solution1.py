


from collections import deque


class Broadcaster:
    def __init__(self, destinations, name) -> None:
        self.destinations = destinations
        self.name = name
    
    def process(self, source, pulse) -> [(str, int, str)]:
        return [(destination, 0, self.name) for destination in self.destinations]
    

class FlipFlop:
    def __init__(self, destinations, name) -> None:
        self.destinations = destinations
        self.state = 0
        self.name = name
    
    def process(self, source, pulse) -> [(str, int, str)]:
        if pulse == 1:
            return []
        
        if self.state == 0:
            self.state = 1
            return [(destination, 1, self.name) for destination in self.destinations]
        else:
            self.state = 0
            return [(destination, 0, self.name) for destination in self.destinations]

class Conjunction:
    def __init__(self, sources, destinations, name) -> None:
        self.name = name
        self.sources = {}
        for source in sources:
            self.sources[source] = 0
        self.destinations = destinations
    
    def process(self, source, pulse) -> [(str, int, str)]:
        self.sources[source] = pulse
        
        if all(element == 1 for element in self.sources.values()):
            return [(destination, 0, self.name) for destination in self.destinations]
        else:
            return [(destination, 1, self.name) for destination in self.destinations]

def run_processes(modules):
    result_low = 0
    result_high = 0

    processes = deque()
    processes.append(('broadcaster', 0, 'button'))

    while processes:
        name, pulse, source = processes.popleft()
        
        if pulse == 0:
            result_low += 1
        else:
            result_high += 1
        
        if name in modules:
            next_processes = modules[name].process(source, pulse)
            processes.extend(next_processes)
    
    return (result_low, result_high)

with open('Day20/input.in', 'r') as file:
    lines = file.read().splitlines()

sources = {}
destinations = {}

types_and_names = []
for line in lines:
    source_string, destinations_string = line.split(' -> ')
    destinations_strings = destinations_string.split(', ')
    if source_string == 'broadcaster':
        types_and_names.append(('b', source_string))
    elif source_string[0] == '%':
        source_string = source_string[1:]
        types_and_names.append(('%', source_string))
    else:
        source_string = source_string[1:]
        types_and_names.append(('&', source_string))

    if source_string in destinations:
        destinations[source_string].extend(destinations_strings)
    else:
        destinations[source_string] = destinations_strings
    
    for destination_string in destinations_strings:
        if destination_string in sources:
            sources[destination_string].append(source_string)
        else:
            sources[destination_string] = [source_string]

modules = {}
start = None
for type, name in types_and_names:
    if type == 'b':
        modules[name] = Broadcaster(destinations[name], name)
    elif type == '%':
        modules[name] = FlipFlop(destinations[name], name)
    else:
        modules[name] = Conjunction(sources[name], destinations[name], name)

result_low = 0
result_high = 0


for i in range(1000):
    rl, rh = run_processes(modules)
    result_low += rl
    result_high += rh

print(result_low*result_high)