import pandas
import simulator, parser
import streamlit as st

placeholder = """// test test
"""

def prettify_transitions(transitions):
    df = pandas.DataFrame(transitions)
    df.columns = ["Current State", "Current Symbol", "Next State", "Written Symbol", "Direction"]
    return df


st.title("Turing Machine Simulator")

uploaded = st.file_uploader("Upload a Turing Machine Definition", type=["txt"])

st.session_state["text"] = ""

if uploaded:
    st.session_state["text"] = uploaded.read().decode("utf-8")


input_states = st.text_area("Write Turing Machine Definition", height=500, placeholder=placeholder, value=st.session_state.get("text", ""))
input_string = st.text_input("Input String")
compile = st.button("Compile")

if compile == True:
    parser = parser.Parser()
    turing_machine = parser.parse(input_states)

    st.subheader("Machine Definition")

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

    st.subheader("Tape Transitions")

    transitions = simulator.simulate(turing_machine, input_string)

    tape_container = st.container(height=300)

    for transition in transitions:
        transition[1][transition[0]] = "-" + transition[1][transition[0]] + "-"

        df = pandas.DataFrame([{
            "Head Position": transition[0],
            "Tape": " | ".join(transition[1]),
            "Current State": transition[2],
            "Next State": transition[3],
        }])

        tape_container.dataframe(df, hide_index=True)

