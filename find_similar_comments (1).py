import os
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Assuming 'config' is already defined, similar to previous code
config = {
    "email": "example@example.com",
    "root": "/path/to/save/directory"
    }

def load_comments(file_path):
    """Loads the comments from the provided file path."""
    with open(file_path, 'r') as file:
        comments = file.readlines()
    return [comment.strip() for comment in comments]

def save_similar_comments(comment1, comment2, similarity, output_path):
    """Saves the most similar pair of comments to the output file."""
    with open(output_path, 'w') as file:
        file.write(f"Comment 1: {comment1}\n")
        file.write(f"Comment 2: {comment2}\n")
        file.write(f"Similarity: {similarity:.4f}\n")

def find_most_similar_comments(comments, model):
    """Finds the most similar pair of comments based on cosine similarity of their embeddings."""
    embeddings = model.encode(comments)
    
    # Compute cosine similarity between all pairs
    similarity_matrix = cosine_similarity(embeddings)

    # Set the diagonal to zero to ignore self-similarity
    np.fill_diagonal(similarity_matrix, 0)

    # Find the indices of the highest similarity value
    max_sim_index = np.unravel_index(np.argmax(similarity_matrix, axis=None), similarity_matrix.shape)

    # Return the most similar comments and their similarity score
    return comments[max_sim_index[0]], comments[max_sim_index[1]], similarity_matrix[max_sim_index]

def a9_find_most_similar_comments():
    """Finds the most similar pair of comments and saves them."""
    # Load comments from the file
    comments = load_comments(os.path.join(config["root"], "comments.txt"))
    
    # Initialize the SentenceTransformer model
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

    # Find the most similar comments
    comment1, comment2, similarity = find_most_similar_comments(comments, model)

    # Save the result to the output file
    save_similar_comments(comment1, comment2, similarity, os.path.join(config["root"], "comments-similar.txt"))

if __name__ == "__main__":
    # Run the function to find and save the most similar comments
    a9_find_most_similar_comments()
