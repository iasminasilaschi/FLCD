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
