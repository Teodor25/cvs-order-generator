from data import getCityData;

import random

fullList = getCityData();

postalCodes =  fullList[0]
cities = fullList[1]
        
def generate_customer(UUID):
    cityIndex = 0; 
    number = random.randint(0, 1000);
    if number < 350: 
        cityIndex = random.randint(0, 8);
    elif (number > 350) and (number < 550):
        cityIndex = random.randint(42, 46);
    elif (number > 550) and (number < 680):
        cityIndex = 53
    elif (number > 680) and (number < 730):
        cityIndex = 50
    elif (number > 730) and (number < 800):
        cityIndex = random.randint(21, 24);
    else:
        cityIndex = random.randint(0, len(postalCodes) - 1);
    
    obj = {
        'customerId': UUID,
        'postalCode': postalCodes[cityIndex],
        'city': cities[cityIndex],
    }
    return obj;