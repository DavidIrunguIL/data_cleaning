import streamlit as st
from datetime import datetime as dt 

with st.container():
    st.subheader("🚗 VEHICLE PARTICULARS FORM")
    st.markdown("Please fill in Other Details:")

    with st.form("vehicle_identification_form"):
        col1, col2, col3 = st.columns(3)

        with col1:
            reg_date = st.text_input("Date of Registration", placeholder="e.g. KDA 123A", key="veh_reg")
            
            Logbook_Number = st.text_input("Logbook Number", placeholder="e.g. 123GHJ", key="Logbook_Number")

        with col2:
            Previous_Owner = st.text_input("Previous Owner", placeholder="e.g. Joe Doe", key="prev_owner")
            Service_History = st.text_input("Service History", placeholder="e.g. Corolla", key="veh_model")
            

        with col3:
            Comments = st.number_input("Year of Manufacture", min_value=1980, max_value=dt.now().year, step=1, key="veh_year")
            make = st.selectbox("Make (Manufacturer)", 
                                ["Select...", "Toyota", "Nissan", "Mazda", "Mitsubishi", "Honda", "Subaru", "Ford", "Mercedes", "BMW", "Volkswagen", "Other"],
                                key="veh_make")

        # --- Submit Button ---
        submitted = st.form_submit_button("Submit Vehicle Details")

    if submitted:
        if reg_date or Logbook_Number or Comments:
            st.success(f"✅ Submitted successfully!")
            st.write("### Summary of Entered Details")
            st.write({
                "Registration Number": reg_date,
                "Chassis Number": Previous_Owner,
                "Engine Number": Logbook_Number,
                "Make": make,
                "Model": Service_History,
                "Body Type": Comments,
            })
        else:
            st.warning("⚠️ Please fill all required fields before submitting.")
