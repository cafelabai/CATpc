# Calculates cosine similarity between the query embedding and each stored embedding to find the most similar chunk.

import psycopg2
import numpy as np
import torch
from transformers import AutoTokenizer, AutoModel
import torch.nn.functional as F
import dbconn.py

model_ckpt = "sentence-transformers/all-MiniLM-L6-v2"
tokenizer = AutoTokenizer.from_pretrained(model_ckpt)
model = AutoModel.from_pretrained(model_ckpt)

def create_embedding(text):
    encoded_input = tokenizer(text, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        model_output = model(**encoded_input)
    input_mask = encoded_input['attention_mask']
    token_embeddings = model_output.last_hidden_state
    input_mask_expanded = input_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    sum_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1)
    sum_mask = torch.clamp(input_mask_expanded.sum(1), min=1e-9)
    return F.normalize(sum_embeddings / sum_mask, p=2, dim=1)

try:
    cursor = connection.cursor()
    query_text = "Give me an example of community-based STEAM program"
    query_embedding = create_embedding(query_text).numpy()[0]

    cursor.execute("SELECT filename, chunk_index, embedding FROM chunks;")
    db_embeddings = cursor.fetchall()

    max_similarity = -1
    most_similar_chunk = None
    most_similar_filename = None
    most_similar_chunk_index = None

    for filename, chunk_index, embedding_str in db_embeddings:
        db_embedding = np.array(eval(embedding_str.replace('{', '[').replace('}', ']')))
        similarity = np.dot(query_embedding, db_embedding) / (np.linalg.norm(query_embedding) * np.linalg.norm(db_embedding))
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_chunk = chunk_index
            most_similar_filename = filename
            most_similar_chunk_index = chunk_index

    if most_similar_chunk is not None:
        cursor.execute("""
            SELECT title, authors, doi
            FROM metadata
            WHERE filename = %s
        """, (most_similar_filename,))
        most_similar_metadata = cursor.fetchone()
        print("Most similar metadata:", most_similar_metadata)
        print("Most similar chunk index:", most_similar_chunk_index)
    else:
        print("No similar item found.")

    print("Query Embedding:", query_embedding)

finally:
    cursor.close()
    connection.close()
