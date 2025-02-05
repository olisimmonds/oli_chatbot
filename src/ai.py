from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface.llms import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate

# Load embeddings and vector store
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
vector_store = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

prompt_template = PromptTemplate.from_template(
    """
    You are an assistant for answering questions about Oliver Simmonds (Oli). 
    Use the following pieces of retrieved context to answer the question. 
    If you don't know the answer, just say that you don't know. 
    Use three sentences maximum and keep the answer concise.
    Question: {question} 
    Context: {context} 
    Answer:
    """
)

llm = HuggingFacePipeline.from_model_id(
    model_id="gpt2",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 10},
)
def ai_response(question):
    context = "\n\n".join(doc.page_content for doc in vector_store.similarity_search(question))
    messages = prompt_template.invoke({"question": question, "context": context})
    response = llm.invoke(messages)
    return response.split("Answer:")[1].strip()