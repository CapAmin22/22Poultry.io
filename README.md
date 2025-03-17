# PoultryInnovate - Smart Farming Platform 🐔

A comprehensive platform for modern poultry farming management, providing real-time monitoring, analytics, and smart insights.

## Features

- 📊 Real-time dashboard with key metrics
- 🌤️ Weather monitoring and forecasts
- 💉 Health tracking and alerts
- 📈 Market trends and financial analysis
- 📚 Educational resources
- 🔔 Smart notifications
- 👥 Stakeholder management
- 📰 Industry news updates

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/poultry-innovate.git
cd poultry-innovate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure Streamlit secrets:
Create a `.streamlit/secrets.toml` file with the following structure:
```toml
# API Keys
openweather_api_key = "your_openweather_api_key"
news_api_key = "your_news_api_key"

# API URLs
[api_urls]
weather = "https://api.openweathermap.org/data/2.5"
news = "https://newsapi.org/v2"
market = "your_market_api_url"

# Dummy Market Data
[dummy_market_data]
use_dummy_data = true

[dummy_market_data.commodities]
feed_price = 45.50
broiler_price = 120.75
egg_price = 6.25
```

## Configuration

1. Configure the application in `.streamlit/config.toml`:
```toml
[server]
port = 8501
address = "localhost"
enableCORS = true

[theme]
primaryColor = "#2563eb"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f8fafc"
textColor = "#1e293b"
font = "sans-serif"
```

2. Set up logging directory:
```bash
mkdir logs
```

## Running the Application

1. Start the Streamlit server:
```bash
streamlit run app.py
```

2. Open your browser and navigate to `http://localhost:8501`

## Deployment

### Streamlit Cloud

1. Push your code to GitHub
2. Visit [Streamlit Cloud](https://share.streamlit.io)
3. Connect your GitHub repository
4. Configure your secrets in the Streamlit Cloud dashboard

### Docker

1. Build the Docker image:
```bash
docker build -t poultry-innovate .
```

2. Run the container:
```bash
docker run -p 8501:8501 poultry-innovate
```

### 3. Server Deployment (e.g., AWS, DigitalOcean)

1. Set up a server with Python installed
2. Clone the repository
3. Install dependencies
4. Use a process manager (e.g., PM2, Supervisor)
5. Set up Nginx as a reverse proxy

## Project Structure

```
poultry-innovate/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── README.md             # Project documentation
├── .streamlit/           # Streamlit configuration
│   ├── config.toml       # Streamlit settings
│   └── secrets.toml      # API keys and secrets (not in version control)
├── modules/              # Application modules
│   ├── __init__.py
│   ├── weather.py
│   ├── health.py
│   ├── financial.py
│   ├── education.py
│   ├── stakeholders.py
│   └── news.py
├── data/                 # Data storage
├── logs/                 # Application logs
└── tests/               # Unit tests
```

## Configuration

Required secrets in `.streamlit/secrets.toml`:

- `openweather_api_key`: OpenWeather API key
- `news_api_key`: News API key
- API URLs configuration
- Dummy market data settings

## Troubleshooting

1. Port already in use:
```bash
netstat -ano | findstr :8501  # Windows
lsof -i :8501                 # Linux/Mac
```

2. Logging issues:
- Ensure the `logs` directory exists
- Check write permissions
- Verify log configuration in `app.py`

3. Module import errors:
- Verify virtual environment is activated
- Confirm all dependencies are installed
- Check Python version compatibility

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the GitHub repository.

## Authors

- Your Name - Initial work - [YourGitHub](https://github.com/yourusername) 