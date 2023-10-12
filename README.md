# Rafi Irsyad Saharso
# PBP A - 2206082221

## Link Aplikasi
Berikut link aplikasi saya [SHS Item Store](https://itemstorerafi.adaptable.app)

## Jawaban Soal Tugas 6

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

#### Mengubah tugas 5 yang telah dibuat sebelumnya menjadi menggunakan AJAX.
1. AJAX GET
    1. Ubahlah kode *cards* data item agar dapat mendukung AJAX GET.
        - Hapus kode *table* yang sudah dibuat sebelumnya
        - Tambahkan kode dibawah pada `main.html`
            ```
            <div class="table-responsive">
                <table class="table table-striped table-bordered">
                    <tbody id="item_table">
                    </tbody>
                </table>
            </div>
            ```
    2. Lakukan pengambilan task menggunakan AJAX GET.
        - Buat fungsi `get_item_json` pada `views.py` untuk Mengembalikan Data JSON
        - Menambahkan `<script>` pada `main.html`
            ```
            async function getItems() {
                return fetch("{% url 'main:get_item_json' %}").then((res) => res.json())
            }
            ```
2. AJAX POST
    1. Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan item.
        - Menambagkan kode dibawah pada `main.html`
            ```
            <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h1 class="modal-title fs-5" id="exampleModalLabel">Add New Item</h1>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            <form id="form" onsubmit="return false;">
                                {% csrf_token %}
                                <div class="mb-3">
                                    <label for="name" class="col-form-label">Name:</label>
                                    <input type="text" class="form-control" id="name" name="name"></input>
                                </div>
                                <div class="mb-3">
                                    <label for="amount" class="col-form-label">Amount:</label>
                                    <input type="number" class="form-control" id="amount" name="amount"></input>
                                </div>
                                <div class="mb-3">
                                    <label for="description" class="col-form-label">Description:</label>
                                    <textarea class="form-control" id="description" name="description"></textarea>
                                </div>
                            </form>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                            <button type="button" class="btn btn-primary" id="button_add" data-bs-dismiss="modal">Add Item</button>
                        </div>
                    </div>
                </div>
            </div>
            ```
        - Membuat button untuk menambahkan item
            ```
            <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">Add Item by AJAX</button>

            ```
    2. Buatlah fungsi view baru untuk menambahkan item baru ke dalam basis data.
        - Membuat Fungsi `add_item_ajax` pada `views.py`
            ```
            @csrf_exempt
            def add_item_ajax(request):
                if request.method == 'POST':
                    name = request.POST.get("name")
                    amount = request.POST.get("amount")
                    description = request.POST.get("description")
                    user = request.user

                    new_item = Item(name=name, amount=amount, description=description, user=user)
                    new_item.save()

                    return HttpResponse(b"CREATED", status=201)

                return HttpResponseNotFound()
            ```
    3. Buatlah path `/create-ajax/` yang mengarah ke fungsi *view* yang baru kamu buat.
        - Menambahkan Routing Untuk Fungsi `add_item_ajax` pada `urls.py`
        - Menambahkan Routing Untuk Fungsi `get_item_json` pada `urls.py`
    4. Hubungkan form yang telah kamu buat di dalam modal kamu ke *path* `/create-ajax/`.
        - Tambahkan fungsi `addItem` pada `<script>` di `main.html`
            ```
            function addItem() {
                fetch("{% url 'main:add_item_ajax' %}", {
                    method: "POST",
                    body: new FormData(document.querySelector('#form'))
                }).then(refreshItems)

                document.getElementById("form").reset()
                return false
            }
            ```
    5. Lakukan *refresh* pada halaman utama secara asinkronus untuk menampilkan daftar item terbaru tanpa *reload* halaman utama secara keseluruhan.
        - Tambahkan fungsi `refreshItems` pada `<script>` di `main.html`
            ```
            async function refreshItems() {
                document.getElementById("item_table").innerHTML = ""
                const items = await getItems()
                let htmlString = `<tr>
                    <th>Name</th>
                    <th>Amount</th>
                    <th>Description</th>
                    <th>Date Added</th>
                    <th>Action</th>
                </tr>`
                items.forEach((item) => {
                    htmlString += `\n<tr>
                    <td>${item.fields.name}</td>
                    <td>${item.fields.amount}</td>
                    <td>${item.fields.description}</td>
                    <td>${item.fields.date_added}</td>
                    <td>
                        <button class="btn btn-danger" data-url="{% url 'main:delete_item_ajax' 123 %}" onclick="deleteItem(this, ${item.pk})">Delete</button>
                    </td>
                </tr>` 
                })
                
                document.getElementById("item_table").innerHTML = htmlString
            }
            ```
3. Melakukan perintah collectstatic.
    - Menambahkan kode dibawah pada `settings.py`
        ```
        STATIC_URL = 'static/'

        STATIC_ROOT = os.path.join(BASE_DIR, 'static')
        ```
    - Menjalankan `python manage.py collectstatic` pada cmd

### Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
1. **Asynchronous Programming:**
    - Operasi dieksekusi secara independen tanpa harus menunggu satu sama lain
    - Waktu respons lebih cepat karena tidak ada penundaan signifikan antara operasi
    - Penggunaan callback atau await/async untuk mengelola operasi asynchronous
    - Cocok untuk operasi jaringan, I/O berat, dan aplikasi yang perlu responsif terhadap input
2. **Synchronous Programming:**
    - Operasi dieksekusi berurutan, satu per satu
    - Waktu respons lebih lambat karena operasi harus menunggu operasi sebelumnya selesai
    - Tidak memerlukan pengaturan khusus seperti callback
    - Cocok untuk tugas-tugas sederhana dan cepat, serta operasi yang tidak memerlukan jeda waktu

### Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Dalam konteks penerapan JavaScript dan AJAX, paradigma event-driven programming digunakan untuk membangun aplikasi web yang responsif dan interaktif. Paradigma ini berfokus pada penggunaan event sebagai pemicu eksekusi kode, berbeda dengan pendekatan prosedural yang menjalankan kode secara berurutan. Dalam tugas ini, paradigma ini terlihat pada tombol yang memicu fungsi `addItem()` dan `deleteItem()` ketika tombol "Add Item" atau "Delete" ditekan.

### Jelaskan penerapan asynchronous programming pada AJAX.
Asynchronous programming pada AJAX adalah cara untuk melakukan operasi seperti pengambilan data dari server tanpa menghentikan eksekusi kode utama. Ini memungkinkan aplikasi web tetap responsif dan efisien dengan tidak harus menunggu respons dari server, mengizinkan penggunaan callback functions, promise, atau async/await untuk menangani respons dari server.

### Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.
1. **Fetch API:**
    - Fetch API adalah bagian dari JavaScript modern yang lebih ringan dan sederhana, memungkinkan untuk mengirim permintaan HTTP secara asynchronous dengan lebih efisien
    - Menggunakan Promise untuk menangani respons, yang membuatnya lebih mudah dipahami dan menghindari callback hell
2. **jQuery:**
    - jQuery adalah library JavaScript yang lebih besar dengan banyak fitur, termasuk kemampuan untuk mengirim permintaan HTTP asynchronous.
    - Meskipun lebih berat, jQuery memiliki dukungan yang lebih luas untuk browser lama dan menyediakan berbagai fungsi tambahan.

Menurut pandangan saya, Fetch API merupakan pilihan yang lebih unggul karena lebih user-friendly berkat penggunaan Promise. Selain itu, Fetch API memiliki performa yang lebih optimal dan responsif dibandingkan dengan jQuery karena lebih ringan.

## Jawaban Soal Tugas 5

### Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).
1. Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin.
    - **LOGIN**
        - Semua konten utama halaman ditempatkan dalam blok `content`, yang akan menampilkan elemen-elemen HTML pada halaman login
        - Menggunakan `<div class="container mt-5">` sebagai container Bootstrap yang mengatur elemen-elemen dan memberikan margin atas sebanyak 5 satuan
        - Menggunakan `row` dan `col-md-6` untuk membuat tata letak
        - Menggunakan `<div class="card">` untuk mengelompokkan elemen-elemen dalam card
        - Judul "Login" ditampilkan di dalam `card-header`
        - Tombol "Login" menggunakan class `btn btn-primary` dari Bootstrap untuk tampilan yang menarik
        - Pesan kesalahan, jika ada, ditampilkan dalam sebuah `div` dengan class `alert alert-danger`
    - **REGISTER**
        - Semua konten utama halaman ditempatkan dalam blok `content`, menampilkan elemen-elemen HTML pada halaman pendaftaran
        - Menggunakan `<div class="container mt-5">` sebagai container Bootstrap yang mengatur elemen-elemen ke tengah halaman dan memberikan margin atas sebanyak 5 satuan
        - Menggunakan `row` dan `col-md-6` untuk membuat tata letak
        - Menggunakan `<div class="card">` untuk mengelompokkan elemen-elemen dalam card
        - Judul "Register" ditampilkan di dalam `card-header`
        - Tombol "Register" menggunakan class `btn btn-primary` dari Bootstrap untuk tampilan yang menarik
        - Jika terdapat pesan kesalahan (pendaftaran gagal), pesan-pesan tersebut ditampilkan dalam sebuah div dengan class `alert alert-danger`
    - **Tambah Item**
        - Semua konten utama halaman ditempatkan dalam blok `content`
        - Menggunakan `<div class="container mt-5">` sebagai container Bootstrap yang mengatur elemen-elemen dan memberikan margin atas sebanyak 5 satuan
        - Menggunakan `row` dan `col-md-6` untuk membuat tata letak responsif
        - Menggunakan `<div class="card">` untuk mengelompokkan elemen-elemen dalam kotak kartu yang estetis
        - Judul "Add New Item" ditampilkan di dalam `card-header`
        - Tombol "Add Item" menggunakan class `btn btn-success` dari Bootstrap
2. Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan **Card**.
    - Menggunakan `<nav>` dengan class navbar dan atribut navbar-expand-lg untuk membuat navbar Bootstrap
    - Navbar memiliki latar belakang gelap (`bg-dark`) dan teks putih (`navbar-dark`)
    - Terdapat "Welcome, {{ name }}" yang muncul di tengah navbar (`mx-auto`) dan *button* "Logout" di sebelah kanan navbar (`ml-auto`). Tautan Logout menggunakan tombol Bootstrap dengan class `btn btn-outline-light`
    - Menggunakan `<div class="container mt-4">` sebagai container utama untuk konten halaman

### Jelaskan manfaat dari setiap *element selector* dan kapan waktu yang tepat untuk menggunakannya.
1. **Universal Selector (*):**
    - Memungkinkan untuk memilih semua elemen dalam dokumen HTML
    - Biasanya digunakan ketika ingin mengatur beberapa properti gaya dasar untuk seluruh elemen, seperti mengatur margin atau padding secara umum
2. **Type Selector (Tag Selector):**
    - Digunakan untuk memilih semua elemen dengan jenis tag yang sama
    - Digunakan ketika ingin menerapkan gaya umum pada semua elemen dengan jenis tag yang sama
3. **Class Selector (.class):**
    - Memungkinkan memilih elemen berdasarkan nilai atribut `class` yang diberikan
    - Berguna ketika Anda ingin mengaplikasikan gaya pada sekelompok elemen yang memiliki karakteristik atau fungsi yang sama, seperti mengubah warna teks pada tombol dengan class `btn`
4. **ID Selector (#id):**
    - Memungkinkan untuk memilih elemen berdasarkan nilai atribut `id` yang unik
    - Digunakan ketika ingin mengendalikan elemen dengan ID unik atau mengidentifikasi elemen tertentu
5. **Descendant Selector (ancestor descendant):**
    - Memungkinkan untuk memilih elemen turunan (nested) yang berada dalam elemen lain
    - Digunakan ketika ingin menerapkan gaya pada elemen yang berada dalam struktur atau tata letak tertentu
6. **Child Selector (parent > child):**
    - Memungkinkan untuk memilih elemen anak langsung dari elemen induk tertentu
    - Digunakan ketika ingin menerapkan gaya hanya pada elemen anak langsung dalam hubungan parent-child

### Jelaskan HTML5 Tag yang kamu ketahui.
1. `<html>`: Menandai awal dan akhir dari dokumen HTML
2. `<head>`: Menyediakan informasi tentang dokumen HTML
3. `<title>`: Menentukan judul untuk dokumen HTML
4. `<body>`: Menandai awal dan akhir dari isi dokumen HTML
5. `<h1> - <h6>`: Menandai judul dari dokumen HTML dengan ukuran yang berbeda-beda
6. `<p>`: Menandai paragraf dalam dokumen HTML
7. `<a>`: Membuat hyperlink ke page lain atau email address
8. `<img>`: Menampilkan gambar dalam dokumen HTML
9. `<button>`: Menandai tombol yang dapat diklik
10. `<div>`: Menandai sebuah section
11. `<!DOCTYPE html>`: Deklarasi dokumen HTML5 yang mendefinisikan jenis dokumen yang sedang digunakan

### Jelaskan perbedaan antara *margin* dan *padding*.
1. **Margin:**
    - Margin merupakan area di sekeliling elemen HTML yang terletak di luar batas elemen tersebut
    - Margin tidak memiliki latar belakang atau warna, sehingga dapat dianggap sebagai zona yang transparan
    - Penggunaan margin adalah untuk mengendalikan jarak antara elemen dengan elemen-elemen lain yang berada di sekitarnya
    - Dengan margin, kita dapat menentukan seberapa jauh elemen ini dari elemen-elemen lain yang berada di luar elemen tersebut
2. **Padding**
    - Padding merupakan ruang yang berada dalam elemen HTML, terletak di antara batas elemen dan kontennya
    - Padding memiliki latar belakang dan warna yang identik dengan elemen itu sendiri
    - Fungsi padding adalah untuk mengontrol jarak antara batas elemen dan isi (konten) elemen tersebut
    - Dengan padding, kita dapat mengatur jarak antara elemen dan kontennya sendiri dengan presisi

### Jelaskan perbedaan antara *framework* CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
1. **Tailwind CSS**
    -  Framework CSS yang sangat fleksibel dan berbasis utility. Dapat membangun komponen dengan menggabungkan kelas-kelas yang tersedia.
    - Memungkinkan kustomisasi yang sangat mendalam dengan mudah. Dapat mengubah hampir setiap aspek tampilan dengan mengedit file konfigurasi
    - Menghasilkan kode HTML yang lebih besar karena memerlukan lebih banyak kelas dalam elemen HTML.
    - Dapat lebih efisien dalam hal kinerja karena Anda hanya memuat kelas yang diperlukan.
2. **Bootstrap**
    - Lebih terstruktur dengan komponen-komponen yang sudah siap pakai dan gaya bawaan. Bootstrap memiliki desain yang lebih kaku.
    - Lebih sederhana dalam hal kustomisasi, terutama jika ingin melakukan perubahan signifikan dalam gaya komponen.
    - Menghasilkan kode HTML yang lebih ringkas karena banyak komponen telah diatur sebelumnya.
    - Mungkin memiliki ukuran file CSS yang lebih besar karena mengandung semua gaya komponen, bahkan jika kita tidak menggunakannya semua.

- **Kapan Menggunakan Tailwind CSS**
    - Ketika ingin memiliki kontrol yang sangat mendalam atas desain tampilan
    - Ketika memerlukan fleksibilitas yang tinggi dalam mengatur tampilan elemen-elemen
    - Ketika ingin menghindari penambahan CSS yang tidak digunakan dalam proyek

- **Kapan Menggunakan Bootstrap**
    - Ketika membutuhkan prototyping cepat dan ingin memanfaatkan komponen yang sudah jadi.
    - Ketika tidak memiliki banyak waktu untuk menyesuaikan desain tampilan secara mendalam
    - Ketika lebih suka struktur yang lebih kaku dan lebih sedikit keputusan desain yang harus dibuat

## Jawaban Soal Tugas 4

### Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).
1. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
    - **REGISTER**
        - Dalam `views.py` import `redirect`, `UserCreationForm`, `messages `
        - Buat fungsi `register` yang berfungsi untuk menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-*submit* dari form
        - Buat berkas HTML baru dengan nama `register.html` pada folder `main/template` untuk membuat *template* dari *register*
        - Import fungsi `register` ke `urls.py`
        - Tambahkan *path url* ke `urlpatterns`
    - **LOGIN**
        - Dalam `views.py` import fungsi `authenticate`, `login`
        - Buat fungsi `login` yang berfungsi untuk mengautentikasi pengguna yang ingin *login*
        - Buat berkas HTML baru dengan nama `login.html` pada folder `main/template` untuk membuat *template* dari register
        - Import `login_user` ke `urls.py`
        - Tambahkan *path url* ke `urlpatterns`
    - **LOGOUT**
        - Dalam `views.py` import fungsi `logout`
        - Buat fungsi `logout` yang berfungsi untuk melakukan mekanisme *logout*
        - Buka berkas `main.html` tambahkan potongan kode yang berfungsi untuk Add New Product pada berkas `main.html`
        - Import `logout_user` ke `urls.py`
        - Tambahkan *path url* ke `urlpatterns`

2. Membuat **dua** akun pengguna dengan masing-masing **tiga** *dummy* data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun **di lokal**.
<img src='/aset/Dummy1_Tugas4.jpg'>
<img src='/aset/Dummy2_Tugas4.jpg'>

3. Menghubungkan model `Item` dengan `User`.
    - Import `user` pada `models.py`
    - Pada model `Item` yang sudah dibuat, tambahkan `ForeignKey` yang berfungsi untuk menghubungkan satu produk dengan satu user melalui sebuah `relationship`, dimana sebuah produk pasti terasosiasikan dengan seorang user
        - Pada `views.py` ubah fungsi `create_item`
        - Tambahkan parameter `commit=False` yang digunakan  untuk mencegah Django agar tidak langsung menyimpan objek ke database
        - Isi field `user` dengan objek `User` dari return value `request.user` untuk menandakan bahwa objek tersebut dimiliki oleh pengguna yang sedang login

3. Menampilkan detail informasi pengguna yang sedang *logged* in seperti *username* dan menerapkan `cookies` seperti `last login` pada halaman utama aplikasi
    - Ubah fungsi `show_main`
        - Menampilkan objek `Item` yang terasosiasikan dengan pengguna yang sedang login dengan `items = Item.objects.filter(user=request.user)`
        - Tambahkan kode `request.user.username`
    - Dalam `views.py` dan import `HttpResponseRedirect`, `reverse`, dan `datetime`
    - Pada fungsi `login_user` tambahkan fungsi `last_login` untuk melihat kapan terakhir kali pengguna melakukan *login*. Edit **blok** `if user is not None` dengan menambahkan kode:
        - `login(request, user)`
        - `response = HttpResponseRedirect(reverse("main:show_main"))`
        - `response.set_cookie('last_login', str(datetime.datetime.now()))`
        - `return response`
    - Pada fungsi `show_main` tambahkan `'last_login': request.COOKIES['last_login']` ke dalam variabel `context`
    - Ubah fungsi `logout_user` dengan menambahkan kode:
        - `response = HttpResponseRedirect(reverse('main:login'))`
        - `response.delete_cookie('last_login')`
        - `return response`
    - Pada berkas `main.html` tambahkan kode `<h5>Sesi terakhir login: {{ last_login }}</h5>`

### Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?
UserCreationForm adalah impor formulir bawaan yang memudahkan pembuatan formulir pendaftaran pengguna dalam aplikasi web. Dengan formulir ini, pengguna baru dapat mendaftar dengan mudah di situs web tanpa harus menulis kode dari awal.
- **Kelebihan**
    - **Cepat dan Mudah:** UserCreationForm memungkinkan pengembang untuk membuat formulir pendaftaran pengguna dengan cepat tanpa harus menulis kode dari awal.
    - **Integrasi dengan Django:** UserCreationForm terintegrasi secara baik dengan berbagai fitur otentikasi Django, termasuk penggunaan password yang dihash dan proses validasi.
    - **Keamanan Terintegrasi:** UserCreationForm sudah termasuk mekanisme keamanan yang umumnya diperlukan untuk mencegah serangan seperti SQL injection dan cross-site scripting (XSS).
- **Kekurangan**
    - **Terbatas pada Penggunaan Default:** UserCreationForm dirancang untuk pendaftaran pengguna dasar, sehingga memerlukan penyesuaian jika kita membutuhkan atribut atau data tambahan.
    - **Tidak Termasuk Semua Fitur:** Hanya mencakup hal-hal dasar seperti username dan password, jadi kita perlu menambahkan fitur tambahan secara manual seperti verifikasi email atau konfirmasi kata sandi.
    - **Ketergantungan pada Django:** Kita perlu menggunakan Django sebagai kerangka kerja pengembangan jika ingin menggunakan UserCreationForm. Jika kita mempertimbangkan kerangka kerja lain, ini mungkin tidak cocok.

### Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
**Autentikasi** dalam konteks Django adalah proses memeriksa apakah pengguna yang mencoba masuk ke sistem adalah benar-benar orang yang mereka katakan menjadi. Ini umumnya melibatkan proses login dengan menggunakan kombinasi username dan password.

**Otorisasi** adalah langkah untuk menetapkan hak akses pengguna setelah mereka berhasil terotentikasi. Ini mengatur apa yang diizinkan untuk dilakukan oleh pengguna setelah masuk, termasuk akses ke halaman atau sumber daya tertentu.

Keduanya hal diatas penting karena autentikasi memastikan pengguna yang sah, sementara otorisasi mengontrol akses mereka. Ini menjaga keamanan data dan sumber daya di aplikasi web.

### Apa itu *cookies* dalam konteks aplikasi web, dan bagaimana Django menggunakan *cookies* untuk mengelola data sesi pengguna?
*Cookies* di aplikasi web adalah potongan data kecil yang disimpan di perangkat pengguna, berfungsi untuk menyimpan informasi seperti ID sesi atau preferensi, yang dapat diakses oleh server web selama interaksi pengguna dengan situs atau aplikasi tersebut.

Django menggunakan *cookies* untuk mengelola data sesi pengguna dengan cara berikut:
- **Membuat Sesi Pengguna:** Menciptakan sesi pengguna dan ID sesi unik saat akses atau masuk.
- **Penyimpanan Data Sesi:** Menyimpan info sesi dalam cookies dan mengenkripsinya jika perlu.
- **Mengakses Data Sesi:** Membaca cookies pengguna pada permintaan selanjutnya.
- **Pembaruan Data Sesi:** Memungkinkan pengembang memperbarui sesi pengguna.
- **Pengakhiran Sesi:** Membersihkan data sesi saat keluar atau sesi berakhir.

### Apakah penggunaan *cookies* aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Dengan implementasi yang benar dan penggunaan di lingkungan yang aman, penggunaan *cookies* dalam pengembangan web biasanya merupakan praktik yang aman secara bawaan.

Penggunaan *cookies* dalam pengembangan web bisa menimbulkan risiko seperti pelanggaran privasi, pencurian cookie, dan kerentanan terhadap serangan. Untuk menghindari masalah ini, penting bagi pengembang untuk melakukan beberapa hal, seperti memvalidasi data dengan baik, menggunakan HTTPS, dan melindungi aplikasi web dari ancaman serangan. Dengan cara ini, data pengguna dan privasi bisa lebih aman.

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