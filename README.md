## DASAR PEMROGRAMAN JOB SHEET 2: PERINTAH INPUT-OUTPUT
#### Dibuat dan disusun oleh
| Variabel | Nilai               |
|----------|---------------------|
| Nama     | Naufal Reky Ardhana |
| NIM      | 4.33.22.0.21        |
| Kelas    | TI-1A               |


#### Tujuan Praktikum
Setelah melakukan praktikum ini mahasiswa mampu menyelesaikan studi kasus menggunakan perintah-perintah input dan output, variabel, tipe data, dan operator.

#### Perintah

| No  | Tugas                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | Seorang developer diberi tugas untuk membuat aplikasi kalkulator sederhana berbasis teks untuk memproses penjumlahan antar dua operand. Pengguna memasukan dua bilangan untuk dijumlahkan. Pada bagian akhir, program menampilkan hasil penjumlahan dan keluar. <br><br>**Modifikasi**: Modifikasi kode program agar dapat menerima dan memproses input bilangan bulat dan atau pecahan!                                                                                                                                                                                                     |
| 2   | Seorang developer diberi tugas untuk membuat aplikasi kalkulator sederhana berbasis teks untuk memproses pengurangan antar dua operand. Pengguna memasukan dua bilangan untuk dikurangkan. Pada bagian akhir, program menampilkan hasil pengurangan dan keluar.                                                                                                                                                                                                             |
| 3   | Seorang developer diberi tugas untuk membuat aplikasi kalkulator sederhana berbasis teks untuk memproses pembagian antar dua operand. Pengguna memasukan dua bilangan untuk dibagikan. Pada bagian akhir, program menampilkan hasil pembagian dan keluar.                                                                                                                                                                                                                   |
| 4   | Seorang developer diberi tugas untuk membuat aplikasi kalkulator sederhana berbasis teks untuk memproses pembagian antar dua operand. Pengguna memasukan dua bilangan untuk dibagikan. Pada bagian akhir, program menampilkan hasil pembagian dan keluar.                                                                                                                                                                                                                   |
| 5   | Seorang developer diberi tugas untuk membuat aplikasi kalkulator sederhana berbasis teks dengan menampilkan menu-menu penjumlahan, pengurangan, perkalian, dan pembagian antar dua bilangan. Pengguna bisa memilih salah satu menu dan memasukan dua bilangan untuk dioperasikan. Pada bagian akhir, program menampilkan hasil operasi dan keluar. <br><br>**Modifikasi**: Modifikasi kode program agar dapat memproses operasi modulus, exponentiation, dan floor division |
| 6   | Sebagai seorang developer, anda diberi tugas untuk membuat aplikasi yang dapat menghitung jumlah huruf dan kata dari kalimat yang dimasukan. Input berupa kalimat yang dimasukan oleh pengguna, dan hasilnya berupa jumlah karakter dan kata.                                                                                                                                                                                                                               |


#### Lembar Kerja

| Kode             | Hasil Program                                                                                                                                                                                                                                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Lembar Kerja 1.1](https://github.com/ardzz/dasar-pemrogaman-2/blob/master/challenge_1.py) | ![](https://github.com/ardzz/dasar-pemrogaman-2/blob/master/images/Screen%20Shot%202022-09-12%20at%2015.19.17.png?raw=true)<br/>Modifikasi: Saya membuat satu fungsi untuk memvalidasi tipe data yang diinputkan user agar hanya tipe data `int` dan `float` saja yang bisa diproses. Berikut kodenya: [Kode Lembar Kerja 1.1](#lembar-kerja-11)<br/>Dari potongan kode tersebut bisa disimpulkan bahwa output yang sudah dimodifikasi tidak memiliki perbedaan |
| Lembar Kerja 1.2 |                                                                                                                                                                                                                                                                                                                                                                                        |
| Lembar Kerja 1.3 |                                                                                                                                                                                                                                                                                                                                                                                        |
| Lembar Kerja 1.4 |                                                                                                                                                                                                                                                                                                                                                                                        |
| Lembar Kerja 1.5 |                                                                                                                                                                                                                                                                                                                                                                                        |
| Praktik no 2     |                                                                                                                                                                                                                                                                                                                                                                                        |

#### Aset Kode
#### Lembar Kerja 1.1
```python
def input_number(message: str) -> int or float:
    return identify_number(input(message))


def identify_number(number) -> int or float:
    try:
        return int(number)
    except ValueError:
        try:
            return float(number)
        except ValueError:
            raise ValueError
        except TypeError:
            raise TypeError
```
