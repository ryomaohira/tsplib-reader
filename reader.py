class reader:
    name = None
    dimensions = 0
    optimum = 0
    cities = []

    
    def __init__(self, file):
        self.open(file)
        return
    
    def readFile(self,file):
        with open(file) as f:
            content = f.read().splitlines()
            cleaned = [x.lstrip() for x in content if x != ""]
            return cleaned
            
    def open(self, file):
        arr = self.readFile(file)
        dimensions = 0
        name = ""
        coordinates = []
        cities_set = []
        
        for item in arr:
            # Get the name
            if "NAME" in item:
                #self.name = str(item[5:])
                pre, space, name = item.split(' ')
                self.name = name
            
            # Get the optimum distance
            if "OPTIMUM" in item:
                self.optimum = int(item[9:])
            
            # Find the number of cities
            if "DIMENSION" in item:
                self.dimensions = int(item[11:])
            
            for num in range(1, self.dimensions + 1):
                if item.startswith(str(num)):
                    row = item.split(' ')
                    if row[0] not in cities_set:
                        cities_set.append(row[0])
                        city = {
                            'index': int(row[0]),
                            'x': float(row[1]),
                            'y': float(row[2])
                        }
                        self.cities.append(city)
