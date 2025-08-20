#!/usr/bin/env python3
"""
Test script for frequency analysis
Tests the functionality with a smaller sample if the full dataset is not available
"""

import json
import os

def create_sample_data():
    """Create sample tokenized data for testing"""
    sample_data = [
        ["આ વીડિયો જુઓ આજથી બંધ"],
        [""],
        ["કોંગ્રેસ અધ્યક્ષ રાહુલ ગાંધી દ્વારા પ્રથમ પ્રતિક્રિયા આપવામાં આવી છે"],
        ["આ આંકડો માટે અને વજન ઘટાડવા માટે પ્રકાશનનો દિવસ વિતાવવો"],
        ["આ ઠેકાઓ પરથી લીમડી તેમજ ઝાલોદના બૂટલેગરો"],
        ["કેન્દ્રીય મંત્રી જ્યોતિરાદિત્ય સિંધિયાની જન આશિર્વાદ યાત્રા"],
        ["ઉત્તર પ્રદેશમાં લગભગ બાળ કેદીઓને મુક્ત કરવામાં આવશે"],
        ["આ આ આ કેટલીક વખત આ શબ્દ આવે છે"]
    ]
    return sample_data

def test_frequency_analysis():
    """Test the frequency analysis functions"""
    
    # Check if main tokenized file exists
    main_file = "c:\\Users\\rudra\\OneDrive\\Desktop\\AI I53\\Sem V\\NLP\\Lab\\Lab 1\\tokenized_gujarati_sentences.json"
    
    if os.path.exists(main_file):
        print("✓ Main tokenized file found!")
        print("✓ You can run the main analysis script.")
        
        # Test with first few lines
        try:
            with open(main_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
            
            print(f"✓ File loaded successfully with {len(data)} sentence groups")
            
            # Show sample data
            print("\nSample sentences from the dataset:")
            for i, sentence_group in enumerate(data[:3]):
                for sentence in sentence_group:
                    if sentence.strip():
                        print(f"  {i+1}. {sentence}")
                        break
            
        except Exception as e:
            print(f"✗ Error reading file: {e}")
    
    else:
        print("✗ Main tokenized file not found.")
        print("✓ Creating sample data for testing...")
        
        # Create sample file
        sample_data = create_sample_data()
        sample_file = "sample_tokenized_data.json"
        
        with open(sample_file, 'w', encoding='utf-8') as file:
            json.dump(sample_data, file, ensure_ascii=False, indent=2)
        
        print(f"✓ Sample file created: {sample_file}")
        print("✓ You can modify the script to use this sample file for testing")
    
    # Test basic functionality
    print("\n" + "="*50)
    print("Testing core functionality...")
    
    # Test manual frequency counting
    sample_words = ["આ", "અને", "આ", "કે", "આ", "અને", "માટે"]
    word_freq = {}
    
    for word in sample_words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    print("✓ Manual frequency counting works:")
    for word, freq in word_freq.items():
        print(f"  '{word}': {freq}")
    
    # Test manual sorting
    word_list = [(word, freq) for word, freq in word_freq.items()]
    
    # Manual bubble sort
    for i in range(len(word_list)):
        for j in range(i + 1, len(word_list)):
            if word_list[i][1] < word_list[j][1]:
                word_list[i], word_list[j] = word_list[j], word_list[i]
    
    print("✓ Manual sorting works:")
    for word, freq in word_list:
        print(f"  '{word}': {freq}")
    
    # Test matplotlib import
    try:
        import matplotlib.pyplot as plt
        print("✓ Matplotlib is available for plotting")
    except ImportError:
        print("✗ Matplotlib not available. Install with: pip install matplotlib")
    
    print("\n" + "="*50)
    print("Test completed!")

if __name__ == "__main__":
    test_frequency_analysis()
