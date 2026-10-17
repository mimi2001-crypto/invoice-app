import streamlit as st

st.title("حاسبة الفواتير")

product = st.text_input("اسم المنتج")
price = st.number_input("السعر", min_value=0.0)
quantity = st.number_input("الكمية", min_value=1, step=1)

subtotal = price * quantity
vat = subtotal * 0.15
total = subtotal + vat

if st.button("احسب"):
    st.write(f"المنتج: {product}")
    st.write(f"المجموع قبل الضريبة: {subtotal:.2f} ريال")
    st.write(f"الضريبة 15%: {vat:.2f} ريال")
    st.success(f"الإجمالي: {total:.2f} ريال")