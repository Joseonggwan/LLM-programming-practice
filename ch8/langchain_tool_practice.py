from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

# API KEY 불러오기
load_dotenv()
llm = ChatOpenAI(model="gpt-4o-mini")
llm.invoke([HumanMessage("잘 지냈어?")])

# 도구 정의
from langchain_core.tools import tool
from datetime import datetime
import pytz

@tool
def get_current_time(timezone: str, location: str) -> str:
    """현재 시각을 반환하는 함수

    Args:
        timezone (str): 타임존 (예: 'Asia/Seoul') 실제 존재하는 타임존이어야 함
        location (str): 지역명. 타임존이 모든 지명에 대응되지 않기 때문에 이후 llm 답변 생성에 사용됨
    """
    tz = pytz.timezone(timezone)
    now = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
    location_and_local_time = f'{timezone} ({location}) 현재시각 {now} '
    print(location_and_local_time)
    return location_and_local_time


# 모델에 도구 바인딩
tools = [get_current_time,]
tool_dict = {"get_current_time": get_current_time,}

llm_with_tools = llm.bind_tools(tools)


# 1단계 : 모델의 도구 호출 결정
from langchain_core.messages import SystemMessage

messages = [
    SystemMessage("너는 사용자의 질문에 답변을 하기 위해 tools를 사용할 수 있다."),
    HumanMessage("부산은 지금 몇시야?"),
]

response = llm_with_tools.invoke(messages)
messages.append(response)

print(messages)


# 2단계 : 도구 실행
for tool_call in response.tool_calls:
    selected_tool = tool_dict[tool_call["name"]]
    print(tool_call["args"])
    tool_msg = selected_tool.invoke(tool_call)
    messages.append(tool_msg)


# 3단계 : 모델의 최종 답변
final_response = llm_with_tools.invoke(messages)
print(final_response.content)
# ==========================================
# [문제 2] AIMessage에 포함된 핵심 정보
# ==========================================

# AIMessage의 tool_calls에는 모델이 호출하려는 도구 정보가 포함된다.
#
# 1. name
#    호출할 도구의 이름 (get_current_time)
#
# 2. args
#    도구에 전달할 인자
#    - timezone: Asia/Seoul
#    - location: 부산
#
# 3. id
#    각 도구 호출을 식별하는 고유 ID
#
# 따라서 AIMessage의 tool_calls를 확인하면
# 모델이 어떤 도구를 어떤 인자로 호출하려고 하는지 알 수 있다.
