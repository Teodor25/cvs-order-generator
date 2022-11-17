from data import getCityData;

import random
import uuid
import csv

fullList = getCityData();

postalCodes =  fullList[0]
cities = fullList[1]

        
def generate_customer():
    customerUUID = uuid.uuid1();

    cityIndex = random.randint(0, len(postalCodes) - 1);
    
    obj = {
        'customerId': customerUUID.__str__(),
        'postalCode': postalCodes[cityIndex],
        'cities': cities[cityIndex],
    }
    return obj;

def generate_product():
    
    designTypes = ['family_tree', 'quotable', 'love_letter', 'pet_sign', 'custom_order', 'baby_sign'];
    sizes = ['small', 'medium', 'large'];
    familyTreePrices = [499, 699, 999];
    quotablePrices = [299, 399, 499];

    designTypeIndex = random.randint(0, len(designTypes) - 1);
    sizeIndex = random.randint(0, len(sizes) - 1);

    designType = designTypes[designTypeIndex];
    size = sizes[sizeIndex];
    productPrice = 0; 

    if designTypes[designTypeIndex] == 'family_tree':
        productPrice = familyTreePrices[sizeIndex];
    else:
        productPrice = quotablePrices[sizeIndex];

    return [designType, size, productPrice];

def generate_order():
    product = generate_product();
    orderUUID = uuid.uuid1();
    obj = {
        'designType': product[0],
        'size': product[1],
        'price': product[2],
        'discount': 'false',
        'userId': orderUUID.__str__(),
    }
    return obj;

def generate_list_of_customers(amount):
    customersList = []
    for i in range(amount):
        customersList.append(generate_customer());
    
    return customersList;

def generate_list_of_orders(amount):
    ordersList = []
    for i in range(amount):
        ordersList.append(generate_order());
    
    return ordersList;


def export_list_of_customers_to_csv(): 
    customerList = generate_list_of_customers(10000);

    customer_csv = open('customers.csv', 'w')
    csv_writer = csv.writer(customer_csv)

    count = 0;

    for customer in customerList: 
        if count == 0:
            #write header
            header = customer.keys()
            csv_writer.writerow(header)
            count += 1

        csv_writer.writerow(customer.values())

    customer_csv.close()

def export_list_of_orders_to_csv(): 
    orderList = generate_list_of_orders(10000);

    order_csv = open('orders.csv', 'w')
    csv_writer = csv.writer(order_csv)

    count = 0;

    for order in orderList: 
        if count == 0:
            #write header
            header = order.keys()
            csv_writer.writerow(header)
            count += 1

        csv_writer.writerow(order.values())

    order_csv.close()

export_list_of_customers_to_csv();
export_list_of_orders_to_csv()