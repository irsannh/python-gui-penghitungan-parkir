from tkinter import *
from tkinter import messagebox
import sqlite3

class MyWindow:
    def __init__(self, win):
        self.window = window
        self.window.title("Project Akhir DAA - Irsan Nur Hidayat")
        self.window.geometry("430x500")

        self.var = IntVar()
        self.no_transaksi = StringVar()
        self.no_polisi = StringVar()
        self.jam_masuk = StringVar()
        self.jam_keluar = StringVar()
        self.lama = StringVar()
        self.bayar = StringVar()

        #Label-Label
        self.label_1 = Label(win, text="Penghitungan Parkir", font=("Arial", 14, "bold"))
        self.label_1.place(x=110,y=40)
        self.label_2 = Label(win, text="Nomor Transaksi", font=("Arial", 12))
        self.label_2.place(x=30,y=130)
        self.label_3 = Label(win, text="Jenis Kendaraan", font=("Arial", 12))
        self.label_3.place(x=30,y=160)
        self.label_4 = Label(win, text="Nomor Polisi", font=("Arial", 12))
        self.label_4.place(x=30,y=190)
        self.label_5 = Label(win, text="Waktu Parkir", font=("Arial", 12))
        self.label_5.place(x=30,y=220)
        self.label_6 = Label(win, text="Jam Masuk (hh.mm)", font=("Arial", 12))
        self.label_6.place(x=50,y=250)
        self.label_7 = Label(win, text="Jam Keluar (hh.mm)", font=("Arial", 12))
        self.label_7.place(x=50,y=280)
        self.label_8 = Label(win, text="Lama Parkir", font=("Arial", 12))
        self.label_8.place(x=30,y=360)
        self.label_9 = Label(win, text="jam", font=("Arial", 12))
        self.label_9.place(x=340,y=360)
        self.label_10 = Label(win, text="Total Bayar", font=("Arial", 12))
        self.label_10.place(x=30,y=390)

        #button-button
        self.button_1 = Button(win, text="Transaksi Baru", width=20, command=self.transaksi_baru)
        self.button_1.place(x=30,y=85)
        self.button_2 = Button(win, text="Hitung", width=20, command=self.hitung)
        self.button_2.place(x=150,y=320)
        self.button_3 = Button(win, text="Proses Transaksi", width=20, command=self.simpan)
        self.button_3.place(x=150,y=430)

        #radiobutton
        self.radiobutton_1 = Radiobutton(win, text="1. Motor", variable=self.var, value=1, font=("Arial", 12))
        self.radiobutton_1.place(x=200,y=160)
        self.radiobutton_2 = Radiobutton(win, text="2. Mobil", variable=self.var, value=2, font=("Arial", 12))
        self.radiobutton_2.place(x=300,y=160)

        #entry
        self.entry_1 = Entry(win, width=30, textvar=self.no_transaksi)
        self.entry_1.place(x=200,y=130)
        self.entry_2 = Entry(win, width=30, textvar=self.no_polisi)
        self.entry_2.place(x=200,y=190)
        self.entry_3 = Entry(win, width=30, textvar=self.jam_masuk)
        self.entry_3.place(x=200,y=250)
        self.entry_4 = Entry(win, width=30, textvar=self.jam_keluar)
        self.entry_4.place(x=200,y=280)
        self.entry_5 = Entry(win, width=20, textvar=self.lama)
        self.entry_5.place(x=200,y=360)
        self.entry_6 = Entry(win, width=30, textvar=self.bayar)
        self.entry_6.place(x=200,y=390)

        #default setting
        self.button_1.configure(state=NORMAL)
        self.entry_1.configure(state=DISABLED)
        self.entry_2.configure(state=DISABLED)
        self.entry_3.configure(state=DISABLED)
        self.entry_4.configure(state=DISABLED)
        self.button_2.configure(state=DISABLED)
        self.entry_5.configure(state=DISABLED)
        self.entry_6.configure(state=DISABLED)
        self.button_3.configure(state=DISABLED)
        self.radiobutton_1.configure(state=DISABLED)
        self.radiobutton_2.configure(state=DISABLED)

    def transaksi_baru(self, *win):
        self.button_1.configure(state=DISABLED)
        self.entry_1.configure(state=NORMAL)
        self.radiobutton_1.configure(state=NORMAL)
        self.radiobutton_2.configure(state=NORMAL)
        self.entry_2.configure(state=NORMAL)
        self.entry_3.configure(state=NORMAL)
        self.entry_4.configure(state=NORMAL)
        self.button_2.configure(state=NORMAL)

    def hitung(self, *win):
        self.button_2.configure(state=DISABLED)
        self.entry_5.configure(state=NORMAL)
        self.entry_6.configure(state=NORMAL)
        self.button_3.configure(state=NORMAL)

        #hitung waktu parkir
        jam_masuk, menit_masuk = self.entry_3.get().split('.')
        jam_keluar, menit_keluar = self.entry_4.get().split('.')
        waktu_masuk = (int(jam_masuk) * 60) + int(menit_masuk)
        waktu_keluar = (int(jam_keluar) * 60) + int(menit_keluar)
        durasi_parkir = waktu_keluar - waktu_masuk
        selisih = "%i" %(durasi_parkir // 60)
        self.entry_5.insert(END, selisih)

        #hitung biaya parkir
        lama_parkir = durasi_parkir // 60
        if self.var.get() == 1:
            if lama_parkir > 2:
                total_bayar = ((lama_parkir - 2) * 1000) + 3000
            else:
                total_bayar = 3000
        elif self.var.get() == 2:
            if lama_parkir > 2:
                total_bayar = ((lama_parkir - 2) * 2000) + 5000
            else:
                total_bayar = 5000
        self.entry_6.insert(END, int(total_bayar))

    def simpan(self, *win):
        nomor_transaksi = self.entry_1.get()
        jenis = self.var.get()
        nomor_polisi = self.entry_2.get()
        masuk = self.entry_3.get()
        keluar = self.entry_4.get()
        durasi = self.entry_5.get()
        bayar = self.entry_6.get()
        conn = sqlite3.connect('datatransaksi.db')
        with conn:
            cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Transaksi(nomor_transaksi TEXT, jenis TEXT, nomor_polisi TEXT, masuk TEXT, keluar TEXT, durasi TEXT, bayar TEXT)')
        cursor.execute('INSERT INTO Transaksi (nomor_transaksi, jenis, nomor_polisi, masuk, keluar, durasi, bayar) VALUES(?,?,?,?,?,?,?)', (nomor_transaksi, jenis, nomor_polisi, masuk, keluar, durasi, bayar))
        conn.commit()

        self.button_1.configure(state=NORMAL)
        self.button_2.configure(state=DISABLED)
        self.button_3.configure(state=DISABLED)
        self.radiobutton_1.configure(state=DISABLED)
        self.radiobutton_2.configure(state=DISABLED)
        self.entry_1.delete(0, END)
        self.entry_2.delete(0, END)
        self.entry_3.delete(0, END)
        self.entry_4.delete(0, END)
        self.entry_5.delete(0, END)
        self.entry_6.delete(0, END)
        self.entry_1.configure(state=DISABLED)
        self.entry_2.configure(state=DISABLED)
        self.entry_3.configure(state=DISABLED)
        self.entry_4.configure(state=DISABLED)
        self.entry_5.configure(state=DISABLED)
        self.entry_6.configure(state=DISABLED)

        self.approved = messagebox.showinfo("Transaksi Berhasil","Transaksi Telah Berhasil Disimpan!")
        self.question = messagebox.askquestion("Transaksi Baru","Apakah Ingin Membuat Transaksi Baru?")
        if self.question == 'yes':
            self.answer = messagebox.showinfo("Transaksi Baru", "Silakan Buat Transaksi Baru")
        elif self.question == 'no':
            self.window.destroy()

window = Tk()
mywin = MyWindow(window)
window.mainloop()