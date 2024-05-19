import streamlit as st
from datetime import time, datetime, timedelta
import pandas as pd
import ast


def result():
    query=f'輸出兩個python串列1.從資料内找出13個最佳的景點（""輸出成python串列， 輸出景點名稱即可，不需其他文字敘述""）, 需是{io}、位置範圍:{area}附近、{move}, 時段為{time_display}。2.從前面選出串列裡平均評分的前5名，同樣以串列輸出、不含其他文字敘述。'
    st.write(query)

def rec_loc(x):
    if x in selection:
        return True
    else:
        return False

def time_estimate(loc1,loc2):
    x1,y1=travel_df[travel_df['景點地名']==loc1].loc[:,'lon'].iloc[0],travel_df[travel_df['景點地名']==loc1].loc[:,'lat'].iloc[0]
    x2,y2=travel_df[travel_df['景點地名']==loc2].loc[:,'lon'].iloc[0],travel_df[travel_df['景點地名']==loc2].loc[:,'lat'].iloc[0]

    d=((x1-x2)**2+(y1-y2)**2)**0.5
    if d<0.025:
        return 10
    else:
        return 10+int(d//0.05+1)*10

def loc_time(loc):
    return travel_df[travel_df['景點地名']==loc].loc[:,'時間'].iloc[0]

def time_format(m):
    h=m//60
    m%=60
    return f'{h}:{m}' if m>=10 else f'{h}:00'

def place_sort(l):  
    gps=[];l_=[]
    for i in l:
        gps.append(travel_df[travel_df['景點地名']==i].loc[:,'gps'].iloc[0])
    gps=sorted(gps)
    for i in gps:
        l_.append(travel_df[travel_df['gps']==i].loc[:,'景點地名'].iloc[0])
    return l_[::-1]

rec_flag=False

st.title('AI search 高雄觀光景點')

#st.subheader('室內/室外')
io = st.selectbox('室內/室外',('室內','室外'))

#st.subheader('行政區')
area = st.multiselect("行政區",['不限','鹽埕區','鼓山區','左營區','楠梓區','三民區','新興區','前金區','苓雅區','前鎮區','旗津區','小港區','鳳山區','林園區','大寮區','大樹區','大社區','仁武區','鳥松區','岡山區','橋頭區','燕巢區','田寮區','阿蓮區','路竹區','湖內區','茄萣區','永安區','彌陀區','梓官區','旗山區','美濃區','六龜區','甲仙區','杉林區','內門區','茂林區','桃源區','那瑪夏區'],placeholder='不限')

#st.subheader('靜態/動態')
move = st.radio("靜態/動態",['靜態','動態'],index=None,)

#st.subheader('時間')
time_ = st.slider("時間",min_value=time(8, 00), max_value=time(22, 00),value=(time(9, 00), time(12, 00)))
st.write(time_)
time_display=f'{time_[0].hour}:{time_[0].minute} ~ {time_[1].hour}:{time_[1].minute}'
start_datetime = datetime.combine(datetime.today(), time_[0])
end_datetime = datetime.combine(datetime.today(), time_[1])
total_time=end_datetime - start_datetime
st.write(f"total time:{total_time}")
st.session_state['all_time'] = total_time.total_seconds()//60
st.session_state['current_min'] = time_[0].hour*60+time_[0].minute
st.write(f'總時長: {str(total_time)}')



#-------------------------------------------------------------------------------------------------------------------------------------------------------------
query_result="""1. ['西子灣風景區', '壽山動物園', '駁二藝術特區', '愛河', '蓮池潭風景區', '新威景觀大橋', '六合夜市', '新崛江商圈', '南華夜市', '紫蝶幽谷', '多納高吊橋', '情人谷', '茂林谷', '小長城步道', '十八羅漢山風景區', '新威森林公園', '茂林國家風景區', '城市光廊', '光之穹頂-美麗島捷運站', '立德棒球場']

2. ['蓮池潭風景區', '壽山動物園', '新崛江商圈', '駁二藝術特區', '新威森林公園']"""

loc_list=ast.literal_eval(query_result.splitlines()[0][2:])
selection=ast.literal_eval(query_result.splitlines()[2][2:])
#loc_list_rec

loc_list=list(set(loc_list))

travel_df=pd.read_csv('D:\code\streamlit\data.csv')
travel_df

#st.markdown(travel_df[travel_df['景點地名']=='愛河'].loc[:,'類型'].iloc[0])


df = pd.DataFrame(
    data = [{'Select': rec_loc(i), "Location": i, "Area": travel_df[travel_df['景點地名']==i].loc[:,'所屬地區'].iloc[0],"Sort": travel_df[travel_df['景點地名']==i].loc[:,'類型'].iloc[0], "Time(min)": loc_time(i), "Rating": ('⭐'+str(travel_df[travel_df['景點地名']==i].loc[:,'平均評分'].iloc[0]))} for i in loc_list]
)


if st.button(label="Submit",type="primary",key="submit_button_1"):
    result()
    rec_flag=True

edited_df = st.data_editor(df,use_container_width=True,hide_index=True)

selection = edited_df.loc[edited_df["Select"] == True]["Location"].tolist()
time_select = edited_df.loc[edited_df["Select"] == True]["Time(min)"].tolist()

st.markdown(f'已選: {selection}')
loc_num=len(selection)
all_time = total_time.total_seconds()//60
select_time = sum(time_select)
remain_time = all_time-select_time
#st.write(remain_time)
hour = remain_time // 60
minute = int((remain_time% 60)//60)
if minute==0: minute="00"
if remain_time<=0:
    st.warning(f'超過預設時間，請重新選擇景點')
else:
    st.markdown(f'剩餘時間 {int(hour)}小時 {minute}分鐘 (請預留一小時的交通時間)')

if st.button(label="Submit",type="primary",key="submit_button_2") or rec_flag:
    if loc_num<=1:
        st.error('請勾選至少2個景點', icon='⚠️')
    else:
        selection=place_sort(selection)   #sort selection

        trans_time,trans_url=[],[]
        for i in range(loc_num-1):
            trans_time.append(time_estimate(selection[i],selection[i+1]))
            trans_url.append('https://www.google.com/maps/dir/'+selection[i]+'/'+selection[i+1])

        container = st.container(border=True)
        container.markdown("## 行程表:")
        total_route='/'.join(x for x in selection)
        #st.write(total_route)
        container.markdown(f"#### [[總行程路線]](https://www.google.com/maps/dir/{total_route})")
        current_min=time_[0].hour*60+time_[0].minute

        for i in range(loc_num-1):
            container.markdown(f"""
                <div style='
                    background-color: #f0f0f0;
                    border: 2px solid #000000;
                    border-radius: 6px;
                    padding: 8px;
                    box-shadow: 1px 1px 5px #888888;
                '>
                    <h3 style='color: #000000;'>{selection[i]}</h3>
                    <p style='color: #000000;'>{loc_time(selection[i])}分鐘 | {time_format(current_min)}~{time_format(current_min+loc_time(selection[i]))}</p>
                </div>

                **<font size=4>:oncoming_automobile: 約{trans_time[i]}分鐘</font>**   [:mag_right: Google Map]({trans_url[i]})
                        """,unsafe_allow_html=True)
            current_min+=loc_time(selection[i])+trans_time[i]

            col1,col2,_,_,_,_,_,_,_,_,_,_ = container.columns(12)
            if col1.button("🔼",key=f"up_button{i}"):
                rec_flag==True
            if col2.button("🔽",key=f"down_button{i}"):
                rec_flag==True

        container.markdown(f"""
            <div style='
                background-color: #f0f0f0;
                border: 2px solid #000000;
                border-radius: 6px;
                padding: 8px;
                box-shadow: 1px 1px 5px #888888;
            '>
                <h3 style='color: #000000;'>{selection[loc_num-1]}</h3>
                <p style='color: #000000;'>{loc_time(selection[loc_num-1])}分鐘 | {time_format(current_min)}~{time_format(current_min+loc_time(selection[i]))}</p>
            </div>
            """,unsafe_allow_html=True)