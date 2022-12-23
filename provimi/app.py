import streamlit as st

text = st.text_input("Shkruani nje text: ")


upper_list=[]


def convert_list(text):
    lst1=text.split()
    return lst1
convert=convert_list(text)
def all_upper(convert):
    for x in convert:
        txt=x.upper() 
        upper_list.append(txt)
    return upper_list
upper=all_upper(convert)

def count(convert):
    return  len(convert)
count_elements = count(convert)
if st.button('Return list'):
    st.write(convert)

if st.button('upper list'):
    st.write(upper)

if st.button('print'):
    st.write(count_elements)


