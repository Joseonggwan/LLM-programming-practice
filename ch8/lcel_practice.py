from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

from typing import Literal
from pydantic import BaseModel, Field

load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini")

system_template = "너는 {story}에 나오는 {character_a} 역할이다. 그 캐릭터에 맞게 사용자와 대화하라."
human_template = "안녕? 저는 {character_b}입니다. 오늘 시간 괜찮으시면 {activity} 같이 할까요?"

prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("user", human_template),
])

class Adlib(BaseModel):
    """스토리 설정과 사용자 입력에 반응하는 대사를 만드는 클래스"""

    answer: str = Field(description="스토리 설정과 사용자와의 대화 기록에 따라 생성된 대사")
    main_emotion: Literal["기쁨", "분노", "슬픔", "공포", "냉소", "불쾌", "중립"] = Field(description="대사의 주요 감정")
    main_emotion_intensity: float = Field(description="대사의 주요 감정의 강도 (0.0 ~ 1.0)")
structured_llm = model.with_structured_output(Adlib)

adlib_chain = prompt_template | structured_llm

result = adlib_chain.invoke({
    "story": "미녀와 야수",
    "character_a": "벨",
    "character_b": "개스톤",
    "activity": "저녁"
})

print(result)
# [학습 내용 정리]
# BaseModel은 출력 데이터의 구조와 각 필드의 자료형 및 규칙을 정의한다.
# model.with_structured_output()은 모델의 응답이 정의된 구조에 맞게 반환되도록 설정한다.
# 두 가지를 함께 사용하면 LLM의 응답을 일관된 데이터 구조로 받을 수 있으며,
# 후속 작업에서도 각 필드에 쉽게 접근하고 활용할 수 있다.
