class City:
    """description of class"""
    def __init__(self, name, region, country, centrePopulation, metroPopulation, latitude, longetude, elevation):
        self.name = name
        self.region = region
        self.country = country
        self.centrePopulation = centrePopulation
        self.metroPopulation = metroPopulation
        self.latitude = latitude
        self.longetude = longetude
        #elevation is in meters
        self.elevation = elevation

    def megacity(self):
        if (self.centrePopulation >= 3000000 or self.metroPopulation >= 8000000):
            return True
        else:
            return False

    def toCoordinates(self, toLat, toLong):
        if (self.toLat > 0.000):
            print("Latitude:  " + str(self.toLat) + "°N")
        else:
            toLat *= -1
            print("Latitude:  " + str(self.toLat) + "°S")

        if (toLong > 0.000):
            print("Latitude:  " + str(self.toLong) + "°E")
        else:
            toLong *= -1
            print("Latitude:  " + str(self.toLong) + "°W")

    def getInfo(self):
        print("City:   " + self.name + ", " + self.region + ", " + self.country)
        print("Centre Population: " + str(self.centrePopulation))
        print("Metro Population:  " + str(self.metroPopulation))
        self.toCoordinates(self.latitude, self.longetude)
        print ("Elevation:    " + str(self.elevation) + " metres")
        if (self.megacity is True):
            print(self.name + " is a megacity.")
        else:
            print(self.name + "is a large city but not a megacity.")
        #newline
        print("")
