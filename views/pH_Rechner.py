import streamlit as st
import math
import pandas as pd
from datetime import datetime
from utils.data_manager import DataManager  # --- NEW CODE: import data manager ---
 
from functions.pH_Rechner import calculate_ph
from functions.pH_Rechner import ph_result
 
def app() -> None:
    st.title("pH‑Rechner")
    st.write("Ermitteln des pH‑Werts aus der Wasserstoffionenkonzentration [H⁺].")
 
    h_input = st.number_input(
        "Konzentration [H⁺] (mol L⁻¹)",
        min_value=0.0,
        format="%.6g"
    )
 
    if st.button("Berechnen"):
        if h_input <= 0:
            st.error("Bitte geben Sie einen Wert größer als 0 ein.")
        else:
            try:
                ph_val = calculate_ph(h_input)
                st.success(f"pH = {ph_val:.3f}")
            except Exception as exc:
                st.error(str(exc))
if __name__ == "__main__":
    app()
 

# --- NEW CODE to update history in session state and display it ---
st.session_state['data_df'] = pd.concat([st.session_state['data_df'], pd.DataFrame([ph_val])])
        

# --- CODE UPDATE: save data to data manager ---
data_manager = DataManager()
data_manager.save_user_data(st.session_state['data_df'], 'data.csv')
# --- END OF CODE UPDATE ---

# --- NEW CODE to display the history table ---
st.dataframe(st.session_state['data_df'])