from langchain.chains import RetrievalQA
from langchain.llms import Ollama
from config import OLLAMA_MODEL

def build_rag_chain(db):
    retriever = db.as_retriever(search_kwargs={"k": 3})
    llm = Ollama(model=OLLAMA_MODEL)
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
