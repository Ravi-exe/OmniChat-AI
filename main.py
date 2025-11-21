import os

from fastapi import FastAPI

from dotenv import load_dotenv

from langchain.agents import create_agent

from langchain_openai import ChatOpenAI
# from langchain.chat_models import 
from typing import cast
# from openai import 

# from 

load_dotenv()

app = FastAPI()

openai_key = cast(str, os.getenv("openai_key"))

print(openai_key)

@app.get("health", tags=["health-check"])
async def root():
    return {"status": "ok"}


@app.get("/question")
async def askQuestion():
    return {
        
    }

if __name__=="__main__":
    print("app started")







#===========================prac==========================================================#

openai_conn = ChatOpenAI(model="gpt-4o-mini",api_key=lambda: openai_key, temperature=0.6)

ans = openai_conn.invoke(input="hello, world")

print(ans)
# openai_conn.


# agent = create_agent(
#     model=""
# )

#===========================prac==========================================================#


