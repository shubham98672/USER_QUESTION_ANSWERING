from haystack.nodes import TfidfRetriever
from haystack.document_stores import SQLDocumentStore
from haystack.pipelines import ExtractiveQAPipeline
from haystack.nodes import FARMReader

# Initialize the document store (same as in index_pipeline.py)
document_store = SQLDocumentStore(url="sqlite:///qa.db")

# Initialize the retriever
retriever = TfidfRetriever(document_store=document_store)

# Initialize the reader
reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2")
reader.save('reader')  # saving the reader model

# Create the pipeline
pipe = ExtractiveQAPipeline(reader, retriever)

# Sample query
sample_query = "Who inspired the author to write this book?"

# Parameters for the retriever and reader
params = {
    "Retriever": {"top_k": 5},  # Top 5 relevant documents in the document store
    "Reader": {"top_k": 3}  # Top 3 answers
}

# Run the pipeline
prediction = pipe.run(query=sample_query, params=params)

# Output the answers
print(prediction['answers'])
