import streamlit as st
import requests
import pypdf

st.set_page_config(
    page_title = "Visalify AI // Platform",
    page_icon = "🛡️",
    layout = "wide",
    initial_sidebar_state = "collapsed"
)

st.markdown("""
    <style>
        /* General Canvas Restyling */
        .stApp {
            background-color: #FFFFFF !important;
            color: #1E293B !important;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }
        
        /* Main Headers */
        h1, h2, h3, .stSubheader {
            color: #003399 !important;
            font-weight: 700 !important;
        }
        
        /* Clean Custom Input Box Styles */
        textarea {
            background-color: #FCFDFF !important;
            border: 1px solid #D2E0F4 !important;
            border-radius: 16px !important;
            color: #1E293B !important;
            transition: all 0.2s ease-in-out;
        }
        textarea:focus {
            border-color: #003399 !important;
            box-shadow: 0 0 0 3px rgba(0, 51, 153, 0.1) !important;
        }
        
        /* Pill-Shaped Action Button */
        div.stButton > button {
            background-color: #003399 !important;
            color: white !important;
            border-radius: 50px !important;
            border: none !important;
            padding: 0.6rem 2rem !important;
            font-weight: 600 !important;
            letter-spacing: 0.3px;
            transition: all 0.2s ease;
            box-shadow: 0 4px 12px rgba(0, 51, 153, 0.15);
        }
        div.stButton > button:hover {
            background-color: #002266 !important;
            transform: translateY(-1px);
            box-shadow: 0 6px 16px rgba(0, 51, 153, 0.25);
            color: white !important;
        }
        
        /* Styled Metric Cards */
        [data-testid="stMetricValue"] {
            color: #003399 !important;
            font-size: 2.5rem !important;
            font-weight: 700 !important;
        }
        [data-testid="stMetricLabel"] {
            color: #64748B !important;
            font-size: 0.9rem !important;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        /* Clean Accent Cards for Results */
        .reportview-container .main .block-container{
            max-width: 1100px;
        }
        
        /* Code blocks / Optimized Profile styling */
        code {
            background-color: #F8FAFC !important;
            color: #0F172A !important;
            border: 1px solid #E2E8F0 !important;
            border-radius: 12px !important;
            padding: 15px !important;
        }
    </style>
""", unsafe_allow_html = True)


st.title("Visalify AI")
st.write("Optimize professional alignment and mitigate regulatory compliance risk in real time.")

st.markdown("<br>", unsafe_allow_html = True)

col1, col2 = st.columns(2, gap = "large")

with col1:
    st.markdown("Candidate Profile")
    profile_input = st.text_area(
        "Paste Candidate Profile or Resume Text:", 
        label_visibility = "collapsed",
        height = 300,
        placeholder = "Type or paste experience here..."
    )

with col2:
    st.markdown("Target Market Data")
    jd_input = st.text_area(
        "Paste Target Job Description:", 
        label_visibility = "collapsed",
        height = 300,
        placeholder = "Paste the target job requirements / descriptions here..."
    )

st.markdown("<br>", unsafe_allow_html = True)

if st.button("⚡ Run Pipeline Analysis", use_container_width = True):
    if not profile_input or not jd_input:
        st.error("Please provide both a candidate profile and a target job description to run the analysis.")
    else:
        with st.spinner("Executing Agentic Pipeline (Critique & Optimize)..."):
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
                        st.metric(label = "Visa Compliance Tier", value = data['compliance_verdict'])
                    
                    st.markdown("---")
                    
                    st.markdown("### Strategic Gap Analysis")
                    for gap in data['detected_gaps']:
                        with st.expander(f"📍 {gap['category']} detected"):
                            st.markdown(f"**Identified Risk/Mismatch:** {gap['detected_risk']}")
                            st.markdown(f"**Optimization Strategy:** {gap['optimization_strategy']}")
                    
                    st.markdown("---")
                    
                    st.markdown("### Automatically Optimized Profile Version")
                    st.caption("This block aligns technical terminology to the job market while reframing non-compliant language:")
                    st.code(data['optimized_profile'], language = "text")
                    
                else:
                    st.error(f"Backend returned an operational error code: {response.status_code}")
            except Exception as e:
                st.error(f"Failed to connect to the Visalify engine: {e}")