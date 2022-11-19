from . import Operasi

DB_NAME = "data.txt"

TEMPLATE = {
    "pk" : "XXXXXX",
    "nik" : "XXXXXXXXXXXXXXXX",
    "nama" : 255*" "
}

def init_console():
    try:
        with open(DB_NAME,"r") as file:
            print("Database ready init done!")
    except:
        print("Database not found!, Creadted!")
        with open(DB_NAME,"w",encoding="utf-8") as file:
            Operasi.create_first_data()
 