import graphviz
from q2 import MorphologicalFST

class FSTVisualizer:
    def __init__(self):
        self.fst = MorphologicalFST()
        
    def create_fst_diagram(self):
        """Create a graphviz diagram representing the morphological FST"""
        dot = graphviz.Digraph(comment='Morphological FST for English Plurals')
        dot.attr(rankdir='LR')
        dot.attr('node', shape='circle')
        
        # Add states
        dot.node('START', 'START', shape='circle')
        dot.node('ROOT', 'ROOT', shape='circle')
        dot.node('S_END', 'S_END', shape='circle')
        dot.node('Z_END', 'Z_END', shape='circle')
        dot.node('X_END', 'X_END', shape='circle')
        dot.node('CH_END', 'CH_END', shape='circle')
        dot.node('SH_END', 'SH_END', shape='circle')
        dot.node('Y_END', 'Y_END', shape='circle')
        dot.node('ACCEPT', 'ACCEPT', shape='doublecircle')
        dot.node('REJECT', 'REJECT', shape='circle')
        
        # Add transitions representing morphological rules
        
        # From START to ROOT (any alphabetic input)
        dot.edge('START', 'ROOT', 'α/α\n(any letter)')
        
        # From ROOT to various ending states based on morphological patterns
        dot.edge('ROOT', 'S_END', 's/+PL\n(ends with s)')
        dot.edge('ROOT', 'Z_END', 'z/+PL\n(ends with z)')
        dot.edge('ROOT', 'X_END', 'x/+PL\n(ends with x)')
        dot.edge('ROOT', 'CH_END', 'ch/+PL\n(ends with ch)')
        dot.edge('ROOT', 'SH_END', 'sh/+PL\n(ends with sh)')
        dot.edge('ROOT', 'Y_END', 'y/ies\n(y→ies rule)')
        
        # From ending states to ACCEPT
        dot.edge('S_END', 'ACCEPT', 'es/ε\n(add es)')
        dot.edge('Z_END', 'ACCEPT', 'es/ε\n(add es)')
        dot.edge('X_END', 'ACCEPT', 'es/ε\n(add es)')
        dot.edge('CH_END', 'ACCEPT', 'es/ε\n(add es)')
        dot.edge('SH_END', 'ACCEPT', 'es/ε\n(add es)')
        dot.edge('Y_END', 'ACCEPT', 'ies/ε\n(y→ies)')
        
        # Direct path for regular plurals
        dot.edge('ROOT', 'ACCEPT', 's/+PL\n(regular plural)')
        
        # Irregular forms (special transitions)
        dot.edge('START', 'ACCEPT', 'irregular/+PL\n(children, feet, etc.)')
        
        # Singular forms
        dot.edge('ROOT', 'ACCEPT', 'ε/+SG\n(singular)')
        
        # Error transitions to REJECT
        dot.edge('START', 'REJECT', 'invalid/ε\n(invalid input)')
        dot.edge('ROOT', 'REJECT', 'invalid/ε\n(invalid pattern)')
        
        return dot
    
    def create_simplified_fst_diagram(self):
        """Create a simplified FST diagram focusing on main morphological rules"""
        dot = graphviz.Digraph(comment='Simplified Morphological FST')
        dot.attr(rankdir='LR')
        dot.attr('node', shape='circle')
        
        # States
        dot.node('q0', 'START', shape='circle')
        dot.node('q1', 'WORD', shape='circle')
        dot.node('q2', 'S_STEM', shape='circle')
        dot.node('q3', 'Y_STEM', shape='circle')
        dot.node('q4', 'IRREGULAR', shape='circle')
        dot.node('q5', 'ACCEPT', shape='doublecircle')
        
        # Main transitions
        dot.edge('q0', 'q1', 'letter/letter')
        dot.edge('q1', 'q1', 'letter/letter')
        
        # Plural formation rules
        dot.edge('q1', 'q2', 's,x,z,ch,sh/stem')
        dot.edge('q2', 'q5', 'es/+N+PL')
        
        dot.edge('q1', 'q3', 'consonant+y/stem')
        dot.edge('q3', 'q5', 'ies/+N+PL')
        
        dot.edge('q1', 'q5', 's/+N+PL\n(regular)')
        dot.edge('q1', 'q5', 'ε/+N+SG\n(singular)')
        
        # Irregular plurals
        dot.edge('q0', 'q4', 'irregular_word/stem')
        dot.edge('q4', 'q5', 'ε/+N+PL')
        
        return dot
    
    def generate_visualization(self, filename_prefix="MorphologicalFST"):
        """Generate both detailed and simplified FST visualizations"""
        
        # Generate detailed FST
        detailed_fst = self.create_fst_diagram()
        detailed_fst.render(f'Lab2/{filename_prefix}_detailed', format='png', cleanup=True)
        
        # Generate simplified FST
        simplified_fst = self.create_simplified_fst_diagram()
        simplified_fst.render(f'Lab2/{filename_prefix}_simplified', format='png', cleanup=True)
        
        print(f"FST diagrams generated:")
        print(f"- {filename_prefix}_detailed.png")
        print(f"- {filename_prefix}_simplified.png")

def main():
    visualizer = FSTVisualizer()
    
    # Test some words first
    fst = MorphologicalFST()
    test_words = ['cats', 'foxes', 'tries', 'children', 'book']
    
    print("Testing FST analysis:")
    for word in test_words:
        analysis = fst.analyze_word(word)
        print(analysis)
    
    print("\nGenerating FST visualizations...")
    visualizer.generate_visualization("MorphologicalFST")

if __name__ == "__main__":
    main()
