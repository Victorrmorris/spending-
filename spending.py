import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards

# Set page configuration
st.set_page_config(
    page_title="Cross-Border Spending Insights",
    layout="wide",
    page_icon="🌍",
)

# Sample Data
# Replace with actual data processing if you have a CSV file loaded
us_data = {
    "Total Spent": "$4,200.50",
    "Categories": {
        "Transportation": "$650.00",
        "Rent": "$2,100.00",
        "Entertainment": "$450.50",
        "Utilities": "$300.00",
        "Groceries": "$700.00",
    },
}
italy_data = {
    "Total Spent": "€3,800.75",
    "Categories": {
        "Transportation": "€450.00",
        "Rent": "€1,800.75",
        "Entertainment": "€300.00",
        "Utilities": "€500.00",
        "Groceries": "€750.00",
    },
}

# Chatbot Sample Q&A
chatbot_responses = {
    "What is the biggest expense in the US?": "In the US, the biggest expense is Rent, which accounts for $2,100.00.",
    "What is the biggest expense in Italy?": "In Italy, the biggest expense is Rent, which accounts for €1,800.75.",
    "How can I save on utilities in Italy?": "To save on utilities in Italy, consider reducing energy usage during peak hours and exploring more affordable energy plans.",
    "How can I reduce grocery expenses in the US?": "To reduce grocery expenses in the US, consider using coupons, buying in bulk, and exploring local farmer's markets.",
}

# Helper Functions
def style_section_title(title):
    st.markdown(f"<h2 style='text-align: center; color: #4CAF50;'>{title}</h2>", unsafe_allow_html=True)

def display_budget_data(country, data):
    st.metric(label=f"{country} Total Spent", value=data["Total Spent"])
    st.write("**Category Breakdown:**")
    for category, amount in data["Categories"].items():
        st.markdown(f"- **{category}:** {amount}")

# Main Content
st.title("🌍 Cross-Border Spending Insights")
st.markdown(
    """
    Welcome to the Cross-Border Spending Insights Dashboard! This app provides actionable 
    insights into household spending in the US and Italy. Use the chatbot below to ask specific 
    questions about spending patterns and saving tips.
    """
)
st.markdown("---")

# US and Italy Insights Section
col1, col2 = st.columns(2)
with col1:
    style_section_title("US Household Spending")
    display_budget_data("US", us_data)

with col2:
    style_section_title("Italy Household Spending")
    display_budget_data("Italy", italy_data)

# Chatbot Section
st.markdown("---")
style_section_title("💬 Chat with Your Spending Assistant")
user_query = st.text_input("Ask a question about cross-border spending insights:")
if user_query:
    response = chatbot_responses.get(user_query, "I'm sorry, I don't have an answer for that question yet.")
    st.write(f"**Your Question:** {user_query}")
    st.info(f"**Chatbot Response:** {response}")
else:
    st.write("Try asking questions like:")
    for question in chatbot_responses.keys():
        st.markdown(f"- **{question}**")
