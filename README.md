# Rafi Irsyad Saharso
# PBP A - 2206082221

## Link Aplikasi
Berikut link aplikasi saya [SHS Item Store](https://itemstorerafi.adaptable.app)

## Jawaban Soal Tugas 3

### Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial)
1. Membuat input `form` untuk menambahkan objek model pada app sebelumnya
    - Buat file `forms.py` di folder "main" untuk membuat class `ItemForm` yang merupakan `ModelForm` untuk model `Item`. Ini mendefinisikan atribut yang akan ditampilkan dalam form
    - Buat fungsi `create_item` dalam `views.py` yang mengelola input form. Dalam fungsi ini, form `ItemForm` diisi dengan data dari `request.POST` dan diverifikasi. Jika valid, data disimpan dan pengguna diarahkan kembali ke halaman utama
    - Menambahkan fungsi untuk merender `create_item.html`
    - Tambahkan `items = Item.objects.all()` pada fungsi `show_main` dalam `views.py` untuk mengambil semua objek `Item` dari database dan menyertakannya dalam konteks
    - Import fungsi yang diperlukan dan tambahkan path URL untuk mengakses fungsi-fungsi ini dalam urls.py di "main"
    - Buat file `create_item.htm`l dalam folder "templates" di "main" dan isi dengan kode yang sesuai untuk membuat antarmuka tabel dan formulir
    - Tambahkan kode di `main.html` untuk menampilkan data item dalam bentuk tabel dan menambahkan tombol "Add New Product" yang mengarahkan ke halaman formulir
2. Menambahkan Fungsi Views untuk Melihat Data dalam Berbagai Format:
    - Buat fungsi `show_xml` dalam `views.py` dan path URL untuk mengaksesnya. Fungsi ini mengambil data `Item` dan mengembalikannya dalam format XML
    - Buat fungsi `show_json` dalam `views.py` dan path URL untuk mengaksesnya. Fungsi ini mengambil data Item dan mengembalikannya dalam format JSON
    - Buat fungsi s`how_xml_by_id` dalam `views.py` dan path URL untuk mengaksesnya. Fungsi ini mengambil data Item berdasarkan ID yang disediakan dan mengembalikannya dalam format XML
    - Buat fungsi `show_json_by_id` dalam `views.py` dan path URL untuk mengaksesnya. Fungsi ini mengambil data Item berdasarkan ID yang disediakan dan mengembalikannya dalam format JSON

### Apa perbedaan antara form `POST` dan form `GET` dalam Django?
- **POST**
    - Metode POST mengirimkan data atau nilai langsung ke target action tanpa memunculkannya di URL
    - Dalam metode POST, variabel `$_POST` digunakan untuk menampung data atau nilai yang dikirim
    - Metode POST memungkinkan pengiriman data yang berukuran tidak terbatas
- **GET**
    - Metode GET menampilkan data atau nilai dalam URL, yang kemudian akan ditangani oleh action
    - Dalam metode GET, variabel `$_GET` digunakan untuk menampung data atau nilai yang ditempatkan dalam URL
    - Metode GET memiliki batasan panjang URL maksimum sekitar 2047 karakter yang tidak boleh melebihi jumlah tersebut

### Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
- **XML**
    XML digunakan untuk pertukaran data terstruktur dengan struktur kuat menggunakan tag pembuka dan penutup, meskipun kurang mudah dibaca oleh manusia. Cocok untuk konfigurasi aplikasi, penyimpanan data terstruktur, dan integrasi dengan berbagai bahasa pemrograman
- **JSON**
    JSON digunakan untuk komunikasi data antar aplikasi dengan format notasi objek yang simpel, mudah dimengerti manusia, umum di pengembangan web dan API, serta lebih mudah diintegrasikan dengan bahasa pemrograman
- **HTML**
    HTML digunakan untuk membuat tampilan web, mengatur tampilan konten di peramban, memiliki struktur lebih sederhana dibandingkan dengan XML atau JSON, mudah dibaca, dan digunakan dalam pengembangan web untuk mengontrol tampilan dan interaksi pengguna.

### Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
- **Kelegibilitas:** JSON mudah dibaca dan dipahami manusia
- **Efisiensi:** Format JSON lebih ringkas dan efisien dalam penggunaan bandwidth
- **Dukungan Universal:** JSON didukung oleh hampir semua bahasa pemrograman
- **Integrasi JavaScript:** JSON terintegrasi dengan JavaScript, cocok untuk pengembangan web
- **Umum dalam API Web:** JSON digunakan secara luas dalam API web modern
- **Pendekatan Berbasis Objek:** JSON mendukung representasi objek, sejalan dengan pendekatan berbasis objek dalam pengembangan web
- **Keamanan:** JSON jarang menghadapi masalah keamanan seperti serangan injeksi XML atau HTML

### Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam `README.md`.
<img src='/aset/HTML.jpg'>
<img src='/aset/XML.jpg'>
<img src='/aset/JSON.jpg'>
<img src='/aset/XML by ID.jpg'>
<img src='/aset/JSON by ID.jpg'>

## Jawaban Soal Tugas 2

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara *step-by-step* 
1. Membuat sebuah proyek Django baru.
    - Untuk membuat proyek Django baru, pertama-tama kita perlu membuat *virtual environment*
    ```
    python -m venv env
    ```
    - Kemudian aktifkan *virtual environment* tersebut
    ```
    env\Scripts\activate
    ```
    - Dalam direktori yang sama, buat file bernama requirements.txt dan tambahkan dependensi yang dibutuhkan.
    - Lalu, jalankan perintah `pip install -r requirements.txt` untuk menginstall dependensi tersebut.
    - Kemudian, mulailah proyek dengan menjalankan perintah `django-admin startproject proyek_pbp`
    - Untuk  deployment, tambahkan `"*"` ke dalam pengaturan `ALLOWED_HOSTS` di dalam `settings.py`
    - Perlunya juga menambahkan file `.gitignore` untuk menentukan berkas-berkas dan direktori-direktori yang harus diabaikan oleh Git
2. Membuat aplikasi dengan nama `main` pada proyek tersebut.
    - Jalankan perintah python `manage.py startapp main` untuk membuat aplikasi `main`
    - Buat folder `templates` di dalam direktori `main` dan tambahkan file `main.html` ke dalam folder tersebut. File html berfungsi sebagai tampilan saat mengunjungi app
3. Melakukan routing pada proyek agar dapat menjalankan aplikasi `main`.
    - Pada `urls.py` di dalam proyek `library_col`, tambahkan `path('main/', include('main.urls'))`
4. Membuat model pada aplikasi `main` dengan nama `Item` dan memiliki atribut wajib sebagai berikut.
    - `name` dengan tipe Charfield
    - `amount` dengan tipe IntegerField
    - `description` dengan tipe TextField
5. Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
    - Pada berkas `views.py`, tambahkan fungsi `show_main` dengan konteks nama aplikasi, nama, kelas yang akan mereturn field tersebut ke `html`
6. Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
    - Melakukan add, commit, dan push dari direktori repositori lokal ke repository GitHub
    - Melakukan deploy dari website adaptable sesuai ketentuan Tutorial 0

### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.
<img src='/aset/flowchart.jpg'>

### Jelaskan mengapa kita menggunakan ***virtual environment?*** Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan ***virtual environment***?
Virtual environment sangat penting dalam pengembangan aplikasi web berbasis Django karena membantu mengisolasi proyek, memungkinkan manajemen dependensi yang efisien. Dengan menggunakan virtual environment, setiap proyek dapat memiliki dependensi dan paket Python yang terisolasi, mencegah konflik dan masalah versi. Ini juga membuat pengelolaan dependensi proyek menjadi lebih mudah.

Selain itu, virtual environment juga meningkatkan keamanan proyek dengan menghindari konflik antara paket-paket yang berbeda di proyek yang berbeda. Secara keseluruhan, penggunaan virtual environment adalah praktik terbaik dalam pengembangan aplikasi Django, memastikan kebersihan, isolasi, dan manajemen dependensi yang efisien.

### Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
- **Model-View-Controller (MVC):**
    - **Model:** Menyimpan data dan logika aplikasi.
    - **View:** Menampilkan data dari model dan menghubungkannya dengan template.
    - **Controller:** Menentukan tampilan antarmuka pengguna.

- **Model-View-Template (MVT):**
    - **Model:** Menyimpan data dan logika aplikasi.
    - **View:** Menampilkan data dari model dan menghubungkannya dengan template.
    - **Template:** Mengatur tampilan HTML dan cara data dari Model ditampilkan dalam halaman web. 

- **Model-View-ViewModel (MVVM):**
    - **Model:** Menyimpan data dan logika aplikasi.
    - **View:** Menampilkan data dari model dan menghubungkannya dengan template.
    - **ViewModel:** Memproses data dari Model dan mempersiapkannya untuk ditampilkan oleh View.

**Perbedaan:**
Perbedaan antara MVC, MVT, dan MVVM terletak pada bagaimana mereka mengelola alur aplikasi. Dalam MVC, Controller mengendalikan alur aplikasi, sedangkan MVT menggantinya dengan Template untuk mengatur tampilan. MVVM memperkenalkan ViewModel yang memproses data dari Model dan memfasilitasi pengikatan data kuat antara Model dan View. Jadi, perbedaan utama adalah peran komponen tengah dalam mengelola logika dan alur aplikasi.