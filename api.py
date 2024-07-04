from langchain_core.prompts import ChatPromptTemplate
import os
import uvicorn
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from fastapi import FastAPI
from langserve import add_routes
load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")  # type: ignore



#api endpoints
app=FastAPI(
    title="Langchain server",
    version="1.0",
    description="a simpl test server for langserve"
)

  
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash")#type:ignore
prompt = ChatPromptTemplate.from_template ( "you are a helpful assistant, response to use queries: {question}")
add_routes(
    app,prompt|llm,path='/gemini'
)
if __name__=="__main__":
    uvicorn.run(app,host='localhost',port=8080)
