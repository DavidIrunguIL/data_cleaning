import streamlit as st
from datetime import datetime as dt

with st.container():
    st.subheader("🚗 VEHICLE PARTICULARS FORM")
    st.markdown("Please fill in the vehicle identification details below:")

    with st.form("vehicle_identification_form"):
        col1, col2, col3 = st.columns(3)

        with col1:
            Gear =  st.selectbox("Transamission Type", 
                                ["Select...", "Automatic", "Manual","Others",],
                                key="transamission")
            Fuel_Type = st.selectbox("Fuel_Type", 
                                ["Select...", "Petrol", "Diesel", "Hybrid", "Electric",],
                                key="Fuel_Type")
            engine_capacity = st.text_input("Engine Capacity (cc)", placeholder="e.g. 1500", key="engine_capacity")

        with col2:
            Seating_Capacity = st.text_input("Seating Capacity", placeholder="e.g. 5", key="seating_cap")
            Weight = st.text_input("Gross Vehicle Weight (kg)", placeholder="e.g. 1200", key="Weight")
            Odometer  = st.number_input("Odometer Reading (km)", min_value=10, step=1, key="Odometer")

        with col3:
            Condition = st.selectbox("Condition", 
                                ["Select...", "New" , "Used" , "Damaged" , "Salvaged"],
                                key="Condition")
            body_type = st.selectbox("Body Type", 
                                     ["Select...", "Saloon", "Pickup", "Truck", "Bus", "SUV", "Van", "Motorcycle", "Other"],
                                     key="veh_body")
            country = st.selectbox("Country of Origin", 
                                   ["Select...", "Japan", "Kenya", "Germany", "UK", "South Africa", "USA", "China", "India", "Other"],
                                   key="veh_country")

        # --- Submit Button ---
        submitted = st.form_submit_button("Submit Vehicle Specifications")

    
    col1, col2 = st.columns(2)

    with col1:
            
        if submitted:
            if Gear and Fuel_Type and Condition != "Select...":
                st.success(f"✅ Vehicle Specifics submitted successfully!")
                st.write("### Summary of Entered Details")
                st.write({
                    "Registration Number": Gear,
                    "Chassis Number": Fuel_Type,
                    "Engine Number": engine_capacity,
                    "Make": Seating_Capacity,
                    "Model": Weight,
                    "Body Type": body_type,
                    "Country of Origin": country
                })
            else:
                st.warning("⚠️ Please fill all required fields before submitting.")

        
    with col2:
            
        if submitted:
            if Gear and Fuel_Type and Condition != "Select...":
                st.success(f"✅ Vehicle Specifics submitted successfully!")
                st.write("### Summary of Entered Details")
                st.write({
                    "Registration Number": Gear,
                    "Chassis Number": Fuel_Type,
                    "Engine Number": engine_capacity,
                    "Make": Seating_Capacity,
                    "Model": Weight,
                    "Body Type": body_type,
                    "Country of Origin": country
                })
            else:
                st.warning("⚠️ Please fill all required fields before submitting.")

