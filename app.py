import streamlit as st
st.title("Is Digit")
a=st.text_input(label="enter number")
if st.button("submit"):
    try:
        for i in a:
            if i.isdigit():
                st.write(i)
    except InterruptedError:
        st.write("something happened")
    


