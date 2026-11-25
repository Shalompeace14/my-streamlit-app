import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Mechanical Engineering App", page_icon="⚙️", layout="wide")

# ---------------------------------------------------------------
# DATA
# ---------------------------------------------------------------
materials = pd.DataFrame(
    {
        "Material": ["Steel", "Aluminum", "Copper", "Titanium"],
        "Density (kg/m3)": [7850, 2700, 8960, 4500],
        "Young's Modulus (GPa)": [200, 69, 110, 116],
        "Yield Strength (MPa)": [250, 275, 70, 880],
    }
).set_index("Material")

# ---------------------------------------------------------------
# HEADER (required by the activity: full name as main header)
# ---------------------------------------------------------------
st.header("Marv Thomas Shalom B. Cuarenta")
st.caption("Mechanical Engineering Application")

menu = st.sidebar.radio(
    "Menu",
    ["Home", "Material Properties", "Stress-Strain Curve", "Beam Deflection", "About Me"],
)

# ---------------------------------------------------------------
# HOME
# ---------------------------------------------------------------
if menu == "Home":
    st.subheader("Welcome!")
    st.write("Use the menu on the left to explore the tools in this app.")

    col1, col2, col3 = st.columns(3)
    col1.metric("Materials in database", len(materials))
    col2.metric("Strongest (yield)", materials["Yield Strength (MPa)"].idxmax())
    col3.metric("Lightest", materials["Density (kg/m3)"].idxmin())

    st.write("### Material database")
    st.dataframe(materials, use_container_width=True)

# ---------------------------------------------------------------
# MATERIAL PROPERTIES (bar charts)
# ---------------------------------------------------------------
elif menu == "Material Properties":
    st.subheader("Material Properties")

    choice = st.selectbox("Select a material", materials.index)
    row = materials.loc[choice]

    c1, c2, c3 = st.columns(3)
    c1.metric("Density", str(row["Density (kg/m3)"]) + " kg/m3")
    c2.metric("Young's Modulus", str(row["Young's Modulus (GPa)"]) + " GPa")
    c3.metric("Yield Strength", str(row["Yield Strength (MPa)"]) + " MPa")

    st.write("### Compare all materials")
    prop = st.selectbox("Property to compare", materials.columns)
    st.bar_chart(materials[prop])

# ---------------------------------------------------------------
# STRESS-STRAIN CURVE (line chart)
# ---------------------------------------------------------------
elif menu == "Stress-Strain Curve":
    st.subheader("Stress-Strain Curve (simplified model)")
    st.write(
        "Elastic region follows Hooke's law (stress = E x strain). "
        "After yielding, a small linear hardening slope is used."
    )

    selected = st.multiselect(
        "Materials to plot", list(materials.index), default=["Steel", "Aluminum"]
    )
    max_strain = st.slider("Maximum strain", 0.005, 0.05, 0.02, step=0.005)

    strain = np.linspace(0, max_strain, 200)
    curves = pd.DataFrame(index=strain)

    for name in selected:
        E = materials.loc[name, "Young's Modulus (GPa)"] * 1000  # MPa
        sy = materials.loc[name, "Yield Strength (MPa)"]
        eps_y = sy / E
        hardening = 0.02 * E
        stress = np.where(strain <= eps_y, E * strain, sy + hardening * (strain - eps_y))
        curves[name] = stress

    if selected:
        st.line_chart(curves)
        st.caption("X-axis: strain (mm/mm)   |   Y-axis: stress (MPa)")
    else:
        st.info("Pick at least one material to see the chart.")

# ---------------------------------------------------------------
# BEAM DEFLECTION (calculator + chart)
# ---------------------------------------------------------------
elif menu == "Beam Deflection":
    st.subheader("Simply Supported Beam - Center Point Load")

    material = st.selectbox("Beam material", materials.index)
    left, right = st.columns(2)
    with left:
        L = st.number_input("Beam length (m)", min_value=0.5, value=2.0, step=0.5)
        P = st.number_input("Load at center (N)", min_value=1.0, value=1000.0, step=100.0)
    with right:
        b = st.number_input("Width b (mm)", min_value=5.0, value=50.0, step=5.0)
        h = st.number_input("Height h (mm)", min_value=5.0, value=100.0, step=5.0)

    E = materials.loc[material, "Young's Modulus (GPa)"] * 1e9  # Pa
    I = (b / 1000) * (h / 1000) ** 3 / 12  # m^4
    x = np.linspace(0, L, 100)

    # Deflection formula (valid for x <= L/2, mirrored for the other half)
    xs = np.where(x <= L / 2, x, L - x)
    y_mm = (P * xs * (3 * L**2 - 4 * xs**2) / (48 * E * I)) * 1000

    max_defl = P * L**3 / (48 * E * I) * 1000
    max_moment = P * L / 4
    max_stress = max_moment * (h / 2000) / I / 1e6  # MPa

    m1, m2, m3 = st.columns(3)
    m1.metric("Max deflection", str(round(max_defl, 3)) + " mm")
    m2.metric("Max bending moment", str(round(max_moment, 1)) + " N-m")
    m3.metric("Max bending stress", str(round(max_stress, 1)) + " MPa")

    yield_strength = materials.loc[material, "Yield Strength (MPa)"]
    if max_stress < yield_strength:
        st.success("Safe: bending stress is below the yield strength (" + str(yield_strength) + " MPa).")
    else:
        st.error("Unsafe: bending stress exceeds the yield strength (" + str(yield_strength) + " MPa).")

    st.write("### Deflection along the beam")
    chart_data = pd.DataFrame({"Deflection (mm)": y_mm}, index=np.round(x, 3))
    st.area_chart(chart_data)
    st.caption("X-axis: position along the beam (m)   |   Y-axis: deflection (mm, downward)")

# ---------------------------------------------------------------
# ABOUT ME
# ---------------------------------------------------------------
elif menu == "About Me":
    st.subheader("About the Developer")
    st.write("**Name:** Marv Thomas Shalom B. Cuarenta")
    st.write("**Course:** Mechanical Engineering")
    st.write(
        "I am interested in mechanical systems, machine development, and engineering software."
    )
    st.success("Thank you for visiting my Mechanical Engineering Application!")

st.divider()
st.caption("(c) 2026 Marv Thomas Shalom B. Cuarenta | Mechanical Engineering Application")