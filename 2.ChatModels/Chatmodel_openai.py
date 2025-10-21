from langchain_openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
model = OpenAI(model='gpt-4')

result = model.invoke("what is the capital of india")
print(result.content)