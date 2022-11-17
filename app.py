
def generate_order():
    obj = {
        'productName': 'order',
        'price': 129,
        'discount': 'false',
        'userId': '1asd-asd123-ads-1dsd'
    }
    return obj;

def generate_list_of_orders(amount):
    orderList = []

    for i in range(amount):
        orderList.append(generate_order());
    
    print(orderList);


generate_list_of_orders(10);