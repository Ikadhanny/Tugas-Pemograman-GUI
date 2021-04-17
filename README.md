# Tugas-Praktikum-Pemograman-GUI
Ikadhanny Yudyan Pratama\n19104082\nS1SE03B
# Modul 1 
Installasi dan pengenalan Pyhton
# 1. Pengenalan Python
Menampilkan variabel nama dan umur
![image](https://user-images.githubusercontent.com/72428738/115099818-a3e16080-9f62-11eb-9848-30915449d397.png)
# 2. Membuat dan Eksekusi Kode Program Pada Python
Membuat kode program
1. Buat direktori tempat penyimpanan Anda
2. Jalankan program teks editor
3. Tuliskan kode sebagai berikut print(“Hello World!”)
4. Simpan file tersebut dengan nama hello.py
![image](https://user-images.githubusercontent.com/72428738/115099873-ff135300-9f62-11eb-8215-efc11e1992db.png)
# 3. Variable dan Object
Satu variable dapat berubah-ubah tipe datanya sesuai dengan kebutuhan
![image](https://user-images.githubusercontent.com/72428738/115099947-852f9980-9f63-11eb-8daa-1bdb62a89854.png)
![image](https://user-images.githubusercontent.com/72428738/115099997-e8b9c700-9f63-11eb-8992-2bae170bdca9.png)
Cara  mendapatkan  id  adalah  dengan  menggunakan  perintah id(‘nama_variabel’). Untuk setiap variable jika memiliki nilai yang sama maka python akan menunjuk nilai yang sama untuk variable yang berbeda. Cara  mendapatkan  id  adalah  dengan  menggunakan  perintah id(‘nama_variabel’). Untuk setiap variable jika memiliki nilai yang sama maka python akan menunjuk nilai yang sama untuk variable yang berbeda. Jika anda menggunakan perintah **del** untuk menghapus variable y, maka yang akan dihapus adalah referensinya saja, bukan objek ‘9’ yang tadi ditunjuk oleh variable x dan y. Dengan  menambahkan  kode 'x = true',  maka  referensi  objek  varibel  x  akan dipindahkan dari objek ‘9’ ke objek ‘True’. Dengan demikian objek lama (9) akan diklaim sebagai sampah karena objek tersebut tidak ditunjuk oleh variable apapun.
# 4. Python Bersifat Case-Sensitive
Variable Posisi akan berbeda  dengan  variable posisi.
![image](https://user-images.githubusercontent.com/72428738/115100155-21a66b80-9f65-11eb-901a-82cd3d8646f5.png)
Karena Python bersifat case-sensitive
# 5. Perintah Program (Statement)
Pada python stiap kode program yang dituliskan tidak harus diakhiri dengan sebuah statement (biasanya tanda titik koma) seperti pada Java dan C. Titik koma pada python hanya diberikan pada saat ada dua atau lebih statement pada satu baris yang sama.
![image](https://user-images.githubusercontent.com/72428738/115100193-531f3700-9f65-11eb-8b73-0b03e8db2b2f.png)
Secara umum perintah program ditulis dalam satu baris kode, tetapi jika perintah yang dituliskan panjang maka anda dapat memecah perintah tersebut menjadi beberapa baris. Dimana setiap baris harus dihubungkan dengan tanda backslash (\).
![image](https://user-images.githubusercontent.com/72428738/115100232-81047b80-9f65-11eb-932f-065ae4ba8a4e.png)
Tetapi tanda backslah tidak diperlukan jika kita menulis perintah kode dalam bentuk array atau kode yang terdapat diantara tanda (…), […] atau {…}.
![image](https://user-images.githubusercontent.com/72428738/115100244-a6918500-9f65-11eb-8d30-33e842fed8f0.png)
# 6. Tipe Numerik
A. Bilangan Bulat
Dalam python terapat dua tipe bilangan bulat yaitu int dan bool. Selain tipe integral primitive python juga dapat menggunakan bilangan integral dengan basis decimal (10), biner (2), octal (8) maupun heksadesimal (16).
![image](https://user-images.githubusercontent.com/72428738/115100411-9d54e800-9f66-11eb-8061-3b7349238a6a.png)
Tipe bilangan bulat yang kedua adalah tipe Boolean, dimana seperti yang telah kita ketahui tipe data boleean bernilai true atau false saja.
![image](https://user-images.githubusercontent.com/72428738/115100476-22400180-9f67-11eb-8bce-ef0b2434073d.png)
Proses perhitungan dan penambahan bilangan pada python akan menghasilkan objek baru, hal ini terlihat dari id nya.
B. Bilangan Riil
Untuk tipe bilangan riil, python menyediakan tipe float, decimal. Decimal dan complex. Type bilangan float menggunakan titik untuk tanda desimalnya.
![image](https://user-images.githubusercontent.com/72428738/115100504-50254600-9f67-11eb-82c7-2770a4d788ed.png)
Sedangkan untuk tipe decimal hampir sama dengan tipe data float, akan ntetapi tipe decimal  digunakn  untuk  melakukan perhitungan  dengan  nilai  koma yang  lebih presisi.
# 7. Tipe String
Tipe data string dalam python direpresentasikan  dengan tipe str.Objek string dapat dibuat dengan tiga cara yaitu:
• Menggunakan tanda pertik tunggal
• Menggunakan tanda petik ganda
• Menggunakan tanda petik tunggal ataupun ganda yang direpetisi sebanyak tiga kali
![image](https://user-images.githubusercontent.com/72428738/115100548-895db600-9f67-11eb-9128-0594a95c88d7.png)
Karakter khusus dalam phyton harus diawali dengan backslash (\) diikuti dengan karakter khususnya.
Python juga dapat menggabungkan dua objek string menjadi satu dengan operator +.
![image](https://user-images.githubusercontent.com/72428738/115100571-b3af7380-9f67-11eb-9831-03f655f413f6.png)
A. Membandingkan String
operator >, <=, >=
![image](https://user-images.githubusercontent.com/72428738/115100636-130d8380-9f68-11eb-9ab5-cc7839d730fd.png)
B. Mengekstrak Substring
Substring  di dalam string dapat diekstrak dengan menggunakan operator slice (:) dengan menyertakan indeks awal dan akhir sebagai penanda. 
![image](https://user-images.githubusercontent.com/72428738/115100653-2c163480-9f68-11eb-96ad-ed98d030768d.png)
Kode tersebut mengambil substring dari variable s mulai dari indeks ke 0 sampai indeks ke 11. Jika kita tidak menyertakan indeks maka string yang akan diekstrak adalah sepanjang string tersebut / string sisanya.
Contoh:
![image](https://user-images.githubusercontent.com/72428738/115100664-4223f500-9f68-11eb-8f0a-7dc2124a9a84.png)
C. Membuat String dengan format tertentu
Phyton pada dasarnya juga dapat memnggabungkan tipoe data atau format lain ke dalam string yang telah dibuat. Antara lain dengan menggunakan $d, %f, %s dan lain sebagainya.
![image](https://user-images.githubusercontent.com/72428738/115100674-58ca4c00-9f68-11eb-9e06-ac22509dc8b9.png)
# 8. Tipe Koleksi
Tipe koleksi biasa disebut dengan tipe container. Beberapa tie koleksi antara lain list, dictionary, tuple dan set.
![image](https://user-images.githubusercontent.com/72428738/115100693-74355700-9f68-11eb-8a39-a50831ff5213.png)
Objek list dibuat dengan menggunakan tanda [], setiap objek yang berada di dlamnya dipisahkan dengan menggunakan koma dan dapat terdiri dari berbagai macam tipe data.
Model dan cara akses list dapat digabungkan dengan fungsi perulangan dasar seperti for, while dan lain sebagainya.
Untuk menghapus atau merubah elemen pada list anda dapat menggunakan perintah del[‘indeks_list’] sedangkan  untuk  merubah  dapat  menggunakan  perintah namaList[‘indeks’] = value baru. Untuk menambahkan elemen pada list anda dapat menggunakan  perintah extend([list])’.
![image](https://user-images.githubusercontent.com/72428738/115100708-962ed980-9f68-11eb-9cc8-fdce8f594f9a.png)
