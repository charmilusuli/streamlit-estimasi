import pickle
import streamlit as st

model = pickle.load(open('Estimasi_rumahdijs.sav','rb'))

st.title('Estimasi Harga Rumah Di Area Jakarta Selatan')

LuasTanah = st.number_input('Input Luas Tanah')
LuasBangunan = st.number_input('Input Luas Bangunan')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[LuasTanah, LuasBangunan]]
    )
    st.write ('Estimasi Harga Rumah Di Jakarta Selatan : ',  predict)