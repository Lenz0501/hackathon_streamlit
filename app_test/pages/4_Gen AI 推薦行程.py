import streamlit as st
from datetime import time, datetime, timedelta
import pandas as pd
import ast



def result():
    query=f'輸出兩個python串列1.從資料内找出13個最佳的景點（""輸出成python串列， 輸出景點名稱即可，不需其他文字敘述""）, 需是{io}、位置範圍:{area}附近、{move}, 時段為{time_display}。2.從前面選出串列裡平均評分的前5名，同樣以串列輸出、不含其他文字敘述。'
    st.write(query)


st.title('AI search 高雄觀光景點')

#st.subheader('室內/室外')
io = st.selectbox('室內/室外',('室內','室外'))

#st.subheader('行政區')
area = st.multiselect("行政區",['不限','鹽埕區','鼓山區','左營區','楠梓區','三民區','新興區','前金區','苓雅區','前鎮區','旗津區','小港區','鳳山區','林園區','大寮區','大樹區','大社區','仁武區','鳥松區','岡山區','橋頭區','燕巢區','田寮區','阿蓮區','路竹區','湖內區','茄萣區','永安區','彌陀區','梓官區','旗山區','美濃區','六龜區','甲仙區','杉林區','內門區','茂林區','桃源區','那瑪夏區'],placeholder='不限')

#st.subheader('靜態/動態')
move = st.radio("靜態/動態",['靜態','動態'],index=None,)

#st.subheader('時間')
time_ = st.slider("時間",min_value=time(8, 00), max_value=time(22, 00),value=(time(9, 00), time(12, 00)))
time_display=f'{time_[0].hour}:{time_[0].minute} ~ {time_[1].hour}:{time_[1].minute}'
start_datetime = datetime.combine(datetime.today(), time_[0])
end_datetime = datetime.combine(datetime.today(), time_[1])
total_time=end_datetime - start_datetime
st.session_state['all_time_'] = total_time.total_seconds()//60
st.session_state['current_min_'] = time_[0].hour*60+time_[0].minute
st.write(f'總時長: {str(total_time)}')

if st.button(label="Submit",type="primary",key="submit_button_1"):
    result()
st.page_link("pages/5_AI 行程.py", label="Submit",icon='🔮')
