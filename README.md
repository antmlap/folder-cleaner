# 📝 Word Stats Analyzer

A Python script that reads a `.txt` file and reports useful statistics:  
- Total lines, words, and characters  
- Top 5 most frequent words  

Useful for analyzing notes, articles, logs, and other text-based data.

## 🚀 Features
- Counts words, lines, and characters
- Displays most common words using `collections.Counter`
- Command-line support via `argparse`

## 📦 Example Usage

```bash
# Basic
python3 word_stats.py sample.txt

# Output:
Lines: 3
Words: 22
Characters: 123
Top 5 Words:
hello: 4
this: 1
is: 1
a: 1
sample: 1
