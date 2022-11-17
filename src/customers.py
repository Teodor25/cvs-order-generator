from data import getCityData;

import random
import uuid

fullList = getCityData();

postalCodes =  fullList[0]
cities = fullList[1]
        
def generate_customer():
    cityIndex = 0; 
    number = random.randint(0, 1000);
    if number < 300: 
        cityIndex = random.randint(0, 8);
    elif (number > 300) and (number < 450):
        cityIndex = random.randint(42, 46);
    elif (number > 450) and (number < 520):
        cityIndex = 53
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