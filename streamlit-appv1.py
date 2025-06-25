import streamlit as st
import math

# Fungsi perhitungan
def luas_persegi(s):
    return s * s

def keliling_persegi(s):
    return 4 * s

def luas_persegi_panjang(p, l):
    return p * l

def keliling_persegi_panjang(p, l):
    return 2 * (p + l)

def luas_segitiga(a, t):
    return 0.5 * a * t

def keliling_segitiga(a, b, c):
    return a + b + c

def luas_lingkaran(r):
    return math.pi * r**2

def keliling_lingkaran(r):
    return 2 * math.pi * r

def luas_jajar_genjang(a, t):
    return a * t

def keliling_jajar_genjang(a, b):
    return 2 * (a + b)

def luas_trapesium(a, b, t):
    return 0.5 * (a + b) * t

def keliling_trapesium(a, b, c, d):
    return a + b + c + d

def luas_belah_ketupat(d1, d2):
    return 0.5 * d1 * d2

def keliling_belah_ketupat(s):
    return 4 * s

def luas_layang_layang(d1, d2):
    return 0.5 * d1 * d2

def keliling_layang_layang(a, b):
    return 2 * (a + b)

# Sidebar Navigasi
st.sidebar.title("🔷 Menu Bangun Datar")
menu_bangun = st.sidebar.selectbox("Pilih Bangun Datar", [
    "Persegi", "Persegi Panjang", "Segitiga", "Lingkaran",
    "Jajar Genjang", "Trapesium", "Belah Ketupat", "Layang-Layang"
])

menu_operasi = st.sidebar.radio("Pilih Operasi", ["Luas", "Keliling"])

st.title(f"{menu_operasi} {menu_bangun}")

# Konten berdasarkan pilihan
if menu_bangun == "Persegi":
    s = st.number_input("Masukkan panjang sisi", min_value=0.0)
    if menu_operasi == "Luas":
        st.success(f"Luas Persegi = {luas_persegi(s)}")
    else:
        st.success(f"Keliling Persegi = {keliling_persegi(s)}")

elif menu_bangun == "Persegi Panjang":
    p = st.number_input("Masukkan panjang", min_value=0.0)
    l = st.number_input("Masukkan lebar", min_value=0.0)
    if menu_operasi == "Luas":
        st.success(f"Luas Persegi Panjang = {luas_persegi_panjang(p, l)}")
    else:
        st.success(f"Keliling Persegi Panjang = {keliling_persegi_panjang(p, l)}")

elif menu_bangun == "Segitiga":
    if menu_operasi == "Luas":
        a = st.number_input("Masukkan alas", min_value=0.0)
        t = st.number_input("Masukkan tinggi", min_value=0.0)
        st.success(f"Luas Segitiga = {luas_segitiga(a, t)}")
    else:
        a = st.number_input("Sisi A", min_value=0.0)
        b = st.number_input("Sisi B", min_value=0.0)
        c = st.number_input("Sisi C", min_value=0.0)
        st.success(f"Keliling Segitiga = {keliling_segitiga(a, b, c)}")

elif menu_bangun == "Lingkaran":
    r = st.number_input("Masukkan jari-jari", min_value=0.0)
    if menu_operasi == "Luas":
        st.success(f"Luas Lingkaran = {luas_lingkaran(r):.2f}")
    else:
        st.success(f"Keliling Lingkaran = {keliling_lingkaran(r):.2f}")

elif menu_bangun == "Jajar Genjang":
    if menu_operasi == "Luas":
        a = st.number_input("Masukkan alas", min_value=0.0)
        t = st.number_input("Masukkan tinggi", min_value=0.0)
        st.success(f"Luas Jajar Genjang = {luas_jajar_genjang(a, t)}")
    else:
        a = st.number_input("Sisi A", min_value=0.0)
        b = st.number_input("Sisi B", min_value=0.0)
        st.success(f"Keliling Jajar Genjang = {keliling_jajar_genjang(a, b)}")

elif menu_bangun == "Trapesium":
    if menu_operasi == "Luas":
        a = st.number_input("Sisi Atas", min_value=0.0)
        b = st.number_input("Sisi Bawah", min_value=0.0)
        t = st.number_input("Tinggi", min_value=0.0)
        st.success(f"Luas Trapesium = {luas_trapesium(a, b, t)}")
    else:
        a = st.number_input("Sisi A", min_value=0.0)
        b = st.number_input("Sisi B", min_value=0.0)
        c = st.number_input("Sisi C", min_value=0.0)
        d = st.number_input("Sisi D", min_value=0.0)
        st.success(f"Keliling Trapesium = {keliling_trapesium(a, b, c, d)}")

elif menu_bangun == "Belah Ketupat":
    if menu_operasi == "Luas":
        d1 = st.number_input("Diagonal 1", min_value=0.0)
        d2 = st.number_input("Diagonal 2", min_value=0.0)
        st.success(f"Luas Belah Ketupat = {luas_belah_ketupat(d1, d2)}")
    else:
        s = st.number_input("Sisi", min_value=0.0)
        st.success(f"Keliling Belah Ketupat = {keliling_belah_ketupat(s)}")

elif menu_bangun == "Layang-Layang":
    if menu_operasi == "Luas":
        d1 = st.number_input("Diagonal 1", min_value=0.0)
        d2 = st.number_input("Diagonal 2", min_value=0.0)
        st.success(f"Luas Layang-Layang = {luas_layang_layang(d1, d2)}")
    else:
        a = st.number_input("Sisi A", min_value=0.0)
        b = st.number_input("Sisi B", min_value=0.0)
        st.success(f"Keliling Layang-Layang = {keliling_layang_layang(a, b)}")
