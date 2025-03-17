import streamlit as st
from modules import weather, news, statistics, education, financial, stakeholders, health
import os
from streamlit_option_menu import option_menu
from streamlit_extras.app_logo import add_logo
from streamlit_lottie import st_lottie
import requests
import json
import logging
from datetime import datetime
import sys
from pathlib import Path

# Configure basic logging to stdout
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger(__name__)
logger.info("Application starting up")

# Initialize configuration from Streamlit secrets
def get_secret(key, default=None):
    """Safely get a secret from Streamlit secrets."""
    try:
        return st.secrets[key]
    except KeyError:
        if default is not None:
            return default
        raise KeyError(f"Missing required secret: {key}")

# Load configuration
try:
    # API Keys
    OPENWEATHER_API_KEY = get_secret("openweather_api_key")
    NEWS_API_KEY = get_secret("news_api_key")
    COMMODITIES_API_KEY = get_secret("commodities_api_key")
    
    # API URLs
    WEATHER_API_URL = get_secret("api_urls")["weather"]
    NEWS_API_URL = get_secret("api_urls")["news"]
    MARKET_API_URL = get_secret("api_urls")["market"]
    
    # Application Settings
    DEBUG = get_secret("settings")["debug"]
    ENVIRONMENT = get_secret("settings")["environment"]
    CACHE_TIMEOUT = get_secret("settings")["cache_timeout"]
    
    logger.info("Configuration loaded successfully")
except Exception as e:
    logger.error(f"Error loading configuration: {e}")
    st.error("Failed to load application configuration. Please check your settings.")
    st.stop()

def load_lottie_url(url: str) -> dict | None:
    """
    Load a Lottie animation from a URL.
    
    Args:
        url (str): The URL of the Lottie animation JSON file
        
    Returns:
        dict | None: The Lottie animation as a dictionary if successful, None otherwise
    """
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        logger.error(f"Error loading Lottie animation from {url}: {str(e)}")
        return None

# Load animations
lottie_chicken = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_GofK09iPAE.json")
lottie_weather = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_KUFdS6.json")

# Page configuration
st.set_page_config(
    page_title="PoultryInnovate | Smart Farming Platform",
    page_icon="🐔",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Modern mobile-first CSS with enhanced design
st.markdown("""
<style>
    /* Global Styling */
    .stApp {
        background: linear-gradient(135deg, #ffffff 0%, #f5f7fa 100%);
        font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
    }

    .css-1d391kg {
        padding-top: 1rem;
    }

    /* Typography Improvements */
    h1 {
        color: #1e293b;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
        letter-spacing: -0.5px;
        text-shadow: 0 1px 2px rgba(0,0,0,0.1);
    }

    h2 {
        color: #334155;
        font-size: 1.8rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }

    h3 {
        color: #475569;
        font-size: 1.4rem;
        font-weight: 500;
    }

    p {
        color: #334155;
        line-height: 1.7;
        font-size: 1.1rem;
        font-weight: 400;
    }

    /* Modern Card Design */
    .modern-card {
        background: white;
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 8px 30px rgba(0,0,0,0.08);
        margin-bottom: 1.5rem;
        border: 1px solid rgba(0,0,0,0.06);
        transition: all 0.3s ease;
    }

    .modern-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 40px rgba(0,0,0,0.12);
    }

    /* Dashboard Stats Cards */
    .stat-card {
        background: white;
        padding: 1.5rem;
        border-radius: 16px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        text-align: center;
        transition: transform 0.2s ease;
    }

    .stat-card:hover {
        transform: translateY(-2px);
    }

    /* Input Fields */
    .stTextInput input, .stSelectbox select {
        border-radius: 12px;
        border: 2px solid rgba(37, 99, 235, 0.2);
        padding: 0.75rem 1rem;
        transition: all 0.2s ease;
        font-size: 1rem;
        color: #1e293b;
        background: white;
    }

    .stTextInput input:focus, .stSelectbox select:focus {
        border-color: #2563eb;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.2);
    }

    /* Buttons */
    .stButton button {
        border-radius: 12px;
        padding: 0.6rem 1.5rem;
        font-weight: 600;
        transition: all 0.2s ease;
        background: #2563eb;
        color: white;
        border: none;
    }

    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2);
        background: #1d4ed8;
    }

    /* Navigation Menu */
    .nav-link {
        border-radius: 12px !important;
        margin: 4px 0 !important;
        padding: 0.8rem !important;
        transition: all 0.2s ease !important;
        color: #475569 !important;
    }

    .nav-link:hover {
        background-color: rgba(37, 99, 235, 0.1) !important;
        color: #2563eb !important;
    }

    .nav-link.active {
        background-color: #2563eb !important;
        color: white !important;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2) !important;
    }

    /* Metrics and KPIs */
    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        color: #2563eb;
        text-shadow: 0 1px 2px rgba(0,0,0,0.1);
    }

    .metric-label {
        font-size: 1rem;
        color: #475569;
        margin-top: 0.5rem;
        font-weight: 500;
    }

    /* Charts and Graphs */
    .plot-container {
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }

    /* Tables */
    .dataframe {
        border-radius: 12px;
        overflow: hidden;
        border: none;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }

    .dataframe th {
        background: #f1f5f9;
        padding: 1rem;
        font-weight: 600;
        color: #334155;
    }

    .dataframe td {
        padding: 1rem;
        border-bottom: 1px solid #e2e8f0;
        color: #475569;
    }

    /* Notifications */
    .notification {
        background: white;
        padding: 1rem;
        border-radius: 12px;
        border-left: 4px solid #2563eb;
        margin-bottom: 0.8rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }

    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }

    ::-webkit-scrollbar-track {
        background: #f1f5f9;
        border-radius: 4px;
    }

    ::-webkit-scrollbar-thumb {
        background: #94a3b8;
        border-radius: 4px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: #64748b;
    }

    /* Hide default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .block-container {padding-bottom: 1rem;}
</style>
""", unsafe_allow_html=True)

def main() -> None:
    """
    Main application function that sets up the Streamlit interface and handles navigation.
    Manages the main layout, navigation, and different sections of the application.
    """
    try:
        # Add logo with enhanced styling
        with st.container():
            col1, col2 = st.columns([1, 5])
            with col1:
                add_logo("generated-icon.png", height=80)
            with col2:
                st.markdown("<h1 style='margin-top: 0.5rem;'>PoultryInnovate</h1>", unsafe_allow_html=True)

        # Initialize session state
        if 'user_location' not in st.session_state:
            st.session_state.user_location = None
            logger.info("Initialized user_location in session state")
        if 'notifications' not in st.session_state:
            st.session_state.notifications = []
            logger.info("Initialized notifications in session state")

        # Modern Navigation
        selected = option_menu(
            menu_title=None,
            options=["Dashboard", "Health", "Weather", "Market", "Education", "Network", "News"],
            icons=["graph-up", "heart-pulse", "cloud-sun", "currency-dollar", "book", "people", "newspaper"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",
            styles={
                "container": {
                    "padding": "0.5rem",
                    "background-color": "transparent",
                    "border-radius": "15px",
                    "margin-bottom": "2rem"
                },
                "icon": {"color": "#2563eb", "font-size": "1.1rem"},
                "nav-link": {
                    "font-size": "1rem",
                    "text-align": "center",
                    "padding": "1rem",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
            }
        )
        logger.info(f"User selected navigation: {selected}")

        # Handle navigation selection
        try:
            if selected == "Dashboard":
                display_dashboard()
            elif selected == "Health":
                health.show_health_module()
            elif selected == "Weather":
                weather.show_weather_module()
            elif selected == "Market":
                financial.show_market_module()
            elif selected == "Education":
                education.show_education_module()
            elif selected == "Network":
                stakeholders.show_network_module()
            elif selected == "News":
                news.show_news_module()
        except Exception as e:
            logger.error(f"Error in module {selected}: {str(e)}")
            st.error(f"An error occurred while loading the {selected} module. Please try again later.")

    except Exception as e:
        logger.error(f"Critical error in main application: {str(e)}")
        st.error("An unexpected error occurred. Please refresh the page or contact support.")

def display_dashboard() -> None:
    """
    Display the main dashboard with key metrics and overview information.
    Includes weather summary, health alerts, market trends, and recent news.
    """
    try:
        st.markdown("## Dashboard Overview")
        
        # Create dashboard layout
        col1, col2, col3 = st.columns(3)
        
        with col1:
            display_weather_summary()
        with col2:
            display_health_metrics()
        with col3:
            display_market_trends()
            
        # Display recent notifications
        display_notifications()
        
    except Exception as e:
        logger.error(f"Error in dashboard display: {str(e)}")
        st.error("Unable to load dashboard components. Please refresh the page.")

def display_weather_summary() -> None:
    """Display a summary of current weather conditions and forecasts."""
    try:
        with st.container():
            st.markdown("### Weather Summary")
            weather.display_weather_widget()
    except Exception as e:
        logger.error(f"Error displaying weather summary: {str(e)}")
        st.warning("Weather information temporarily unavailable")

def display_health_metrics() -> None:
    """Display key health metrics and alerts for the poultry farm."""
    try:
        with st.container():
            st.markdown("### Health Metrics")
            health.display_health_summary()
    except Exception as e:
        logger.error(f"Error displaying health metrics: {str(e)}")
        st.warning("Health metrics temporarily unavailable")

def display_market_trends() -> None:
    """Display current market trends and financial indicators."""
    try:
        with st.container():
            st.markdown("### Market Trends")
            financial.display_market_summary()
    except Exception as e:
        logger.error(f"Error displaying market trends: {str(e)}")
        st.warning("Market trends temporarily unavailable")

def display_notifications() -> None:
    """Display recent notifications and alerts in the dashboard."""
    try:
        with st.container():
            st.markdown("### Recent Notifications")
            if st.session_state.notifications:
                for notification in st.session_state.notifications:
                    st.markdown(f"""
                        <div class="notification">
                            <strong>{notification['title']}</strong><br>
                            {notification['message']}
                        </div>
                    """, unsafe_allow_html=True)
            else:
                st.info("No new notifications")
    except Exception as e:
        logger.error(f"Error displaying notifications: {str(e)}")
        st.warning("Unable to load notifications")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.critical(f"Application failed to start: {str(e)}")
        st.error("Critical error: Unable to start the application. Please contact support.")