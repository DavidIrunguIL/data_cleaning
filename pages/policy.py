import streamlit as st
from datetime import datetime as dt
import pandas as pd
# import vehciles_details as details_page


st.subheader("🚗 EXISTING POLICY DETAILS")

# # --- Ensure a shared record exists ---
# if "vehicle_record" not in st.session_state:
#     st.session_state["vehicle_record"] = {}

# record = st.session_state["vehicle_record"]
# --- Use defaults from existing data (if available) ---
#record from previous page
existing_df = st.session_state.get("vehicle_df", {})
if isinstance(existing_df, dict):
    existing_df = pd.DataFrame()
record = existing_df.iloc[0].to_dict() if not existing_df.empty else {}


#  '', 'RenewalPremium', 'RateApplied', 'Brokercode',
#        '', '', 'EffectiveDate', '',
#        'NumberOfMonths', 'ClassCode', 'ClassDesc', 'SchemeName', 'NCDDiscount',
#        'DepartCode', 'DepartmentName', 'ValuationSent', 'ValuationDone',
#        'LetterRef', 'DateofBirth', 'SittingCapacity', 'ItemKey', 'Brokerno',
#        'schemecode', 'Schemedesc', 'AgencyType', 'Branchcode', 'BranchDesc',
#        'OriginalAttachmentdate', 'PolicyLossRatio', 'InsuredPIN', 'Financier',
#        'OsClaims', 'WrittenPremium', 'PaidClaims'


basicprem = record.get("BasicPremium", "")
rate_ = record.get("RateApplied", "")
broker_name = record.get("BrokerName", "")
renew_date = record.get("RenewalDate", "")
eff_date = record.get("EffectiveDate", "")
expr_date = record.get("ExpiryDate", "")
class_desc = record.get("ClassDesc", "")
claims_paid = record.get("PaidClaims", "")
department = record.get("DepartmentName", "")

with st.form("cover_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        basicprem = st.text_input("Basic Premium", value=basicprem, key="basic_premium")

        rate_ = st.text_input("Rate Applied", value=rate_, key="rate_applied")
        broker_name = st.text_input("Broker Name", value=broker_name, key="broker_name")
    

    with col2:
        renew_date = st.date_input("Renewal Date",
                                   value=pd.to_datetime(renew_date) if renew_date else dt.now(),
                                   key="renewal_date")
        
        eff_date = st.date_input("Effective Date",
                                 value=pd.to_datetime(eff_date) if eff_date else dt.now(),
                                 key="effective_date")
        expr_date = st.date_input("Expiry Date",
                                  value=pd.to_datetime(expr_date) if expr_date else dt.now(),
                                  key="expiry_date")
        
    with col3:
        class_desc = st.text_input("Class Description", value=class_desc, key="class_desc") 
        claims_paid = st.text_input("Claims Paid", value=claims_paid, key="claims_paid")
        department = st.text_input("Department Name", value=department, key="department_name")
        
        submitted = st.form_submit_button("✅ Submit Vehicle Specifications")
        
if submitted:
    # Save values back into shared session state
    st.session_state["vehicle_record"] = {
        "basic_premium": basicprem,
        "rate_applied": rate_,
        "broker_name": broker_name,
        "renewal_date": str(renew_date),
        "effective_date": str(eff_date),
        "expiry_date": str(expr_date),
        "class_desc": class_desc,
        "claims_paid": claims_paid,
        "department_name": department
    }

    st.success("✅ Vehicle specifications saved successfully!")

    st.write("### Summary of Entered Specifications")
    st.json(st.session_state["vehicle_record"])