import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Cross-Border Spending Insights",
    layout="wide",
    page_icon="🌍",
)

# Google Sheets Setup
# Path to your Google Cloud credentials JSON file
credentials_file = "credentials.json"  # Ensure this path is correct

# Google Sheets URL
sheet_url = "https://docs.google.com/spreadsheets/d/1lJAlPxYHSbmXaW31QWk8cKmQGRdElBL3JqwFvt8eopQ/edit?usp=sharing"

# Connect to Google Sheets
def connect_to_google_sheet(credentials_file, sheet_url):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    credentials = Credentials.from_service_account_file(credentials_file, scopes=scope)
    gc = gspread.authorize(credentials)
    sheet = gc.open_by_url(sheet_url)
    return sheet

# Fetch data from the sheet
def fetch_spreadsheet_data(sheet, sheet_name="Sheet1"):
    worksheet = sheet.worksheet(sheet_name)
    data = worksheet.get_all_records()  # Fetch all rows as dictionaries
    return pd.DataFrame(data)

# Main Content
st.title("🌍 Cross-Border Spending Insights")
st.markdown(
    """
    Welcome to the Cross-Border Spending Insights Dashboard! This app provides actionable 
    insights into household spending using data from a 90-day spending spreadsheet.
    """
)
st.markdown("---")

# Load Google Sheets data
try:
    sheet = connect_to_google_sheet(credentials_file, sheet_url)
    spending_data = fetch_spreadsheet_data(sheet)
    st.success("Google Sheet data loaded successfully!")
    st.dataframe(spending_data)  # Display the data

    # Ensure required columns exist
    if all(col in spending_data.columns for col in ["Date", "Amount"]):
        spending_data["Date"] = pd.to_datetime(spending_data["Date"], errors="coerce")
        spending_data["Amount"] = pd.to_numeric(spending_data["Amount"], errors="coerce")
        
        # Drop rows with missing critical data
        spending_data = spending_data.dropna(subset=["Date", "Amount"])
        
        # Provide insights
        st.header("Spending Insights")
        total_spending = spending_data["Amount"].sum()
        st.metric(label="Total Spending (90 days)", value=f"${total_spending:.2f}")

        # Monthly Breakdown
        spending_data["Month"] = spending_data["Date"].dt.to_period("M")
        monthly_spending = spending_data.groupby("Month")["Amount"].sum()
        st.bar_chart(monthly_spending)
    else:
        st.warning("The Google Sheet is missing required columns: 'Date' or 'Amount'.")
except Exception as e:
    st.error(f"Error loading Google Sheet: {e}")

