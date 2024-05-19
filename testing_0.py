import streamlit as st

l=[1,2,3,4,5]
st.session_state['selection_']=l

def form_callback():
    st.write(st.session_state.my_slider)
    st.write(st.session_state.my_checkbox)
    st.markdown(st.session_state.selection_)

with st.form(key='my_form'):
    slider_input = st.slider('My slider', 0, 10, 5, key='my_slider')
    checkbox_input = st.checkbox('Yes or No', key='my_checkbox')
    l[0],l[1]=l[1],l[0]
    print(l)
    st.session_state['selection_']=l
    submit_button = st.form_submit_button(label='Submit', on_click=form_callback)