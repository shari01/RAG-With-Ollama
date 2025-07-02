import os
import tempfile
from langchain.document_loaders import (
    PDFPlumberLoader, TextLoader, CSVLoader, Docx2txtLoader
)

def load_uploaded_file(uploaded_file):
    suffix = os.path.splitext(uploaded_file.name)[1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded_file.read())
        path = tmp.name

    if suffix == ".pdf":
        loader = PDFPlumberLoader(path)
    elif suffix in [".txt", ".md"]:
        loader = TextLoader(path)
    elif suffix == ".csv":
        loader = CSVLoader(path)
    elif suffix == ".docx":
        loader = Docx2txtLoader(path)
    else:
        return None

    return loader.load()
