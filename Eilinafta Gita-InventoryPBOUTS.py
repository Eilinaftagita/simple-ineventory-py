import os

# fungsi untuk membersihkan layar
def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# inisialisasi stok awal
stock = {}

# fungsi untuk memasukkan barang
def add_item():
    clean_screen()
    print("===========================")
    print("=== MEMASUKKAN BARANG ===")
    print("===========================")
    name = input("Nama Barang: ")
    item_id = input("ID Barang: ")
    date = input("Tanggal Masuk (dd/mm/yyyy): ")
    amount = int(input("Jumlah Masuk: "))
    if item_id in stock:
        stock[item_id]["quantity"] += amount
    else:
        stock[item_id] = {"name": name, "quantity": amount, "date": date}
    input("Barang berhasil dimasukkan. Tekan Enter untuk kembali ke menu.")

# fungsi untuk mengeluarkan barang
def remove_item():
    clean_screen()
    print("==============================")
    print("=== MENGELOLA BARANG KELUAR===")
    print("==============================")
    item_id = input("ID Barang: ")
    if item_id in stock:
        print("Nama Barang: ", stock[item_id]["name"])
        print("Jumlah saat ini: ", stock[item_id]["quantity"])
        date = input("Tanggal Keluar (dd/mm/yyyy): ")
        amount = int(input("Jumlah Keluar: "))
        if amount <= stock[item_id]["quantity"]:
            stock[item_id]["quantity"] -= amount
            input("Barang berhasil dikeluarkan. Tekan Enter untuk kembali ke menu.")
        else:
            input("Jumlah barang yang dikeluarkan melebihi stok. Tekan Enter untuk kembali ke menu.")
    else:
        input("Barang tidak ditemukan. Tekan Enter untuk kembali ke menu.")

# fungsi untuk melihat stok barang
def view_stock():
    clean_screen()
    print("============================")
    print("=== STOK BARANG ===")
    print("============================")
    print("ID Barang\tNama Barang\tJumlah Barang\tTanggal Masuk")
    for item_id, item in stock.items():
        print(f"{item_id}\t\t{item['name']}\t\t{item['quantity']}\t\t{item['date']}")
    input("Tekan Enter untuk kembali ke menu.")

# fungsi utama
def main():
    while True:
        clean_screen()
        print("============================")
        print("=== MAIN MENU ===")
        print("============================")
        print("1. Barang Masuk")
        print("2. Barang Keluar")
        print("3. Stok Barang")
        print("4. Keluar")
        choice = input("Pilih menu: ")
        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            view_stock()
        elif choice == "4":
            break
        else:
            input("Pilihan tidak valid. Tekan Enter untuk kembali ke menu.")

if __name__ == "__main__":
    main()
