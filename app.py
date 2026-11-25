import streamlit as st

st.header("Marv Thomas Shalom B. Cuarenta")
st.write("Welcome to my Streamlit app!")

import streamlit as st
import math

# Page Configuration
st.set_page_config(
    page_title="Mechanical Engineering App",
    page_icon="⚙️",
    layout="wide"
)

# Header
st.title("⚙️ Marv Thomas Shalom B. Cuarenta")
st.subheader("Mechanical Engineering Application")
st.write("Welcome to my Mechanical Engineering Dashboard!")

st.divider()

# Sidebar Navigation
menu = st.sidebar.selectbox(
    "Select Engineering Tool",
    [
        "Home",
        "Mechanical Engineering",
        "Engineering Calculators",
        "Materials and Properties",
        "About Me"
    ]
)

# HOME
if menu == "Home":
    st.header("Welcome!")
    st.write("""
    This application showcases different concepts and calculations
    related to Mechanical Engineering.
    """)
    
    st.info("Explore the engineering tools using the sidebar.")

    st.subheader("Mechanical Engineering Fields")

    col1, col2, col3 = st.columns(3)

    col1.metric("Field 1", "Thermodynamics")
    col2.metric("Field 2", "Fluid Mechanics")
    col3.metric("Field 3", "Machine Design")

# MECHANICAL ENGINEERING
elif menu == "Mechanical Engineering":
    st.header("⚙️ Mechanical Engineering")
    
    st.write("Mechanical Engineering involves the design, analysis, and manufacturing of mechanical systems.")

    st.subheader("Major Engineering Subjects")

    st.markdown("""
    - Thermodynamics
    - Fluid Mechanics
    - Heat Transfer
    - Machine Design
    - Mechanics of Materials
    - Manufacturing Processes
    - Engineering Mechanics
    - Power Plant Engineering
    """)

# ENGINEERING CALCULATORS
elif menu == "Engineering Calculators":
    st.header("🧮 Engineering Calculators")

    calculator = st.selectbox(
        "Choose Calculator",
        ["Force Calculator", "Power Calculator", "Pressure Calculator"]
    )

    if calculator == "Force Calculator":
        st.subheader("Newton's Second Law")

        mass = st.number_input("Enter Mass (kg)", min_value=0.0)
        acceleration = st.number_input("Enter Acceleration (m/s²)", min_value=0.0)

        if st.button("Calculate Force"):
            force = mass * acceleration
            st.success(f"Force = {force:.2f} Newtons (N)")

    elif calculator == "Power Calculator":
        st.subheader("Mechanical Power")

        work = st.number_input("Enter Work (Joules)", min_value=0.0)
        time = st.number_input("Enter Time (seconds)", min_value=0.0)

        if st.button("Calculate Power"):
            if time > 0:
                power = work / time
                st.success(f"Power = {power:.2f} Watts (W)")
            else:
                st.error("Time must be greater than zero.")

    elif calculator == "Pressure Calculator":
        st.subheader("Pressure Formula")

        force = st.number_input("Enter Force (N)", min_value=0.0)
        area = st.number_input("Enter Area (m²)", min_value=0.0)

        if st.button("Calculate Pressure"):
            if area > 0:
                pressure = force / area
                st.success(f"Pressure = {pressure:.2f} Pascals (Pa)")
            else:
                st.error("Area must be greater than zero.")

# MATERIALS AND PROPERTIES
elif menu == "Materials and Properties":
    st.header("🔩 Engineering Materials")

    material = st.selectbox(
        "Select Material",
        ["Steel", "Aluminum", "Copper"]
    )

    properties = {
        "Steel": {
            "Density": "7850 kg/m³",
            "Young's Modulus": "200 GPa"
        },
        "Aluminum": {
            "Density": "2700 kg/m³",
            "Young's Modulus": "69 GPa"
        },
        "Copper": {
            "Density": "8960 kg/m³",
            "Young's Modulus": "110 GPa"
        }
    }

    st.write("### Material Properties")
    st.write(f"**Density:** {properties[material]['Density']}")
    st.write(f"**Young's Modulus:** {properties[material]['Young's Modulus']}")

# ABOUT ME
elif menu == "About Me":
    st.header("About the Developer")

    st.write("**Name:** Marv Thomas Shalom B. Cuarenta")
    st.write("**Course:** Mechanical Engineering")

    st.write("""
    I am interested in mechanical systems, engineering design,
    machine development, and engineering calculations.
    """)

    st.success("Thank you for visiting my Mechanical Engineering Application!")

st.divider()
st.caption("© 2026 Marv Thomas Shalom B. Cuarenta | Mechanical Engineering Application")