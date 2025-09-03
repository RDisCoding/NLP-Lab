import graphviz
from q2 import MorphologicalFST

class EnglishMorphologyFST:
    def __init__(self):
        self.fst = MorphologicalFST()
        
    def create_english_morphology_fst(self):
        """Create FST diagram for English morphological analysis similar to DFA1 style"""
        dot = graphviz.Digraph(comment='English Morphological FST')
        dot.attr(rankdir='LR', size='12,8')
        dot.attr('node', shape='circle', fontsize='10')
        dot.attr('edge', fontsize='9')
        
        # Define states matching the original FST
        dot.node('q0', 'START', shape='circle', style='bold')
        dot.node('q1', 'READING', shape='circle')
        dot.node('q2', 'S_ENDING', shape='circle')
        dot.node('q3', 'ES_NEEDED', shape='circle')
        dot.node('q4', 'Y_ENDING', shape='circle')
        dot.node('q5', 'IRREGULAR', shape='circle')
        dot.node('q6', 'ACCEPT', shape='doublecircle', style='bold')
        dot.node('q7', 'REJECT', shape='circle', style='filled', fillcolor='lightgray')
        
        # Transitions for word reading
        dot.edge('q0', 'q1', 'α (letter)')
        dot.edge('q1', 'q1', 'α (continue reading)')
        
        # Regular plural with 's'
        dot.edge('q1', 'q2', 'word ending')
        dot.edge('q2', 'q6', 's → +N+PL\\n(cats, dogs)')
        
        # Plural requiring 'es' (s, x, z, ch, sh endings)
        dot.edge('q1', 'q3', 's|x|z|ch|sh ending')
        dot.edge('q3', 'q6', 'es → +N+PL\\n(foxes, watches)')
        
        # Y to ies transformation
        dot.edge('q1', 'q4', 'consonant+y ending')
        dot.edge('q4', 'q6', 'y→ies → +N+PL\\n(tries, flies)')
        
        # Irregular plurals
        dot.edge('q0', 'q5', 'irregular pattern')
        dot.edge('q5', 'q6', 'children→child+N+PL\\nfeet→foot+N+PL')
        
        # Singular words
        dot.edge('q2', 'q6', 'no suffix → +N+SG\\n(cat, book)')
        
        # Error handling
        dot.edge('q0', 'q7', 'invalid input')
        dot.edge('q1', 'q7', 'invalid pattern')
        
        return dot
    
    def view(self, filename="EnglishMorphologyFST"):
        """Generate visualization similar to DFA1's view method"""
        dot = self.create_english_morphology_fst()
        
        # Save the .gv file
        dot.save(f'{filename}.gv')
        
        # Render to PNG
        dot.render(filename, format='png', cleanup=True)
        
        print(f"FST visualization saved as {filename}.gv and {filename}.png")

def main():
    # Test the FST functionality
    fst_analyzer = MorphologicalFST()
    
    print("English Morphological FST Analysis Examples:")
    print("=" * 50)
    
    test_words = [
        'cat', 'cats', 'dog', 'dogs', 'fox', 'foxes',
        'watch', 'watches', 'try', 'tries', 'fly', 'flies',
        'child', 'children', 'foot', 'feet', 'mouse', 'mice',
        'book', 'books', 'glass', 'glasses'
    ]
    
    for word in test_words:
        analysis = fst_analyzer.analyze_word(word)
        print(analysis)
    
    print("\n" + "=" * 50)
    print("Generating FST Visualization...")
    
    # Create and save the FST visualization
    fst_visualizer = EnglishMorphologyFST()
    fst_visualizer.view("Lab2/EnglishMorphologyFST")

if __name__ == "__main__":
    main()
