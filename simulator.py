from tape import Tape


def build_table(tm):
    table = {}
    for s, r, ns, w, d in tm["transitions"]:
        table[(s, r)] = (ns, w, d)
    return table


def simulate(tm, input_string, max_steps=10000):
    tape = Tape(input_string)
    table = build_table(tm)

    current_state = tm["start_state"]
    final_states = tm["final_states"]

    transitions = []
    steps = 0

    while steps < max_steps:
        symbol = tape.read()
        key = (current_state, symbol)

        if key not in table:
            raise ValueError("Invalid string.")

        next_state, write_sym, direction = table[key]

        pos, snapshot = tape.display_tape()
        transitions.append([pos, snapshot, current_state, next_state])

        tape.write(write_sym)

        if direction == "R":
            tape.move_right()
        else:
            tape.move_left()

        current_state = next_state
        steps += 1

        if current_state in final_states:
            break

    if steps >= max_steps:
        raise ValueError("Machine exceeded max steps.")

    return transitions
