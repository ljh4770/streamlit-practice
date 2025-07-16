import streamlit as st


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


a = st.button("클릭")
print(f"a: {a}")

if st.button("클릭2"):
    st.write(True)

b = st.button("클릭3")
print(f"b: {b}")

if image := st.camera_input('Click a Snap to download'): # 동영상
    # 사진찍기 전에 image는 None이므로 에러 발생
    st.download_button("download the image", image, 'my.png')

