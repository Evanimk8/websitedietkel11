import streamlit as st

st.set_page_config(page_title="Diet Sehat", page_icon="🍇", layout="centered")

st.markdown("""
    <h1 style='text-align: center; color: black;'>Jagalah Tubuh Anda dengan Diet yang Sehat!</h1>
    <div style='text-align: center;'>
        <img src='https://cdn.pixabay.com/photo/2017/01/20/15/06/fruits-1995056_960_720.jpg' width='500'/>
    </div>
    <br><h2 style='text-align: center; color: black;'>Apa yang ingin kamu capai?</h2>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("Turun Berat Badan"):
        st.switch_page("Turun.py")

with col2:
    if st.button("Naik Berat Badan"):
        st.switch_page("Naik.py")
