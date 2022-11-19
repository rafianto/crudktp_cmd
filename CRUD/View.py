from . import Operasi

def read_console():
    data_file = Operasi.read()
    
    index = "No"
    judul = "NIK"
    nama = "Nama"
   
    # Header
    print("\n"+"="*100)
    print(f"{index:4} | {nik:40} | {nama:40}")
    print("-"*100)
    
    # Data
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        nik = data_break[2]
        nama = data_break[3]
        print(f"{index+1:4} | {nik:.40} | {nama:.40}",end="")

    # Footer
    print("="*100+"\n")