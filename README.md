# Rafi Irsyad Saharso
# PBP A - 2206082221

## Link Aplikasi
Berikut link aplikasi saya [SHS Item Store](https://itemstorerafi.adaptable.app)

## Jawaban Soal

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


### Jelaskan mengapa kita menggunakan ***virtual environment?*** Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan ***virtual environment***?
- **Model-View-Controller (MVC):**
**Model:** Menyimpan data dan logika aplikasi.
**View:** Menampilkan data dari model dan menghubungkannya dengan template.
**Template:** Menentukan tampilan antarmuka pengguna.

- **Model-View-Template (MVT):**
**Model:** Menyimpan data dan logika aplikasi.
**View:** Menampilkan data dari model dan menghubungkannya dengan template.
**Template:** Mengatur tampilan HTML dan cara data dari Model ditampilkan dalam halaman web. 

- **Model-View-ViewModel (MVVM):**
**Model:** Menyimpan data dan logika aplikasi.
**View:** Menampilkan data dari model dan menghubungkannya dengan template.
**ViewModel:** Memproses data dari Model dan mempersiapkannya untuk ditampilkan oleh View.

**Perbedaan:**
Perbedaan antara MVC, MVT, dan MVVM terletak pada bagaimana mereka mengelola alur aplikasi. Dalam MVC, Controller mengendalikan alur aplikasi, sedangkan MVT menggantinya dengan Template untuk mengatur tampilan. MVVM memperkenalkan ViewModel yang memproses data dari Model dan memfasilitasi pengikatan data kuat antara Model dan View. Jadi, perbedaan utama adalah peran komponen tengah dalam mengelola logika dan alur aplikasi.