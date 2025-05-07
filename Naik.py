import streamlit as st

st.set_page_config(page_title="Naik Berat Badan", page_icon="⬆️")

st.title("🎯 Naik Berat Badan")
st.write("Masukkan data tubuhmu untuk menghitung Indeks Massa Tubuh (BMI):")

# Input berat dan tinggi
berat = st.number_input("Berat badan (kg)", min_value=30.0, max_value=200.0, value=50.0)
tinggi = st.number_input("Tinggi badan (cm)", min_value=100.0, max_value=250.0, value=165.0)

if berat and tinggi:
    tinggi_m = tinggi / 100
    bmi = round(berat / (tinggi_m ** 2), 2)

    st.markdown(f"### BMI Anda: **{bmi}**")

    # Interpretasi BMI
    if bmi < 18.5:
        status = "Kurus"
    elif 18.5 <= bmi < 25:
        status = "Normal"
    elif 25 <= bmi < 30:
        status = "Gemuk"
    else:
        status = "Obesitas"

    st.success(f"Status: {status}")
