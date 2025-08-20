# NLP Lab 3: Frequency Distribution Analysis

## Assignment Overview

This assignment performs frequency distribution analysis on the tokenized Gujarati dataset from Assignment 1. The analysis includes:

1. **Manual Frequency Distribution**: Creating word frequency counts without using predefined libraries
2. **Visualization**: Plotting the most frequent 100 words
3. **Stop Word Identification**: Using frequency thresholds to identify stop words
4. **Comparative Analysis**: Showing frequency distributions after stop word removal with three different thresholds

## Files Structure

```
Lab 3/
├── simple_frequency_analysis.py    # Main implementation (recommended)
├── frequency_analysis.py           # Advanced implementation with detailed analysis
├── requirements.txt                # Python dependencies
├── README.md                      # This file
└── Generated outputs:
    ├── top_100_words_original.png
    ├── top_100_words_threshold_50.png
    ├── top_100_words_threshold_100.png
    └── top_100_words_threshold_150.png
```

## Implementation Details

### Key Features

1. **Manual Implementation**: 
   - Frequency counting implemented from scratch without using `Counter` or similar libraries
   - Custom sorting algorithms for finding top frequent words
   - Manual stop word identification and removal

2. **Gujarati Text Processing**:
   - Unicode range filtering for Gujarati text (U+0A80 to U+0AFF)
   - Punctuation and number removal
   - Proper handling of Gujarati script

3. **Multiple Threshold Analysis**:
   - Three different frequency thresholds: 50, 100, 150
   - Comparative analysis showing the effect of different thresholds
   - Visual representation of changes in word distribution

### Algorithm Details

#### Frequency Distribution Creation
```python
# Manual frequency counting
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
```

#### Top N Words Extraction
```python
# Manual sorting without using built-in sort functions
for i in range(len(word_list)):
    for j in range(i + 1, len(word_list)):
        if word_list[i][1] < word_list[j][1]:
            word_list[i], word_list[j] = word_list[j], word_list[i]
```

#### Stop Word Identification
```python
# Frequency-based stop word identification
stop_words = []
for word, freq in word_freq.items():
    if freq >= threshold:
        stop_words.append(word)
```

## Usage Instructions

### Prerequisites

Install required dependencies:
```bash
pip install matplotlib numpy
```

### Running the Analysis

#### Option 1: Simple Implementation (Recommended)
```bash
python simple_frequency_analysis.py
```

#### Option 2: Advanced Implementation
```bash
python frequency_analysis.py
```

### Expected Outputs

1. **Console Output**:
   - Total word counts and statistics
   - Top 10 most frequent words
   - Stop words identified at each threshold
   - Summary of filtering results

2. **Generated Plots**:
   - Original frequency distribution of top 100 words
   - Three filtered distributions showing effect of stop word removal

## Analysis Results

### Sample Output Structure

```
=== Frequency Distribution Analysis ===
Loading tokenized dataset...
Loaded 3948 sentence groups

1. Creating frequency distribution...
Total unique words: 15432
Total words: 45678

2. Getting top 100 most frequent words...
Top 10 most frequent words:
 1. 'છે' - 1234 times
 2. 'અને' - 987 times
 3. 'થી' - 876 times
 4. 'હતી' - 765 times
 5. 'કે' - 654 times
 ...

3. Plotting frequency distribution of top 100 words...

4. Analyzing with different stop word thresholds: [50, 100, 150]

--- Threshold: 50 ---
Identified 45 stop words (frequency >= 50)
Top stop words identified:
  'છે' - 1234 times
  'અને' - 987 times
  ...
```

### Threshold Analysis

- **Threshold 50**: Removes very common words (articles, conjunctions, common verbs)
- **Threshold 100**: More aggressive filtering, removes moderately frequent words
- **Threshold 150**: Very aggressive filtering, keeps only domain-specific and content words

## Technical Implementation Notes

### Why Manual Implementation?

The assignment specifically requires avoiding predefined libraries for frequency distribution. Our implementation:

1. **Manual Dictionary Operations**: Using basic dictionary operations for counting
2. **Custom Sorting**: Implementing bubble sort for frequency ranking
3. **Manual Filtering**: Custom loops for stop word removal
4. **Only matplotlib for visualization**: As plotting is the only allowed library usage

### Gujarati Text Handling

- **Unicode Support**: Proper handling of Gujarati Unicode characters
- **Script Filtering**: Removes non-Gujarati characters while preserving text integrity
- **Encoding**: UTF-8 encoding for proper character representation

### Performance Considerations

- Time Complexity: O(n log n) for sorting, O(n) for frequency counting
- Space Complexity: O(n) for storing word frequencies
- Optimized for readability over performance as per educational requirements

## Expected Learning Outcomes

1. **Understanding Frequency Distributions**: How word frequencies follow Zipf's law
2. **Stop Word Identification**: Learning automatic methods for stop word detection
3. **Text Preprocessing**: Practical experience with real-world text cleaning
4. **Data Visualization**: Creating meaningful plots for linguistic analysis
5. **Manual Algorithm Implementation**: Understanding underlying mechanisms of NLP libraries

## Troubleshooting

### Common Issues

1. **File Not Found**: Ensure the tokenized_gujarati_sentences.json file exists in the correct path
2. **Unicode Errors**: Verify file encoding is UTF-8
3. **Memory Issues**: For large datasets, consider processing in chunks
4. **Plot Display**: If plots don't display, ensure matplotlib backend is configured correctly

### File Path Issues

Update the file path in the script if your tokenized data is in a different location:
```python
file_path = "path/to/your/tokenized_gujarati_sentences.json"
```

## Assignment Submission

Include the following files in your submission:
1. `simple_frequency_analysis.py` (main implementation)
2. All generated PNG files
3. This README.md file
4. Optional: `frequency_analysis.py` (advanced version)

## References

- Gujarati Unicode Standard: https://unicode.org/charts/PDF/U0A80.pdf
- Zipf's Law in Natural Language: Powers, frequency distributions, and vocabulary
- Stop Words in Information Retrieval: Manning, Raghavan & Schütze

