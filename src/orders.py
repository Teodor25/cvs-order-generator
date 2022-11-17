from products import generate_product
import uuid

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

def generate_list_of_orders(amount):
    ordersList = []
    for i in range(amount):
        ordersList.append(generate_order());
    
    return ordersList;