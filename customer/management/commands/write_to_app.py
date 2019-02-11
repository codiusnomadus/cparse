import csv
import os.path
import time

import gspread
from django.utils.dateparse import parse_date
import datetime

from django.conf import settings
from django.core.management.base import BaseCommand
from customer.models import Customer



import csv
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'client_secrets.json', scope)


def write_to_app():
    creds = gspread.authorize(credentials)
    worksheet = creds.open('digi_copy_file').sheet1
    data = worksheet.get_all_values()
    data.pop(0)
    print(data[0])
    for row in data:
        Customer.objects.create(
            registration_date = datetime.datetime.strptime(row[0], "%m/%d/%Y %H:%M:%S"),
            staff_msa_id=row[1],
            store_name=row[2],
            customer_name=row[3],
            customer_phone=row[4],
            device_make_model=row[5],
            imei_number=row[6],
            package_name=row[7], 
            pf_package_variant=row[8],
            pf_190_detail=row[9],
            pf_160_detail=row[10],
            pf_120_detail=row[11],
            pf_80_detail=row[12],
            dpb_package_variant=row[13],
            dpb_190_detail=row[14],
            dpb_160_detail=row[15],
            dpb_120_detail=row[16],
            dpb_80_detail=row[17],
            agreement_1=row[18],
            agreement_2=row[19]
        )

# CSV_PATH = settings.BASE_DIR + '/customers.csv'

# def write_to_app():
#     with open(CSV_PATH, newline='') as csvfile:
#         customer_file = csv.reader(csvfile, delimiter=',')
#         for row in customer_file:
#             utc_date = row[0]
#             print(utc_date)
#             Customer.objects.create(
#                 registration_date = datetime.datetime.strptime(utc_date, "%m/%d/%Y %H:%M:%S").date(),
#                 staff_msa_id=row[1],
#                 store_name=row[2],
#                 customer_name=row[3],
#                 customer_phone=row[4],
#                 device_make_model=row[5],
#                 imei_number=row[6],
#                 package_name=row[7],
#                 pf_package_variant=row[8],
#                 pf_190_detail=row[9],
#                 pf_160_detail=row[10],
#                 pf_120_detail=row[11],
#                 pf_80_detail=row[12],
#                 dpb_package_variant=row[13],
#                 dpb_190_detail=row[14],
#                 dpb_160_detail=row[15],
#                 dpb_120_detail=row[16],
#                 dpb_80_detail=row[17],
#                 agreement_1=row[18],
#                 agreement_2=row[19]
#             )
#             # Example -> Book.objects.create(ISBNCode=row[0], title=row[1], author=row[2])


class Command(BaseCommand):
    def handle(self, **options):
        write_to_app()
