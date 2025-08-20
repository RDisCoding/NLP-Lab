#!/usr/bin/env python3
"""
Simple Frequency Distribution Analysis
NLP Lab 3 Assignment

Creates frequency distribution without using predefined libraries for the core functionality.
Only matplotlib is used for plotting as required.
"""

import json
import matplotlib.pyplot as plt
import re

def create_frequency_distribution(tokenized_data):
    """
    Create frequency distribution manually without using predefined libraries
    
    Args:
        tokenized_data: List of tokenized sentences
        
    Returns:
        Dictionary with word frequencies
    """
    word_freq = {}
    total_words = 0
    
    print("Building frequency distribution manually...")
    
    for sentence_group in tokenized_data:
        for sentence in sentence_group:
            if sentence.strip():  # Skip empty sentences
                # Clean and split sentence
                # Remove punctuation and numbers, keep only Gujarati text
                cleaned_sentence = re.sub(r'[^\u0A80-\u0AFF\s]', '', sentence)
                words = cleaned_sentence.split()
                
                # Count frequencies manually
                for word in words:
                    word = word.strip()
                    if word:
                        if word in word_freq:
                            word_freq[word] += 1
                        else:
                            word_freq[word] = 1
                        total_words += 1
    
    print(f"Total unique words: {len(word_freq)}")
    print(f"Total words: {total_words}")
    
    return word_freq

def get_top_n_words(word_freq, n=100):
    """
    Get top N most frequent words manually (without Counter)
    
    Args:
        word_freq: Dictionary of word frequencies
        n: Number of top words to return
        
    Returns:
        List of (word, frequency) tuples sorted by frequency
    """
    # Convert dictionary to list of tuples
    word_list = [(word, freq) for word, freq in word_freq.items()]
    
    # Sort manually by frequency (descending)
    for i in range(len(word_list)):
        for j in range(i + 1, len(word_list)):
            if word_list[i][1] < word_list[j][1]:
                word_list[i], word_list[j] = word_list[j], word_list[i]
    
    return word_list[:n]

def plot_frequency_distribution(top_words, title, filename=None):
    """
    Plot frequency distribution
    
    Args:
        top_words: List of (word, frequency) tuples
        title: Plot title
        filename: Optional filename to save the plot
    """
    words = [item[0] for item in top_words]
    frequencies = [item[1] for item in top_words]
    
    plt.figure(figsize=(15, 8))
    
    # Create bar plot
    bars = plt.bar(range(len(words)), frequencies, color='lightblue', alpha=0.8)
    
    # Customize plot
    plt.title(title, fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Word Rank', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    
    # Show every 5th word on x-axis to avoid crowding
    step = max(1, len(words) // 20)
    plt.xticks(range(0, len(words), step), 
               [words[i] for i in range(0, len(words), step)], 
               rotation=45, ha='right')
    
    # Add frequency values on top of first 10 bars
    for i in range(min(10, len(top_words))):
        plt.text(i, frequencies[i] + max(frequencies) * 0.01, 
                str(frequencies[i]), ha='center', va='bottom', fontsize=9)
    
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    
    if filename:
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"Plot saved as: {filename}")
    
    plt.show()

def identify_stop_words(word_freq, threshold):
    """
    Identify stop words based on frequency threshold
    
    Args:
        word_freq: Dictionary of word frequencies
        threshold: Minimum frequency to consider a word as stop word
        
    Returns:
        List of stop words
    """
    stop_words = []
    for word, freq in word_freq.items():
        if freq >= threshold:
            stop_words.append(word)
    
    return stop_words

def remove_stop_words(word_freq, stop_words):
    """
    Remove stop words from frequency distribution
    
    Args:
        word_freq: Original word frequency dictionary
        stop_words: List of stop words to remove
        
    Returns:
        New frequency dictionary without stop words
    """
    filtered_freq = {}
    for word, freq in word_freq.items():
        if word not in stop_words:
            filtered_freq[word] = freq
    
    return filtered_freq

def main():
    """Main function"""
    print("=== Frequency Distribution Analysis ===")
    print("Assignment: NLP Lab 3")
    print()
    
    # Load tokenized data
    print("Loading tokenized dataset...")
    file_path = "c:\\Users\\rudra\\OneDrive\\Desktop\\AI I53\\Sem V\\NLP\\Lab\\Lab 1\\tokenized_gujarati_sentences.json"
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            tokenized_data = json.load(file)
        print(f"Loaded {len(tokenized_data)} sentence groups")
    except FileNotFoundError:
        print(f"Error: File {file_path} not found!")
        return
    except Exception as e:
        print(f"Error loading file: {e}")
        return
    
    # Create frequency distribution manually
    print("\n1. Creating frequency distribution...")
    word_frequencies = create_frequency_distribution(tokenized_data)
    
    # Get top 100 most frequent words
    print("\n2. Getting top 100 most frequent words...")
    top_100_words = get_top_n_words(word_frequencies, 100)
    
    print("Top 10 most frequent words:")
    for i, (word, freq) in enumerate(top_100_words[:10]):
        print(f"{i+1:2d}. '{word}' - {freq} times")
    
    # Plot original frequency distribution
    print("\n3. Plotting frequency distribution of top 100 words...")
    plot_frequency_distribution(
        top_100_words, 
        "Top 100 Most Frequent Words - Original Dataset",
        "top_100_words_original.png"
    )
    
    # Define three different thresholds for stop word identification
    thresholds = [50, 100, 150]
    
    print(f"\n4. Analyzing with different stop word thresholds: {thresholds}")
    
    for threshold in thresholds:
        print(f"\n--- Threshold: {threshold} ---")
        
        # Identify stop words
        stop_words = identify_stop_words(word_frequencies, threshold)
        print(f"Identified {len(stop_words)} stop words (frequency >= {threshold})")
        
        # Show some examples of stop words
        stop_word_examples = []
        for word in stop_words:
            stop_word_examples.append((word, word_frequencies[word]))
        
        # Sort stop words by frequency
        for i in range(len(stop_word_examples)):
            for j in range(i + 1, len(stop_word_examples)):
                if stop_word_examples[i][1] < stop_word_examples[j][1]:
                    stop_word_examples[i], stop_word_examples[j] = stop_word_examples[j], stop_word_examples[i]
        
        print("Top stop words identified:")
        for i, (word, freq) in enumerate(stop_word_examples[:5]):
            print(f"  '{word}' - {freq} times")
        
        # Remove stop words
        filtered_frequencies = remove_stop_words(word_frequencies, stop_words)
        print(f"Words remaining after stop word removal: {len(filtered_frequencies)}")
        
        # Get top 100 words after filtering
        top_100_filtered = get_top_n_words(filtered_frequencies, 100)
        
        print("Top 5 words after stop word removal:")
        for i, (word, freq) in enumerate(top_100_filtered[:5]):
            print(f"  {i+1}. '{word}' - {freq} times")
        
        # Plot filtered distribution
        title = f"Top 100 Words After Stop Word Removal (Threshold >= {threshold})"
        filename = f"top_100_words_threshold_{threshold}.png"
        
        plot_frequency_distribution(top_100_filtered, title, filename)
    
    print("\n=== Analysis Complete ===")
    print("Generated files:")
    print("- top_100_words_original.png")
    for threshold in thresholds:
        print(f"- top_100_words_threshold_{threshold}.png")

if __name__ == "__main__":
    main()
