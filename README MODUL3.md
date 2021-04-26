# MODUL 3
KELAS DAN MODUL
## 1. PRINSIP DASAR PEMROGRAMAN BERORIENTASI OBJEK
### A. Abstraksi
Abstraksi adalah konsep penyembunyian informasi dalam suatu kelas. Abstraksi juga sering  didefinisikan  sebagai  proses pemodelan kasus pemrograman menjadi satu kelas
### B. Enkasulasi
Enkaspsulasi  adalah pemodelan suatu  permasalahan  program menjadi satu  kelas utama. Implementasinya dilakukan dengan  cara membungkus daftar  atribut dan metode menjadi entitas tunggal dengan na ma tertentu (kelas) dimana setiap kelas harus memiliki nama yang unik.
### C. Pewarisan
Pewarisan dalah konsep yang mendefinisikan kelas baru yang diwariskan dari kelas lain yang telah ada. Kelas turunan dari kelas induk memiliki sifat sifat yang sama dengan kelas induknya. Tetapi di dalam pewarisan anda dapat mendefinisikan sifat- sifat baru ke dalam kelas turunannya.
### D. Polimorfisme
Polimorfisme merupakan konsep yang diartikan  sebagai kemampuan suatu objek untuk mengungkapkan banyak hal yang berbeda melalui satu cara yang sama.
## 2. MENDEFINISIKAN KELAS
Kelas merupakan suatu tipe data yang berisi atribut dan metode.

## 3. MEMBUAT OBJEK
Objek merupakan instance dari suatu kelas.

## 4. ATRIBUT STATIS
Atribut statis biasa disebut dengan class variable, sedangkan atribut normal disebut dengan instance / object variable. Dengan demikian nilai atribut dapat berbeda untuk masing - masing objek. Atribut statis harus didefinisikan di luar metode dan tanpa diawali dengan self.

## 5. METODE STATIS
Metode statis dalam python dpat langsung dipanggil dari nama kelasnya, tanpa harus membuat objek terlebih dahulu untuk kelas dari objek yang bersangkutan. Tetapi metode statis dapat juga dipanggil melalui objek kelas. Untuk membuat sebuah metode statis, anda dapat menggunakan statement @staticmethod.

## 6. PEWARISAN
Pewarisan kelas dalam python dapat didefinisikan dengan syntax berikut.

namaObjek = namaKelas(parameter kelas)

## 7. METODE ABSTRAK DAN KELAS ABSTRAK
Metode abstrak adalah metode yang tidak memiliki implementasi. Kelas abstrak tidak dapat dibuat objeknya. Metode abstrak yang dimiliki oleh kelas abstrak harus diimplementasikan oleh kelas - kelas turunannya. Untuk mendefinisikan kelas abstrak pada python menggunakan ABCMeta dan @absrtactmethod.

## 8. POLIMORFISME
Polimorfisme adalah kemampuan suatu objek untuk melakukan banyak hal menggunakan satu cara yang sama.

## 9. MEMECAH KODE MENJADI BEBRAPA FILE
