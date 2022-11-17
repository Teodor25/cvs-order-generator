import random
import uuid

def generate_customer():
    customerUUID = uuid.uuid1;
    
    obj = {
        'customerId': customerUUID,
        'city': '129',
        'zipcode': 'false',
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
    obj = {
        'productName': 'order',
        'price': 129,
        'discount': 'false',
        'userId': '1asd-asd123-ads-1dsd'
    }
    return obj;

def generate_list_of_x(amount):
    orderList = []

    for i in range(amount):
        orderList.append(generate_product());
    
    print(orderList);


generate_list_of_x(10);