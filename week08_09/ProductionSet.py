class ProductionSet:
    def __init__(self):
        self.hashMap = {}

    def getProductionSet(self):
        return self.hashMap

    def check_CFG(self):
        for key in self.hashMap.keys():
            if len(key) > 1:
                return False
        return True

    def addProduction(self, key, values):
        if key not in self.hashMap.keys():
            self.hashMap[key] = []
        self.hashMap[key].extend(values)

    def toString(self):
        hash_map = ""
        for i in self.hashMap.keys():
            hash_map += "["
            hash_map += i
            hash_map += "->"
            hash_map += str(self.hashMap[i])
            hash_map += "], "
        return hash_map
