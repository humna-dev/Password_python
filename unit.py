import streamlit as st

# Page setup
st.set_page_config(page_title="Smart Converter", page_icon="🧠")

# Header and intro
st.title("🧠 Smart Unit Conversion")
st.markdown("#### Effortlessly switch between units with ease 🌐")
st.write("Hi there! 👋 Just pick what you want to convert, enter a value, and get instant results!")

# Category selection
category = st.selectbox("🔎 **Select Measurement Type**", [
    "Length", "Weight", "Time", "Temperature", "Area", "Volume", "Speed", "Pressure",
    "Energy", "Power", "Frequency", "Digital Storage", "Fuel Economy", "Plane Angle", "Data Transfer Rate"
])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
        elif unit == "Meters to Feet":
            return value * 3.28084
        elif unit == "Feet to Meters":
            return value / 3.28084
        elif unit == "Centimeters to Inches":
            return value * 2.54
        elif unit == "Inches to Centimeters":
            return value / 2.54
        elif unit == "Millimeters to Inches":
            return value * 25.4
        elif unit == "Inches to Millimeters":
            return value / 25.4
        elif unit == "Yards to Meters":
            return value * 0.9144
        elif unit == "Meters to Yards":
            return value / 0.9144
        elif unit == "Kilometers to Meters":
            return value * 1000
        elif unit == "Meters to Kilometers":
            return value / 1000
        elif unit == "Miles to Feet":
            return value * 5280
        elif unit == "Feet to Miles":
            return value / 5280
        elif unit == "Micrometers to Inches":
            return value * 0.0000393701
        elif unit == "Inches to Micrometers":
            return value / 0.0000393701
        elif unit == "Nanometers to Inches":
            return value * 0.0000000393701
        elif unit == "Inches to Nanometers":
            return value / 0.0000000393701
        
    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462
        elif unit == "Grams to Ounces":
            return value * 0.035274
        elif unit == "Ounces to Grams":
            return value / 0.035274
        elif unit == "Milligrams to Grains":
            return value * 15.4324
        elif unit == "Grains to Milligrams":
            return value / 15.4324
        elif unit == "Micrograms to Milligrams":
            return value / 1000
        elif unit == "Milligrams to Micrograms":
            return value * 1000
        
    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24
        
    elif category == "Temperature":
        if unit == "Celsius to Fahrenheit":
            return (value * 9/5) + 32
        elif unit == "Fahrenheit to Celsius":
            return (value - 32) * 5/9
        elif unit == "Celsius to Kelvin":
            return value + 273.15
        elif unit == "Kelvin to Celsius":
            return value - 273.15
        elif unit == "Fahrenheit to Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif unit == "Kelvin to Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        
    elif category == "Area":
        if unit == "Square Meters to Square Feet":
            return value * 10.7639
        elif unit == "Square Feet to Square Meters":
            return value / 10.7639
        elif unit == "Acres to Hectares":
            return value * 0.404686
        elif unit == "Hectares to Acres":
            return value / 0.404686
        elif unit == "Square Kilometers to Square Miles":
            return value * 0.386102
        elif unit == "Square Miles to Square Kilometers":
            return value / 0.386102
        elif unit == "Square Centimeters to Square Inches":
            return value * 0.155
        elif unit == "Square Inches to Square Centimeters": 
            return value / 0.155
        
    elif category == "Volume":
        if unit == "Liters to Gallons":
            return value * 0.264172
        elif unit == "Gallons to Liters":
            return value / 0.264172
        elif unit == "Milliliters to Fluid Ounces":
            return value * 0.033814
        elif unit == "Fluid Ounces to Milliliters":
            return value / 0.033814
        elif unit == "Cubic Meters to Cubic Feet":
            return value * 35.3147
        elif unit == "Cubic Feet to Cubic Meters":
            return value / 35.3147
        elif unit == "Cubic Meters to Liters":
            return value * 1000
        elif unit == "Liters to Cubic Meters":
            return value / 1000
        
    elif category == "Speed":
        if unit == "Kilometers per Hour to Miles per Hour":
            return value * 0.621371
        elif unit == "Miles per Hour to Kilometers per Hour":
            return value / 0.621371
        elif unit == "Meters per Second to Kilometers per Hour":
            return value * 3.6
        elif unit == "Kilometers per Hour to Meters per Second":
            return value / 3.6
        elif unit == "Feet per Second to Meters per Second":
            return value * 0.3048
        elif unit == "Meters per Second to Feet per Second":
            return value / 0.3048
        elif unit == "Knots to Miles per Hour":
            return value * 1.15078
        elif unit == "Miles per Hour to Knots":
            return value / 1.15078
        
    elif category == "Pressure":
        if unit == "Pascals to Atmospheres":
            return value / 101325
        elif unit == "Atmospheres to Pascals":
            return value * 101325
        elif unit == "Pascals to Bar":
            return value / 100000
        elif unit == "Bar to Pascals":
            return value * 100000
        elif unit == "Pascals to Torr":
            return value * 0.00750062
        elif unit == "Torr to Pascals":
            return value / 0.00750062
        elif unit == "Pascals to PSI":
            return value / 6894.76
        elif unit == "PSI to Pascals":
            return value * 6894.76
        
    elif category == "Energy":
        if unit == "Joules to Calories":
            return value / 4.184
        elif unit == "Calories to Joules":
            return value * 4.184
        elif unit == "Kilojoules to Calories":
            return value * 239.006
        elif unit == "Calories to Kilojoules":
            return value / 239.006
        elif unit == "Kilowatt-hours to Joules":
            return value * 3600000
        elif unit == "Joules to Kilowatt-hours":
            return value / 3600000
        
    elif category == "Power":
        if unit == "Watts to Horsepower":
            return value / 745.7
        elif unit == "Horsepower to Watts":
            return value * 745.7
        elif unit == "Watts to Kilowatts":
            return value / 1000
        elif unit == "Kilowatts to Watts":
            return value * 1000
        elif unit == "Horsepower to Kilowatts":
            return value * 0.7457
        elif unit == "Kilowatts to Horsepower":
            return value / 0.7457
        elif unit == "Megawatts to Watts":
            return value * 1e6
        elif unit == "Watts to Megawatts":
            return value / 1e6
        
    elif category == "Frequency":
        if unit == "Hertz to Kilohertz":
            return value / 1000
        elif unit == "Kilohertz to Hertz":
            return value * 1000
        elif unit == "Megahertz to Hertz":
            return value * 1e6
        elif unit == "Hertz to Megahertz":
            return value / 1e6
        elif unit == "Gigahertz to Hertz":
            return value * 1e9
        elif unit == "Hertz to Gigahertz":
            return value / 1e9
        
    elif category == "Digital Storage":
        if unit == "Bytes to Bits":
            return value * 8
        elif unit == "Bits to Bytes":
            return value / 8
        elif unit == "Kilobytes to Bytes":
            return value * 1024
        elif unit == "Bytes to Kilobytes":
            return value / 1024
        elif unit == "Kilobytes to Megabytes":
            return value / 1024
        elif unit == "Megabytes to Kilobytes":
            return value * 1024
        elif unit == "Gigabytes to Megabytes":
            return value * 1024
        elif unit == "Megabytes to Gigabytes":
            return value / 1024
        elif unit == "Terabytes to Gigabytes":
            return value * 1024
        elif unit == "Gigabytes to Terabytes":
            return value / 1024
            
    elif category == "Fuel Economy":
        if unit == "Miles per Gallon to Liters per 100km":
            return 235.215 / value
        elif unit == "Liters per 100km to Miles per Gallon":
            return 235.215 / value
        elif unit == "Kilometers per Liter to Miles per Gallon":
            return value * 2.35215
        elif unit == "Miles per Gallon to Kilometers per Liter":
            return value / 2.35215
        elif unit == "Liters per 100km to Kilometers per Liter":
            return 100 / value
        elif unit == "Kilometers per Liter to Liters per 100km":
            return 100 / value
        elif unit == "Miles per Gallon to Liters per 100km":
            return 235.215 / value
        elif unit == "Liters per 100km to Miles per Gallon":
            return 235.215 / value
        
    elif category == "Plane Angle":
        if unit == "Degrees to Radians":
            return value * (3.141592653589793 / 180)
        elif unit == "Radians to Degrees":
            return value * (180 / 3.141592653589793)
        elif unit == "Gradians to Degrees":
            return value * (9 / 10)
        elif unit == "Degrees to Gradians":
            return value * (10 / 9)
        elif unit == "Gradians to Radians":
            return value * (3.141592653589793 / 200)
        elif unit == "Radians to Gradians":
            return value * (200 / 3.141592653589793)
        elif unit == "Degrees to Turns":
            return value / 360
        elif unit == "Turns to Degrees":
            return value * 360
        
    elif category == "Data Transfer Rate":
        if unit == "Megabits per Second to Megabytes per Second":
            return value / 8
        elif unit == "Megabytes per Second to Megabits per Second":
            return value * 8
        elif unit == "Kilobits per Second to Kilobytes per Second":
            return value / 8
        elif unit == "Kilobytes per Second to Kilobits per Second":
            return value * 8
        elif unit == "Gigabits per Second to Gigabytes per Second":
            return value / 8
        elif unit == "Gigabytes per Second to Gigabits per Second":
            return value * 8
        elif unit == "Terabits per Second to Terabytes per Second":
            return value / 8
        

# Unit selection based on category
if category == "Length":
    unit = st.selectbox("📏 **Choose Unit Conversion**", ["Kilometers to Miles", "Miles to Kilometers", "Meters to Feet", "Feet to Meters", "Centimeters to Inches", "Inches to Centimeters", "Millimeters to Inches", "Inches to Millimeters", "Yards to Meters", "Meters to Yards", "Kilometers to Meters", "Meters to Kilometers", "Miles to Feet", "Feet to Miles", "Micrometers to Inches", "Inches to Micrometers", "Nanometers to Inches", "Inches to Nanometers"])
elif category == "Weight":
    unit = st.selectbox("⚖️ **Choose Unit Conversion**", ["Kilograms to Pounds", "Pounds to Kilograms", "Grams to Ounces", "Ounces to Grams", "Milligrams to Grains", "Grains to Milligrams", "Micrograms to Milligrams", "Milligrams to Micrograms"])
elif category == "Time":
    unit = st.selectbox("⏱️ **Choose Unit Conversion**", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"])
elif category == "Temperature":
    unit = st.selectbox("🌡️ **Choose Unit Conversion**", ["Celsius to Fahrenheit", "Fahrenheit to Celsius", "Celsius to Kelvin", "Kelvin to Celsius", "Fahrenheit to Kelvin", "Kelvin to Fahrenheit"])
elif category == "Area":
    unit = st.selectbox("📐 **Choose Unit Conversion**", ["Square Meters to Square Feet", "Square Feet to Square Meters", "Acres to Hectares", "Hectares to Acres", "Square Kilometers to Square Miles", "Square Miles to Square Kilometers", "Square Centimeters to Square Inches", "Square Inches to Square Centimeters"])
elif category == "Volume":
    unit = st.selectbox("💧 **Choose Unit Conversion**", ["Liters to Gallons", "Gallons to Liters", "Milliliters to Fluid Ounces", "Fluid Ounces to Milliliters", "Cubic Meters to Cubic Feet", "Cubic Feet to Cubic Meters", "Cubic Meters to Liters", "Liters to Cubic Meters"])
elif category == "Speed":
    unit = st.selectbox("🚗 **Choose Unit Conversion**", ["Kilometers per Hour to Miles per Hour", "Miles per Hour to Kilometers per Hour", "Meters per Second to Kilometers per Hour", "Kilometers per Hour to Meters per Second", "Feet per Second to Meters per Second", "Meters per Second to Feet per Second", "Knots to Miles per Hour", "Miles per Hour to Knots"])
elif category == "Pressure":
    unit = st.selectbox("💨 **Choose Unit Conversion**", ["Pascals to Atmospheres", "Atmospheres to Pascals", "Pascals to Bar", "Bar to Pascals", "Pascals to Torr", "Torr to Pascals", "Pascals to PSI", "PSI to Pascals"])
elif category == "Energy":
    unit = st.selectbox("⚡ **Choose Unit Conversion**", ["Joules to Calories", "Calories to Joules", "Kilojoules to Calories", "Calories to Kilojoules", "Kilowatt-hours to Joules", "Joules to Kilowatt-hours"])
elif category == "Power":
    unit = st.selectbox("🔋 **Choose Unit Conversion**", ["Watts to Horsepower", "Horsepower to Watts", "Watts to Kilowatts", "Kilowatts to Watts", "Horsepower to Kilowatts", "Kilowatts to Horsepower", "Megawatts to Watts", "Watts to Megawatts"])
elif category == "Frequency":
    unit = st.selectbox("🔊 **Choose Unit Conversion**", ["Hertz to Kilohertz", "Kilohertz to Hertz", "Megahertz to Hertz", "Hertz to Megahertz", "Gigahertz to Hertz", "Hertz to Gigahertz"])
elif category == "Digital Storage":
    unit = st.selectbox("💾 **Choose Unit Conversion**", ["Bytes to Bits", "Bits to Bytes", "Kilobytes to Bytes", "Bytes to Kilobytes", "Kilobytes to Megabytes", "Megabytes to Kilobytes", "Gigabytes to Megabytes", "Megabytes to Gigabytes", "Terabytes to Gigabytes", "Gigabytes to Terabytes"])
elif category == "Fuel Economy":
    unit = st.selectbox("⛽ **Choose Unit Conversion**", ["Miles per Gallon to Liters per 100km", "Liters per 100km to Miles per Gallon", "Kilometers per Liter to Miles per Gallon", "Miles per Gallon to Kilometers per Liter", "Liters per 100km to Kilometers per Liter", "Kilometers per Liter to Liters per 100km"])
elif category == "Plane Angle":
    unit = st.selectbox("🌀 **Choose Unit Conversion**", ["Degrees to Radians", "Radians to Degrees", "Gradians to Degrees", "Degrees to Gradians", "Gradians to Radians", "Radians to Gradians", "Degrees to Turns", "Turns to Degrees"])
elif category == "Data Transfer Rate":
    unit = st.selectbox("📡 **Choose Unit Conversion**", ["Megabits per Second to Megabytes per Second", "Megabytes per Second to Megabits per Second", "Kilobits per Second to Kilobytes per Second", "Kilobytes per Second to Kilobits per Second", "Gigabits per Second to Gigabytes per Second", "Gigabytes per Second to Gigabits per Second", "Terabits per Second to Terabytes per Second"])

# Input field
value = st.number_input("📥 **Input the value you wish to convert**", step=0.1)

# Convert button and result
if st.button("🚀 Run Conversion"):
    result = convert_units(category, value, unit)
    st.success(f"🎯 Result: {result:.2f}")
