import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config("Universal Converter 🌍", layout="wide")

# --- STYLING ---
st.markdown(
    """
    <style>
    .big-title {
        text-align: center;
        font-size: 3em;
        font-weight: 600;
        color: #4CAF50;
    }
    .subtitle {
        text-align: center;
        font-size: 1.2em;
        color: gray;
        margin-bottom: 30px;
    }
    </style>
    """, unsafe_allow_html=True
)

# --- HEADER ---
st.markdown("<div class='big-title'>🌍 Universal Converter</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Simple, Fast & Accurate - Convert between units effortlessly</div>", unsafe_allow_html=True)
st.divider()

# --- FUNCTION ---
def convert(value, from_u, to_u, category):
    if category == "Length":
        table = {
            ("Meters", "Feet"): value * 3.28084,
            ("Feet", "Meters"): value * 0.3048,
            ("Kilometers", "Miles"): value * 0.621371,
            ("Miles", "Kilometers"): value * 1.60934
        }
        return table.get((from_u, to_u), value)
    
    elif category == "Weight":
        table = {
            ("Kilograms", "Pounds"): value * 2.20462,
            ("Pounds", "Kilograms"): value * 0.453592,
            ("Grams", "Ounces"): value * 0.035274,
            ("Ounces", "Grams"): value * 28.3495
        }
        return table.get((from_u, to_u), value)
    
    elif category == "Temperature":
        if from_u == to_u:
            return value
        elif from_u == "Celsius" and to_u == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_u == "Fahrenheit" and to_u == "Celsius":
            return (value - 32) * 5/9
    return value

# --- SIDEBAR CONTROLS ---
st.sidebar.header("🔧 Settings")
unit_group = st.sidebar.radio("Select Category", ["Length", "Weight", "Temperature"])

options = {
    "Length": ["Meters", "Feet", "Kilometers", "Miles"],
    "Weight": ["Kilograms", "Pounds", "Grams", "Ounces"],
    "Temperature": ["Celsius", "Fahrenheit"]
}

units = options[unit_group]

from_col, to_col = st.columns(2)
with from_col:
    from_unit = st.selectbox("From Unit", units)
with to_col:
    to_unit = st.selectbox("To Unit", units)

value = st.number_input(f"Enter {from_unit} value", step=0.01)

# --- RESULT DISPLAY ---
st.markdown("### 🎯 Conversion Result")

if from_unit == to_unit:
    st.warning("Please choose different units for conversion.")
elif value == 0:
    st.info("Enter a value above zero to convert.")
else:
    result = convert(value, from_unit, to_unit, unit_group)
    st.success(f"{value} {from_unit} = **{round(result, 3)} {to_unit}**")

# --- FOOTER ---
st.divider()
st.caption("Made with ❤️ using Streamlit | Supports common Length, Weight, and Temperature conversions.")
