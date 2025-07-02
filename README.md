# RAG-With-Ollama
Free &amp; open-source chatbot to summarize and query your PDFs, CSVs, DOCX, and TXT files locally using Ollama + RAG

Upload your PDF, DOCX, CSV, or TXT file and ask any question. This local, private chatbot uses Retrieval-Augmented Generation (RAG) to give factual answers and summarize your content — all offline.


---

## 🔧 Features

✅ Upload PDFs, articles, notes, datasets  
✅ Ask direct questions or request full summaries  
✅ Powered by Ollama (LLaMA 3 / Mistral)  
✅ Uses LangChain + FAISS for fast retrieval  
✅ Streamlit UI with memory chat interface  
✅ Clean software-engineering project layout  
✅ 100% free & open-source — works offline!

---

## 💡 Example Prompts

- “Summarize this research paper”
- “List all the genes mentioned”
- “What pathways are enriched in this study?”
- “Give the conclusion from this article”

---

## 🧪 Use Cases

- 🧬 Bioinformatics document Q&A  
- 📝 Research article summarizer  
- 🏥 Offline clinical or HIPAA-safe document reader  
- 🎓 Lecture notes or academic material assistant  

---

## ⚙️ Installation

```bash
git clone https://github.com/shari01/rag-chatbot-ollama
cd rag-chatbot-ollama
pip install -r requirements.txt
ollama run llama3  # or mistral, gemma, etc.
streamlit run app.py
