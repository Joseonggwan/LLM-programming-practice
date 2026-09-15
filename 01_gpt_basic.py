import os
from dotenv import load_dotenv
from openai import OpenAI

# .env 파일에 저장된 환경변수 로드
load_dotenv()

# 환경변수에서 OPENAI_API_KEY 불러오기
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "2022년 월드컵 우승 팀은 어디야?"},
    ],
)

# GPT 답변 출력
print(response.choices[0].message.content)
