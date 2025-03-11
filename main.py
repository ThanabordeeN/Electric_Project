import streamlit as st
from database import DatabaseManager
import form_page
import dashboard_page
import data_management_page

# Set page config and custom CSS
st.set_page_config(
    page_title="Water Management System",
    page_icon="💧",
    layout="wide",
)

# Custom CSS for larger fonts and better styling
st.markdown("""
<style>
    .main-title {
        font-size: 3rem !important;
        font-weight: 700 !important;
        color: #1E88E5 !important;
        margin-bottom: 1.5rem !important;
    }
    .section-header {
        font-size: 2rem !important;
        font-weight: 600 !important;
        color: #0D47A1 !important;
        margin-top: 1rem !important;
    }
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size: 1.2rem !important;
    }
    .stMarkdown p, .stText {
        font-size: 1.1rem !important;
    }
    .metric-label {
        font-size: 1.3rem !important;
    }
    .metric-value {
        font-size: 1.8rem !important;
    }
    .stRadio [data-baseweb="radio"] {
        font-size: 1.2rem !important;
    }
    .stButton button {
        font-size: 1.2rem !important;
        border-radius: 8px !important;
        height: 3em;
    }
    .stNumberInput input, .stTextInput input {
        font-size: 1.1rem !important;
        padding: 1rem 0.75rem !important;
    }
    div[data-testid="stForm"] {
        background-color: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# Constants
DB_PATH = 'water_management.db'
UNIT_PER_PRICE = 4.5

# Initialize database manager
db_manager = DatabaseManager(DB_PATH)
db_manager.init_db()

# Title with emoji and animation
with st.container():
    st.markdown('<p class="main-title">💧 Water Management System</p>', unsafe_allow_html=True)

# Sidebar with improved styling
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/water.png", width=80)
    st.markdown("### Navigation")
    page = st.radio('', ['Form', 'Dashboard', "Data Management"], key='navigation')
    
    with st.expander("ℹ️ About"):
        st.write("""
        This application helps manage water usage and billing for residential properties.
        
        Current water price: **{:.1f} Bath per unit**
        """.format(UNIT_PER_PRICE))

# Display the selected page
if page == 'Form':
    form_page.show_form_page(db_manager, UNIT_PER_PRICE)
elif page == 'Dashboard':
    dashboard_page.show_dashboard_page(db_manager)
elif page == "Data Management":
    data_management_page.show_data_management_page(db_manager)
