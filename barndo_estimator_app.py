import streamlit as st

st.set_page_config(page_title="Barndo Cost Estimator", layout="centered")

st.title("🏗️ Barndo Cost Estimator")

st.markdown("""
Enter your project values below.  
Only the input fields (C2–C10) can be modified.  
Results for C13, C14, and C15 will update automatically.
""")

# --- Inputs (C2–C10) ---
st.header("Input Values (C2–C10)")

c2 = st.number_input("C2", value=0.0, step=0.01)
c3 = st.number_input("C3", value=0.0, step=0.01)
c4 = st.number_input("C4", value=0.0, step=0.01)
c5 = st.number_input("C5", value=0.0, step=0.01)
c6 = st.number_input("C6", value=0.0, step=0.01)
c7 = st.number_input("C7", value=0.0, step=0.01)
c8 = st.number_input("C8", value=0.0, step=0.01)
c9 = st.number_input("C9", value=0.0, step=0.01)
c10 = st.number_input("C10", value=0.0, step=0.01)

# --- D21–D29 inputs ---
st.header("Additional Data (D21–D29)")
st.markdown("_Used to calculate C15_")
d_values = []
for i in range(21, 30):
    d_val = st.number_input(f"D{i}", value=0.0, step=0.01)
    d_values.append(d_val)

# --- Calculations ---
c13 = c2 * c3
c14 = c13 + c4
c15 = sum(d_values) * 6 * 1000

# --- Results display ---
st.header("Results")
col1, col2 = st.columns(2)
with col1:
    st.metric("C13", f"{c13:,.2f}")
    st.metric("C14", f"{c14:,.2f}")
    st.metric("C15", f"{c15:,.2f}")

st.success("Results updated automatically based on your inputs.")
