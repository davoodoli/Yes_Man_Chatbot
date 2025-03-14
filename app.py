from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model="gpt-4o")
template = ChatPromptTemplate.from_messages(
    [
    ("system","You are s yes man person and just you answer 'I do not have any knwoledge' exept for questions about sports to all the questions"),
    ("user","{input}")
    ]
)

output_parser = StrOutputParser()

chain = template|llm|output_parser

result = chain.invoke("Who is Cristiano Ronaldo in Soccer?")
print(result)

