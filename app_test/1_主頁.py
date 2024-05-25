import streamlit as st

st.set_page_config(layout="wide")

l=[1,2,3,4,5]
st.session_state['selection_test']=l
st.session_state["selection_"]=['蓮池潭風景區', '壽山動物園', '新崛江商圈', '駁二藝術特區', '新威森林公園']
st.session_state['loc_num_'] = 0

st.title('歡迎來到高雄～')

st.markdown("### [Gen AI 生成式Schedule] ")
st.image(r'_4274d1f0-5dc7-4f62-8373-81ee2bba23f3.jpg', use_column_width=True)
_,_,_,_,_,_,schedule_button=st.columns(7)

with schedule_button:
    st.page_link("pages/4_Gen AI 推薦行程.py", label="Submit",icon='🔮')

st.markdown('------')
A,B,C,D = st.columns(4)
with A:
    st.markdown("""
    ## 演唱會:
    """)
    st.image('pexels-vishnurnair-1105666.jpg',use_column_width=True)
    _,_,_,button_1=st.columns(4)

    with button_1:
        st.page_link("pages/2_訂票系統.py", label="Go~")
with B:
    st.markdown("""
    ## 藝術展覽:
    """)
    st.image('pexels-prismattco-2372978.jpg')
    _,_,_,button_1=st.columns(4)

    with button_1:
        st.button('GO~',key='a')
with C:
    st.markdown("""
    ## 運動賽事:
    """)
    st.image('pexels-pixabay-248547.jpg')
    _,_,_,button_1=st.columns(4)

    with button_1:
        st.button('GO~',key='b')
with D:
    st.markdown("""
    ## 景點:
    """)
    st.image('pexels-souvenirpixels-1598073.jpg')
    _,_,_,button_1=st.columns(4)

    with button_1:
        st.button('GO~',key='c')
