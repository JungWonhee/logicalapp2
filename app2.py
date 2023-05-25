#Scripts\activate.bat
#streamlit run app2.py

import openai
import streamlit as st

messages = []
content = ""
chat_response = ""
infer = [0, 0, 0, 0, 0]

openai.api_key = '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'

st.title("수리논리학 계산기")
number_string = st.number_input("개별적 사실을 몇 개 입력받겠습니까? (최대 5개)", 1, 5)

number = int(number_string)
for i in range(number):
    infer[i] = st.text_input(f"개별적 사실{i+1}", value = "홈플러스에서 5000원에 라면을 팔고, 3000원에 커피를 판다.", key = f"infer{i}")
Ginfer2 = st.text_input("질문", value = "손님 = (5000원 → 라면 세트) ", key = "infer5")
if st.button("입력", key = "button"):
    for i in range(number):
        content += f'"{infer[i]}", '
    content += f'일 때, "{Ginfer2}"라는 문장은 성립하는가?'
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "넌 철학자야."},
            {"role": "user", "content": content}
        ]
    )

# 응답 결과 표시
    chat_response = completion.choices[0].message.content
    st.text(chat_response)
