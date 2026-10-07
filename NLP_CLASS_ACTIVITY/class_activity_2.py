class EndingInAbFSA:
    def __init__(self):

        self.states = {'q0', 'q1', 'q2'}
        self.start_state = 'q0'
        self.accept_states = {'q2'}
        
        self.transitions = {
            'q0': {'a': 'q1', 'b': 'q0'},
            'q1': {'a': 'q1', 'b': 'q2'},
            'q2': {'a': 'q1', 'b': 'q0'}
        }

    def accepts(self, input_string):
        current_state = self.start_state
        
        for char in input_string:
            if char not in {'a', 'b'}:
                current_state = 'q0'
                continue
                
            current_state = self.transitions[current_state][char]
            
        return current_state in self.accept_states

fsa = EndingInAbFSA()
test_strings = ["ab", "aab", "bab", "bbaab", "aba", "b", "a", "abc", "abab"]

print("=== Finite State Automaton Tests (Ending in 'ab') ===")
for s in test_strings:
    result = fsa.accepts(s)
    print(f"String: '{s:7}' -> Accepted: {result}")