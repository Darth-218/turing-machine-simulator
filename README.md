# Turing-machine-simulator

>This README is using the language $0^n1^n$ as an example.

## TM Definition

$$
M = (Q, \Sigma, \Gamma, \delta, q_{0}, H)
$$

```python
turing_machine = {
    "name": "zeros-equal-ones",
    "states": {"q_0", "q_1", "q_2", "q_3", "q_4", "q_5", "q_6"},
    "alphabet": {"0", "1"},
    "tape_alphabet": {"0", "1", "X", "Y", "_"},
    "transitions": [
        ["q_0", "0", "q_1", "X", "R"],
        ["q_0", "X", "q_0", "X", "R"],
        ["q_0", "Y", "q_0", "Y", "R"],
        ["q_0", "_", "q_5", "_", "R"],
        ["q_1", "0", "q_1", "0", "R"],
        ["q_1", "X", "q_1", "X", "R"],
        ["q_1", "Y", "q_1", "Y", "R"],
        ["q_1", "1", "q_2", "Y", "L"],
        ["q_1", "_", "q_6", "_", "R"],
        ["q_2", "X", "q_2", "X", "L"],
        ["q_2", "Y", "q_2", "Y", "L"],
        ["q_2", "1", "q_2", "1", "L"],
        ["q_2", "0", "q_0", "0", "R"],
        ["q_2", "_", "q_6", "_", "R"],
    ],
    "start_state": "q_0",
    "final_states": {"q_5", "q_6"}
}
```

## Tape Implementation.

For the input `0011`:
- Tape object is initialized with blanks preceeding and suceeding 
the input string, `["_", "0", "0", "1", "1", "_"]`.

### Tape Methods

- Move Right/Left.
- Current tape state (the current string inside the tape and the head position).

## Parser

- Input: A file/text.
- Output: TM definition.

### Process

Converts the input text/file into the machine's python definition.

### Input format

```txt
name: zeros-equal-ones
init: q_0
accept: q_5, q_6

q_0, 0: q_1, X, R
q_0, X: q_0, X, R
q_0, Y: q_0, Y, R
q_0, _: q_5, _, R

q_1, 0: q_1, 0, R
q_1, X: q_1, X, R
q_1, Y: q_1, Y, R
q_1, 1: q_2, Y, L
q_1, _: q_6, _, R

q_2, X: q_2, X, L
q_2, Y: q_2, Y, L
q_2, 1: q_2, 1, L
q_2, 0: q_0, 0, R
q_2, _: q_6, _, R
```

## Simulation Engine

- Input: TM definition.
- Output: List of transitions leading to the input string.

### Process

Applys the given transitions on the input string. Returns an error when the string is not valid.
