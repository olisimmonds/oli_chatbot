from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Document Paths
cv_doc_path = "docs/CV_june_24.pdf"
linkedin_doc_path = "docs/LinkedIn Profile as of 20-25.pdf"
doc_paths = [cv_doc_path, linkedin_doc_path]

# Load documents
def load_docs(doc_paths):
    docs = []
    for file_path in doc_paths:
        loader = PyPDFLoader(file_path)
        docs.extend(loader.load())  # Extend to handle multiple pages properly
    return docs

def get_split_docs():
    documents = load_docs(doc_paths)
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = splitter.split_documents(documents)
    return split_docs

