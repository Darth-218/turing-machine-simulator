import pandas
import simulator, parser
import streamlit as st

st.title("Turing Machine Simulator")

placeholder = """// test test
"""

select_preset = st.button("Upload")
input_states = st.text_area("States/Definition", height=500, placeholder=placeholder)
input_string = st.text_input("Input String")
compile = st.button("Compile")

if compile == True:
    turing_machine = parser.Parser().parse(input_states)

    st.subheader("Machine Definition")

    st.markdown(rf"""
    $$
    M = (Q, \Sigma, \Gamma, \delta, q_0, \sqcup, F)
    $$

    - **$Q$** = {turing_machine.states}
    - **$\Sigma$** = {turing_machine.alphabet}
    - **$\Gamma$** = "Tape alphabet"
    - **$q_0$** = {turing_machine.start_state}
    - **$F$** = {turing_machine.final_states}
    """)

    st.subheader("Tape Transitions")

    transitions = simulator.simulate(turing_machine, input_string)

    for transition in transitions:
        transition[1][transition[0]] = "-" + transition[1][transition[0]] + "-"

        df = pandas.DataFrame([{
            "Head Position": transition[0],
            "Tape": "  ".join(transition[1]),
            "Current State": transition[2],
            "Next State": transition[3],
        }])

        st.dataframe(df, hide_index=True)

