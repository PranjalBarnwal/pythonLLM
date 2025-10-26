from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


openai_client = OpenAI()
embedding_model = OpenAIEmbeddings(model="text-embedding-3-large")

vector_db = QdrantVectorStore.from_existing_collection(
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_rag",
)

user_query = input("Ask your nodejs question: ")

search_results = vector_db.similarity_search(user_query)

context = "\n\n\n".join(
    [
        f"Page Content: {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}"
        for result in search_results
    ]
)
SYSTEM_PROMPT = f"""
 You are an helpful assistant who answers user query based on the context retrieved from a PDF file along with page_contents and page_number.

 You should only answer the user based on the following context and navigate the user to open the right page number to know more.

 Context:
{context}
"""

response = openai_client.chat.completions.create(
    model = "gpt-5-mini",
    messages = [
        {"role":"system", "content":SYSTEM_PROMPT},
        {"role":"user", "content":user_query}
    ]
)

print(response.choices)
print(response.choices[0].message.content)

