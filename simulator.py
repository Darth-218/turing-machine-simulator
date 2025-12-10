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

        if current_state in final_states:
            break

        symbol = tape.read()
        key = (current_state, symbol)

        if key not in table:

            raise ValueError(
                "No transition for state '{}' and symbol '{}'. Input rejected."
                .format(current_state, symbol)
            )

        next_state, write_sym, direction = table[key]

        pos, snapshot = tape.display_tape()
        transitions.append([pos, snapshot, current_state, next_state])

        tape.write(write_sym)

        if direction == "R":
            tape.move_right()
        elif direction == "L":
            tape.move_left()
        elif direction == "S":
            pass
        else:
            raise ValueError("Unknown head direction '{}'".format(direction))

        current_state = next_state
        steps += 1

    if steps >= max_steps:

        raise ValueError("Machine exceeded max steps without halting.")

    return transitions
