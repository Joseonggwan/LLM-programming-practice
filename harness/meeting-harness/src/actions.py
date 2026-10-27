def extract_actions(text):
    """회의록의 '할 일:' 줄에서 작업 내용을 추출한다."""
    actions = []
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("할 일:"):
            action = line.split(":", 1)[1].strip()
            if action:
                actions.append(action)
    return actions
