import streamlit as st
from datetime import time, datetime, timedelta, date
import pandas as pd
import ast
import pydeck as pdk

title_display,_,_,_,_,_,print_button= st.columns(7)

with print_button:
    st.write(' ')
    st.write(' ')
    st.button('Print',use_container_width=True)

with title_display:
    st.title('TRAVEL !!')

col0,col1,col2,col3,col4,col5= st.columns(6)

with col0:
    st.write(' ')
    st.write(' ')
    st.button('Restart',type='primary',use_container_width=True)

with col1:
    today = datetime.now()
    jan_1 = date(today.year, 1, 1)
    dec_31 = date(today.year, 12, 31)

    d = st.date_input(
        "Date",
        (jan_1, date(2024, 5, 11)),
        jan_1,
        dec_31,
        format="MM.DD.YYYY",
    )
with col2:
    title = st.text_input("出發時間", "8:00")

with col3:
    title = st.text_input("結束時間", "18:00")
    
with col4:
    traffic_option = st.selectbox(
        "Traffic",
        ('大眾運輸','自駕','自行車','摩托車'))
    
with col5:
    title = st.text_input("Departure", "US, New York")

with st.expander("Advance"):
    st.write("...")

schelde,other = st.columns(2)

with schelde:
    st.markdown("""
    # 高雄觀光排程

    ## Day 1

    ### 08:00 - 早餐
    - **六合夜市**
    - 地址: 高雄市新興區六合二路
    - 描述: 夜市的早餐選擇多樣，可以品嘗到當地特色小吃。
    
    ### 09:00 - 西子灣風景區
    - **西子灣**
    - 地址: 高雄市鼓山區蓮海路
    - 描述: 欣賞海景，散步放鬆。

    ### 11:00 - 壽山動物園
    - **壽山動物園**
    - 地址: 高雄市鼓山區萬壽路
    - 描述: 參觀各類動物，適合家庭出遊。

    ### 13:00 - 午餐
    - **駁二藝術特區**
    - 地址: 高雄市鹽埕區大勇路1號
    - 描述: 駁二內有多家餐廳和咖啡店，可以享用午餐並欣賞藝術展覽。

    ### 15:00 - 愛河
    - **愛河**
    - 地址: 高雄市鹽埕區河東路
    - 描述: 愛河畔散步，搭乘愛之船，享受悠閒的午後時光。

    ### 18:00 - 晚餐
    - **新崛江商圈**
    - 地址: 高雄市前金區中山一路
    - 描述: 商圈內有多家餐廳和小吃店，可以品嘗美食。

    ### 20:00 - 夜晚活動
    - **光之穹頂 - 美麗島捷運站**
    - 地址: 高雄市新興區中山一路115號
    - 描述: 欣賞世界四大美麗捷運站之一的光之穹頂，感受夜晚的璀璨。

    ## Day 2

    ### 09:00 - 早餐
    - **蓮池潭風景區**
    - 地址: 高雄市左營區蓮潭路
    - 描述: 享用當地早餐，並環繞蓮池潭散步。

    ### 11:00 - 新威景觀大橋
    - **新威景觀大橋**
    - 地址: 高雄市橋頭區
    - 描述: 欣賞大橋的壯觀景色，適合拍照。

    ### 13:00 - 午餐
    - **六合夜市**
    - 地址: 高雄市新興區六合二路
    - 描述: 再次光顧六合夜市，嘗試不同的美食。

    ### 15:00 - 城市光廊
    - **城市光廊**
    - 地址: 高雄市前鎮區新光路
    - 描述: 漫步在城市光廊，欣賞高雄市區的現代建築和景觀。

    ### 18:00 - 晚餐
    - **南華夜市**
    - 地址: 高雄市苓雅區三多四路
    - 描述: 南華夜市的美食也是高雄的一大特色，不容錯過。

    ### 20:00 - 結束
    - **立德棒球場**
    - 地址: 高雄市三民區立德路
    - 描述: 看一場棒球賽，為高雄的旅程畫上圓滿的句點。

    """)

with other:
    r_display,l_display = st.columns(2)
    right_1,right_2=st.columns(2)
    with right_1:
        st.image('D:\code\streamlit\A.jpg',use_column_width='always')
    with right_2:
        st.markdown("""
            ### ONE OK ROCK高雄演唱會2024｜ONE OK ROCK 2024 PREMONITION WORLD TOUR IN KAOHSIUNG｜高雄世運主場館  
            ##### 9月21日(週六)
            """)
        st.write('')
        st.write('')  
        st.write('[價格待公布]')
        st.button('前往訂票',type='primary')
    view_state = pdk.ViewState(latitude=22.621985, longitude=120.350205, zoom=11, bearing=0, pitch=45)
    deck = pdk.Deck(map_style="mapbox://styles/mapbox/outdoors-v12",layers=[], initial_view_state=view_state)
    st.pydeck_chart(deck)