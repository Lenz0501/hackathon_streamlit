import streamlit as st

st.title('想聽誰的演唱會?')

left,right=st.columns(2)


with left:
    st.markdown('## 熱賣中')
    left_1,left_2=st.columns(2)
    with left_1:
        st.image('A.jpg',use_column_width='always')
        st.write('')
        st.image('B.jpg',use_column_width='always')
        st.write('')
        st.image('C.jpg',use_column_width='always')
    with left_2:
        st.markdown("""
            ### ONE OK ROCK高雄演唱會2024｜ONE OK ROCK 2024 PREMONITION WORLD TOUR IN KAOHSIUNG｜高雄世運主場館  
            ##### 9月21日(週六)
            """)
        st.write('')
        st.write('')
        st.write('')   
        st.write('[價格待公布]')
        st.page_link("pages/3_行程設定.py", label="info")
        st.markdown("""
            ### 2024 康士坦的變化球 KST《眠月線》演唱會高雄站｜高雄流行音樂中心  
            ##### 8月31日(週六)
            """) 
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('[價格待公布]')
        st.write('')
        st.write('')
        st.markdown("""
            ### 宇宙人高雄演唱會2024｜宇宙人《 α：回到未來 》20週年演唱會-高雄｜高雄巨蛋
            ##### 8月10日(週六)
            """)
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('[價格待公布]')

with right:
    st.markdown('## 已售完:')
    right_1,right_2=st.columns(2)
    with right_1:
        st.image('A.jpg',use_column_width='always')
    with right_2:
        st.markdown("""
            ### ONE OK ROCK高雄演唱會2024｜ONE OK ROCK 2024 PREMONITION WORLD TOUR IN KAOHSIUNG｜高雄世運主場館  
            ##### 9月21日(週六)
            """)
        st.write('')
        st.write('')
        st.write('')   
        st.write('[價格待公布]')
