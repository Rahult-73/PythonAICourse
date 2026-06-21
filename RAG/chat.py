from langchain_qdrant import QdrantVectorStore
from langchain_ollama import OllamaEmbeddings
from ollama import Client

#Embedding of the chunks needs to be done
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

#Take the chunks from vector db
#Using here from existing collection to take the available vector embedds
vector_db = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    url="http://localhost:6333",
    collection_name="rag_docs"
)

#ask something : user asks question here use this to fecth the vector embedding
userquestion = input("👉 Ask anything :")

#Now, only fecth the relavent embeddings from db
searched_result=vector_db.similarity_search(query=userquestion)
# print(searched_result)
#Now make the vector_db result in structured format
content = "\n\n".join([
    f"""
SOURCE PDF: {result.metadata['source']}
PAGE NUMBER: {result.metadata['page_label']}

CONTENT:
{result.page_content}
"""
    for result in searched_result
])

print(content)

#region latstep

#Create system prompt and add this content to the it
system_prompt = f"""You are an AI assistant.

Answer the user's question using only the information inside the CONTENT sections.

IMPORTANT:

* You must include the page number and PDF path used for the answer.
* Do not omit the reference section.
* If multiple pages are used, list all page numbers.
* If the answer is not present in the content, say "I could not find the answer in the provided documents."

Response format:

Answer: <answer>

Reference:
PDF: <SOURCE PDF>
Page Number: <PAGE NUMBER>

"""
#now create normal chat function and pass the sysprompt and user question
client = Client(host="http://localhost:11434")

response = client.chat(
    model="qwen2.5:1.5b",
    messages=[{"role":"system","content":system_prompt},
              {"role":"user","content":userquestion}]
)
#print the output
print(response["message"]["content"])

#endregion