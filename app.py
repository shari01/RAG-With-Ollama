import streamlit as st
from rag.loaders import load_uploaded_file
from rag.vector_store import prepare_vector_store
from rag.chain_builder import build_rag_chain
from config import SUPPORTED_TYPES

st.set_page_config(page_title=" RAG Chatbot", layout="wide")
st.title(" RAG Chatbot (Memory + Upload + Ollama)")

# --- Session state for memory ---
if "messages" not in st.session_state:
    st.session_state.messages = []

if "db" not in st.session_state:
    st.session_state.db = None

# --- File upload ---
uploaded_file = st.file_uploader("Upload a PDF, TXT, DOCX, or CSV file", type=SUPPORTED_TYPES)

if uploaded_file:
    with st.spinner(" Processing file..."):
        documents = load_uploaded_file(uploaded_file)
        if documents:
            st.session_state.db = prepare_vector_store(documents)
            st.success("File processed successfully!")
        else:
            st.error(" Unsupported or unreadable file.")

# --- Chat interface ---
if st.session_state.db:
    user_input = st.chat_input("Ask something based on your uploaded file...")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Build the chain and generate answer
        rag_chain = build_rag_chain(st.session_state.db)
        with st.spinner(" Thinking..."):
            answer = rag_chain.run(user_input)
        st.session_state.messages.append({"role": "assistant", "content": answer})

    # Display full conversation
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
else:
    st.info("Upload a document to begin chatting.")
