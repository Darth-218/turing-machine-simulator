import pandas
import streamlit as st

st.title("Turing Machine Simulator")

placeholder = """// test test
"""

select_preset = st.button("Upload")
input_states = st.text_area("States/Definition", height=500, placeholder=placeholder)
input_string = st.text_input("Input String")
compile = st.button("Compile")

transitions = [
    [1, ["_","0","0","1","1","_"], "q_0", "q_1"],
    [2, ["_","X","0","1","1","_"], "q_1", "q_1"],
    [3, ["_","X","0","1","1","_"], "q_1", "q_2"],
    [2, ["_","X","0","Y","1","_"], "q_2", "q_2"],
    [1, ["_","X","0","Y","1","_"], "q_2", "q_0"],
    [2, ["_","X","0","Y","1","_"], "q_0", "q_1"],
    [3, ["_","X","X","Y","1","_"], "q_1", "q_1"],
    [4, ["_","X","X","Y","1","_"], "q_1", "q_2"],
    [3, ["_","X","X","Y","Y","_"], "q_2", "q_2"],
    [2, ["_","X","X","Y","Y","_"], "q_2", "q_2"],
    [1, ["_","X","X","Y","Y","_"], "q_2", "q_0"],
    [2, ["_","X","X","Y","Y","_"], "q_0", "q_0"],
    [3, ["_","X","X","Y","Y","_"], "q_0", "q_0"],
    [4, ["_","X","X","Y","Y","_"], "q_0", "q_0"],
    [5, ["_","X","X","Y","Y","_"], "q_0", "q_5"],
   ]

# if compile == True:
if True:
    st.subheader("Tape Transitions")

    for transition in transitions:
        transition[1][transition[0]] = "-" + transition[1][transition[0]] + "-"

        df = pandas.DataFrame([{
            "Head Position": transition[0],
            "Tape": "  ".join(transition[1]),
            "Current State": transition[2],
            "Next State": transition[3],
        }])

        st.dataframe(df, hide_index=True)

    st.subheader("Machine Definition")

