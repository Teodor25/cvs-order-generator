from products import generate_product
from customers import generate_customer
import uuid
import random
import datetime

teamtcDiscount = [
    'procent',
    10,
    'teamtc10',
]

blackFridayDiscount = [
    'procent',
    30,
    'blackfriday21',
]

christmasDiscount = [
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
        'orderId': orderUUID.__str__(),
        'designType': product[0],
        'size': product[1],
        'subtotal': subtotal,
        'total': total,
        'currency': 'DKK',
        'userId': userUUID.__str__(),
        'shipping': shipping,
        'discount': discountUsed,
        'date': date
    }
    return obj;


def generate_list_of_orders():

    chance = 1
    min = int(1 * chance)
    max = int(10 * chance)

    ordersList = []
    customerList = []
    months = [1,2,3,4,5,6,7,8,9,10,11,12]

    monthOrderCount = 0;

    # YEAH
    for month in months:
        # MONTH
        for i in range(28):
            amountOfOrders = random.randint(min, max)
            monthOrderCount += amountOfOrders
            # DAY
            for x in range(amountOfOrders):
                number = random.randint(0, 100);
                # discount 
                discount = 'none'
                isUsingDiscount = 'false';

                # January
                if month == 1:
                    chance = 0.8
                    min = int(1 * chance)
                    max = int(10 * chance)
                    if (number < 25):
                        discount = teamtcDiscount
                        isUsingDiscount = 'true'
                # Feb - Sep
                elif (month > 1) and (month < 9):
                    chance = 1
                    min = int(1 * chance)
                    max = int(10 * chance)
                    if (number < 25):
                        discount = teamtcDiscount
                        isUsingDiscount = 'true'
                # September
                elif month == 9:
                    chance = 1.2
                    min = int(1 * chance)
                    max = int(10 * chance)
                    if (number < 25):
                        discount = teamtcDiscount
                        isUsingDiscount = 'true'
                # October
                elif month == 10:
                    chance = 1.6
                    min = int(1 * chance)
                    max = int(10 * chance)
                    if (number < 25):
                        discount = teamtcDiscount
                        isUsingDiscount = 'true'
                    elif (number > 25) and (number > 50):
                        discount = christmasDiscount
                        isUsingDiscount = 'true'
                # November
                elif month == 11:
                    chance = 3
                    min = int(1 * chance)
                    max = int(10 * chance)
                    if (number < 50):
                        discount = blackFridayDiscount
                        isUsingDiscount = 'true'
                    elif (number > 25) and (number > 50):
                        discount = christmasDiscount
                        isUsingDiscount = 'true'
                    elif (number > 50) and (number > 60):
                        discount = teamtcDiscount
                        isUsingDiscount = 'true'
                # December
                if month == 12:
                    chance = 4
                    min = int(1 * chance)
                    max = int(10 * chance)
                    if (number < 25):
                        discount = teamtcDiscount
                        isUsingDiscount = 'true'
                    elif (number > 25) and (number > 50):
                        discount = christmasDiscount
                        isUsingDiscount = 'true'

                    if i > 16:
                        chance = 0.8
                        min = int(1 * chance)
                        max = int(10 * chance)

                # time
                date = datetime.datetime(2021, month, i+1)

                newOrder = generate_order(isUsingDiscount, discount, date)
                ordersList.append(newOrder);
                customerList.append(generate_customer())
            
        print(monthOrderCount)

    return [ordersList, customerList];