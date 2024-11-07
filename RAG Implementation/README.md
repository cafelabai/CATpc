
### RAG Model with PostgreSQL and pgvector

**Description**

This project implements a Retrieval-Augmented Generation (RAG) model that utilizes PostgreSQL with the pgvector extension to store vector embeddings. The model processes `.docx` files, extracts text and metadata, generates vector embeddings, and stores them in a PostgreSQL database. When a user query is received, it is converted into a vector representation, and the most relevant text chunks are retrieved from the database using cosine similarity. These chunks are then used to augment the input to a LLaM...

**Prerequisites**

- Python 3.8 or higher
- PostgreSQL 15 with pgvector extension
- Jupyter Notebook (optional, recommended)
- Google Colab with a faster runtime (A100 or L4 with HIGH RAM enabled)

**Implementation**

1. Run the following command to install all the necessary packages:

   ```bash
   pip install -r requirements.txt
   ```

2. Clone the repository and navigate to the dataset preparation directory:

   ```bash
   git clone https://github.iu.edu/sunchak/CATpc.git
   cd "CATpc\RAG Implementation"
   ```

3. There are two implementation options:

   3.1 For local execution, follow these instructions:

   3.2 Run the `dbconn.py` file with your local DB username and password to connect to the database:

   ```bash
   python dbconn.py
   ```

   3.3 Run the `vectorEmbeddings.py` file to divide the documents into chunks and create vector embeddings:

   ```bash
   python vectorEmbeddings.py
   ```

   3.4 Run the `similarityfunc.py` to find the cosine similarity for the vector embeddings:

   ```bash
   python similarityfunc.py
   ```

   3.5 Run the `ollama.py` and `transformers.py` files to connect with the LLaMA-3-8B model:

   ```bash
   python ollama.py
   python transformers.py
   ```

4. For Google Colab execution:

   4.1 Use the `complete_rag_pipeline.ipynb` notebook available in the project. This notebook contains the entire pipeline implementation of the RAG model.

   4.2 Execute the notebook cell by cell to process the data, generate embeddings, and perform retrieval using the RAG model.

   **Note:** Run the following command to install all the necessary packages before running the Colab code:

   ```bash
   pip install -r requirements.txt
   ```
