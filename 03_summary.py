from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPEN_API_KEY')


def summarize_txt(file_path: str):

    client = OpenAI(api_key=api_key)

    # 주어진 텍스트 파일 읽기
    with open(file_path, 'r', encoding='utf-8') as f:
        txt = f.read()

    # 긴 문서를 여러 부분으로 나누기
    chunk_size = 50000
    chunks = [txt[i:i + chunk_size] for i in range(0, len(txt), chunk_size)]

    summaries = []

    # 각 부분 요약
    for i, chunk in enumerate(chunks):

        system_prompt = f'''
        너는 다음 글을 요약하는 봇이다.
        아래 글을 읽고, 저자의 문제 인식과 주장 및 주요 내용을 요약하라.

        이 글은 전체 논문의 일부이다.
        중요한 내용과 핵심 주장을 중심으로 요약하라.

        =============== 이하 텍스트 ===============

        {chunk}
        '''

        print(f'{i + 1}/{len(chunks)}번째 부분을 요약하는 중...')

        response = client.chat.completions.create(
            model="gpt-4o",
            temperature=0.1,
            messages=[
                {"role": "system", "content": system_prompt},
            ]
        )

        summaries.append(response.choices[0].message.content)

    # 부분 요약들을 하나로 합쳐 최종 요약
    combined_summary = '\n\n'.join(summaries)

    final_prompt = f'''
    너는 논문 요약 전문가이다.
    아래는 하나의 논문을 여러 부분으로 나누어 요약한 결과이다.

    각 요약을 종합하여 논문의 전체적인 내용을 정리하라.

    작성해야 하는 포맷은 다음과 같다.

    # 제목

    ## 저자의 문제 인식 및 주장 (15문장 이내)

    ## 저자 소개

    =============== 부분 요약 ===============

    {combined_summary}
    '''

    print('전체 내용을 종합하여 최종 요약을 생성하는 중...')

    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0.1,
        messages=[
            {"role": "system", "content": final_prompt},
        ]
    )

    return response.choices[0].message.content


if __name__ == '__main__':

    file_path = '/Users/joseong-gwan/LLM-programming-practice/output/2303.18223v19_with_preprocessing.txt'

    summary = summarize_txt(file_path)

    print(summary)

    # 요약 내용 파일 저장
    with open('./output/crop_model_summary.txt', 'w', encoding='utf-8') as f:
        f.write(summary)
