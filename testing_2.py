import streamlit as st
import pydeck as pdk
import pandas as pd



def s_route():
    l=[]
    #for i in 
    
#def e_route()

travel_df=pd.read_csv('D:\code\streamlit\data.csv')
travel_df

l=['蓮池潭風景區', '壽山動物園', '新崛江商圈', '駁二藝術特區', '新威森林公園']
l1=[[120.62307,22.89351],[120.2969,22.67873],[120.2728486,22.6355162]]
l2=[[120.2969,22.67873],[120.2728486,22.6355162],[120.3019,22.62326]]

positions = travel_df[['lon','lat']]
positions


route_df = pd.DataFrame(data = [{"No":i, "Location": f'{l[i]}~{l[i+1]}', "lon": travel_df[travel_df['place']==l[i]].loc[:,'lon'].iloc[0], "lat": travel_df[travel_df['place']==l[i]].loc[:,'lat'].iloc[0], "lon2": travel_df[travel_df['place']==l[i+1]].loc[:,'lon'].iloc[0], "lat2": travel_df[travel_df['place']==l[i+1]].loc[:,'lat'].iloc[0]} for i in range(len(l)-1)])
route_df

 
"""layer = pdk.Layer(
    "ScatterplotLayer",
    data=[{"position": [120.2815287, 22.6199803]}],
    get_position="position",
    get_fill_color=[255,0,0],
    get_radius=100,
)"""

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


# 设置视图状态
view_state = pdk.ViewState(latitude=22.621985, longitude=120.350205, zoom=11, bearing=0, pitch=60)

# 创建 PyDeck 地图组件
deck = pdk.Deck(map_style="mapbox://styles/mapbox/streets-v11",layers=[layer_1,layer_2,layer_2_1], initial_view_state=view_state)

# 显示 PyDeck 地图
st.pydeck_chart(deck)
