import csv
from customers import generate_list_of_customers
from orders import generate_list_of_orders

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