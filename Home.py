import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Diet Sehat", page_icon="🍇", layout="centered")

# CSS untuk background gradasi dan style teks
st.markdown("""
    <style>
        body {
            background: linear-gradient(to right, #5dade2, #d2b4de);
        }
        .title {
            text-align: center;
            color: black;
            font-size: 36px;
            font-weight: bold;
            margin-top: 50px;
        }
        .image-container {
            text-align: center;
            margin-top: 30px;
        }
        .button-container {
            display: flex;
            justify-content: center;
            margin-top: 40px;
        }
    </style>
""", unsafe_allow_html=True)

# Judul
st.markdown("<div class='title'>Jagalah Tubuh Anda dengan Diet yang Sehat!</div>", unsafe_allow_html=True)

# Gambar buah-buahan
st.markdown("""
    <div class='image-container'>
        <img src='https://cdn.pixabay.com/photo/2017/01/20/15/06/fruits-1995056_960_720.jpg' width='500'/>
    </div>
""", unsafe_allow_html=True)

# Tombol "Lanjut"
st.markdown("<div class='button-container'>", unsafe_allow_html=True)
lanjut = st.button("Lanjut")
st.markdown("</div>", unsafe_allow_html=True)

# Aksi ketika tombol ditekan
if lanjut:
    st.success("Bagus! Lanjutkan pola hidup sehatmu 🌿🍎")


