# 📊 Sales Data Analytics Dashboard

## About the Project
The Sales Data Analytics Dashboard is a simple web application developed using **Python, Streamlit, and Pandas**. It reads sales data from a CSV file and displays the records in an interactive table.

## Features
- Displays the dashboard title.
- Reads sales data from `sales.csv`.
- Displays sales records in a table.
- Uses Pandas for reading and handling data.
- Uses Streamlit to create the web interface.

## Technologies Used
- **Python** – Programming language
- **Streamlit** – Web dashboard interface
- **Pandas** – Data handling and CSV reading
- **CSV** – Data storage format

## Project Structure

```text
Sales-Analytics-Dashboard/
│
├── dashboard.py
├── sales.csv
└── README.md
```

## Installation and Setup

### Step 1: Install Python
Download Python from [python.org](https://www.python.org/downloads/).

### Step 2: Install Required Libraries

Open your terminal or PowerShell and run:

```bash
pip install streamlit pandas
```

### Step 3: Prepare the CSV File

Create a file named `sales.csv` in the same folder as `dashboard.py`.

Add your sales data to the CSV file. For example:

```csv
Product,City,Quantity,Price,Revenue,Date
Laptop,Delhi,2,50000,100000,2026-10-01
Mobile,Lucknow,3,15000,45000,2026-10-02
Keyboard,Kanpur,5,1000,5000,2026-10-03
```

### Step 4: Run the Application

Open the terminal in your project folder and execute:

```bash
streamlit run dashboard.py
```

The dashboard will open in your web browser.

## How It Works
1. Imports Streamlit and Pandas.
2. Reads sales data from `sales.csv`.
3. Displays the dashboard heading.
4. Shows the sales records using Streamlit's dataframe component.

## Future Improvements
- Add total sales and revenue calculations.
- Display sales charts and graphs.
- Filter data by product, city, and date.
- Add sales data through a form.
- Generate sales reports.

## Author
Developed as a Python data analytics project.

## License
This project is available for educational and learning purposes.
