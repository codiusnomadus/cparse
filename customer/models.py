from django.db import models


# Create your models here.
class Customer(models.Model):
    registration_date = models.DateTimeField(['%m/%d/%Y %H:%M:%S'])
    staff_msa_id = models.CharField(max_length=250)
    store_name = models.CharField(max_length=250)
    customer_name = models.CharField(max_length=250)
    customer_phone = models.BigIntegerField()
    device_make_model = models.CharField(max_length=250)
    imei_number = models.BigIntegerField()
    package_name = models.CharField(max_length=250)
    pf_package_variant = models.CharField(
        max_length=250, null=True, blank=True)
    pf_190_detail = models.CharField(max_length=250, null=True, blank=True)
    pf_160_detail = models.CharField(max_length=250, null=True, blank=True)
    pf_120_detail = models.CharField(max_length=250, null=True, blank=True)
    pf_80_detail = models.CharField(max_length=250, null=True, blank=True)
    dpb_package_variant = models.CharField(
        max_length=250, null=True, blank=True)
    dpb_190_detail = models.CharField(max_length=250, null=True, blank=True)
    dpb_160_detail = models.CharField(max_length=250, null=True, blank=True)
    dpb_120_detail = models.CharField(max_length=250, null=True, blank=True)
    dpb_80_detail = models.CharField(max_length=250, null=True, blank=True)
    agreement_1 = models.CharField(max_length=250)
    agreement_2 = models.CharField(max_length=250)

    def __str__(self):
        return self.customer_name

# TRANS_DATE	MSA_ID	STORE_NAME	CUST_NAME	CUST_PHONENO	CUST_EMAIL	DEVICE_MAKEMODEL	IMEI_NO	AGREEMENT	AGREEMENT2

    def product_name(self):
        if self.package_name == 'Phone Freedom 365':
            return self.product_name_for_phone_freedom(self.pf_package_variant)
        elif self.package_name == 'Digi Phone Bundle':
            return self.product_name_for_digi_phone_bundle(self.dpb_package_variant)
        else:
            return 'No variant found.'

    def product_name_for_phone_freedom(self, variant):
        return {
            'Digi Postpaid 190': 'PF365_POSTPAID190',
            'Digi Postpaid 160': 'PF365_POSTPAID160',
            'Digi Postpaid 120': 'PF365_POSTPAID120',
            'Digi Postpaid 80': 'PF365_POSTPAID80'
        }.get(variant, lambda: 'Product variant not defined')

    def product_name_for_digi_phone_bundle(self, variant):
        return {
            'Digi Postpaid 190': 'DPB_POSTPAID190',
            'Digi Postpaid 160': 'DPB_POSTPAID160',
            'Digi Postpaid 120': 'DPB_POSTPAID120',
            'Digi Postpaid 80': 'PF365_POSTPAID80'
        }.get(variant, lambda: 'Product variant not defined')

        # def remapped(self):
        #     if self.registration_date != None:
        #         return "{} {}".format(self.registration_date, self.staff_msa_id);
