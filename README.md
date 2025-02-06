# Oli Chatbot

Built a RAG Langchain chatbot using Streamlit as host. This code can be used as a template for others. I used PDF downloads of my CV and LinkedIn profile as the document input. To make this chatbot your own, switch the pdf documents, delete the `faiss_index` folder, and then run the `vector_store.py` file. This will create new embeddings based on the documents provided. To run the app write the command `streamlit run app.py`. 

This app currently uses a free Hugging Face model which hinders performance. If a paid-for API is used the performance is very impressive. Below is an example of the app running on the free `google/flan-t5-large` model.

![image](https://github.com/user-attachments/assets/1d3e0a6e-5d8c-41e1-a026-db3c896581ab)

