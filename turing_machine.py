class TuringMachine:
    def __init__(self):
        self._name = ""
        self._states = set()
        self._alphabet = set()
        self._tape_alphabet = set()
        self._transitions = []
        self._start_state = ""
        self._final_states = set()
    
    @property
    def name(self):
        """Get the machine name"""
        return self._name
    
    @property
    def states(self):
        """Get the set of states"""
        return self._states
    
    @property
    def alphabet(self):
        """Get the input alphabet"""
        return self._alphabet
    
    @property
    def tape_alphabet(self):
        """Get the tape alphabet"""
        return self._tape_alphabet
    
    @property
    def transitions(self):
        """Get the list of transitions"""
        return self._transitions
    
    @property
    def start_state(self):
        """Get the start state"""
        return self._start_state
    
    @property
    def final_states(self):
        """Get the set of final states"""
        return self._final_states
    
    @name.setter
    def name(self, value):
        """Set the machine name"""
        self._name = str(value)
    
    @states.setter
    def states(self, value):
        """Set the states"""
        if not isinstance(value, set):
            raise TypeError("states must be a set")
        self._states = value
    
    @alphabet.setter
    def alphabet(self, value):
        """Set the input alphabet"""
        if not isinstance(value, set):
            raise TypeError("alphabet must be a set")
        self._alphabet = value
    
    @tape_alphabet.setter
    def tape_alphabet(self, value):
        """Set the tape alphabet"""
        if not isinstance(value, set):
            raise TypeError("tape_alphabet must be a set")
        self._tape_alphabet = value
    
    @transitions.setter
    def transitions(self, value):
        """Set the transitions"""
        if not isinstance(value, list):
            raise TypeError("transitions must be a list")
        self._transitions = value
    
    @start_state.setter
    def start_state(self, value):
        """Set the start state"""
        self._start_state = str(value)
    
    @final_states.setter
    def final_states(self, value):
        """Set the final states"""
        if not isinstance(value, set):
            raise TypeError("final_states must be a set")
        self._final_states = value
    
    # Methods for adding individual items
    def add_state(self, state):
        """Add a single state to the machine"""
        self._states.add(str(state))
    
    def add_alphabet_symbol(self, symbol):
        """Add a symbol to the input alphabet"""
        self._alphabet.add(str(symbol))
    
    def add_tape_symbol(self, symbol):
        """Add a symbol to the tape alphabet"""
        self._tape_alphabet.add(str(symbol))
    
    def add_transition(self, current_state, read_symbol, next_state, write_symbol, direction):
        """Add a single transition to the machine"""
        self._transitions.append([
            str(current_state), 
            str(read_symbol), 
            str(next_state), 
            str(write_symbol), 
            str(direction).upper()
        ])
    
    def add_final_state(self, state):
        """Add a state to the set of final states"""
        self._final_states.add(str(state))
    
    def get_transition(self, state, symbol):
        """Get the transition for a given state and symbol, or None if not found"""
        for transition in self._transitions:
            if transition[0] == state and transition[1] == symbol:
                return transition[2:]  # Returns [next_state, write_symbol, direction]
        return None
    
    def is_final_state(self, state):
        """Check if a state is a final/accepting state"""
        return state in self._final_states
    
    def clear(self):
        """Clear all attributes of the Turing Machine"""
        self._name = ""
        self._states.clear()
        self._alphabet.clear()
        self._tape_alphabet.clear()
        self._transitions.clear()
        self._start_state = ""
        self._final_states.clear()