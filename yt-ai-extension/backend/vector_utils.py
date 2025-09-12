import os
from dotenv import load_dotenv
load_dotenv()

# This should now be present in your `.env` file:
# GOOGLE_API_KEY=AIzaSy...

from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from langchain.vectorstores import FAISS
from langchain.embeddings.base import Embeddings
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

class SentenceTransformerEmbeddings(Embeddings):
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, texts):
        return self.model.encode(texts, convert_to_numpy=True).tolist()

    def embed_query(self, text):
        return self.model.encode([text], convert_to_numpy=True)[0].tolist()

def build_vector_store(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = splitter.create_documents([text])
    embeddings = SentenceTransformerEmbeddings()
    return FAISS.from_documents(docs, embeddings)

def get_answer(vector_store, question):
    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})
    docs = retriever.invoke(question)
    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = PromptTemplate(
        template="""
        Answer only using the following context:
        {context}

        Question: {question}
        """,
        input_variables=["context", "question"]
    )

    chain = prompt | ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.2)
    return chain.invoke({"context": context, "question": question}).content
