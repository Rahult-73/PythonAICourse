from pathlib import Path
import warnings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_qdrant import QdrantVectorStore
from langchain_ollama import OllamaEmbeddings
warnings.filterwarnings("ignore")

pdfpath= Path(__file__).parent / "sample.pdf"

#Load this pdf file in the python program

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(pdfpath)
docs = loader.load()

#Chuncking of the documents
text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size=1000,
    chunk_overlap=400
)

chunks=text_splitter.split_documents(docs)

#Embedding of the chunks needs to be done
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

#Now send the chunks to vector DB
qdrant = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embeddings,
    url="http://localhost:6333",
    collection_name="rag_docs"
)
print("Indexing of the document is done")

