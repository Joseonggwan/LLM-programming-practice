#!/usr/bin/env python
# coding: utf-8

# # 랭체인 멀티턴
# 
# - LangChain의 RunnableWithMessageHistory를 사용하여 대화기록을 관리하는 챗봇 구현
# - 세션 ID별로 대화 기록이 어떻게 분리되어 저장되는지 확인

# ## 라이브러리 불러오기

# In[1]:


from langchain_core.chat_history import InMemoryChatMessageHistory  # 메모리에 대화 기록을 저장하는 클래스
from langchain_core.runnables.history import RunnableWithMessageHistory  # 메시지 기록을 활용해 실행 가능한 래퍼wrapper 클래스
from langchain_openai import ChatOpenAI  # 오픈AI 모델을 사용하는 랭체인 챗봇 클래스
from langchain_core.messages import HumanMessage


# ## API KEY 불러오기

# In[2]:


from openai import OpenAI
from dotenv import load_dotenv
import os


# In[3]:


load_dotenv()


# ## 대화 기록 함수 정의

# In[4]:


model = ChatOpenAI(model="gpt-4o-mini")

# 세션별 대화 기록을 저장할 딕셔너리
store = {}

# 세션 ID에 따라 대화 기록을 가져오는 함수
def get_session_history(session_id: str):
    # 만약 해당 세션 ID가 store에 없으면, 새로 생성해 추가함
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()  # 메모리에 대화 기록을 저장하는 객체 생성
    return store[session_id]  # 해당 세션의 대화 기록을 반환

# 모델 실행 시 대화 기록을 함께 전달하는 래퍼 객체 생성
with_message_history = RunnableWithMessageHistory(model, get_session_history)


# ## 첫 번째 대화

# In[5]:


config = {"configurable": {"session_id": "abc2"}}  # 세션 ID를 설정하는 config 객체 생성

response = with_message_history.invoke(
    [HumanMessage(content="안녕? 난 김정은이야.")],
    config=config,
)

print(response.content)


# ## 두 번째 대화

# In[6]:


response = with_message_history.invoke(
    [HumanMessage(content="내 이름이 뭐지?")],
    config=config,
)

print(response.content)


# ## 세션 테스트

# In[7]:


config = {"configurable": {"session_id": "abc3"}}

response = with_message_history.invoke(
    [HumanMessage(content="내 이름이 뭐지?")],
    config=config,
)

response.content


# In[8]:


config = {"configurable": {"session_id": "abc2"}}

response = with_message_history.invoke(
    [HumanMessage(content="아까 우리가 무슨 얘기 했지?")],
    config=config,
)

response.content


# ## 스트리밍 응답 출력

# In[9]:


config = {"configurable": {"session_id": "abc2"}}
for r in with_message_history.stream(
    [HumanMessage(content = "내가 어느 나라 사람인지 맞춰보고, 그 나라의 문화에 대해 말해봐")],
    config=config,
):
    print(r.content, end="")
    # print(r.content, end="|")

# ==========================================
# [학습 내용 정리]
# ==========================================

# 1. InMemoryChatMessageHistory는 대화 기록을 메모리에 저장한다.
# 2. store 딕셔너리는 session_id를 기준으로 대화 기록을 구분한다.
# 3. get_session_history()는 해당 세션의 대화 기록을 반환한다.
# 4. RunnableWithMessageHistory는 모델 실행 시 대화 기록을 함께 관리한다.
# 5. session_id가 다르면 서로 다른 대화 기록을 사용한다.
# 6. stream()을 사용하면 모델의 응답을 순차적으로 출력할 수 있다.
