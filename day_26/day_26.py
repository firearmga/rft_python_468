"""
AI Resume Screening Tool
=========================
Reads resumes (TXT/CSV), extracts candidate details (Name, Skills, Experience,
Education), matches each resume against a job description using TF-IDF +
cosine similarity, ranks candidates by Match Score, and exports the
shortlisted candidates to a CSV file.

USAGE
-----
    python resume_screener.py

Edit the CONFIG section at the bottom (RESUME_SOURCE, JOB_DESCRIPTION_PATH,
OUTPUT_CSV_PATH, SCORE_THRESHOLD) to point at your own files, or import the
functions below into your own pipeline.

RESUME_SOURCE can be:
    - a folder containing .txt resumes and/or .csv resume batches, or
    - a path to a single .csv file with columns Name, Skills, Experience, Education
"""

import os
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ----------------------------------------------------------------------
# 1. Extraction Functions
# ----------------------------------------------------------------------

def extract_text_from_txt(file_path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


def parse_resume_content(raw_text, source_file=""):
    """
    Heuristic-based parser to extract Name, Skills, Experience, and Education.
    Adjust regex patterns to fit your specific resume formats.
    """
    lines = [line.strip() for line in raw_text.splitlines() if line.strip()]

    # Prefer an explicit "Name:" label; fall back to the first non-empty line
    name_match = re.search(r"^\s*name\s*:\s*(.+)$", raw_text, re.IGNORECASE | re.MULTILINE)
    name = name_match.group(1).strip() if name_match else (lines[0] if lines else "Unknown")

    # Extraction patterns for labeled sections
    skills_match = re.search(
        r"(?:skills|technical skills|technologies)[:\n\s]+(.*?)(?=\n[A-Z][a-zA-Z\s]+:|\Z)",
        raw_text, re.IGNORECASE | re.DOTALL,
    )
    exp_match = re.search(
        r"(?:experience|work experience|employment)[:\n\s]+(.*?)(?=\n[A-Z][a-zA-Z\s]+:|\Z)",
        raw_text, re.IGNORECASE | re.DOTALL,
    )
    edu_match = re.search(
        r"(?:education|qualifications|academic)[:\n\s]+(.*?)(?=\n[A-Z][a-zA-Z\s]+:|\Z)",
        raw_text, re.IGNORECASE | re.DOTALL,
    )

    return {
        "Name": name,
        "Skills": re.sub(r"\s+", " ", skills_match.group(1)).strip() if skills_match else "N/A",
        "Experience": re.sub(r"\s+", " ", exp_match.group(1)).strip() if exp_match else "N/A",
        "Education": re.sub(r"\s+", " ", edu_match.group(1)).strip() if edu_match else "N/A",
        "Source_File": source_file,
        "Full_Text": raw_text,
    }


# ----------------------------------------------------------------------
# 2. Ingest Multiple Resumes (TXT / CSV)
# ----------------------------------------------------------------------

def load_resumes(folder_path_or_csv):
    """
    Loads candidates from either:
      - a single .csv file, or
      - a folder containing any mix of .txt resumes and .csv batch files.
    """
    candidates = []

    def load_csv_file(csv_path):
        df_csv = pd.read_csv(csv_path)
        rows = []
        for _, row in df_csv.iterrows():
            full_text = f"{row.get('Name', '')} {row.get('Skills', '')} {row.get('Experience', '')} {row.get('Education', '')}"
            rows.append({
                "Name": row.get("Name", "Unknown"),
                "Skills": row.get("Skills", "N/A"),
                "Experience": row.get("Experience", "N/A"),
                "Education": row.get("Education", "N/A"),
                "Source_File": os.path.basename(csv_path),
                "Full_Text": full_text,
            })
        return rows

    # Case 1: input is a single CSV file
    if os.path.isfile(folder_path_or_csv) and folder_path_or_csv.lower().endswith(".csv"):
        candidates.extend(load_csv_file(folder_path_or_csv))

    # Case 2: input is a folder — pick up both .txt resumes and .csv batches
    elif os.path.isdir(folder_path_or_csv):
        for filename in sorted(os.listdir(folder_path_or_csv)):
            file_path = os.path.join(folder_path_or_csv, filename)
            if filename.lower().endswith(".txt"):
                raw_text = extract_text_from_txt(file_path)
                candidates.append(parse_resume_content(raw_text, source_file=filename))
            elif filename.lower().endswith(".csv"):
                candidates.extend(load_csv_file(file_path))

    return candidates


# ----------------------------------------------------------------------
# 3. Matching & Scoring Engine (TF-IDF + Cosine Similarity)
# ----------------------------------------------------------------------

def score_and_rank_resumes(candidates, job_description, score_threshold=10.0):
    if not candidates:
        return pd.DataFrame(), pd.DataFrame()

    corpus = [job_description] + [c["Full_Text"] for c in candidates]

    # Calculate TF-IDF Cosine Similarity
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(corpus)
    similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    # Assign percentage match score
    for i, candidate in enumerate(candidates):
        candidate["Match_Score (%)"] = round(similarity_scores[i] * 100, 2)

    # Convert to DataFrame, sort, and filter by threshold
    df = pd.DataFrame(candidates).drop(columns=["Full_Text"])
    df = df.sort_values(by="Match_Score (%)", ascending=False).reset_index(drop=True)
    df["Rank"] = df.index + 1

    shortlisted = df[df["Match_Score (%)"] >= score_threshold].reset_index(drop=True)
    return df, shortlisted


# ----------------------------------------------------------------------
# 4. Execution Pipeline
# ----------------------------------------------------------------------

if __name__ == "__main__":

    # ---------------- CONFIG ----------------
    # Point this at a folder of resumes (.txt and/or .csv) or a single .csv file
    RESUME_SOURCE = "sample_resumes"
    # Job description can be loaded from a file...
    JOB_DESCRIPTION_PATH = "job_description.txt"
    OUTPUT_CSV_PATH = "shortlisted_candidates.csv"
    SCORE_THRESHOLD = 10.0
    # -----------------------------------------

    if os.path.exists(JOB_DESCRIPTION_PATH):
        with open(JOB_DESCRIPTION_PATH, "r", encoding="utf-8", errors="ignore") as f:
            job_description = f.read()
    else:
        # Fallback inline job description if no file is found
        job_description = """
        Looking for a Python Developer experienced in Django, REST APIs, SQL,
        Docker, and Machine Learning libraries like scikit-learn and pandas.
        Bachelor's degree in Computer Science or related field required.
        """

    if os.path.exists(RESUME_SOURCE):
        candidate_list = load_resumes(RESUME_SOURCE)
        ranked_df, shortlisted_df = score_and_rank_resumes(
            candidate_list,
            job_description,
            score_threshold=SCORE_THRESHOLD,
        )

        print("\n=== ALL CANDIDATES (Ranked) ===")
        print(ranked_df.to_string(index=False))

        # Export shortlisted candidates to CSV
        shortlisted_df.to_csv(OUTPUT_CSV_PATH, index=False)
        print(f"\nExported {len(shortlisted_df)} shortlisted candidates to '{OUTPUT_CSV_PATH}'.")
    else:
        print(f"Source path '{RESUME_SOURCE}' not found. Please provide a valid directory or CSV path.")
