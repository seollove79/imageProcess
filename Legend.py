class Legend:
    coord = ''
    rgbValue = ''
    temp = ''

    def __init__(self,coord,rgbValue,temp):
        self.coord = coord
        self.rgbValue = rgbValue
        self.temp = temp

    def getCoord(self):
        return self.coord
    
    def getRgbValue(self):
        return self.rgbValue
    
    def getTemp(self):
        return self.temp