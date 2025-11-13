import streamlit as st
import pandas as pd
from datetime import datetime as dt
from db.models import get_footprint_data_from_db


field_keys = {
    "veh_reg": "",
    "veh_make": "Select...",
    "veh_color": "",
    "veh_vin": "",
    "veh_model": "",
    "veh_year": dt.now().year,
    "veh_engine": "",
    "veh_body": "Select...",
    "veh_country": ""
}
for k, v in field_keys.items():
    if k not in st.session_state:
        st.session_state[k] = v

st.subheader("🚗 VEHICLE SPECIFICATIONS FORM")
col1, col2 = st.columns(2)
reg_input = col1.text_input("Enter Reg No to Review or Add", placeholder="e.g. KDA 123A", key="search_reg")
chassis_number = col2.text_input("Enter Chasis No to Review or Add", placeholder="e.g. ABC1234567890", key="search_chassis")
# Review button 
if st.button("🔍 Review Existing Details"):
    reg = st.session_state.get("search_reg", "").strip()
    if not reg:
        st.warning("Please enter a registration number first.")
    else:
        df = get_footprint_data_from_db(reg)
        if df.empty:
            st.info(f"No existing records found for {reg}.")
        else:
            st.success(f"Existing record found for {reg}")
            st.session_state["vehicle_df"] = df
            rec = df.iloc[0].to_dict()
            # Map DB columns to session_state keys (use .get to avoid KeyError)
            st.session_state["veh_reg"] = rec.get("RegistrationNo", reg)
            st.session_state["veh_make"] = rec.get("VehicleMake", "Select...")
            st.session_state["veh_color"] = rec.get("Color", "")
            st.session_state["veh_vin"] = rec.get("ChassisNo", "")
            st.session_state["veh_model"] = rec.get("VehicleModel", "")
            st.session_state["veh_year"] = int(rec.get("YearOfManufacture", dt.now().year))
            st.session_state["veh_engine"] = rec.get("EngineNo", "")
            st.session_state["veh_body"] = rec.get("BodyType", "Select...")
            st.session_state["veh_country"] = rec.get("Country", "")
            st.session_state["log_serial_no"] = rec.get("LogBookNo", "missing")
            st.session_state["engine_cc"] = rec.get("CubicCapacity", "missing")
            st.session_state["seating_capacity"] = rec.get("CarryingCapacity", "missing")
            st.session_state["fuel_type"] = rec.get("FuelType", "Select...")
            st.session_state["use_type"] = rec.get("VehiclePurpose", 2)

            

# --- The form reads initial values from st.session_state via keys ---


with st.form("vehicle_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        reg_number = st.text_input("Registration Number",
                                   key="veh_reg")  # initial value comes from session_state

        make_options = ["Select...", "TOYOTA", "Nissan", "Mazda", "Mitsubishi", "Honda", "Subaru", "Ford", "Mercedes", "BMW", "Volkswagen", "Other"]
        # selectbox with key reads/writes st.session_state["veh_make"]
        make = st.selectbox("Make (Manufacturer)", make_options, index=make_options.index(st.session_state.get("veh_make", "Select...")) if st.session_state.get("veh_make") in make_options else 0, key="veh_make")

        color = st.text_input("Color", key="veh_color")

        number_of_axles = st.number_input("Number of Axles", key="num_axles")

        country_origin = st.text_input("Country of Origin", key="veh_country")

    with col2:
        chassis_number = st.text_input("Chassis Number (VIN)", key="veh_vin")

        model = st.text_input("Model", key="veh_model")

        year = st.number_input("Year of Manufacture",
                               value=int(st.session_state.get("veh_year", dt.now().year)),
                               key="veh_year")
        
        engine_capacity = st.text_input("Engine Capacity (CC)", key="engine_cc")

        body_serial_number = st.text_input("Body Serial Number (if applicable)", key="body_serial")

    with col3:
        engine_number = st.text_input("Engine Number", key="veh_engine")

        body_type_options = ["Select...", "Saloon", "Pickup", "Truck", "Bus", "SUV", "Van", "Motorcycle", "Other"]
        body = st.selectbox("Body Type", body_type_options,
                            index=body_type_options.index(st.session_state.get("veh_body", "Select...")) if st.session_state.get("veh_body") in body_type_options else 0,
                            key="veh_body")

        fuel_type = st.selectbox("Fuel Type",
                                     ["Select...", "Petrol", "Diesel", "Electric", "Hybrid", "Other"],
                                     index=["Select...", "Petrol", "Diesel", "Electric", "Hybrid", "Other"].index(st.session_state.get("fuel_type", "Select..."))
                                     if st.session_state.get("fuel_type") in ["Select...", "Petrol", "Diesel", "Electric", "Hybrid", "Other"] else 0,
                                     key="fuel_type")
        
        sitting_capacity = st.text_input("Seating Capacity", key="seating_capacity")

    submitted = st.form_submit_button("✅ Submit Vehicle Details")


if submitted:
    # read final values from session_state (widgets already updated it)
    final = {k: st.session_state[k] for k in field_keys}
    # simple validation example
    if final["veh_reg"] and final["veh_vin"] and final["veh_make"] != "Select...":
        st.success(f"Vehicle details for {final['veh_reg']} submitted.")
        st.json(final)

        pd.DataFrame([final]).to_excel("vehicle_particulars_submissions.xlsx", index=False)
    else:
        st.warning("Please fill required fields: Registration Number, Chassis Number and Make.")


with st.form("ownership_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        owner = st.text_input("Name of Registered Owner",
                                   key="reg_owner")  

        # selectbox with key reads/writes st.session_state["veh_make"]
        owner_id = st.text_input("ID / Passport / Company PIN", key="owner_id")
        owner_addres = st.text_input("Physical Address / Postal Address", key="owner_address")

    with col2:
        owner_contact = st.text_input("Phone Number / Email", key="owner_contact")

        reg_date = st.date_input("Date of Registration",
                               key="reg_date")
        
        veh_use_type = st.text_input("Vehicle Purpose", key="use_type")

    with col3:
        name_prev_owner = st.text_input("Name of Previous Owner", key="name_prev_own")

        date_prev_transfer = st.date_input("Date of Previous Transfer",
                               key="date_prev_transfer")

        number_prev_owner = st.number_input("Number of Previous Owners", min_value=0, max_value=20, step=1, key="num_prev_owners")


    submitted_ownership = st.form_submit_button("✅ Submit Ownership Details")




