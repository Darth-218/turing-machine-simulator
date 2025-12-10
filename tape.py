class Tape:
    def __init__(self, input_string):
        self.blank = "_"
        self.tape = [self.blank] + list(input_string) + [self.blank]
        self.current_position = 1

        def read(self):
            return self.tape[self.current_position]
        
        def write(self, symbol):
            self.tape[self.current_position] = symbol

        def move_right(self):
            self.current_position += 1
            if self.current_position >= len(self.tape):
                self.tape.append(self.blank)

        def move_left(self):
            if self.current_position == 0:
                self.tape.insert(0, self.blank)

            else:
                self.current_position -= 1

        def display_tape(self):
            return self.current_position, self.tape.copy()