class ProductionSet:
    def __init__(self):
        self.hash_map = {}
        self.isCFG = True

    def getSet(self):
        return self.hash_map

    def getKeys(self):
        return self.hash_map.keys()

    def getValue(self, key):
        return self.hash_map.get(key)

    def getIsCFG(self):
        return self.isCFG

    def addProduction(self, key, values):
        if key not in self.hash_map.keys():
            self.hash_map[key] = []
        else:
            self.isCFG = False
        self.hash_map[key].extend(values)

    def __str__(self):
        hash_map = ""
        for i in self.hash_map.keys():
            hash_map += "{'"
            hash_map += i
            hash_map += "': "
            hash_map += str(self.hash_map[i])
            hash_map += "}, "
        # hash_map += "}"
        return hash_map
