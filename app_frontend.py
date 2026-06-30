import streamlit as st
import requests

st.set_page_config(page_title = "VisaGuard Compliance AI", page_icon = "🛡️", layout = "wide")

st.title("🛡️ VisaGuard: Compliance Analysis Dashboard")
st.markdown("Evaluate job descriptions against TN Visa occupational restrictions using NLP context-awareness.")

col1, col2 = st.columns([3, 2])

with col1:
    st.subheader("📋 Input Job Description")
    job_text = st.text_area(
        "Paste the raw role responsibilities below:", 
        height = 300, 
        placeholder = "e.g., You will manage a team of engineers and oversee our code deployment pipelines..."
    )
    analyze_button = st.button("Run Compliance Audit", type = "primary", use_container_width = True)

with col2:
    st.subheader("📊 Telemetry Metrics")
    
    if analyze_button and job_text:
        try:
            response = requests.post("http://127.0.0.1:8000/analyze", json = {"job_description": job_text})
            
            if response.status_code == 200:
                results = response.json()
                
                score = results.get("risk_score", 0)
                level = results.get("overall_risk_level", "Safe")
                
                if level in ["Critical", "High"]:
                    st.error(f"Overall Status: {level} Risk ({score}/100)")
                elif level == "Medium":
                    st.warning(f"Overall Status: {level} Risk ({score}/100)")
                else:
                    st.success(f"Overall Status: {level} / Compliant ({score}/100)")
                
                flags = results.get("flags", [])
                if not flags:
                    st.balloons()
                    st.success("✨ Zero compliance regularities or structural risks detected!")
                else:
                    st.markdown(f"### Found {len(flags)} Risk Factors:")
                    for idx, flag in enumerate(flags):
                        with st.expander(f"⚠️ Flag #{idx+1}: '{flag['matched_text']}' ({flag['severity'].upper()})"):
                            st.markdown(f"**Reason:** {flag['reason']}")
                            st.info(f"💡 **Suggested Rephrasing:** {flag['suggested_alternative']}")
            else:
                st.error("Engine Communication Error: Backend API returned a faulty status code.")
        except requests.exceptions.ConnectionError:
            st.error("Infrastructure Offline: Please make sure your FastAPI Uvicorn server is running on port 8000.")
    else:
        st.info("Awaiting input text. Input a description and click analyze to populate compliance telemetry.")