import csv
from customers import generate_list_of_customers
from orders import generate_list_of_orders

def export_list_of_customers_to_csv(): 
    customerList = generate_list_of_customers(1000);

    customer_csv = open('customers.csv', 'w')
    csv_writer = csv.writer(customer_csv)

    count = 0;

    for customer in customerList: 
        if count == 0:
            header = customer.keys()
            csv_writer.writerow(header)
            count += 1

        csv_writer.writerow(customer.values())

    customer_csv.close()

def export_list_of_orders_to_csv(): 
    orderList = generate_list_of_orders();

    order_csv = open('orders.csv', 'w')
    product_csv = open('products.csv', 'w')
    csv_order_writer = csv.writer(order_csv)
    csv_product_writer = csv.writer(product_csv)

    count = 0;

    for order in orderList: 
        if count == 0:
            #write header
            orderHeader = order.keys()
            productHeader = ['designType', 'price', 'size']
            csv_product_writer.writerow(productHeader)
            csv_order_writer.writerow(orderHeader)
            count += 1

        csv_order_writer.writerow(order.values())
        productRow = [order['designType'], order['price'], order['size']]
        csv_product_writer.writerow(productRow)

    order_csv.close()