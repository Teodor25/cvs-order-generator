def getCityData(): 
    cityFile = open('cities.txt', 'r');
    lines = cityFile.readlines();
    postalCodes = []
    cities = []

    for line in lines:
        if len(line) > 4:
            postalCodes.append(line.split()[0])
            cities.append(line.split()[1])
    
    return [postalCodes, cities];