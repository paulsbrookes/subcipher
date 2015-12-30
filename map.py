from functions2 import rm_duplicate_arrays

class Map(object):
    def __init__(self, map):
        self.map = map

    def invert(self):
        inverted_map = np.zeros(self.map.size)
        for x in range(self.map.size):
            inverted_map[self.map[x]] = x
        self.map = inverted_map

    def proliferate(self, proliferation_functions):
        new_maps = [self.map]
        for function in proliferation_functions:
            new_maps += function(self.map)
        new_maps = rm_duplicate_arrays(new_maps)
        return new_maps
