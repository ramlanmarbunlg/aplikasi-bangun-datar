import streamlit as st
import math
from PIL import Image
import time
import random
import json
import os

# Konfigurasi halaman
st.set_page_config(page_title="🎲 Bangun Datar Anak", layout="centered")

# Tema warna ceria dinamis
warna_ceria = [
    {"bg": "#FFF8DC", "text": "#333333"},
    {"bg": "#FFFAF0", "text": "#FF1493"},
    {"bg": "#E0FFFF", "text": "#008080"},
    {"bg": "#FDF5E6", "text": "#8B008B"},
    {"bg": "#FFF0F5", "text": "#DC143C"},
]

# Inisialisasi session state
if "mulai_main" not in st.session_state:
    st.session_state.mulai_main = False
if "loading_page" not in st.session_state:
    st.session_state.loading_page = False
if "mode_anak" not in st.session_state:
    st.session_state.mode_anak = False
if "tema_anak" not in st.session_state:
    st.session_state.tema_anak = random.choice(warna_ceria)
if "mode_quiz" not in st.session_state:
    st.session_state.mode_quiz = False
if "quiz_index" not in st.session_state:
    st.session_state.quiz_index = 0
if "quiz_jawaban" not in st.session_state:
    st.session_state.quiz_jawaban = {}
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
if "kategori_quiz" not in st.session_state:
    st.session_state.kategori_quiz = None
if "high_score" not in st.session_state:
    st.session_state.high_score = {}

# Jika sedang di halaman loading
if st.session_state.loading_page:
    st.markdown("<h4 style='text-align:center;'>⏳ Memuat permainan seru untukmu...</h4>", unsafe_allow_html=True)
    progress_bar = st.progress(0)
    percent_text = st.empty()
    for i in range(101):
        time.sleep(0.01)
        progress_bar.progress(i)
        percent_text.markdown(f"<h5 style='text-align:center;'>{i} %</h5>", unsafe_allow_html=True)
    st.session_state.loading_page = False
    st.session_state.mulai_main = True
    st.session_state.mode_anak = True
    st.rerun()

# Halaman pembuka
if not st.session_state.mulai_main:
    st.markdown("<h1 style='text-align: center; color: #FF69B4;'>🎉 Selamat Datang Anak Hebat!</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Mari belajar bangun datar sambil bermain 🧠🎨</h3>", unsafe_allow_html=True)
    st.image("images/karakter1.png", width=150, caption="Ayo mulai petualanganmu!")

    if st.button("👉 Klik untuk Mulai Bermain 🎲", type="primary"):
        st.session_state.loading_page = True
        st.rerun()

    st.stop()

# Mode anak-anak aktif
if st.session_state.mode_anak:
    tema = st.session_state.tema_anak
    st.markdown(f"""
        <style>
        body {{
            background-color: {tema['bg']};
            color: {tema['text']};
            font-size: 18px;
        }}
        </style>
    """, unsafe_allow_html=True)
    st.balloons()

# Sidebar
if st.sidebar.button("🔙 Halaman Awal"):
    st.session_state.mulai_main = False
    st.session_state.mode_quiz = False
    st.rerun()

if st.sidebar.button("🎯 Mode Quiz"):
    st.session_state.mode_quiz = True
    st.session_state.quiz_index = 0
    st.session_state.quiz_jawaban = {}
    st.session_state.kategori_quiz = None
    st.session_state.start_time = time.time()
    st.rerun()

if st.sidebar.button("📐 Mode Kalkulasi"):
    st.session_state.mode_quiz = False
    st.session_state.quiz_index = 0
    st.session_state.quiz_jawaban = {}
    st.session_state.start_time = time.time()
    st.rerun()


st.sidebar.markdown("<h4 style='margin-bottom:10px;'>📐 Pilih Bangun Datar</h4>", unsafe_allow_html=True)

# =============== MODE QUIZ ==================
if st.session_state.mode_quiz:
    if not st.session_state.kategori_quiz:
        kategori = st.selectbox("Pilih kategori quiz:", [
            "Persegi", "Persegi Panjang", "Segitiga", "Lingkaran",
            "Jajar Genjang", "Trapesium", "Belah Ketupat", "Layang-Layang"])
        if st.button("Mulai Quiz"):
            st.session_state.kategori_quiz = kategori
            st.session_state.start_time = time.time()
            st.rerun()
        st.stop()

    # Load soal dari file JSON
    with open("soal_quiz.json") as f:
        all_soal = json.load(f)

    soal_data = [s for s in all_soal if s["kategori"] == st.session_state.kategori_quiz]
    total_soal = len(soal_data)
    indeks = st.session_state.quiz_index

    st.header(f"🎓 Quiz: {st.session_state.kategori_quiz} - Soal {indeks + 1} dari {total_soal}")

    if indeks < total_soal:
        soal = soal_data[indeks]
        st.markdown(f"**{soal['soal']}**")
        jawaban = st.radio("Pilih jawaban:", soal["opsi"], key=f"soal_{indeks}")

        elapsed = int(time.time() - st.session_state.start_time)
        sisa_waktu = max(0, 15 - elapsed)
        st.info(f"⏳ Sisa waktu: {sisa_waktu} detik")

        if sisa_waktu == 0:
            st.session_state.quiz_jawaban[indeks] = jawaban
            st.session_state.quiz_index += 1
            st.session_state.start_time = time.time()
            st.rerun()

        if st.button("✅ Jawab dan Lanjut"):
            st.session_state.quiz_jawaban[indeks] = jawaban
            st.session_state.quiz_index += 1
            st.session_state.start_time = time.time()
            st.rerun()

        st.stop()

    # Tampilkan hasil akhir
    st.subheader("📊 Hasil Evaluasi")
    skor = 0
    for i, soal in enumerate(soal_data):
        user_jawaban = st.session_state.quiz_jawaban.get(i, "(Belum Dijawab)")
        benar = user_jawaban == soal["jawaban"]
        ikon = "✅" if benar else "❌"
        warna = "green" if benar else "red"
        if benar:
            skor += 1
        st.markdown(f"**Soal {i+1}: {ikon}**")
        st.markdown(soal["soal"])
        st.markdown(f"**Jawabanmu:** {user_jawaban}")
        st.markdown(f"<span style='color:{warna};'>**Jawaban benar:** {soal['jawaban']}</span>", unsafe_allow_html=True)
        st.markdown(f"📝 *Pembahasan:* {soal['pembahasan']}")
        st.markdown("---")

    st.success(f"🎉 Skor kamu: {skor} dari {total_soal}")

    # Cek dan simpan skor tertinggi per kategori
    kategori = st.session_state.kategori_quiz
    if kategori not in st.session_state.high_score or skor > st.session_state.high_score[kategori]:
        st.session_state.high_score[kategori] = skor
        st.balloons()
        st.success("🌟 Selamat! Skor tertinggi baru!")

    # Tampilkan skor tertinggi semua kategori
    st.markdown("### 🏆 Skor Tertinggi Tiap Kategori")
    for k, v in st.session_state.high_score.items():
        st.markdown(f"- **{k}**: {v} poin")

    if st.button("🔁 Ulangi Quiz"):
        for key in list(st.session_state.keys()):
            if key.startswith("soal") or key.startswith("quiz") or key == "kategori_quiz":
                del st.session_state[key]
        st.session_state.mode_quiz = True
        st.session_state.quiz_index = 0
        st.session_state.quiz_jawaban = {}
        st.session_state.start_time = time.time()
        st.rerun()

    # ✅ Tombol untuk kembali ke mode kalkulasi
    if st.button("📐 Kembali ke Mode Kalkulasi"):
    st.session_state.mode_quiz = False
    st.session_state.quiz_index = 0
    st.session_state.quiz_jawaban = {}
    st.session_state.start_time = time.time()
    st.rerun()

    st.stop()

# ============= MODE KALKULASI BANGUN DATAR=============
# Gambar ilustrasi tiap bangun
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

# Fungsi rumus masing-masing bangun
# (Disusun sesuai kebutuhan Luas dan Keliling)
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

# Sidebar pilihan bangun datar
bangun = st.sidebar.selectbox("🔷 Bangun Datar", list(gambar_dict.keys()))

# Tab Luas dan Keliling
st.markdown("---")
tab1, tab2 = st.tabs(["📏 Luas", "📐 Keliling"])

with tab1:
    st.subheader(f"Luas {bangun}")
    if bangun == "Persegi":
        s = st.number_input("Sisi", min_value=0.0, key="luas_s")
        st.success(f"Luas: {luas_persegi(s)} cm²")
    elif bangun == "Persegi Panjang":
        p = st.number_input("Panjang", min_value=0.0, key="luas_p")
        l = st.number_input("Lebar", min_value=0.0, key="luas_l")
        st.success(f"Luas: {luas_persegi_panjang(p, l)} cm²")
    elif bangun == "Segitiga":
        a = st.number_input("Alas", min_value=0.0, key="luas_a")
        t = st.number_input("Tinggi", min_value=0.0, key="luas_t")
        st.success(f"Luas: {luas_segitiga(a, t)} cm²")
    elif bangun == "Lingkaran":
        r = st.number_input("Jari-jari", min_value=0.0, key="luas_r")
        st.success(f"Luas: {luas_lingkaran(r):.2f} cm²")
    elif bangun == "Jajar Genjang":
        a = st.number_input("Alas", min_value=0.0, key="luas_ajg")
        t = st.number_input("Tinggi", min_value=0.0, key="luas_tjg")
        st.success(f"Luas: {luas_jajar_genjang(a, t)} cm²")
    elif bangun == "Trapesium":
        a = st.number_input("Sisi Atas", min_value=0.0, key="luas_a1t")
        b = st.number_input("Sisi Bawah", min_value=0.0, key="luas_b1t")
        t = st.number_input("Tinggi", min_value=0.0, key="luas_t1t")
        st.success(f"Luas: {luas_trapesium(a, b, t)} cm²")
    elif bangun == "Belah Ketupat":
        d1 = st.number_input("Diagonal 1", min_value=0.0, key="luas_d1")
        d2 = st.number_input("Diagonal 2", min_value=0.0, key="luas_d2")
        st.success(f"Luas: {luas_belah_ketupat(d1, d2)} cm²")
    elif bangun == "Layang-Layang":
        d1 = st.number_input("Diagonal 1", min_value=0.0, key="luas_d1l")
        d2 = st.number_input("Diagonal 2", min_value=0.0, key="luas_d2l")
        st.success(f"Luas: {luas_layang_layang(d1, d2)} cm²")

with tab2:
    st.subheader(f"Keliling {bangun}")
    if bangun == "Persegi":
        s = st.number_input("Sisi", min_value=0.0, key="kel_s")
        st.success(f"Keliling: {keliling_persegi(s)} cm")
    elif bangun == "Persegi Panjang":
        p = st.number_input("Panjang", min_value=0.0, key="kel_p")
        l = st.number_input("Lebar", min_value=0.0, key="kel_l")
        st.success(f"Keliling: {keliling_persegi_panjang(p, l)} cm")
    elif bangun == "Segitiga":
        a = st.number_input("Sisi A", min_value=0.0, key="kel_a")
        b = st.number_input("Sisi B", min_value=0.0, key="kel_b")
        c = st.number_input("Sisi C", min_value=0.0, key="kel_c")
        st.success(f"Keliling: {keliling_segitiga(a, b, c)} cm")
    elif bangun == "Lingkaran":
        r = st.number_input("Jari-jari", min_value=0.0, key="kel_r")
        st.success(f"Keliling: {keliling_lingkaran(r):.2f} cm")
    elif bangun == "Jajar Genjang":
        a = st.number_input("Sisi A", min_value=0.0, key="kel_ajg")
        b = st.number_input("Sisi B", min_value=0.0, key="kel_bjg")
        st.success(f"Keliling: {keliling_jajar_genjang(a, b)} cm")
    elif bangun == "Trapesium":
        a = st.number_input("Sisi A", min_value=0.0, key="kel_at")
        b = st.number_input("Sisi B", min_value=0.0, key="kel_bt")
        c = st.number_input("Sisi C", min_value=0.0, key="kel_ct")
        d = st.number_input("Sisi D", min_value=0.0, key="kel_dt")
        st.success(f"Keliling: {keliling_trapesium(a, b, c, d)} cm")
    elif bangun == "Belah Ketupat":
        s = st.number_input("Sisi", min_value=0.0, key="kel_sb")
        st.success(f"Keliling: {keliling_belah_ketupat(s)} cm")
    elif bangun == "Layang-Layang":
        a = st.number_input("Sisi A", min_value=0.0, key="kel_ak")
        b = st.number_input("Sisi B", min_value=0.0, key="kel_bk")
        st.success(f"Keliling: {keliling_layang_layang(a, b)} cm")

# Tampilkan gambar dan link materi
img = Image.open(gambar_dict[bangun])
st.image(img.resize((150,150)), caption=f"Gambar {bangun}")

link_dict = {
    "Persegi": "https://id.wikipedia.org/wiki/Persegi",
    "Persegi Panjang": "https://id.wikipedia.org/wiki/Persegi_panjang",
    "Segitiga": "https://id.wikipedia.org/wiki/Segitiga",
    "Lingkaran": "https://id.wikipedia.org/wiki/Lingkaran",
    "Jajar Genjang": "https://id.wikipedia.org/wiki/Jajar_genjang",
    "Trapesium": "https://id.wikipedia.org/wiki/Trapesium_(geometri)",
    "Belah Ketupat": "https://id.wikipedia.org/wiki/Belah_ketupat",
    "Layang-Layang": "https://id.wikipedia.org/wiki/Layang-layang_(geometri)"
}

st.markdown(f"📚 [Baca materi lengkap tentang {bangun}]({link_dict[bangun]})")

# Footer
st.markdown("---")
st.markdown("👩‍🏫 Dibuat untuk belajar sambil bermain • By Ramlan Marbun ❤️")
