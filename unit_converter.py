import streamlit as st

st.title("⚙️ Unit Converter")
st.caption("Smart Conversions at Your Fingertips!")



option = st.selectbox("Choose a conversion type:", [
    "Length", "Weight", "Temperature", "Time", "Liquid Measurement", "Energy", "Data Capacity"
])


if option == "Length":
    value = st.number_input("Enter value:")
    from_unit = st.selectbox("Convert from:", ["kilometers", "meters"])
    to_unit = st.selectbox("Convert to:", ["meters", "kilometers"])
    if st.button("Convert"):
        if from_unit == to_unit:
            converted = value
        elif from_unit == "meters" and to_unit == "kilometers":
            converted = value / 1000
        elif from_unit == "kilometers" and to_unit == "meters":
            converted = value * 1000
        st.write(f"{value} {from_unit} = {converted} {to_unit}")


elif option == "Weight":
    value = st.number_input("Enter value:")
    from_unit = st.selectbox("Convert from:", ["kilograms", "grams"])
    to_unit = st.selectbox("Convert to:", ["grams", "kilograms"])
    if st.button("Convert"):
        if from_unit == to_unit:
            converted = value
        elif from_unit == "grams" and to_unit == "kilograms":
            converted = value / 1000
        elif from_unit == "kilograms" and to_unit == "grams":
            converted = value * 1000
        st.write(f"{value} {from_unit} = {converted} {to_unit}")


elif option == "Temperature":
    value = st.number_input("Enter temperature:")
    from_unit = st.selectbox("Convert from:", ["Fahrenheit", "Celsius", "Kelvin"])
    to_unit = st.selectbox("Convert to:", ["Celsius", "Fahrenheit", "Kelvin"])
    if st.button("Convert"):
        if from_unit == to_unit:
            converted = value
        elif from_unit == "Celsius":
            converted = (value * 9/5) + 32 if to_unit == "Fahrenheit" else value + 273.15
        elif from_unit == "Fahrenheit":
            converted = (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            converted = value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32
        st.write(f"{value}°{from_unit} = {converted:.2f}°{to_unit}")


elif option == "Time":
    value = st.number_input("Enter time value:")
    from_unit = st.selectbox("Convert from:", ["seconds", "minutes", "hours", "days", "weeks", "months", "years"])
    to_unit = st.selectbox("Convert to:", ["minutes", "seconds", "hours", "days", "weeks", "months", "years"])

    time_factors = {
        "seconds": 1,
        "minutes": 60,
        "hours": 3600,
        "days": 86400,
        "weeks": 604800,
        "months": 2629746,
        "years": 31556952
    }

    if st.button("Convert"):
        if from_unit == to_unit:
            converted = value
        else:
            seconds = value * time_factors[from_unit]
            converted = seconds / time_factors[to_unit]
        st.write(f"{value} {from_unit} = {converted:.4f} {to_unit}")



elif option == "Liquid Measurement":
    value = st.number_input("Enter value:")
    from_unit = st.selectbox("Convert from:", ["Milliliters", "Liters", "Gallons", "Cups"])
    to_unit = st.selectbox("Convert to:", ["Liters", "Milliliters", "Gallons", "Cups"])

    conversions = {
        "Liters": {"Milliliters": 1000, "Gallons": 0.264172, "Cups": 4.22675},
        "Milliliters": {"Liters": 0.001, "Gallons": 0.000264172, "Cups": 0.00422675},
        "Gallons": {"Liters": 3.78541, "Milliliters": 3785.41, "Cups": 16},
        "Cups": {"Liters": 0.236588, "Milliliters": 236.588, "Gallons": 0.0625}
    }

    if st.button("Convert"):
        if from_unit == to_unit:
            converted = value
        elif to_unit in conversions[from_unit]:
            converted = value * conversions[from_unit][to_unit]
        else:
            st.error(f"Conversion from {from_unit} to {to_unit} not supported.")
            converted = None

        if converted is not None:
            st.write(f"{value} {from_unit} = {converted:.4f} {to_unit}")


elif option == "Energy":
    value = st.number_input("Enter energy value:")
    from_unit = st.selectbox("Convert from:", ["Joules", "Kilojoules", "Calories", "Kilocalories", "Watt-hours"])
    to_unit = st.selectbox("Convert to:", ["Joules", "Kilojoules", "Calories", "Kilocalories", "Watt-hours"])

    energy_factors = {
        "Joules": 1,
        "Kilojoules": 1000,
        "Calories": 4.184,
        "Kilocalories": 4184,
        "Watt-hours": 3600
    }

    if st.button("Convert"):
        if from_unit == to_unit:
            converted = value
        else:
            joules = value * energy_factors[from_unit]
            converted = joules / energy_factors[to_unit]
        st.write(f"{value} {from_unit} = {converted:.4f} {to_unit}")



elif option == "Data Capacity":
    value = st.number_input("Enter data size:")
    from_unit = st.selectbox("Convert from:", ["Bits", "Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes"])
    to_unit = st.selectbox("Convert to:", ["Bits", "Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes"])

    data_factors = {
        "Bits": 1,
        "Bytes": 8,
        "Kilobytes": 8 * 1024,
        "Megabytes": 8 * 1024**2,
        "Gigabytes": 8 * 1024**3,
        "Terabytes": 8 * 1024**4
    }

    if st.button("Convert"):
        if from_unit == to_unit:
            converted = value
        else:
            bits = value * data_factors[from_unit]
            converted = bits / data_factors[to_unit]
        st.write(f"{value} {from_unit} = {converted:.4f} {to_unit}")




        

