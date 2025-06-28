import streamlit as st
import math
from PIL import Image

# Konfigurasi halaman
st.set_page_config(page_title="🎲 Bangun Datar Anak", layout="centered")

# Cek apakah sudah mulai
if "mulai_main" not in st.session_state:
    st.session_state.mulai_main = False

# Halaman pembuka
if not st.session_state.mulai_main:
    st.markdown("<h1 style='text-align: center; color: #FF69B4;'>🎉 Selamat Datang Anak Hebat!</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Mari belajar bangun datar sambil bermain 🧠🎨</h3>", unsafe_allow_html=True)
    st.image("images/karakter1.png", width=200, caption="Ayo mulai petualanganmu!")
    
    if st.button("👉 Klik untuk Mulai Bermain 🎲", type="primary"):
        st.session_state.mulai_main = True
        st.session_state.mode_anak = True  # Otomatis aktifkan mode anak
        st.rerun()

    st.stop()

# --------- MAIN APLIKASI ---------
# Aktifkan mode anak-anak jika dipilih
mode_anak = st.session_state.get("mode_anak", False)

if mode_anak:
    st.markdown("<style>body {background-color: #FFF8DC; color: #333; font-size:18px;}</style>", unsafe_allow_html=True)
    st.balloons()
    st.markdown(
        """
        <audio autoplay>
            <source src="audio/yay.mp3" type="audio/mpeg">
        </audio>
        """,
        unsafe_allow_html=True
    )

# Bangun datar & gambar
gambar_dict = {
    "Persegi": "images/persegi.png",
    "Persegi Panjang": "images/persegi_panjang.png",
    "Segitiga": "images/segitiga.png",
    "Lingkaran": "images/lingkaran.png",
    "Jajar Genjang": "images/jajar_genjang.png",
    "Trapesium": "images/trapesium.png",
    "Belah Ketupat": "images/belah_ketupat.png",
    "Layang-Layang": "images/layang_layang.png"
}

# Fungsi perhitungan
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

# Sidebar menu
st.sidebar.title("📐 Pilih Bangun Datar")
bangun = st.sidebar.selectbox("🔷 Bangun Datar", list(gambar_dict.keys()))

# Gambar dan link materi
img = Image.open(gambar_dict[bangun])
img_resized = img.resize((500, 500))
st.image(img_resized, caption=f"Gambar {bangun}")

# Link materi (contoh)
link_dict = {
    "Persegi": "https://example.com/persegi",
    "Persegi Panjang": "https://example.com/persegi-panjang",
    "Segitiga": "https://example.com/segitiga",
    "Lingkaran": "https://example.com/lingkaran",
    "Jajar Genjang": "https://example.com/jajar-genjang",
    "Trapesium": "https://example.com/trapesium",
    "Belah Ketupat": "https://example.com/belah-ketupat",
    "Layang-Layang": "https://example.com/layang-layang"
}
st.markdown(f"📚 [Baca materi lengkap tentang {bangun}]({link_dict[bangun]})")

# Tab luas dan keliling
tab1, tab2 = st.tabs(["📏 Luas", "📏 Keliling"])

with tab1:
    st.subheader(f"Luas {bangun}")
    if bangun == "Persegi":
        s = st.number_input("Sisi", min_value=0.0, key="sisi_luas_persegi")
        st.success(f"Luas: {luas_persegi(s)}")
    elif bangun == "Persegi Panjang":
        p = st.number_input("Panjang", min_value=0.0, key="p_luas_pp")
        l = st.number_input("Lebar", min_value=0.0, key="l_luas_pp")
        st.success(f"Luas: {luas_persegi_panjang(p, l)}")
    elif bangun == "Segitiga":
        a = st.number_input("Alas", min_value=0.0, key="a_luas_seg")
        t = st.number_input("Tinggi", min_value=0.0, key="t_luas_seg")
        st.success(f"Luas: {luas_segitiga(a, t)}")
    elif bangun == "Lingkaran":
        r = st.number_input("Jari-jari", min_value=0.0, key="r_luas_ling")
        st.success(f"Luas: {luas_lingkaran(r):.2f}")
    elif bangun == "Jajar Genjang":
        a = st.number_input("Alas", min_value=0.0, key="a_luas_jg")
        t = st.number_input("Tinggi", min_value=0.0, key="t_luas_jg")
        st.success(f"Luas: {luas_jajar_genjang(a, t)}")
    elif bangun == "Trapesium":
        a = st.number_input("Sisi Atas", min_value=0.0, key="a_luas_trap")
        b = st.number_input("Sisi Bawah", min_value=0.0, key="b_luas_trap")
        t = st.number_input("Tinggi", min_value=0.0, key="t_luas_trap")
        st.success(f"Luas: {luas_trapesium(a, b, t)}")
    elif bangun == "Belah Ketupat":
        d1 = st.number_input("Diagonal 1", min_value=0.0, key="d1_luas_bk")
        d2 = st.number_input("Diagonal 2", min_value=0.0, key="d2_luas_bk")
        st.success(f"Luas: {luas_belah_ketupat(d1, d2)}")
    elif bangun == "Layang-Layang":
        d1 = st.number_input("Diagonal 1", min_value=0.0, key="d1_luas_ll")
        d2 = st.number_input("Diagonal 2", min_value=0.0, key="d2_luas_ll")
        st.success(f"Luas: {luas_layang_layang(d1, d2)}")

with tab2:
    st.subheader(f"Keliling {bangun}")
    if bangun == "Persegi":
        s = st.number_input("Sisi", min_value=0.0, key="sisi_kel_persegi")
        st.success(f"Keliling: {keliling_persegi(s)}")
    elif bangun == "Persegi Panjang":
        p = st.number_input("Panjang", min_value=0.0, key="p_kel_pp")
        l = st.number_input("Lebar", min_value=0.0, key="l_kel_pp")
        st.success(f"Keliling: {keliling_persegi_panjang(p, l)}")
    elif bangun == "Segitiga":
        a = st.number_input("Sisi A", min_value=0.0, key="a_kel_seg")
        b = st.number_input("Sisi B", min_value=0.0, key="b_kel_seg")
        c = st.number_input("Sisi C", min_value=0.0, key="c_kel_seg")
        st.success(f"Keliling: {keliling_segitiga(a, b, c)}")
    elif bangun == "Lingkaran":
        r = st.number_input("Jari-jari", min_value=0.0, key="r_kel_ling")
        st.success(f"Keliling: {keliling_lingkaran(r):.2f}")
    elif bangun == "Jajar Genjang":
        a = st.number_input("Sisi A", min_value=0.0, key="a_kel_jg")
        b = st.number_input("Sisi B", min_value=0.0, key="b_kel_jg")
        st.success(f"Keliling: {keliling_jajar_genjang(a, b)}")
    elif bangun == "Trapesium":
        a = st.number_input("Sisi A", min_value=0.0, key="a_kel_trap")
        b = st.number_input("Sisi B", min_value=0.0, key="b_kel_trap")
        c = st.number_input("Sisi C", min_value=0.0, key="c_kel_trap")
        d = st.number_input("Sisi D", min_value=0.0, key="d_kel_trap")
        st.success(f"Keliling: {keliling_trapesium(a, b, c, d)}")
    elif bangun == "Belah Ketupat":
        s = st.number_input("Sisi", min_value=0.0, key="s_kel_bk")
        st.success(f"Keliling: {keliling_belah_ketupat(s)}")
    elif bangun == "Layang-Layang":
        a = st.number_input("Sisi A", min_value=0.0, key="a_kel_ll")
        b = st.number_input("Sisi B", min_value=0.0, key="b_kel_ll")
        st.success(f"Keliling: {keliling_layang_layang(a, b)}")

# Footer
st.markdown("---")
st.markdown("👩‍🏫 Dibuat untuk belajar sambil bermain • By Ramlan Marbun ❤️")
