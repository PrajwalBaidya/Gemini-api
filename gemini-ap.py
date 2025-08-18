	
import os
import numpy as np
import google.generativeai as genai
import streamlit as st
# ====== CONFIG ======
GOOGLE_API_KEY = "AIzaSyDE_yOm79Aw_yNqsf_ac2Ei2DHWXsCgojo"  # <-- Put your Gemini API key here
TEXT_FILE = "job.txt"           # <-- Path to your text file
CHUNK_SIZE = 500                 # characters per chunk
TOP_K = 3
EMBED_MODEL = "text-embedding-004"
GEN_MODEL = "gemini-1.5-flash"
# ====================
st.title("Google AI with Job description")
# Setup
genai.configure(api_key=GOOGLE_API_KEY)

# Read and split text into chunks
with open(TEXT_FILE, "r") as f:
    text = f.read()

chunks = [text[i:i+CHUNK_SIZE] for i in range(0, len(text), CHUNK_SIZE)]
# st.write(chunks)
# Function to embed text(s)
def embed(texts):
    resp = genai.embed_content(model=EMBED_MODEL, content=texts)["embedding"]
    # st.write(resp)
    vectors = [e for e in resp]
    # st.write(vectors)
    arr = np.array(vectors)
    return arr / (np.linalg.norm(arr, axis=1, keepdims=True) + 1e-10)

# # Embed chunks
chunk_vectors = embed(chunks)

# # User query
def prompting(query= "hello there"):
    try:
        query_vec = embed([query])[0]

        # # Retrieve top-k chunks
        sims = chunk_vectors @ query_vec
        top_idx = np.argsort(-sims)[:TOP_K]
        context = "\n\n".join([chunks[i] for i in top_idx])
        # Ask Gemini using retrieved context
        prompt = f"Answer using only this context:\n{context}\n\nQuestion: {query}"
        model = genai.GenerativeModel(GEN_MODEL)
        resp = model.generate_content(prompt)

        st.write('User ->',query)
        st.write('Robot ->', resp.text)

    except:
        pass

query = st.chat_input('Enterv any query!')
prompting(query)