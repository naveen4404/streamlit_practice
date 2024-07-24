import streamlit as st
st.set_page_config(page_title="portfolio",page_icon="❤️",layout="wide")
column1,column2,column3,column6=st.columns(4)
with column1:
    st.title("Naveen Gundavarapu",anchor=False)
with column2:
    st.write()
with column6:
    st.image("profile.jpg",width=100)
st.subheader("Web Developer",anchor=False)
with st.container(border=True):
    st.info("I am Btech III-year student from Vishnu Institute of Technonology")
st.subheader("Educational Information: ")
col1,col2,col3,col4=st.columns(4)
with col1:
    st.write("Education")
    st.write("Graduation")
with col2:
    st.write("Grade")
    st.write("9.37")
with col3:
    st.write("Year")
    st.write("2022-2026")
with col4:
    st.write("Institution")
    st.write("Vishnu Institute of Technology")
st.subheader("Skills:")
st.info("Python")
st.info("HTML")
st.info("CSS")


