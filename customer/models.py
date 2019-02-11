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
    pf_package_variant = models.CharField(max_length=250,null=True,blank=True)
    pf_190_detail = models.CharField(max_length=250, null=True, blank=True)
    pf_160_detail = models.CharField(max_length=250, null=True, blank=True)
    pf_120_detail = models.CharField(max_length=250,null=True,blank=True)
    pf_80_detail = models.CharField(max_length=250,null=True,blank=True)
    dpb_package_variant = models.CharField(max_length=250,null=True,blank=True)
    dpb_190_detail = models.CharField(max_length=250,null=True,blank=True)
    dpb_160_detail = models.CharField(max_length=250,null=True,blank=True)
    dpb_120_detail = models.CharField(max_length=250,null=True,blank=True)
    dpb_80_detail = models.CharField(max_length=250,null=True,blank=True)
    agreement_1 = models.CharField(max_length=250)
    agreement_2 = models.CharField(max_length=250)

    def __str__(self):
        return self.customer_name

    # def remapped(self):
    #     if self.registration_date != None:
    #         return "{} {}".format(self.registration_date, self.staff_msa_id);

