import pandas
import simulator
import streamlit as st

placeholder = """// To define a Turing Machine:
name: machine_name
init: start_state
accept: accept_state_1, accept_state_2, ...

// Machine states:
current_state, current_symbol: next_state, written_symbol, direction
"""

st.title("Turing Machine Simulator")

uploaded = st.file_uploader("Upload a Turing Machine Definition", type=["txt"])

st.session_state["text"] = ""

if uploaded:
    st.session_state["text"] = uploaded.read().decode("utf-8")

input_states = st.text_area("Write Turing Machine Definition", height=500, placeholder=placeholder, value=st.session_state.get("text", ""))
input_string = st.text_input("Input String")
compile = st.button("Compile")

def prettify_transitions(transitions):
    df = pandas.DataFrame(transitions)
    df.columns = ["Current State", "Current Symbol", "Next State", "Written Symbol", "Direction"]
    return df


def check_error(error):
    if error:
        st.badge("Input Rejected.", color='red')
    else:
        st.badge("Input Accepted.", color='green')


def draw_def(turing_machine):
    st.markdown(rf"""
    $$
    M = (Q, \Sigma, \Gamma, \delta, q_0, \sqcup, F)
    $$

    - **$Q$** = {turing_machine.states}
    - **$\Gamma$** = {turing_machine.tape_alphabet}
    - **$q_0$** = {turing_machine.start_state}
    - **$F$** = {turing_machine.final_states}
    - **$\delta$** =
    """)

    st.dataframe(prettify_transitions(turing_machine.transitions), hide_index=True)


def tape_states(transitions, error, head_char="> "):
    tape_container = st.container(height=300)

    for position, tape, current, next in transitions:
        tape[position] = head_char + tape[position]

        meta = {
            "Current State": current,
            "Next State": next,
            "Head Position": position,
        }

        tape_dict = {f"{i}": symbol for i, symbol in enumerate(tape)}

        row = {**meta, **tape_dict}
        df = pandas.DataFrame([row])

        tape_container.dataframe(df, hide_index=True)

    if error:
        st.error(error)
        tape_container.badge("Halt.", color='red')
        return

    tape_container.badge("Halt.", color='green')


def main():
    import parser
    parser = parser.Parser()
    turing_machine = parser.parse(input_states)
    transitions, error = simulator.simulate(turing_machine, input_string)

    check_error(error)

    st.subheader("Machine Definition")
    draw_def(turing_machine)

    st.subheader("Tape Transitions")
    tape_states(transitions, error)


if compile == True:
    main()
