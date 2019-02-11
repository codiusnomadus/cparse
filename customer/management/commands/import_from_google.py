from django.core.management.base import BaseCommand
from django.conf import settings
from datetime import datetime

import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'client_secrets.json', scope)

def import_from_google():
    creds = gspread.authorize(credentials)
    worksheet = creds.open('digi_copy').sheet1
    data = worksheet.get_all_records()
    csv.register_dialect('customerDialect', delimiter=',', quoting=csv.QUOTE_ALL)

    with open('customers.csv', 'w') as csvFile:
        fields = [
            " ",
            "STAFF MSA ID",
            "Store Name (Code)",
            "Customer's Name",
            "Customer's Phone No",
            "Device Make & Model",
            "IMEI Number",
            "Digi Package",
            "Phone Freedom 365",
            "Phone Freedom 365 (Digi Postpaid 190)",
            "Phone Freedom 365 (Digi Postpaid 160)",
            "Phone Freedom 365 (Digi Postpaid 120)",
            "Phone Freedom 365 (Digi Postpaid 80)",
            "Digi Phone Bundle",
            "Digi Phone Bundle (Digi Postpaid 190)",
            "Digi Phone Bundle (Digi Postpaid 160)",
            "Digi Phone Bundle (Digi Postpaid 120)",
            "Digi Phone Bundle (Digi Postpaid 80)",
            "Do you declare and agree on the above?",
            "Do you declare and agree on the above?"
        ]

        writer = csv.DictWriter(csvFile, fieldnames=fields,
                                dialect="customerDialect")

        writer.writerows(data)


    print("writing completed")

    csvFile.close()

class Command(BaseCommand):
    def handle(self, **options):
        import_from_google()
