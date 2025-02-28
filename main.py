from fastapi import FastAPI, Request
from knowledge_base import search_knowledge
import requests

app = FastAPI()

@app.post("/ask")
async def ask_question(request: Request):
    data = await request.json()
    user_question = data.get("question")
    
    # 优先查询知识库
    kb_answer = search_knowledge(user_question)
    if kb_answer:
        return {"answer": kb_answer}
    
    # 调用深度求索API
    headers = {"Authorization": "Bearer YOUR_DEEPSEEK_KEY"}
    response = requests.post(
        "https://api.deepseek.com/v1/chat/completions",
        json={"messages": [{"role": "user", "content": user_question}]},
        headers=headers
    )
    return response.json()
from fastapi.responses import PlainTextResponse

@app.get("/wechat")
async def wechat_verify(signature: str, timestamp: str, nonce: str, echostr: str):
    # 此处需要实现签名验证逻辑
    return PlainTextResponse(echostr)