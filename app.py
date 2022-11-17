import random
import uuid
import json
import csv

cityFile = open('cities.txt', 'r');
lines = cityFile.readlines();
postalCodes = []

for line in lines:
    if len(line) > 4:
        postalCodes.append(line.split()[0])
        
def generate_customer():
    customerUUID = uuid.uuid1();
    
    obj = {
        'customerId': customerUUID.__str__(),
        'postalCode': random.choice(postalCodes),
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

    obj = {
        'designType': designType,
        'size': size,
        'productPrice': productPrice,
    }
    return obj;

def generate_order():
    product = generate_product();
    jsonProduct = json.dumps(product);
    print (jsonProduct)
    obj = {
        'designType': jsonProduct.designType,
        'price': product['productPrice'],
        'discount': 'false',
        'userId': '1asd-asd123-ads-1dsd'
    }
    return obj;

def generate_list_of_customers(amount):
    customersList = []
    for i in range(amount):
        customersList.append(generate_customer());
    
    return customersList;


def export_list_of_customers_to_csv(): 
    customerList = generate_list_of_customers(10);

    customer_csv = open('customers.csv', 'w')
    csv_writer = csv.writer(customer_csv)

    customerListJson = json.dumps(customerList);

    count = 0;

    for customer in customerList: 
        if count == 0:
            #write header
            header = customer.keys()
            csv_writer.writerow(header)
            count += 1

        csv_writer.writerow(customer.values())

    customer_csv.close()
