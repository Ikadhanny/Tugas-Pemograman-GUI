# UTS GUI

# No.1 Buatlah sebuah desain aplikasi GUI sederhana yang bertujuan untuk mendata mahasiswa terdiri dari fitur tambah, edit, tampilan data mahasiswa dan hapus data mahasiswa menggunakan PyQT5. Lampirkan hasil codingan dan screenshot nya melalui github repository! (25 Poin) Gunakan Dummy Data agar desain tampilan terlihat.

<img src = "https://github.com/Ikadhanny/Tugas-Pemograman-GUI/blob/UTS-GUI/UTS/Screenshot%202021-06-04%20152829.png">

<img src = "https://github.com/Ikadhanny/Tugas-Pemograman-GUI/blob/UTS-GUI/UTS/Data%20ditambah.png">

Contoh Data Berhasil Ditambahkan

<img src = "https://github.com/Ikadhanny/Tugas-Pemograman-GUI/blob/UTS-GUI/UTS/Data%20diedit.png">

Contoh Data Berhasil Diedit

<img src = "https://github.com/Ikadhanny/Tugas-Pemograman-GUI/blob/UTS-GUI/UTS/Data%20di-clear.png">

Contoh Data berhasil di-Clear

<img src = "https://github.com/Ikadhanny/Tugas-Pemograman-GUI/blob/UTS-GUI/UTS/Data%20dihapus.png">

Contoh Data berhasil Dihapus



# No.2  Perbaiki codingan berikut ini, lalu jalankan apa yang dihasilkan. Berikan analisa anda dan screenshot hasilnya melalui readme pada github repository! (25 Poin)

  from PyQt5.QtWidgets import *
  
  app = QApplication([])
  
  button = QPushButton('Click')
  
  def on_button_clicked():
  
      alert = QMessageBox()
  
      alert.setText('You clicked the button!')
      
      alert.exec_()
  
  button.clicked.connect(on_button_clicked)
  
  button.show()
       
       app.exec_();

HASIL :
<img src = "https://github.com/Ikadhanny/Tugas-Pemograman-GUI/blob/UTS-GUI/UTS/UTS2.png">

