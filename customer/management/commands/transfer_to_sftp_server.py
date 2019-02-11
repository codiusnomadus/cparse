from django.core.management.base import BaseCommand
from django.conf import settings
import paramiko

private_key = paramiko.RSAKey.from_private_key_file(
    settings.BASE_DIR + "/DIGI_VOL.pem")

TRANSPOSED_LIST_PATH = settings.BASE_DIR + '/names.csv'


def transfer_to_sftp_server():
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print("connecting")
    ssh_client.connect(hostname="13.250.94.208",
                       username="DIGI_VOL", pkey=private_key)
    print("connected")
    localpath = '/digi_vol/Transpose/transposed_list.csv'
    sftp = ssh_client.open_sftp()
    sftp.put(TRANSPOSED_LIST_PATH, localpath)
    print("File uploaded")
    ssh_client.close()


class Command(BaseCommand):

    def handle(self, **options):
        transfer_to_sftp_server()
