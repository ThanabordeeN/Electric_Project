
# Water Management System 💧

A streamlined web application built with Streamlit for tracking water consumption and billing for residential properties. This MVP (Minimum Viable Product) helps property managers monitor water usage, generate reports, and manage billing information.

![Water Management System](https://placeholder-for-screenshot.png)

## Features

- **Data Entry Form**: Easily record water meter readings for each property
- **Interactive Dashboard**: Visualize water usage patterns with charts and graphs
- **Data Management**: View, export, and manage all recorded data
- **Financial Tracking**: Automatically calculate billing amounts based on water consumption
- **Search & Filter**: Find specific readings by house number or date range
- **Data Export**: Export data to CSV format for further analysis

## Installation

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**

```bash
git clone <repository-url>
cd Electric_Project
```

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the application**

```bash
streamlit run main.py
```

## Usage Guide

### Data Entry
1. Navigate to the "Form" page using the sidebar
2. Enter house number and current water meter reading
3. Click "Save Data" to record the entry

### Viewing Analytics
1. Go to the "Dashboard" page
2. View overall metrics in the "Overview" tab
3. Explore different chart visualizations in the "Charts" tab
4. Search and filter detailed data in the "Detailed Data" tab

### Managing Data
1. Access the "Data Management" page
2. View complete dataset
3. Export data to CSV when needed
4. Clear all data if necessary (use with caution)

## Project Structure

```
Electric_Project/
│
├── main.py                # Main application entry point
├── database.py            # Database manager class
├── form_page.py           # Form page module
├── dashboard_page.py      # Dashboard page module
├── data_management_page.py # Data management page module
├── water_management.db    # SQLite database (created on first run)
└── README.md              # Project documentation
```

## Technologies Used

- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **SQLite**: Database storage
- **Plotly**: Interactive charts and visualizations
- **Streamlit Extras**: Enhanced UI components

## Current Limitations

- Single user system
- Local database only
- Fixed water pricing model
- Limited to water management only

## Future Improvements

- **User Authentication**: Multi-user support with role-based access
- **Cloud Database**: Migrate to a cloud database solution
- **Mobile Responsiveness**: Optimize for mobile devices
- **PDF Reports**: Generate downloadable PDF reports
- **Predictive Analytics**: Implement usage forecasting
- **Multiple Utility Support**: Extend to track electricity and other utilities
- **Custom Pricing Models**: Support tiered pricing and special rates
- **Notifications**: Alert system for unusual consumption patterns

## Contributing

Contributions to improve the Water Management System are welcome. Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

