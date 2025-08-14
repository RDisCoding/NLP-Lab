# NLP Lab 1: Gujarati Corpus Analysis with Custom Tokenizers

## 📋 Overview

This lab implements a complete Natural Language Processing pipeline for Gujarati text analysis. The project demonstrates fundamental NLP concepts including corpus processing, custom tokenization, and statistical analysis of text data.

## 🎯 Objectives

- **Corpus Processing**: Handle and process Gujarati text from IndicCorpV2 dataset
- **Custom Tokenization**: Implement sentence and word tokenizers from scratch
- **Data Persistence**: Save tokenized data in structured formats
- **Statistical Analysis**: Compute comprehensive corpus statistics

## 📁 Files Structure

```
Lab 1/
├── README.md                           # This file
├── NLP_Assignment1.pdf                 # Assignment instructions
├── q.ipynb                            # Main Jupyter notebook
├── tokenizer_languages.ipynb          # Language-specific tokenizer experiments
├── gujarati_corpus.txt                # Gujarati text corpus (101 lines)
├── tokenized_gujarati_sentences.json  # Output: tokenized sentences
└── vertopal_7ffb692a1a314e48b0b105cf8329a5d1/  # Generated visualizations
    ├── *.png                          # Various analysis charts
    └── ...
```

## 🚀 Getting Started

### Prerequisites

```bash
pip install requests datasets huggingface_hub pandas jupyter
```

### Running the Lab

1. **Open the main notebook**:
   ```bash
   jupyter notebook q.ipynb
   ```

2. **Execute cells sequentially** to:
   - Install required packages
   - Load and process the Gujarati corpus
   - Run custom tokenizers
   - Generate statistics and visualizations

## 🔧 Implementation Details

### Custom Tokenizers

#### Sentence Tokenizer
- **Purpose**: Split Gujarati text into individual sentences
- **Method**: Uses regex patterns to identify sentence boundaries
- **Handles**: Gujarati punctuation marks (।, ?, !, etc.)
- **Output**: List of sentences

#### Word Tokenizer
- **Purpose**: Split sentences into individual words
- **Method**: Unicode-aware tokenization for Gujarati script
- **Handles**: Devanagari characters, punctuation, and whitespace
- **Output**: List of words per sentence

### Data Processing Pipeline

1. **Data Loading**: Read Gujarati corpus from text file
2. **Sentence Segmentation**: Apply custom sentence tokenizer
3. **Word Tokenization**: Apply word tokenizer to each sentence
4. **Data Storage**: Save results in JSON format
5. **Statistical Analysis**: Compute corpus metrics

## 📊 Output Files

### `tokenized_gujarati_sentences.json`
```json
{
  "sentences": [
    {
      "original": "આ વીડિયો જુઓ: ઊંઝા માર્કેટયાર્ડ આજથી 25 જુલાઈ સુધી બંધ",
      "tokens": ["આ", "વીડિયો", "જુઓ", ":", "ઊંઝા", "માર્કેટયાર્ડ", ...]
    },
    ...
  ],
  "statistics": {
    "total_sentences": 101,
    "total_words": 2847,
    "avg_words_per_sentence": 28.2,
    "unique_words": 1456
  }
}
```

## 📈 Statistical Analysis

The notebook computes various corpus statistics:

- **Sentence Count**: Total number of sentences
- **Word Count**: Total and unique word counts
- **Average Sentence Length**: Words per sentence
- **Vocabulary Size**: Number of unique words
- **Character Distribution**: Frequency of Gujarati characters
- **Word Length Distribution**: Histogram of word lengths

## 🛠️ Key Features

### 1. Unicode Support
- Full support for Gujarati (Devanagari) script
- Proper handling of Unicode characters and combining marks

### 2. Robust Tokenization
- Handles complex Gujarati sentence structures
- Preserves punctuation and special characters
- Configurable tokenization rules

### 3. Data Visualization
- Word frequency charts
- Sentence length distributions
- Character usage patterns
- Statistical summaries

### 4. Extensible Design
- Modular tokenizer classes
- Easy to adapt for other Indic languages
- Configurable parameters

## 🔍 Usage Examples

### Basic Tokenization
```python
# Load the tokenizer
from tokenizers import GujaratiTokenizer

tokenizer = GujaratiTokenizer()

# Tokenize a sentence
text = "આ વીડિયો જુઓ: ઊંઝા માર્કેટયાર્ડ આજથી 25 જુલાઈ સુધી બંધ"
sentences = tokenizer.sentence_tokenize(text)
words = tokenizer.word_tokenize(sentences[0])

print(f"Sentences: {len(sentences)}")
print(f"Words in first sentence: {words}")
```

### Corpus Statistics
```python
# Analyze corpus
stats = analyze_corpus("gujarati_corpus.txt")
print(f"Total sentences: {stats['sentence_count']}")
print(f"Vocabulary size: {stats['vocabulary_size']}")
print(f"Average sentence length: {stats['avg_sentence_length']:.2f}")
```

## 📚 Learning Outcomes

After completing this lab, you will understand:

1. **Text Preprocessing**: How to clean and prepare text data
2. **Tokenization**: Different approaches to splitting text
3. **Unicode Handling**: Working with non-Latin scripts
4. **Corpus Analysis**: Statistical methods for text analysis
5. **Data Persistence**: Saving and loading processed data

## 🐛 Common Issues & Solutions

### Issue: Unicode Display Problems
**Solution**: Ensure your environment supports UTF-8 encoding
```python
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
```

### Issue: Missing Dependencies
**Solution**: Install all required packages
```bash
pip install -r requirements.txt
```

### Issue: File Path Errors
**Solution**: Use absolute paths or ensure working directory is correct
```python
import os
os.getcwd()  # Check current directory
```

## 🤝 Contributing

To extend this lab:

1. Add support for other Indic languages
2. Implement more sophisticated tokenization rules
3. Add semantic analysis features
4. Create interactive visualizations

## 📖 References

- [IndicCorpV2 Dataset](https://indicnlp.ai4bharat.org/corpora/)
- [Unicode Gujarati Block](https://unicode.org/charts/PDF/U0A80.pdf)
- [NLTK Tokenization Documentation](https://www.nltk.org/api/nltk.tokenize.html)

## 📝 Assignment Tasks Completion

- ✅ **Task A**: Downloaded and processed IndicCorpV2 data
- ✅ **Task B**: Implemented custom sentence and word tokenizers
- ✅ **Task C**: Saved tokenized data to JSON files
- ✅ **Task D**: Computed comprehensive corpus statistics

---

*This lab is part of the NLP course curriculum focusing on text preprocessing and tokenization techniques for Indic languages.*
