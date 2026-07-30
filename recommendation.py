"""
DecodeLabs AI Internship - Project 03: AI Recommendation System
Engineered using an Input-Process-Output (IPO) Architecture,
TF-IDF Vector Mapping, and Cosine Similarity Metrics.
"""

import os
import sys
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print("=" * 70)
    print("        DECODELABS AI MATCHMAKER ENGINE — RECOMMENDATION SYSTEM")
    print("=" * 70)

def load_dataset(file_path):
    """
    Ingests and validates the structured dataset.
    """
    if not os.path.exists(file_path):
        print(f"\n[ERROR] Dataset missing at: {file_path}")
        print("Please verify your folder path structure before execution.")
        sys.exit(1)
    
    df = pd.read_csv(file_path)
    
    # Fill any null values to secure the data pipeline
    df['Genre'] = df['Genre'].fillna('')
    df['Keywords'] = df['Keywords'].fillna('')
    
    # Merge structural features into a unified text metadata space
    df['Metadata_Space'] = df['Genre'] + " " + df['Keywords']
    return df

def get_user_preferences():
    """
    Step 1: Ingestion Pipeline.
    Gathers a minimum of 3 specific explicit preference metrics to guarantee 
    sufficient data density and bypass structural empty input vectors.
    """
    print("\n[STEP 1: USER PREFERENCE INGESTION]")
    print("Provide 3 distinct keywords or genres you want to watch right now.")
    print("Examples: Action, Sci-Fi, Comedy, Space, Heist, Horror, Superhero\n")
    
    inputs = []
    for i in range(1, 4):
        while True:
            user_input = input(f" Enter Choice #{i}: ").strip().lower()
            if not user_input:
                print("   ⚠️  Input cannot be empty. Please specify an interest attribute.")
                continue
            inputs.append(user_input)
            break
            
    return " ".join(inputs)

def compute_recommendations(df, user_profile, top_n=3):
    """
    Steps 2 & 3: Processing & Similarity Scoring Pipeline.
    Maps terms to TF-IDF vectors and computes mathematical angular cosine alignment.
    """
    print("\n[STEP 2: VECTOR MAPPING & COSINE SIMILARITY PROCESSING]")
    
    # Initialize TF-IDF Vectorizer to extract and weigh distinct terminology features
    vectorizer = TfidfVectorizer(stop_words='english')
    
    # Fit and transform the comprehensive movie metadata space
    tfidf_matrix = vectorizer.fit_transform(df['Metadata_Space'])
    
    # Transform the ingested user preference profile into the exact same vector room
    user_vector = vectorizer.transform([user_profile])
    
    # Handle User Cold Start Problem: Check if user vector contains only zeros
    if user_vector.nnz == 0:
        print("⚠️ [COLD START ACTIVATED] Preferences didn't match any attributes in our database.")
        print("   Bypassing with a global fallback strategy (returning top system listings)...")
        # Fallback ranking baseline mechanism
        df_fallback = df.copy()
        df_fallback['Similarity_Score'] = 0.0
        return df_fallback.head(top_n)

    # Calculate precise angular alignment using Cosine Similarity metrics
    similarity_scores = cosine_similarity(user_vector, tfidf_matrix).flatten()
    
    # Append calculated weights back into our working framework
    df_scored = df.copy()
    df_scored['Similarity_Score'] = similarity_scores
    
    # Step 3 & 4: Sorting & Filtering (Truncating down to Top-N payload)
    df_ranked = df_scored.sort_values(by='Similarity_Score', ascending=False)
    
    return df_ranked.head(top_n)

def display_output(recommendations, user_profile):
    """
    Step 4: Output Rendering Pipeline.
    Displays clear, formatted, mathematical matching results to the user.
    """
    print("\n" + "=" * 70)
    print("                [STEP 3: RANKED RECOMMENDATION TOP-N LIST]")
    print("=" * 70)
    print(f"Processed Ingested Preferences: '{user_profile}'\n")
    
    has_matches = any(recommendations['Similarity_Score'] > 0)
    
    for idx, row in recommendations.iterrows():
        score_pct = row['Similarity_Score'] * 100
        print(f"🎬 Title: {row['Title']}")
        print(f"   Genres: {row['Genre']}")
        
        if score_pct > 0:
            print(f"   💡 Mathematical Match Precision: {score_pct:.2f}%")
        else:
            print(f"   💡 Match Precision: Global Baseline (Fallback)")
            
        print("-" * 70)
    
    print("\nPipeline Execution Finalized Successfully. Ready for portfolio presentation.")
    print("=" * 70 + "\n")

def main():
    clear_screen()
    print_header()
    
    # Establish project relative dataset pathway destinations
    dataset_path = os.path.join("dataset", "movies.csv")
    
    # Execute structural pipeline phases sequentially
    movie_dataframe = load_dataset(dataset_path)
    user_profile = get_user_preferences()
    
    top_recommendations = compute_recommendations(movie_dataframe, user_profile, top_n=3)
    display_output(top_recommendations, user_profile)

if __name__ == "__main__":
    main()