import streamlit as st
import math
from PIL import Image

st.set_page_config(page_title="🎲 Bangun Datar Anak", layout="centered")

# Mode Anak-anak
mode_anak = st.sidebar.checkbox("🌈 Aktifkan Mode Anak-anak")

# Warna & efek suara
if mode_anak:
    st.markdown("<style>body {background-color: #FFF8DC; color: #333; font-size:18px;}</style>", unsafe_allow_html=True)
    st.balloons()
    st.audio("audio/yay.mp3", format="audio/mp3")

# Gambar tiap bangun
gambar_dict = {
    "Persegi": "images/persegi.png",
    "Persegi Panjang": "images/persegi_panjang2.png",
    "Segitiga": "images/segitiga.png",
    "Lingkaran": "images/lingkaran.png",
    "Jajar Genjang": "images/jajar_genjang.png",
    "Trapesium": "images/trapesium.png",
    "Belah Ketupat": "images/belah_ketupat.png",
    "Layang-Layang": "images/layang_layang.png"
}

# Fungsi Matematika
def luas_persegi(s): return s**2
def keliling_persegi(s): return 4 * s
def luas_persegi_panjang(p, l): return p * l
def keliling_persegi_panjang(p, l): return 2 * (p + l)
def luas_segitiga(a, t): return 0.5 * a * t
def keliling_segitiga(a, b, c): return a + b + c
def luas_lingkaran(r): return math.pi * r**2
def keliling_lingkaran(r): return 2 * math.pi * r
def luas_jajar_genjang(a, t): return a * t
def keliling_jajar_genjang(a, b): return 2 * (a + b)
def luas_trapesium(a, b, t): return 0.5 * (a + b) * t
def keliling_trapesium(a, b, c, d): return a + b + c + d
def luas_belah_ketupat(d1, d2): return 0.5 * d1 * d2
def keliling_belah_ketupat(s): return 4 * s
def luas_layang_layang(d1, d2): return 0.5 * d1 * d2
def keliling_layang_layang(a, b): return 2 * (a + b)

# Sidebar Menu
st.sidebar.title("📐 Pilih Bangun Datar")
bangun = st.sidebar.selectbox("🔷 Bangun Datar", list(gambar_dict.keys()))

# Multi-tab
tab1, tab2 = st.tabs(["📏 Luas", "📏 Keliling"])

# --- Tab Luas ---
with tab1:
    st.subheader(f"Luas {bangun}")
    if bangun == "Persegi":
        s = st.number_input("Sisi", min_value=0.0, key="sisi_persegi_luas")
        st.success(f"Luas: {luas_persegi(s)}")
    elif bangun == "Persegi Panjang":
        p = st.number_input("Panjang", min_value=0.0, key="panjang_pp_luas")
        l = st.number_input("Lebar", min_value=0.0, key="lebar_pp_luas")
        st.success(f"Luas: {luas_persegi_panjang(p, l)}")
    elif bangun == "Segitiga":
        a = st.number_input("Alas", min_value=0.0, key="alas_segitiga_luas")
        t = st.number_input("Tinggi", min_value=0.0, key="tinggi_segitiga_luas")
        st.success(f"Luas: {luas_segitiga(a, t)}")
    elif bangun == "Lingkaran":
        r = st.number_input("Jari-jari", min_value=0.0, key="jari_lingkaran_luas")
        st.success(f"Luas: {luas_lingkaran(r):.2f}")
    elif bangun == "Jajar Genjang":
        a = st.number_input("Alas", min_value=0.0, key="alas_jg_luas")
        t = st.number_input("Tinggi", min_value=0.0, key="tinggi_jg_luas")
        st.success(f"Luas: {luas_jajar_genjang(a, t)}")
    elif bangun == "Trapesium":
        a = st.number_input("Sisi Atas", min_value=0.0, key="atas_trapesium_luas")
        b = st.number_input("Sisi Bawah", min_value=0.0, key="bawah_trapesium_luas")
        t = st.number_input("Tinggi", min_value=0.0, key="tinggi_trapesium_luas")
        st.success(f"Luas: {luas_trapesium(a, b, t)}")
    elif bangun == "Belah Ketupat":
        d1 = st.number_input("Diagonal 1", min_value=0.0, key="d1_bk_luas")
        d2 = st.number_input("Diagonal 2", min_value=0.0, key="d2_bk_luas")
        st.success(f"Luas: {luas_belah_ketupat(d1, d2)}")
    elif bangun == "Layang-Layang":
        d1 = st.number_input("Diagonal 1", min_value=0.0, key="d1_ll_luas")
        d2 = st.number_input("Diagonal 2", min_value=0.0, key="d2_ll_luas")
        st.success(f"Luas: {luas_layang_layang(d1, d2)}")

# --- Tab Keliling ---
with tab2:
    st.subheader(f"Keliling {bangun}")
    if bangun == "Persegi":
        s = st.number_input("Sisi", min_value=0.0, key="sisi_persegi_kel")
        st.success(f"Keliling: {keliling_persegi(s)}")
    elif bangun == "Persegi Panjang":
        p = st.number_input("Panjang", min_value=0.0, key="panjang_pp_kel")
        l = st.number_input("Lebar", min_value=0.0, key="lebar_pp_kel")
        st.success(f"Keliling: {keliling_persegi_panjang(p, l)}")
    elif bangun == "Segitiga":
        a = st.number_input("Sisi A", min_value=0.0, key="a_segitiga_kel")
        b = st.number_input("Sisi B", min_value=0.0, key="b_segitiga_kel")
        c = st.number_input("Sisi C", min_value=0.0, key="c_segitiga_kel")
        st.success(f"Keliling: {keliling_segitiga(a, b, c)}")
    elif bangun == "Lingkaran":
        r = st.number_input("Jari-jari", min_value=0.0, key="jari_lingkaran_kel")
        st.success(f"Keliling: {keliling_lingkaran(r):.2f}")
    elif bangun == "Jajar Genjang":
        a = st.number_input("Sisi A", min_value=0.0, key="a_jg_kel")
        b = st.number_input("Sisi B", min_value=0.0, key="b_jg_kel")
        st.success(f"Keliling: {keliling_jajar_genjang(a, b)}")
    elif bangun == "Trapesium":
        a = st.number_input("Sisi A", min_value=0.0, key="a_trap_kel")
        b = st.number_input("Sisi B", min_value=0.0, key="b_trap_kel")
        c = st.number_input("Sisi C", min_value=0.0, key="c_trap_kel")
        d = st.number_input("Sisi D", min_value=0.0, key="d_trap_kel")
        st.success(f"Keliling: {keliling_trapesium(a, b, c, d)}")
    elif bangun == "Belah Ketupat":
        s = st.number_input("Sisi", min_value=0.0, key="sisi_bk_kel")
        st.success(f"Keliling: {keliling_belah_ketupat(s)}")
    elif bangun == "Layang-Layang":
        a = st.number_input("Sisi A", min_value=0.0, key="a_ll_kel")
        b = st.number_input("Sisi B", min_value=0.0, key="b_ll_kel")
        st.success(f"Keliling: {keliling_layang_layang(a, b)}")
        
# Tampilkan Gambar
st.image(Image.open(gambar_dict[bangun]), caption=f"Gambar {bangun}", width=150)
# Tampilkan Materi Bacaan
st.text ("Materi: https://id.wikipedia.org/wiki/Segitiga")

# Footer
st.markdown("---")
st.markdown("👩‍🏫 Dibuat untuk belajar sambil bermain • By Ramlan Marbun ❤️")
