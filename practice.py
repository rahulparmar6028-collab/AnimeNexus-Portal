import streamlit as st

st.title("Streamlit Mastery Lab 🧪")

# 1. Using Columns (Side-by-side)
col1, col2 = st.columns(2)

with col1:
    st.header("User Input")
    # A slider for numbers
    user_level = st.slider("Select your Confidence Level:", 0, 100, 50)
    # A toggle switch
    is_ready = st.toggle("Ready for the next task?")

with col2:
    st.header("App Response")
    if is_ready:
        st.success(f"Confidence is at {user_level}%! Let's go!")
    else:
        st.warning("Take your time, Rahul.")

# 2. Using Tabs (Organization)
tab1, tab2 = st.tabs(["Secret Info", "Data View"])

with tab1:
    st.write("This is a hidden tab for internal notes.")
    # This creates a "click to reveal" box
    with st.expander("Click to see the secret key"):
        st.code("INTERN_SECRET_2024")

with tab2:
    # This creates a nice table
    st.table({"Skill": ["Python", "Streamlit", "GenAI"], "Level": ["Solid", "Learning", "Ready"]})