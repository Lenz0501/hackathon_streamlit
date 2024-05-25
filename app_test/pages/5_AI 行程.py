import streamlit as st
from datetime import time, datetime, timedelta
import pandas as pd
import ast
import pydeck as pdk

#set
flag=False

all_time=st.session_state.all_time_
current_min=st.session_state.current_min_

loc_list=['西子灣風景區', '壽山動物園', '駁二藝術特區', '愛河', '蓮池潭風景區', '新威景觀大橋', '六合夜市', '新崛江商圈', '南華夜市', '紫蝶幽谷', '多納高吊橋', '情人谷', '茂林谷', '小長城步道', '十八羅漢山風景區', '新威森林公園', '茂林國家風景區', '城市光廊', '光之穹頂-美麗島捷運站', '立德棒球場']
selection_0=['蓮池潭風景區', '新崛江商圈', '新威森林公園', '壽山動物園', '哈瑪星鐵道文化園區']

travel_df=pd.read_csv('data.csv')


#function----------------------------------------------------------------------------------------------------------------------------------------------------------------

def rec_loc(x,selection_0):
    if x in selection_0:
        return True
    else:
        return False

def time_estimate(loc1,loc2):
    x1,y1=travel_df[travel_df['place']==loc1].loc[:,'lon'].iloc[0],travel_df[travel_df['place']==loc1].loc[:,'lat'].iloc[0]
    x2,y2=travel_df[travel_df['place']==loc2].loc[:,'lon'].iloc[0],travel_df[travel_df['place']==loc2].loc[:,'lat'].iloc[0]

    d=((x1-x2)**2+(y1-y2)**2)**0.5
    if d<0.025:
        return 10
    else:
        return 10+int(d//0.05+1)*10

def loc_time(loc):
    return travel_df[travel_df['place']==loc].loc[:,'time'].iloc[0]

def time_format(m):
    h=m//60
    m%=60
    return f'{h}:{m}' if m>=10 else f'{h}:00'

def place_sort(l):  
    gps=[];l_=[]    
    for i in l:
        gps.append(travel_df[travel_df['place']==i].loc[:,'gps'].iloc[0])
    gps=sorted(gps)
    for i in gps:
        l_.append(travel_df[travel_df['gps']==i].loc[:,'place'].iloc[0])
    return l_[::-1]

def change(n1,n2):
    global l
    l[n1],l[n2]=l[n2],l[n1]
    st.session_state['selection_']=l

def button_disabled(x,s):
    if x==st.session_state.loc_num_-1 and s=='d':
        return True
    elif x==0 and s=='u':
        return True
    else:
        return False

#choose----------------------------------------------------------------------------------------------------------------------------------------------------------------

st.image('D:\code\streamlit\pic_1.jpeg',use_column_width=True)

st.title('Result Display')

loc_num=len(st.session_state.selection_)

if loc_num!=st.session_state.loc_num_:
    st.session_state['loc_num_'] = (loc_num)
    flag=True
else:
    selection=st.session_state.selection_

df = pd.DataFrame(data = [{'Select': rec_loc(i,selection_0), "Location": i, "Area": travel_df[travel_df['place']==i].loc[:,'area'].iloc[0],"Sort": travel_df[travel_df['place']==i].loc[:,'sort'].iloc[0], "Time(min)": loc_time(i), "Rating": ('⭐'+str(travel_df[travel_df['place']==i].loc[:,'rating'].iloc[0]))} for i in loc_list])
edited_df = st.data_editor(df,use_container_width=True,hide_index=True)


selection = edited_df.loc[edited_df["Select"] == True]["Location"].tolist()
time_select = edited_df.loc[edited_df["Select"] == True]["Time(min)"].tolist()

#st.markdown(selection)
#st.write(loc_num,st.session_state.loc_num_)
loc_num=len(selection)
if flag==True or loc_num!=st.session_state.loc_num_:
    st.session_state['selection_']=place_sort(selection)
loc_num=len(selection)
#time------------------------------------------------------------------------------------------------------------------------------------------------------------------

select_time = sum(time_select)
remain_time = all_time-select_time
#st.write(remain_time)
hour = remain_time // 60
minute = int((remain_time% 60)//60)
if minute==0: minute="00"
#if remain_time<=0:
    #st.warning(f'超過預設time，請重新選擇景點')
#else:
    #st.markdown(f'剩餘time {int(hour)}小時 {minute}分鐘 (請預留一小時的交通time)')

#display---------------------------------------------------------------------------------------------------------------------------------------------------------------
trans_time,trans_url=[],[]
for i in range(len(st.session_state.selection_)-1):
    trans_time.append(time_estimate(st.session_state.selection_[i],st.session_state.selection_[i+1]))
    trans_url.append('https://www.google.com/maps/dir/'+st.session_state.selection_[i]+'/'+st.session_state.selection_[i+1])

l=st.session_state.selection_
#st.markdown(l)
#st.write(loc_num)
down_button,up_button=[],[]

route_flag=True
if loc_num<=1:
    st.error('請勾選至少2個景點', icon='⚠️')
    route_flag=False

if route_flag:
    with st.form(key='display_form'):
        for i in range(len(st.session_state.selection_)):
            st.markdown(f"""
            <div style='
                background-color: #f0f0f0;
                border: 2px solid #000000;
                border-radius: 6px;
                padding: 8px;
            '>
                <h3 style='color: #000000;'>{st.session_state.selection_[i]}</h3>
                <p style='color: #000000;'>{loc_time(st.session_state.selection_[i])}分鐘 | {time_format(current_min)}~{time_format(current_min+loc_time(st.session_state.selection_[i]))}</p>
            </div>
            """,unsafe_allow_html=True)
            #current_min+=loc_time(st.session_state.selection_[i])+trans_time[i]
            col1,col2,_,_,_,_,_,_,_,_,_,_ = st.columns(12)
            up_button.append(col1.form_submit_button(label=f"🔼{i+1}"))
            down_button.append(col2.form_submit_button(label=f"{i+1}🔽"))

            if i!=len(st.session_state.selection_)-1:
                st.markdown(f"""
                    **<font size=4>:oncoming_automobile: 約{trans_time[i]}分鐘</font>**   [:mag_right: Google Map]({trans_url[i]})
                    """,unsafe_allow_html=True)


    for i in range(len(down_button)):
        if down_button[i]:
            st.write(i)
            change(i,i+1)
            st.rerun()
        if up_button[i]:
            st.write(i)
            change(i,i-1)
            st.rerun()


travel_df=pd.read_csv('D:\code\streamlit\data.csv')
#travel_df

route_l=st.session_state.selection_

route_df = pd.DataFrame(data = [{"No":i, "Location": f'{route_l[i]}~{route_l[i+1]}', "lon": travel_df[travel_df['place']==route_l[i]].loc[:,'lon'].iloc[0], "lat": travel_df[travel_df['place']==route_l[i]].loc[:,'lat'].iloc[0], "lon2": travel_df[travel_df['place']==route_l[i+1]].loc[:,'lon'].iloc[0], "lat2": travel_df[travel_df['place']==route_l[i+1]].loc[:,'lat'].iloc[0]} for i in range(len(route_l)-1)])
#route_df


layer_1=pdk.Layer(
    "ScatterplotLayer",
    data=travel_df,
    get_position=["lon", "lat"],
    get_fill_color=[232, 149, 16],
    get_radius=80,
)

layer_2=pdk.Layer(
    "ArcLayer",
    data=route_df,
    get_source_position=["lon", "lat"],
    get_target_position=["lon2", "lat2"],
    get_source_color=[230, 57, 34],
    get_target_color=[230, 57, 34],
    get_height=0.5,
    auto_height=True,
    width_scale=0.0001,
    width_min_pixels=3,
    width_max_pixels=30,
)

layer_2_1=pdk.Layer(
    "ScatterplotLayer",
    data=route_df,
    get_position=["lon", "lat"],
    get_fill_color=[230, 57, 34],
    get_radius=150,
)


view_state = pdk.ViewState(latitude=22.621985, longitude=120.350205, zoom=11, bearing=0, pitch=45)
deck = pdk.Deck(map_style="mapbox://styles/mapbox/satellite-streets-v12",layers=[layer_1,layer_2,layer_2_1], initial_view_state=view_state)
st.pydeck_chart(deck)
