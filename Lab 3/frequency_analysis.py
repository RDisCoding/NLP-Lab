#!/usr/bin/env python3
"""
Frequency Distribution Analysis for Tokenized Gujarati Text
Assignment: Lab 3 - NLP

This script performs:
1. Creates frequency distribution from tokenized dataset
2. Plots most frequent 100 words
3. Identifies stop words using frequency thresholds
4. Plots frequency distributions after stop word removal with different thresholds
"""

import json
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict, Counter
import re
from typing import Dict, List, Tuple

class FrequencyAnalyzer:
    def __init__(self, tokenized_file_path: str):
        """
        Initialize the frequency analyzer with tokenized data
        
        Args:
            tokenized_file_path: Path to the tokenized JSON file
        """
        self.tokenized_file_path = tokenized_file_path
        self.word_frequencies = defaultdict(int)
        self.total_words = 0
        
    def load_and_process_data(self):
        """Load tokenized data and build frequency distribution"""
        print("Loading tokenized data...")
        
        with open(self.tokenized_file_path, 'r', encoding='utf-8') as file:
            tokenized_data = json.load(file)
        
        print("Building frequency distribution...")
        
        # Process each sentence group
        for sentence_group in tokenized_data:
            for sentence in sentence_group:
                if sentence.strip():  # Skip empty sentences
                    # Split sentence into words and clean them
                    words = self._clean_and_split_sentence(sentence)
                    
                    # Count word frequencies
                    for word in words:
                        if word:  # Skip empty words
                            self.word_frequencies[word] += 1
                            self.total_words += 1
        
        print(f"Total unique words: {len(self.word_frequencies)}")
        print(f"Total word count: {self.total_words}")
        
    def _clean_and_split_sentence(self, sentence: str) -> List[str]:
        """
        Clean and split sentence into words
        
        Args:
            sentence: Input sentence
            
        Returns:
            List of cleaned words
        """
        # Remove punctuation and numbers, keep Gujarati text
        # Gujarati Unicode range: \u0A80-\u0AFF
        cleaned_sentence = re.sub(r'[^\u0A80-\u0AFF\s]', '', sentence)
        
        # Split into words and filter empty strings
        words = [word.strip() for word in cleaned_sentence.split() if word.strip()]
        
        return words
    
    def get_top_words(self, n: int = 100) -> List[Tuple[str, int]]:
        """
        Get top N most frequent words
        
        Args:
            n: Number of top words to return
            
        Returns:
            List of (word, frequency) tuples
        """
        return Counter(self.word_frequencies).most_common(n)
    
    def plot_frequency_distribution(self, top_words: List[Tuple[str, int]], 
                                  title: str = "Word Frequency Distribution", 
                                  save_path: str = None):
        """
        Plot frequency distribution
        
        Args:
            top_words: List of (word, frequency) tuples
            title: Plot title
            save_path: Path to save the plot
        """
        words = [word for word, freq in top_words]
        frequencies = [freq for word, freq in top_words]
        
        plt.figure(figsize=(15, 8))
        
        # Create bar plot
        bars = plt.bar(range(len(words)), frequencies, color='skyblue', alpha=0.7)
        
        # Customize plot
        plt.title(title, fontsize=16, fontweight='bold')
        plt.xlabel('Words (Rank)', fontsize=12)
        plt.ylabel('Frequency', fontsize=12)
        plt.xticks(range(0, len(words), max(1, len(words)//20)), 
                   [words[i] for i in range(0, len(words), max(1, len(words)//20))], 
                   rotation=45, ha='right')
        
        # Add frequency values on top of bars for first 20 words
        for i, (word, freq) in enumerate(top_words[:20]):
            plt.text(i, freq + max(frequencies) * 0.01, str(freq), 
                    ha='center', va='bottom', fontsize=8)
        
        plt.tight_layout()
        plt.grid(axis='y', alpha=0.3)
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Plot saved to: {save_path}")
        
        plt.show()
    
    def identify_stop_words_by_threshold(self, threshold: int) -> List[str]:
        """
        Identify stop words based on frequency threshold
        
        Args:
            threshold: Frequency threshold above which words are considered stop words
            
        Returns:
            List of stop words
        """
        stop_words = [word for word, freq in self.word_frequencies.items() if freq >= threshold]
        return stop_words
    
    def remove_stop_words(self, stop_words: List[str]) -> Dict[str, int]:
        """
        Remove stop words from frequency distribution
        
        Args:
            stop_words: List of stop words to remove
            
        Returns:
            New frequency distribution without stop words
        """
        filtered_frequencies = {
            word: freq for word, freq in self.word_frequencies.items() 
            if word not in stop_words
        }
        return filtered_frequencies
    
    def analyze_with_multiple_thresholds(self):
        """Analyze frequency distribution with multiple stop word thresholds"""
        
        # Original frequency distribution
        print("\n" + "="*60)
        print("ORIGINAL FREQUENCY DISTRIBUTION")
        print("="*60)
        
        top_100_original = self.get_top_words(100)
        print(f"\nTop 10 most frequent words:")
        for i, (word, freq) in enumerate(top_100_original[:10]):
            print(f"{i+1:2d}. {word:15s} - {freq:5d} times")
        
        # Plot original distribution
        self.plot_frequency_distribution(
            top_100_original, 
            "Top 100 Most Frequent Words - Original Dataset",
            "original_frequency_distribution.png"
        )
        
        # Define thresholds for stop word identification
        thresholds = [50, 100, 200]
        
        for threshold in thresholds:
            print(f"\n" + "="*60)
            print(f"ANALYSIS WITH THRESHOLD = {threshold}")
            print("="*60)
            
            # Identify stop words
            stop_words = self.identify_stop_words_by_threshold(threshold)
            print(f"\nNumber of stop words identified: {len(stop_words)}")
            print(f"Stop words (frequency >= {threshold}):")
            
            # Show stop words with their frequencies
            stop_word_freqs = [(word, self.word_frequencies[word]) for word in stop_words]
            stop_word_freqs.sort(key=lambda x: x[1], reverse=True)
            
            for word, freq in stop_word_freqs[:20]:  # Show top 20 stop words
                print(f"  {word:15s} - {freq:5d} times")
            
            if len(stop_word_freqs) > 20:
                print(f"  ... and {len(stop_word_freqs) - 20} more")
            
            # Remove stop words and get new distribution
            filtered_frequencies = self.remove_stop_words(stop_words)
            
            # Get top 100 words after stop word removal
            top_100_filtered = Counter(filtered_frequencies).most_common(100)
            
            print(f"\nAfter removing stop words:")
            print(f"Remaining unique words: {len(filtered_frequencies)}")
            print(f"Top 10 words after stop word removal:")
            
            for i, (word, freq) in enumerate(top_100_filtered[:10]):
                print(f"{i+1:2d}. {word:15s} - {freq:5d} times")
            
            # Plot filtered distribution
            title = f"Top 100 Words After Stop Word Removal (Threshold >= {threshold})"
            save_path = f"filtered_frequency_distribution_threshold_{threshold}.png"
            
            self.plot_frequency_distribution(top_100_filtered, title, save_path)
    
    def generate_summary_report(self):
        """Generate a summary report of the analysis"""
        print("\n" + "="*60)
        print("SUMMARY REPORT")
        print("="*60)
        
        print(f"Total unique words in dataset: {len(self.word_frequencies):,}")
        print(f"Total word occurrences: {self.total_words:,}")
        
        # Calculate some statistics
        freq_values = list(self.word_frequencies.values())
        avg_frequency = np.mean(freq_values)
        median_frequency = np.median(freq_values)
        
        print(f"Average word frequency: {avg_frequency:.2f}")
        print(f"Median word frequency: {median_frequency:.2f}")
        
        # Words appearing only once
        hapax_legomena = sum(1 for freq in freq_values if freq == 1)
        print(f"Words appearing only once (Hapax Legomena): {hapax_legomena:,} ({hapax_legomena/len(self.word_frequencies)*100:.1f}%)")
        
        # High frequency words
        high_freq_words = sum(1 for freq in freq_values if freq >= 100)
        print(f"Words appearing 100+ times: {high_freq_words:,} ({high_freq_words/len(self.word_frequencies)*100:.1f}%)")
        
        print("\nFrequency distribution buckets:")
        buckets = [1, 2, 5, 10, 25, 50, 100, 200, 500]
        for i, bucket in enumerate(buckets):
            if i == len(buckets) - 1:
                count = sum(1 for freq in freq_values if freq >= bucket)
                print(f"  {bucket}+ times: {count:,} words")
            else:
                next_bucket = buckets[i + 1]
                count = sum(1 for freq in freq_values if bucket <= freq < next_bucket)
                print(f"  {bucket}-{next_bucket-1} times: {count:,} words")

def main():
    """Main function to run the frequency analysis"""
    
    # Path to the tokenized dataset
    tokenized_file_path = "c:\\Users\\rudra\\OneDrive\\Desktop\\AI I53\\Sem V\\NLP\\Lab\\Lab 1\\tokenized_gujarati_sentences.json"
    
    print("Starting Frequency Distribution Analysis")
    print("="*60)
    
    # Initialize analyzer
    analyzer = FrequencyAnalyzer(tokenized_file_path)
    
    # Load and process data
    analyzer.load_and_process_data()
    
    # Perform analysis with multiple thresholds
    analyzer.analyze_with_multiple_thresholds()
    
    # Generate summary report
    analyzer.generate_summary_report()
    
    print("\n" + "="*60)
    print("ANALYSIS COMPLETE")
    print("="*60)
    print("\nGenerated files:")
    print("1. original_frequency_distribution.png")
    print("2. filtered_frequency_distribution_threshold_50.png") 
    print("3. filtered_frequency_distribution_threshold_100.png")
    print("4. filtered_frequency_distribution_threshold_200.png")

if __name__ == "__main__":
    main()
