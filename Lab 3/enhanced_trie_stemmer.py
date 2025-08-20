"""
Enhanced Trie Stemmer - Comparing Prefix and Suffix Tries for Stemming
Assignment: NLP Lab 3
Dataset: brown_nouns.txt (Brown Corpus Nouns)
"""

import collections
from typing import Dict, List, Tuple, Set
import time

class TrieNode:
    """Node for both prefix and suffix tries"""
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.frequency = 0
        self.words = []  # Store actual words ending at this node
        self.branch_count = 0  # Number of branches from this node

class PrefixTrie:
    """Standard prefix trie implementation"""
    def __init__(self):
        self.root = TrieNode()
        self.total_words = 0
    
    def insert(self, word: str, frequency: int = 1):
        """Insert a word into the prefix trie"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_end_of_word = True
        node.frequency += frequency
        if word not in node.words:
            node.words.append(word)
        self.total_words += frequency
    
    def calculate_branch_counts(self):
        """Calculate branching factor for each node"""
        def dfs(node):
            node.branch_count = len(node.children)
            for child in node.children.values():
                dfs(child)
        dfs(self.root)
    
    def find_stem_suffix(self, word: str) -> Tuple[str, str, float]:
        """Find stem and suffix based on maximum branching point"""
        node = self.root
        path = []
        max_branch_pos = 0
        max_branches = 0
        
        for i, char in enumerate(word):
            if char not in node.children:
                return word, "", 0.0  # Word not found
            
            node = node.children[char]
            path.append((char, node))
            
            # Find position with maximum branching
            if node.branch_count > max_branches:
                max_branches = node.branch_count
                max_branch_pos = i + 1
        
        if max_branch_pos == 0:
            return word, "", 0.0
        
        stem = word[:max_branch_pos]
        suffix = word[max_branch_pos:]
        
        # Calculate confidence based on branching factor
        confidence = min(max_branches / 10.0, 1.0)  # Normalize to 0-1
        
        return stem, suffix, confidence

class SuffixTrie:
    """Suffix trie implementation (words inserted in reverse)"""
    def __init__(self):
        self.root = TrieNode()
        self.total_words = 0
    
    def insert(self, word: str, frequency: int = 1):
        """Insert a word into the suffix trie (reversed)"""
        reversed_word = word[::-1]
        node = self.root
        for char in reversed_word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_end_of_word = True
        node.frequency += frequency
        if word not in node.words:
            node.words.append(word)
        self.total_words += frequency
    
    def calculate_branch_counts(self):
        """Calculate branching factor for each node"""
        def dfs(node):
            node.branch_count = len(node.children)
            for child in node.children.values():
                dfs(child)
        dfs(self.root)
    
    def find_stem_suffix(self, word: str) -> Tuple[str, str, float]:
        """Find stem and suffix based on maximum branching point in suffix trie"""
        reversed_word = word[::-1]
        node = self.root
        path = []
        max_branch_pos = 0
        max_branches = 0
        
        for i, char in enumerate(reversed_word):
            if char not in node.children:
                return word, "", 0.0  # Word not found
            
            node = node.children[char]
            path.append((char, node))
            
            # Find position with maximum branching
            if node.branch_count > max_branches:
                max_branches = node.branch_count
                max_branch_pos = i + 1
        
        if max_branch_pos == 0:
            return word, "", 0.0
        
        # Convert back to normal word positions
        suffix_length = max_branch_pos
        stem = word[:-suffix_length] if suffix_length < len(word) else ""
        suffix = word[-suffix_length:] if suffix_length > 0 else ""
        
        # Calculate confidence based on branching factor
        confidence = min(max_branches / 10.0, 1.0)  # Normalize to 0-1
        
        return stem, suffix, confidence

class TrieStemmerAnalyzer:
    """Main analyzer class to compare prefix and suffix tries"""
    
    def __init__(self):
        self.prefix_trie = PrefixTrie()
        self.suffix_trie = SuffixTrie()
        self.word_frequencies = collections.Counter()
    
    def load_dataset(self, filename: str):
        """Load the brown_nouns.txt dataset"""
        print(f"Loading dataset from {filename}...")
        start_time = time.time()
        
        with open(filename, 'r', encoding='utf-8') as file:
            words = []
            for line_num, line in enumerate(file, 1):
                word = line.strip().lower()
                if word and word.isalpha():  # Only alphabetic words
                    words.append(word)
                    self.word_frequencies[word] += 1
                
                if line_num % 50000 == 0:
                    print(f"Processed {line_num} lines...")
        
        print(f"Loaded {len(words)} total words, {len(self.word_frequencies)} unique words")
        print(f"Loading took {time.time() - start_time:.2f} seconds")
        
        return words
    
    def build_tries(self, words: List[str]):
        """Build both prefix and suffix tries"""
        print("Building prefix and suffix tries...")
        start_time = time.time()
        
        # Build tries with frequency information
        for word in set(words):  # Use unique words only
            frequency = self.word_frequencies[word]
            self.prefix_trie.insert(word, frequency)
            self.suffix_trie.insert(word, frequency)
        
        # Calculate branching factors
        self.prefix_trie.calculate_branch_counts()
        self.suffix_trie.calculate_branch_counts()
        
        print(f"Trie building took {time.time() - start_time:.2f} seconds")
    
    def analyze_stemming(self, sample_words: List[str] = None, max_analysis: int = 100):
        """Analyze stemming performance of both tries"""
        if sample_words is None:
            # Select diverse sample words for analysis
            sample_words = self.select_sample_words(max_analysis)
        
        prefix_results = []
        suffix_results = []
        
        print(f"\nAnalyzing stemming for {len(sample_words)} words...\n")
        print("=" * 80)
        print(f"{'Word':<15} {'Prefix Trie':<25} {'Suffix Trie':<25} {'Frequencies'}")
        print("=" * 80)
        
        for word in sample_words:
            # Prefix trie analysis
            p_stem, p_suffix, p_conf = self.prefix_trie.find_stem_suffix(word)
            prefix_results.append((word, p_stem, p_suffix, p_conf))
            
            # Suffix trie analysis
            s_stem, s_suffix, s_conf = self.suffix_trie.find_stem_suffix(word)
            suffix_results.append((word, s_stem, s_suffix, s_conf))
            
            # Format output
            freq = self.word_frequencies[word]
            prefix_result = f"{p_stem}+{p_suffix}" if p_suffix else p_stem
            suffix_result = f"{s_stem}+{s_suffix}" if s_suffix else s_stem
            
            print(f"{word:<15} {prefix_result:<25} {suffix_result:<25} {freq}")
        
        return prefix_results, suffix_results
    
    def select_sample_words(self, max_words: int) -> List[str]:
        """Select diverse sample words for analysis"""
        # Get words of different lengths and frequencies
        words_by_length = {}
        for word, freq in self.word_frequencies.most_common():
            length = len(word)
            if length not in words_by_length:
                words_by_length[length] = []
            if len(words_by_length[length]) < 10:  # Max 10 per length
                words_by_length[length].append(word)
        
        # Select sample ensuring diversity
        sample_words = []
        for length in sorted(words_by_length.keys()):
            sample_words.extend(words_by_length[length][:5])  # 5 per length
            if len(sample_words) >= max_words:
                break
        
        return sample_words[:max_words]
    
    def evaluate_performance(self, prefix_results: List, suffix_results: List):
        """Evaluate and compare performance of both approaches"""
        print("\n" + "=" * 80)
        print("PERFORMANCE EVALUATION")
        print("=" * 80)
        
        # Analyze prefix trie performance
        prefix_with_suffix = sum(1 for _, stem, suffix, _ in prefix_results if suffix)
        prefix_avg_confidence = sum(conf for _, _, _, conf in prefix_results) / len(prefix_results)
        
        # Analyze suffix trie performance
        suffix_with_suffix = sum(1 for _, stem, suffix, _ in suffix_results if suffix)
        suffix_avg_confidence = sum(conf for _, _, _, conf in suffix_results) / len(suffix_results)
        
        print(f"Prefix Trie:")
        print(f"  - Words with identified suffix: {prefix_with_suffix}/{len(prefix_results)} ({prefix_with_suffix/len(prefix_results)*100:.1f}%)")
        print(f"  - Average confidence: {prefix_avg_confidence:.3f}")
        
        print(f"\nSuffix Trie:")
        print(f"  - Words with identified suffix: {suffix_with_suffix}/{len(suffix_results)} ({suffix_with_suffix/len(suffix_results)*100:.1f}%)")
        print(f"  - Average confidence: {suffix_avg_confidence:.3f}")
        
        # Determine which performs better
        print(f"\nCOMPARISON:")
        if suffix_avg_confidence > prefix_avg_confidence:
            print("✓ Suffix Trie performs better for stemming")
            print("  Reason: Suffix trie directly captures morphological endings")
        else:
            print("✓ Prefix Trie performs better for stemming")
            print("  Reason: Prefix branching correlates well with morphological structure")
        
        # Analyze common patterns
        self.analyze_common_patterns(prefix_results, suffix_results)
    
    def analyze_common_patterns(self, prefix_results: List, suffix_results: List):
        """Analyze common stemming patterns"""
        print(f"\nCOMMON PATTERNS ANALYSIS:")
        print("-" * 40)
        
        # Collect suffixes from both approaches
        prefix_suffixes = collections.Counter()
        suffix_suffixes = collections.Counter()
        
        for _, stem, suffix, conf in prefix_results:
            if suffix and conf > 0.3:  # Only confident predictions
                prefix_suffixes[suffix] += 1
        
        for _, stem, suffix, conf in suffix_results:
            if suffix and conf > 0.3:  # Only confident predictions
                suffix_suffixes[suffix] += 1
        
        print("Most common suffixes identified by Prefix Trie:")
        for suffix, count in prefix_suffixes.most_common(10):
            print(f"  {suffix}: {count} words")
        
        print("\nMost common suffixes identified by Suffix Trie:")
        for suffix, count in suffix_suffixes.most_common(10):
            print(f"  {suffix}: {count} words")

def main():
    """Main execution function"""
    print("Enhanced Trie Stemmer - Brown Corpus Analysis")
    print("=" * 50)
    
    # Initialize analyzer
    analyzer = TrieStemmerAnalyzer()
    
    # Load dataset
    try:
        words = analyzer.load_dataset('brown_nouns.txt')
    except FileNotFoundError:
        print("Error: brown_nouns.txt not found in current directory")
        return
    
    # Build tries
    analyzer.build_tries(words)
    
    # Analyze stemming
    prefix_results, suffix_results = analyzer.analyze_stemming()
    
    # Evaluate performance
    analyzer.evaluate_performance(prefix_results, suffix_results)
    
    print(f"\nAnalysis complete! Processed {len(words)} total words from Brown Corpus.")

if __name__ == "__main__":
    main()
