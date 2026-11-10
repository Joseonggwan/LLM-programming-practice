from openai import OpenAI
from dotenv import load_dotenv
import os

# API KEY 불러오기
load_dotenv()

# 모델 선언
from langchain_openai import ChatOpenAI
model = ChatOpenAI(model="gpt-4o-mini")

# 첫 번째 대화
from langchain_core.messages import HumanMessage

response1 = model.invoke([
    HumanMessage(content="안녕? 나는 김정은이야.")
])

print("첫 번째 대화:")
print(response1.content)


# 두 번째 대화
response2 = model.invoke([
    HumanMessage(content="내 이름이 뭐지?")
])

print("두 번째 대화:")
print(response2.content)
# ==========================================
# [학습 내용 정리]
# ==========================================

# 1. ChatOpenAI의 invoke()는 전달받은 메시지를 바탕으로 응답을 생성한다.
# 2. 각각의 invoke() 호출은 독립적으로 실행된다.
# 3. 이전 대화 기록을 자동으로 기억하지 못한다.
# 4. 멀티턴 대화를 구현하려면 대화 기록을 별도로 관리하고 전달해야 한다.
