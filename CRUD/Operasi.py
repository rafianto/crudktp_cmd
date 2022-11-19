from . import Database
from .utility import random_string

def create_first_data():
    nik = input("Masukan NIK :")
    nama = input("Masukan Nama :")
    alamat = input("Alamat :")
    
    data = Database.TEMPLATE.copy()
    
    data["pk"] =  random_string(6)
    data["nik"] = nik + Database.TEMPLATE["nik"][len(nik):]
    data["nama"] = nama + Database.TEMPLATE["nama"][len(nama):]
    data["alamat"] = alamat + Database.TEMPLATE['alamat'][len(alamat):]
        
    data_str = f'{data["pk"]},{data["nik"]},{data["nama"]},{data["alamat"]}\n'
    print(data_str)
    try:
        with open(Database.DB_NAME,'w',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Gagal Insert Data")


def read():
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            return content
    except:
        print("Membaca database error")
        return False
    
      