import streamlit as st
from datetime import datetime as dt

with st.container():
    st.subheader("🚗 VEHICLE PARTICULARS FORM")
    st.markdown("Please fill in the vehicle identification details below:")

    with st.form("vehicle_identification_form"):
        col1, col2, col3 = st.columns(3)

        with col1:
            reg_number = st.text_input("Registration Number", placeholder="e.g. KDA 123A", key="veh_reg")
            make = st.selectbox("Make (Manufacturer)", 
                                ["Select...", "Toyota", "Nissan", "Mazda", "Mitsubishi", "Honda", "Subaru", "Ford", "Mercedes", "BMW", "Volkswagen", "Other"],
                                key="veh_make")
            color = st.text_input("Color", placeholder="e.g. White", key="veh_color")

        with col2:
            chassis_number = st.text_input("Chassis Number (VIN)", placeholder="e.g. JHMCM56557C404453", key="veh_vin")
            model = st.text_input("Model", placeholder="e.g. Corolla", key="veh_model")
            year = st.number_input("Year of Manufacture", min_value=1980, max_value=dt.now().year, step=1, key="veh_year")

        with col3:
            engine_number = st.text_input("Engine Number", placeholder="e.g. ENG123456789", key="veh_engine")
            body_type = st.selectbox("Body Type", 
                                     ["Select...", "Saloon", "Pickup", "Truck", "Bus", "SUV", "Van", "Motorcycle", "Other"],
                                     key="veh_body")
            country = st.selectbox("Country of Origin", 
                                   ["Select...", "Japan", "Kenya", "Germany", "UK", "South Africa", "USA", "China", "India", "Other"],
                                   key="veh_country")

        # --- Submit Button ---
        submitted = st.form_submit_button("Submit Vehicle Details")

    if submitted:
        if reg_number and chassis_number and make != "Select...":
            st.success(f"✅ Vehicle details for **{reg_number}** submitted successfully!")
            st.write("### Summary of Entered Details")
            st.write({
                "Registration Number": reg_number,
                "Chassis Number": chassis_number,
                "Engine Number": engine_number,
                "Make": make,
                "Model": model,
                "Body Type": body_type,
                "Color": color,
                "Year of Manufacture": year,
                "Country of Origin": country
            })
        else:
            st.warning("⚠️ Please fill all required fields before submitting.")
