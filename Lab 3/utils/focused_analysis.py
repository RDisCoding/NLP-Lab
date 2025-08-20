"""
Focused Stemming Analysis - Showing Clear Examples
This script demonstrates specific stemming examples as requested
"""

import collections
from enhanced_trie_stemmer import TrieStemmerAnalyzer

def run_focused_analysis():
    """Run focused analysis with clear examples"""
    print("Focused Stemming Analysis - Brown Corpus")
    print("=" * 50)
    
    # Initialize analyzer
    analyzer = TrieStemmerAnalyzer()
    
    # Load dataset
    words = analyzer.load_dataset('brown_nouns.txt')
    analyzer.build_tries(words)
    
    # Select specific interesting words for analysis
    test_words = [
        'goes', 'kites', 'books', 'running', 'teacher', 'happiness',
        'children', 'development', 'organization', 'responsibilities',
        'cats', 'dogs', 'houses', 'boxes', 'studies', 'countries',
        'walking', 'talking', 'working', 'reading', 'writing',
        'quickly', 'slowly', 'carefully', 'beautiful', 'wonderful'
    ]
    
    # Filter to only words that exist in our dataset
    available_words = [word for word in test_words if word in analyzer.word_frequencies]
    
    if not available_words:
        # If none of our test words exist, use some from the dataset
        available_words = list(analyzer.word_frequencies.keys())[:25]
    
    print(f"\nAnalyzing {len(available_words)} sample words:\n")
    
    # Analyze with both tries
    prefix_results, suffix_results = analyzer.analyze_stemming(available_words)
    
    print("\n" + "=" * 70)
    print("DETAILED STEMMING COMPARISON")
    print("=" * 70)
    print(f"{'Word':<15} {'Prefix Result':<20} {'Suffix Result':<20} {'Freq'}")
    print("-" * 70)
    
    better_prefix = 0
    better_suffix = 0
    
    for i, word in enumerate(available_words):
        p_word, p_stem, p_suffix, p_conf = prefix_results[i]
        s_word, s_stem, s_suffix, s_conf = suffix_results[i]
        
        freq = analyzer.word_frequencies[word]
        
        # Format results
        prefix_result = f"{p_stem}+{p_suffix}" if p_suffix else p_stem
        suffix_result = f"{s_stem}+{s_suffix}" if s_suffix else s_stem
        
        # Determine which is better for this word
        marker = ""
        if s_conf > p_conf and s_suffix:
            marker = " ← Better"
            better_suffix += 1
        elif p_conf > s_conf and p_suffix:
            marker = " ← Better"  
            better_prefix += 1
        
        print(f"{word:<15} {prefix_result:<20} {suffix_result:<20} {freq}")
    
    # Show some clear examples in the requested format
    print("\n" + "=" * 70)
    print("CLEAR STEMMING EXAMPLES (as requested format)")
    print("=" * 70)
    
    clear_examples = []
    for i, word in enumerate(available_words):
        s_word, s_stem, s_suffix, s_conf = suffix_results[i]
        
        if s_suffix and len(s_suffix) > 0 and len(s_stem) > 2 and s_conf > 0.5:
            clear_examples.append((word, s_stem, s_suffix))
    
    # Sort by suffix for better readability
    clear_examples.sort(key=lambda x: x[2])
    
    for word, stem, suffix in clear_examples[:20]:  # Show top 20
        print(f"{word}={stem}+{suffix}")
    
    print(f"\nSummary:")
    print(f"- Suffix Trie identified meaningful suffixes in {better_suffix} cases")
    print(f"- Prefix Trie performed better in {better_prefix} cases")
    print(f"- Total examples shown: {len(clear_examples)}")

if __name__ == "__main__":
    run_focused_analysis()
