from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient

from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)


vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_rag",
    embedding=embedding_model
)


#user input

user_input=input("👤:Ask Something")

search_result=vector_db.similarity_search(query=user_input)   


# returns relevant chunks only
#  you will get back a list of Document objects from LangChain.
# Each Document has two main attributes:
# page_content → the actual chunk of text from your PDF that matched the query
# metadata → dictionary with extra info (page number, source file, etc.)
# IN PDF: React is a JavaScript library for building user interfaces.
# search_result = vector_db.similarity_search("What is React?")
# search_result: 
#    [
#     Document(
#         page_content="React is a JavaScript library for building user interfaces.",
#         metadata={
#             "source": "react.pdf",
#             "page": 1,
#             "page_label": "1"
#         }
#     )
# ]






context = "\n\n\n".join(
    f"Page Content: {result.page_content}\n"
    f"Page Number: {result.metadata['page_label']}\n"
    f"File Location: {result.metadata['source']}"
    for result in search_result
)

SYSTEM_PROMPT = f"""
You are a helpful AI Assistant who answers user queries based on the available
context retrieved from a PDF file along with page contents and page number.

You should only answer the user based on the following context and navigate the
user to open the right page number to know more.

Context:
{context}
"""


response = openai_client.chat.completions.create(
    model="gpt-5",
    messages=[
        { "role": "system", "content": SYSTEM_PROMPT },
        { "role": "user", "content": user_input }
    ]
)

print(f"🤖: {response.choices[0].message.content}")

