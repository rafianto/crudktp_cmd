from . import Database
from .utility import random_string

def create_first_data():
    nik = input("Masukan NIK :")
    nama = input("Masukan Nama :")
    alamat = input("Alamat :")
    
    data = Database.TEMPLATE().copy()
    
    data["pk"] =  random_string(6)


def read():
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            return content
    except:
        print("Membaca database error")
        return False
    
      