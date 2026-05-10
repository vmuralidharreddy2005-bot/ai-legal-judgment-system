from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load BERT embedding model
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# Sample legal cases
documents = [

    "The accused committed financial fraud and cheating under IPC 420.",

    "The court granted bail in a murder case.",

    "A property dispute was settled in civil court.",

    "The accused was sentenced for cybercrime and online fraud."
]

# Convert legal documents into embeddings
document_embeddings = model.encode(documents)

def find_similar_cases(query):

    # Convert query into embedding
    query_embedding = model.encode([query])

    # Compute cosine similarity
    similarity_scores = cosine_similarity(
        query_embedding,
        document_embeddings
    )

    return similarity_scores[0]