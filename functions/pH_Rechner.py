from datetime import datetime 
import pytz
import math
import streamlit as st

def calculate_ph(h_conc: float) -> float:
    """Berechnet den pH-Wert aus der H⁺-Konzentration.
    Erwartet einen positiven Wert, sonst wird eine Ausnahme geworfen."""
    if h_conc <= 0:
        raise ValueError("Die Konzentration muss größer als 0 sein.")
    return -math.log10(h_conc)

def ph_result(h_conc: float) -> dict:
    """Berechnet den pH‑Wert und gibt ein Dictionary zurück.
 
    Das Ergebnis enthält den Zeitstempel (Schweizer Zeit),
    die eingegebene Konzentration und den errechneten pH‑Wert.
    """
    ph_val = calculate_ph(h_conc)
    return {
        "timestamp": datetime.now(pytz.timezone("Europe/Zurich")),
        "h_concentration": h_conc,
        "ph": ph_val,
    }
 