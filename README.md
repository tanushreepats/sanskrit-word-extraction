# sanskrit-word-extraction

a small script that downloads Sanskrit text from AI4Bharat's IndicCorpV2 dataset, extracts unique Devanagari words, and outputs word frequency as a CSV file

WHAT IT DOES
downloads data/sa.txt from the IndicCorpV2 dataset on Hugging Face.
reads the file line by line, using a regex to extract only genuine Devanagari word characters (excludes punctuation and digits)
counts how often each unique word appears 
saves the results to sanskrit_unique_words.csv, sorted by frequency (descending order of frequency)

DATASET 
ai4bharat/IndicCorpV2 (AI4Bharat) - limited to 5000 lines of the corpus (set MAX_LINES to None to process the entire file)