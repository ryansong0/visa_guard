import streamlit as st
import requests
import pypdf

st.set_page_config(
    page_title = "Visalify AI // Job & Compliance Matcher",
    page_icon = "🛡️",
    layout = "wide",
    initial_sidebar_state = "expanded"
)




st.title("🚀 Visalify AI")
st.subheader("Enterprise Job Optimization & Regulatory Compliance Engine")
st.write("Align candidate profiles to live job markets while automatically mitigating immigration compliance risks.")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📄 Candidate Data")
    profile_input = st.text_area(
        "Paste Candidate Profile or Resume Text:", 
        height = 300,
        placeholder = "Type or paste experience here..."
    )

with col2:
    st.markdown("### 💼 Target Market Data")
    jd_input = st.text_area(
        "Paste Target Job Description:", 
        height = 300,
        placeholder = "Paste the company's job requirements here..."
    )

st.markdown("---")

if st.button("⚡ Run Automated Optimization Loop", use_container_width=True):
    if not profile_input or not jd_input:
        st.error("⚠️ Please provide both a candidate profile and a target job description to run the alignment engine.")
    else:
        with st.spinner("Executing Multi-Stage Agentic Pipeline (Critique & Optimize)..."):
            try:
                payload = {
                    "candidate_profile": profile_input,
                    "job_description": jd_input
                }
                response = requests.post("http://127.0.0.1:8000/match", json = payload, timeout = 60)
                
                if response.status_code == 200:
                    data = response.json()
                    
                    m_col1, m_col2 = st.columns(2)
                    with m_col1:
                        st.metric(label = "Overall Market Match Score", value = f"{data['overall_match_score']}%")
                    with m_col2:
                        st.metric(label = "Visa Compliance Verdict", value = data['compliance_verdict'])
                    
                    st.markdown("---")
                    
                    # 2. Optimization Gap Analytics Display
                    st.markdown("### 🔍 Pipeline Gap Analysis")
                    for gap in data['detected_gaps']:
                        with st.expander(f"📍 {gap['category']} detected"):
                            st.markdown(f"**Identified Risk/Mismatch:** {gap['detected_risk']}")
                            st.markdown(f"**Optimization Strategy:** {gap['optimization_strategy']}")
                    
                    st.markdown("---")
                    
                    st.markdown("### 🛠️ Automatically Optimized Profile Version")
                    st.caption("This block aligns technical terminology to the job market while reframing non-compliant language:")
                    st.code(data['optimized_profile'], language = "text")
                    
                else:
                    st.error(f"Backend returned an operational error code: {response.status_code}")
            except Exception as e:
                st.error(f"Failed to connect to the Visalify engine: {e}")