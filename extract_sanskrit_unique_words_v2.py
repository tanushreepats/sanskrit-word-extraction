import re
import csv
from collections import Counter
from huggingface_hub import hf_hub_download

REPO_ID = "ai4bharat/IndicCorpV2"
FILENAME = "data/sa.txt"          
MAX_LINES = 5000                 
OUTPUT_CSV = "sanskrit_unique_words.csv"

def download_sanskrit_file():
    local_path = hf_hub_download(
        repo_id=REPO_ID,
        repo_type="dataset",
        filename=FILENAME,
    )
    print(f"location: {local_path}")
    return local_path

def extract_words(file_path, max_lines=None):
    word_counts = Counter()
    lines_processed = 0

    with open(file_path, encoding="utf-8") as f:
        for line in f:
            tokens = re.findall(r"[\u0900-\u0963\u0972-\u097F\u200C\u200D]+", line)
            tokens = [t.strip("\u200c\u200d") for t in tokens if t.strip("\u200c\u200d")]
            word_counts.update(tokens)

            lines_processed += 1
            if max_lines and lines_processed >= max_lines:
                break

            if lines_processed % 500 == 0:
                print(f"Processed {lines_processed} lines, {len(word_counts)} unique words so far...")

    print(f"total {lines_processed} lines processed")
    return word_counts

def save_to_csv(word_counts, output_path):
    sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "frequency"])
        writer.writerows(sorted_words)
    print(f"{len(sorted_words)} unique words saved to {output_path}")

if __name__ == "__main__":
    file_path = download_sanskrit_file()
    word_counts = extract_words(file_path, max_lines=MAX_LINES)
    save_to_csv(word_counts, OUTPUT_CSV)