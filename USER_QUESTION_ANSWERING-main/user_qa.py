from haystack.nodes import FARMReader
from haystack.document_stores import SQLDocumentStore
from haystack.nodes import TfidfRetriever
from haystack.pipelines import ExtractiveQAPipeline

# Load pre-trained reader model from Hugging Face
reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2")

# Initialize SQLDocumentStore
document_store = SQLDocumentStore(url="sqlite:///qa.db")

# Initialize retriever
retriever = TfidfRetriever(document_store=document_store)

# Create the pipeline
pipe = ExtractiveQAPipeline(reader, retriever)

# Streamlit app for interactive Q&A
import streamlit as st

st.title("Question Answering system")
question = st.text_area("Enter your question:")
if st.button("Answer"):
    params = {"Retriever": {"top_k": 5}, "Reader": {"top_k": 3}}
    prediction = pipe.run(query=question, params=params)
    
    # Display results
    for ans in prediction['answers']:
        st.write(ans.answer)  # Main answer
        st.write(ans.context)  # Context
        st.write('---')
