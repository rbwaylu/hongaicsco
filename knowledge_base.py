# knowledge_base.py
def search_knowledge(question):
    with open('customer_service_kb.md', 'r', encoding='utf-8') as f:
        content = f.read()
    # 简单文本匹配
    for item in content.split('- Q: '):
        if question in item:
            return item.split('A: ')[1].strip()
    return None