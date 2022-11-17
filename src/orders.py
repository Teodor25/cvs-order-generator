from products import generate_product
import uuid
import random

discount1 = [
    'procent',
    10,
    'teamtc10',
]

discount2 = [
    'procent',
    30,
    'blackfriday21',
]

discount3 = [
    'procent',
    20,
    'christmas21',
]

def generate_order(usesDiscount, discount, time):
    product = generate_product();
    orderUUID = uuid.uuid1();
    userUUID = uuid.uuid1();

    discountUsed = 'none'
    if usesDiscount: discountUsed = discount

    subtotal = product[2];
    total = product[2];
    if discountUsed != 'none':
        total = product[2] * discount[1]

    shipping = random.choice(['home_delivery', 'parcel_shop'])

    obj = {
        'orderId': orderUUID.__str__(), #
        'designType': product[0], #
        'size': product[1], #
        'subtotal': subtotal, #
        'total': total, #
        'currency': 'DKK', #
        'userId': userUUID.__str__(), #
        'shipping': shipping, #
        'discount': discountUsed, #
    }
    return obj;

def generate_list_of_orders(amount):
    ordersList = []
    for i in range(amount):
        ordersList.append(generate_order());
    
    return ordersList;