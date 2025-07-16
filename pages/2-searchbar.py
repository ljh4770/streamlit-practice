import streamlit as st

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

if img_name := st.text_input("이미지 이름 전체 혹은 부분 입력"):
    for i, name in enumerate(ani_list):
        if img_name in name:
            st.image(img_list[i])
            break
    else:
        st.write("없는 애니")


ani_name = st.text_input("애니 이름 입력")
print(f"text_input의 초기값은? {ani_name}, {type(ani_name)} 이거")