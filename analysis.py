import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter
from difflib import SequenceMatcher
from sklearn.metrics import jaccard_score
from itertools import product


def ensure_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def load_honeywords_from_generations(folder_path):
    """Loads honeywords from all files in the generations folder."""
    dataset_honeywords = {}

    if not os.path.exists(folder_path):
        print(f"Folder {folder_path} not found.")
        return {}

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and filename.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as file:
                honeywords = [line.strip() for line in file.readlines() if line.strip()]
                dataset_honeywords[filename] = honeywords

    return dataset_honeywords


def plot_honeyword_length_distribution(honeywords, dataset_name, output_folder):
    ensure_directory(output_folder)
    lengths = [len(word) for word in honeywords]

    plt.figure(figsize=(8, 5))
    sns.histplot(lengths, bins=np.arange(5, 20, 1), kde=True)
    plt.xlabel("Password Length")
    plt.ylabel("Frequency")
    plt.title(f"Honeyword Length Distribution - {dataset_name}")
    plt.xticks(rotation=45)
    plt.savefig(os.path.join(output_folder, f"length_distribution_{dataset_name}.png"))
    plt.close()


def plot_similarity_heatmap(honeywords1, honeywords2, label1, label2, output_folder):
    ensure_directory(output_folder)
    texts = [" ".join(honeywords1), " ".join(honeywords2)]
    vectorizer = TfidfVectorizer().fit_transform(texts)
    similarity_matrix = cosine_similarity(vectorizer)

    plt.figure(figsize=(6, 5))
    sns.heatmap(similarity_matrix, annot=True, cmap="coolwarm", fmt=".2f", xticklabels=[label1, label2],
                yticklabels=[label1, label2])
    plt.title(f"Similarity Heatmap: {label1} vs {label2}")
    plt.savefig(os.path.join(output_folder, f"similarity_{label1}_vs_{label2}.png"))
    plt.close()


def levenshtein_distance(s1, s2):
    return sum(1 for a, b in zip(s1, s2) if a != b) + abs(len(s1) - len(s2))


def plot_levenshtein_distribution(honeywords1, honeywords2, label1, label2, output_folder):
    distances = [levenshtein_distance(w1, w2) for w1, w2 in zip(honeywords1, honeywords2)]

    plt.figure(figsize=(7, 5))
    sns.histplot(distances, bins=10, kde=True)
    plt.xlabel("Levenshtein Distance")
    plt.ylabel("Frequency")
    plt.title(f"Levenshtein Distance Distribution: {label1} vs {label2}")
    plt.savefig(os.path.join(output_folder, f"levenshtein_{label1}_vs_{label2}.png"))
    plt.close()


def entropy(word):
    counts = Counter(word)
    probabilities = [count / len(word) for count in counts.values()]
    return -sum(p * np.log2(p) for p in probabilities)


def plot_entropy_distribution(honeywords, dataset_name, output_folder):
    ensure_directory(output_folder)
    entropies = [entropy(word) for word in honeywords]

    plt.figure(figsize=(7, 5))
    sns.histplot(entropies, bins=10, kde=True)
    plt.xlabel("Entropy")
    plt.ylabel("Frequency")
    plt.title(f"Entropy Distribution - {dataset_name}")
    plt.savefig(os.path.join(output_folder, f"entropy_{dataset_name}.png"))
    plt.close()


def compare_honeywords(dataset_honeywords, output_folder):
    ensure_directory(output_folder)
    paired_files = {}

    for filename in dataset_honeywords:
        if "000webhost" in filename:
            myspace_match = filename.replace("000webhost", "myspace")
            if myspace_match in dataset_honeywords:
                paired_files[filename] = myspace_match

    for webhost_file, myspace_file in paired_files.items():
        honeywords1 = dataset_honeywords[webhost_file]
        honeywords2 = dataset_honeywords[myspace_file]

        plot_similarity_heatmap(honeywords1, honeywords2, webhost_file, myspace_file, output_folder)
        plot_levenshtein_distribution(honeywords1, honeywords2, webhost_file, myspace_file, output_folder)


def main():
    generations_folder = "generations"  # Update if folder path differs
    output_folder = "Visual_Comparison"  # Folder to save visual outputs
    dataset_honeywords = load_honeywords_from_generations(generations_folder)

    if dataset_honeywords:
        compare_honeywords(dataset_honeywords, output_folder)

        for dataset_name, honeywords in dataset_honeywords.items():
            plot_honeyword_length_distribution(honeywords, dataset_name, output_folder)
            plot_entropy_distribution(honeywords, dataset_name, output_folder)
    else:
        print("No honeywords found in the generations folder.")

    print("Completed")
if __name__ == "__main__":
    main()
