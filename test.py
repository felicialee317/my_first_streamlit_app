import streamlit as st

st.title('Be tap lam toan')
col1, col2, col3= st.columns(3)
with col1:
    a=st.number_input('a')
with col2:
    option=st.radio('Phep toan', ('\+', '\-', 'x', ':'), horizontal=True)
with col3:
    b=st.number_input('b')
d=st.number_input('Nhap ket qua')
if st.button('Kiem tra', use_container_width=True):
    if option=='\+':
        c=a+b
    elif option=='\-':
        c=a-b
    elif option==':':
        c=a/b
    elif option=='x':
        c=a*b

    if c==d:
        st.success('Chinh xac')
        st.balloons()
    else: 
        st.snow()
        st.error('Sai')
