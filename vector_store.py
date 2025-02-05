# Run this file to produce the vector store. Once complet this will create a folder named faiss_index.
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from src.doc_loader import get_split_docs

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
vector_store = FAISS.from_documents(get_split_docs(), embeddings)
vector_store.save_local("faiss_index")