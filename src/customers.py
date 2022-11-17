from data import getCityData;

import random
import uuid

fullList = getCityData();

postalCodes =  fullList[0]
cities = fullList[1]
        
def generate_customer():
    customerUUID = uuid.uuid1();

    cityIndex = random.randint(0, len(postalCodes) - 1);
    
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