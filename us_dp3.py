import tkinter as tk

def decimal_to_all():
    # Mendapatkan nilai dari inputan desimal
    decimal_value = decimal_entry.get()
    # Memeriksa apakah nilai tersebut merupakan angka (integer)
    if decimal_value.isdigit(): 
        # Mengkonversi nilai desimal menjadi biner, oktal, heksadesimal, dan ASCII
        decimal_value = int(decimal_value)
        biner_value = bin(decimal_value)[2:]
        octal_value = oct(decimal_value)[2:]
        hexa_value = hex(decimal_value)[2:].upper()
        ascii_value = chr(decimal_value)
        # Menghapus nilai lama pada inputan biner, oktal, heksadesimal, dan ASCII
        biner_entry.delete(0, tk.END)
        octal_entry.delete(0, tk.END)
        hexa_entry.delete(0, tk.END)
        ascii_entry.delete(0, tk.END)
        # Memasukkan nilai yang telah dikonversi ke dalam inputan biner, oktal, heksadesimal, dan ASCII
        biner_entry.insert(0, biner_value)
        octal_entry.insert(0, octal_value)
        hexa_entry.insert(0, hexa_value)
        ascii_entry.insert(0, ascii_value)
    else:
        # Menampilkan pesan error jika input bukan merupakan angka (integer)
        tk.messagebox.showerror("Error", "Input is not a valid integer")

def biner_to_all():
    # Mendapatkan nilai dari inputan biner
    biner_value = biner_entry.get()
    # Memeriksa apakah nilai tersebut merupakan angka biner
    if biner_value.isdigit():
        # Mengkonversi nilai biner menjadi desimal, oktal, heksadesimal, dan ASCII
        decimal_value = int(biner_value, 2)
        octal_value = oct(decimal_value)[2:]
        hexa_value = hex(decimal_value)[2:].upper()
        ascii_value = chr(decimal_value)
        # Menghapus nilai lama pada inputan desimal, oktal, heksadesimal, dan ASCII
        decimal_entry.delete(0, tk.END)
        octal_entry.delete(0, tk.END)
        hexa_entry.delete(0, tk.END)
        ascii_entry.delete(0, tk.END)
        # Memasukkan nilai yang telah dikonversi ke dalam inputan desimal, oktal, heksadesimal, dan ASCII
        decimal_entry.insert(0, decimal_value)
        octal_entry.insert(0, octal_value)
        hexa_entry.insert(0, hexa_value)
        ascii_entry.insert(0, ascii_value)
    else:
        # Menampilkan pesan error jika input bukan merupakan angka biner
        tk.messagebox.showerror("Error", "Input is not a valid binerary number")

def octal_to_all():
    # Mendapatkan nilai dari inputan oktal
    octal_value = octal_entry.get()
    # Memeriksa apakah nilai tersebut merupakan angka oktal
    if octal_value.isdigit():
        # Mengkonversi nilai oktal menjadi desimal, biner, heksadesimal, dan ASCII
        decimal_value = int(octal_value, 8)
        biner_value = bin(decimal_value)[2:]
        hexa_value = hex(decimal_value)[2:].upper()
        ascii_value = chr(decimal_value)
        # Menghapus nilai lama pada inputan desimal, biner, heksadesimal, dan ASCII
        decimal_entry.delete(0, tk.END)
        biner_entry.delete(0, tk.END)
        hexa_entry.delete(0, tk.END)
        ascii_entry.delete(0, tk.END)
        # Memasukkan nilai yang telah dikonversi ke dalam inputan desimal, biner, heksadesimal, dan ASCII
        decimal_entry.insert(0, decimal_value)
        biner_entry.insert(0, biner_value)
        hexa_entry.insert(0, hexa_value)
        ascii_entry.insert(0, ascii_value)
    else:
        # Menampilkan pesan error jika input bukan merupakan angka oktal
        tk.messagebox.showerror("Error", "Input is not a valid octalal number")

def hexa_to_all():
    # Mendapatkan nilai dari inputan heksadesimal dan mengubahnya menjadi huruf kapital
    hexa_value = hexa_entry.get().upper()
        # Mengkonversi nilai heksadesimal menjadi desimal, biner, oktal, dan ASCII
    decimal_value = int(hexa_value, 16)
    biner_value = bin(decimal_value)[2:]
    octal_value = oct(decimal_value)[2:]
    ascii_value = chr(decimal_value)
    # Menghapus nilai lama pada inputan desimal, biner, oktal, dan ASCII
    decimal_entry.delete(0, tk.END)
    biner_entry.delete(0, tk.END)
    octal_entry.delete(0, tk.END)
    ascii_entry.delete(0, tk.END)
    # Memasukkan nilai yang telah dikonversi ke dalam inputan desimal, biner, oktal, dan ASCII
    decimal_entry.insert(0, decimal_value)
    biner_entry.insert(0, biner_value)
    octal_entry.insert(0, octal_value)
    ascii_entry.insert(0, ascii_value)

def string_to_all():
    # Mendapatkan nilai dari inputan string
    string_value = string_entry.get()
    # Menyimpan nilai ASCII dalam bentuk string
    ascii_value = ""
    # Menyimpan nilai desimal, biner, oktal, dan heksadesimal
    decimalimal_value = ""
    binerary_value = ""
    octalal_value = ""
    hexa_value = ""
    # Melakukan iterasi pada setiap karakter dalam string
    for char in string_value:
        # Mengambil nilai ASCII dari karakter saat ini menggunakan fungsi Python ord() (menghasilkan sebuah nilai integer berupa kode ASCII dari sebuah karakter)
        ascii_char = ord(char)
        # Menambahkan nilai ASCII dalam bentuk string
        ascii_value += str(ascii_char) + " "
        # Menambahkan nilai desimal dalam bentuk string
        decimalimal_value += str(ascii_char) + " "
        # Menambahkan nilai biner dalam bentuk string
        binerary_value += bin(ascii_char)[2:] + " "
        # Menambahkan nilai oktal dalam bentuk string
        octalal_value += oct(ascii_char)[2:] + " "
        # Menambahkan nilai heksadesimal dalam bentuk string
        hexa_value += hex(ascii_char)[2:].upper() + " "
    # Menghapus nilai lama pada inputan ASCII, desimal, biner, oktal, dan heksadesimal
    ascii_entry.delete(0, tk.END)
    decimal_entry.delete(0, tk.END)
    biner_entry.delete(0, tk.END)
    octal_entry.delete(0, tk.END)
    hexa_entry.delete(0, tk.END)
    # Memasukkan nilai ASCII, desimal, biner, oktal, dan heksadesimal yang telah dihasilkan ke dalam masing-masing inputan
    ascii_entry.insert(0, ascii_value)
    decimal_entry.insert(0, decimalimal_value)
    biner_entry.insert(0, binerary_value)
    octal_entry.insert(0, octalal_value)
    hexa_entry.insert(0, hexa_value)
    
def delete_all():
    # Menghapus semua nilai pada inputan desimal
    decimal_entry.delete(0, tk.END)
    # Menghapus semua nilai pada inputan biner
    biner_entry.delete(0, tk.END)
    # Menghapus semua nilai pada inputan oktal
    octal_entry.delete(0, tk.END)
    # Menghapus semua nilai pada inputan heksadesimal
    hexa_entry.delete(0, tk.END)
    # Menghapus semua nilai pada inputan ASCII
    ascii_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Konversi Bilangan")
root.geometry("600x400")
root.configure(bg="#C7E9B0")

string_label = tk.Label(root, text="String:", font=("Poppins", 14), bg="#C7E9B0", fg="black")
string_label.grid(row=0, column=0, padx=5, pady=5)
string_entry = tk.Entry(root, font=("Poppins", 14))
string_entry.grid(row=0, column=1, padx=5, pady=5)

decimal_label = tk.Label(root, text="Desimal:", font=("Poppins", 14), bg="#C7E9B0", fg="black")
decimal_label.grid(row=1, column=0, padx=5, pady=5)
decimal_entry = tk.Entry(root, font=("Poppins", 14))
decimal_entry.grid(row=1, column=1, padx=5, pady=5)

biner_label = tk.Label(root, text="Biner:", font=("Poppins", 14), bg="#C7E9B0", fg="black")
biner_label.grid(row=2, column=0, padx=5, pady=5)
biner_entry = tk.Entry(root, font=("Poppins", 14))
biner_entry.grid(row=2, column=1, padx=5, pady=5)

octal_label = tk.Label(root, text="Oktal:", font=("Poppins", 14), bg="#C7E9B0", fg="black")
octal_label.grid(row=3, column=0, padx=5, pady=5)
octal_entry = tk.Entry(root, font=("Poppins", 14))
octal_entry.grid(row=3, column=1, padx=5, pady=5)

hexa_label = tk.Label(root, text="Hexaadesimal:", font=("Poppins", 14), bg="#C7E9B0", fg="black")
hexa_label.grid(row=4, column=0, padx=5, pady=5)
hexa_entry = tk.Entry(root, font=("Poppins", 14))
hexa_entry.grid(row=4, column=1, padx=5, pady=5)

ascii_label = tk.Label(root, text="ASCII:", font=("Poppins", 14), bg="#C7E9B0", fg="black")
ascii_label.grid(row=5, column=0, padx=5, pady=5)
ascii_entry = tk.Entry(root, font=("Poppins", 14))
ascii_entry.grid(row=5, column=1, padx=5, pady=5)

string_button = tk.Button(root, text="Konversi", command=string_to_all, bg="#B3C99C", fg="white", font=("Poppins", 14))
string_button.grid(row=0, column=2, padx=5, pady=5)

decimal_button = tk.Button(root, text="Konversi", command=decimal_to_all, bg="#B3C99C", fg="white", font=("Poppins", 14))
decimal_button.grid(row=1, column=2, padx=5, pady=5)

biner_button = tk.Button(root, text="Konversi", command=biner_to_all, bg="#B3C99C", fg="white", font=("Poppins", 14))
biner_button.grid(row=2, column=2, padx=5, pady=5)

octal_button = tk.Button(root, text="Konversi", command=octal_to_all, bg="#B3C99C", fg="white", font=("Poppins", 14))
octal_button.grid(row=3, column=2, padx=5, pady=5)

hexa_button = tk.Button(root, text="Konversi", command=hexa_to_all, bg="#B3C99C", fg="white", font=("Poppins", 14))
hexa_button.grid(row=4, column=2, padx=5, pady=5)

delete_button = tk.Button(root, text="Delete All", command=delete_all, bg="#ED2B2A", fg="white", font=("Poppins", 14))
delete_button.grid(row=6, column=1, padx=5, pady=5)

root.mainloop()
