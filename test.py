from langchain_google_genai import ChatGoogleGenerativeAI
 #ImportGoogleAPIKey
from dotenv import load_dotenv
import os
load_dotenv()
 #SetyoutLLMtoGoogleGeminiModel
llm=ChatGoogleGenerativeAI(model="gemini-2.5-pro", google_api_key=os.getenv("GOOGLE_API_KEY"))
response=llm.invoke("Who is Mahatma Gandhi?")
print(response.content)