from data import getCityData;

import random
import uuid

fullList = getCityData();

postalCodes =  fullList[0]
cities = fullList[1]
        
def generate_customer():
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

    customerUUID = uuid.uuid1();
    
    obj = {
        'customerId': customerUUID.__str__(),
        'postalCode': postalCodes[cityIndex],
        'city': cities[cityIndex],
    }
    return obj;

def generate_list_of_customers(amount):
    customersList = []
    for i in range(amount):
        customersList.append(generate_customer());
    
    return customersList;