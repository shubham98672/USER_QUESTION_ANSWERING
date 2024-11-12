# USER_QUESTION_ANSWERING

The User Question Answering System is designed to extract relevant information from a given text document (such as a PDF or TXT file) and answer user questions based on that document. It leverages natural language processing (NLP) and machine learning (ML) techniques to process, index, and retrieve information effectively.

This system allows users to upload a document (e.g., a PDF) and ask questions related to its content. The system will process the document, index the content, and then return an answer to the question by searching through the indexed information.

**Features**
PDF/Text File Conversion: Convert PDF documents into text for easy processing.
Document Preprocessing: The system pre-processes documents (splitting text into smaller chunks, handling sentence boundaries, etc.).
Indexing: Uses an indexing pipeline to create a searchable database from the document.
Question Answering: Users can ask questions, and the system will provide relevant answers based on the indexed content.
Support for Multiple Document Formats: Handles both PDFs and TXT documents.
**Requirements**
To run this system, ensure that you have the following dependencies installed:

Python: Version 3.6 or higher
Required Libraries:
requests: For downloading files
PyMuPDF: For PDF text extraction
haystack: For NLP processing, indexing, and search
nltk: For sentence tokenization
faiss (optional): For advanced indexing
Install dependencies via pip:

pip install requests pymupdf haystack nltk
Installation
Clone this repository or download the project files to your local machine.

git clone <repository-url>
Install the required dependencies:

pip install -r requirements.txt
Download any additional NLTK resources required for sentence tokenization. This can be done by running the following Python code:

import nltk
nltk.download('punkt')
**Usage**
**Step 1: Document Upload**
To use the system, you need to provide a PDF or text file. You can either upload a document or download one using the provided URL in the script.

**Step 2: Convert PDF to Text**
If the document is a PDF, it will first be converted to a text format (document.txt), which will be used for further processing.
**Run the script data.py:**
python data.py
This will convert the PDF into a text document.

**Step 3: Index the Document**
After the document is ready, the next step is to index it. This is done using the indexing pipeline.
**Run the script index_pipeline.py:**
python index_pipeline.py
This will process the text, split it into chunks, and index it for easier retrieval during question answering.

**Step 4: Ask a Question**
After indexing, you can now ask questions related to the document. The system will search the indexed data and provide an answer.
**Run the script search_pipeline.py:**
python search_pipeline.py
You can enter a question, and the system will return an answer based on the content of the document.
