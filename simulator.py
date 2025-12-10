from tape import Tape
from turing_machine import TuringMachine


def build_table(tm: TuringMachine):

    table = {}
    for s, r, ns, w, d in tm.transitions:
        table[(s, r)] = (ns, w, d)
    return table


def simulate(tm: TuringMachine, input_string, max_steps=10000):

    tape = Tape(input_string)
    table = build_table(tm)

    current_state = tm.start_state
    final_states = tm.final_states

    transitions = []
    steps = 0

    while steps < max_steps:

        if current_state in final_states:
            break

        symbol = tape.read()
        transition = tm.get_transition(current_state, symbol)

        if transition is None:
            raise ValueError(
                f"No transition for state '{current_state}' and symbol '{symbol}'. Input rejected."
            )

        next_state, write_sym, direction = transition



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
