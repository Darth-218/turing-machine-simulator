from turing_machine import TuringMachine

class Parser:
    def parse(self, input_text):
        lines = input_text.strip().split('\n')

        tm = TuringMachine()

        for line in lines:
            line = line.strip()
            if not line:
                continue

            if line.startswith("name:"):
                tm.name = line.split(":", 1)[1].strip()

            elif line.startswith("init:"):
                start = line.split(":", 1)[1].strip()
                tm.start_state = start
                tm.add_state(start)

            elif line.startswith("accept:"):
                states = line.split(":", 1)[1].strip()
                finals = {s.strip() for s in states.split(",") if s.strip()}
                for s in finals:
                    tm.add_state(s)
                tm.final_states = finals

            elif ',' in line and ':' in line:
                left_part, right_part = line.split(':', 1)
                current_state, read_symbol = left_part.split(',')
                current_state = current_state.strip()
                read_symbol = read_symbol.strip()

                next_state, write_symbol, direction = (p.strip() for p in right_part.split(','))

                tm.add_state(current_state)
                tm.add_state(next_state)
                tm.add_tape_symbol(read_symbol)
                tm.add_tape_symbol(write_symbol)

                tm.add_transition(current_state, read_symbol, next_state, write_symbol, direction)

        return tm