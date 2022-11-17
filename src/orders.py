from products import generate_product
import uuid
import random
import datetime

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

def generate_order(usesDiscount, discount, date):
    product = generate_product();
    orderUUID = uuid.uuid1();
    userUUID = uuid.uuid1();

    discountUsed = 'none'
    if usesDiscount != 'false': discountUsed = discount[2]

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
        'date': date
    }
    return obj;

def generate_list_of_orders():

    chance = 1
    min = int(1 * chance)
    max = int(10 * chance)

    ordersList = []
    months = [1,2,3,4,5,6,7,8,9,10,11,12]

    # YEAH
    for month in months:
        # MONTH
        for i in range(28):
            amountOfOrders = random.randint(min, max)
            # DAY
            for x in range(amountOfOrders):
                # discount 
                discount = 'none'
                isUsingDiscount = 'false';
                # October
                if month == 10:
                    number = random.randint(0, 100);
                    if (number < 25) and (number > 0):
                        discount = discount1
                        isUsingDiscount = 'true'
                    elif (number > 25) and (number > 50):
                        discount = discount3
                        isUsingDiscount = 'true'
                # time
                print(month)
                date = datetime.datetime(2021, month, i+1)

                newOrder = generate_order(isUsingDiscount, discount, date)
                ordersList.append(newOrder);
    
    return ordersList;