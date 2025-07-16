import numpy as np
import pandas as pd

import streamlit as st

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)

import plotly.express as px

# Plotly Bar Chart
fig = px.bar(
    df,
    x="command",     # x축에 command
    y="rating",      # y축에 rating
    color="command", # command별 색깔 구분
    labels={"command": "x축 제목", "rating": "Rating"},
    title="Command Rating Bar Chart"
)

st.plotly_chart(fig, use_container_width=True)

# st.bar_chart(df['rating'], x=df['command'])

# 입력
st.button('Demo')
st.data_editor(df)
st.checkbox('Option 1')

country = st.radio('Pick Country:', ['France','Germany'])
st.write(country)

st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter Article')  # 한 줄 짜리 입력, type=password
st.number_input('Enter required number') # -+버튼 있음
st.text_area('Entered article text')
st.date_input('Select date') # 달력 선택
st.time_input('Select Time')  # 의도되지않은 문자열도 입력가능한 문제
st.file_uploader('File CSV uploader') # 데이터 업로드
# st.download_button('Download Source data', data) # 사용자가 데이터 다운로드
st.camera_input('Click a Snap') # 동영상 
st.color_picker('Pick a color') # 색 선택

# 출력
st.text('Tushar-Aggarwal.com')
st.markdown('[Tushar-Aggarwal.com](https://tushar-aggarwal.com)')
st.caption('Success')
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Supreme Applcations by Tushar Aggarwal')
st.write(['st', 'is <', 3]) # see *
st.title('Streamlit Magic Cheat Sheets')
st.header('Developed by Tushar Aggarwal')
st.subheader('visit tushar-aggarwal.com')
st.code('for i in range(8): print(i)')
st.image('https://i.imgur.com/t2ewhfH.png')
# * optional kwarg unsafe_allow_html = True



"""
1. 버튼을 누르면 화면에 True라고 코드를 리턴하는 간단한 함수 작성
2. 사진을 찍으면, 다운로드 버튼으로 사진을 다운로드 받을 수 있게 작성
"""

# 1. 
# if st.button("Click to True"):
#     st.code(True)


# # 2. 
# image = None
# image = st.camera_input('Click a Snap to download') # 동영상
# st.download_button('Download the Image', image)
