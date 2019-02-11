from django.core.management.base import BaseCommand
from django.conf import settings
from datetime import datetime

import csv
from customer.models import Customer


def export_to_csv():

    customers = Customer.objects.all()

    # fields = OrderedDict([
    #     ("TRANS_DATE", "registered_date"),
    #     ("MSA_ID", "staff_msa_id"),
    #     ("STORE_NAME", "store_name"),
    #     ("CUST_NAME", "customer_name"),
    #     ("CUST_PHONENO", "customer_phone"),
    #     ("DEVICE_MAKEMODEL", "device_make_model"),
    #     ("IMEI_NO", "imei_number"),
    #     ("AGREEMENT", "agreement_1"),
    #     ("AGREEMENT2", "agreement_2"),
    #     ("PRODUCT_NAME", "product_name")
    # ])

    with open('names.csv', 'w') as csvfile:
        fieldnames = ['TRANS_DATE', 'MSA_ID', 'STORE_NAME', 'CUST_NAME', 'CUST_PHONENO',
                      'DEVICE_MAKEMODEL', 'IMEI_NO', 'AGREEMENT', 'AGREEMENT2', 'PRODUCT_NAME']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for customer in customers:
            writer.writerow({
                            'TRANS_DATE': customer.registration_date,
                            'MSA_ID': customer.staff_msa_id,
                            'STORE_NAME': customer.store_name,
                            'CUST_NAME': customer.customer_name,
                            'CUST_PHONENO': customer.customer_phone,
                            'DEVICE_MAKEMODEL': customer.device_make_model,
                            'IMEI_NO': customer.imei_number,
                            'AGREEMENT': customer.agreement_1,
                            'AGREEMENT2': customer.agreement_2,
                            'PRODUCT_NAME': str(customer.product_name())
                            })


class Command(BaseCommand):

    def handle(self, **options):
        export_to_csv()
