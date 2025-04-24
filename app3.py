import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page settings ---
st.set_page_config(page_title="Research Paper Correlation Explorer", layout="wide")
st.title("📊 Research Paper Correlation Explorer")
st.markdown("Explore relationships between variables from both sheets of your research Excel data.")

# --- Excel file link ---
# 🔁 Replace the URL below with the actual direct Excel file link
EXCEL_URL = "https://example.com/Research_paper_data.xlsx"

# Load Excel file from link
@st.cache_data
def load_data_from_url(url):
    xls = pd.ExcelFile(url)
    sheet1 = pd.read_excel(xls, sheet_name=0, header=1)
    sheet2 = pd.read_excel(xls, sheet_name=1)
    return sheet1, sheet2

try:
    sheet1, sheet2 = load_data_from_url(EXCEL_URL)

    # Sidebar controls
    st.sidebar.header("🔍 Graph Settings")
    sheet_names = {
        "📘 Sheet 1: Base Research Info": sheet1,
        "📗 Sheet 2: Detailed Work Breakdown": sheet2
    }

    sheet_choice = st.sidebar.selectbox("Select Data Sheet", list(sheet_names.keys()))
    selected_df = sheet_names[sheet_choice]

    # Data preview
    with st.expander("🔎 Preview Data"):
        st.dataframe(selected_df, use_container_width=True)

    # Axis selections
    col1 = st.sidebar.selectbox("X-axis Column", selected_df.columns)
    col2 = st.sidebar.selectbox("Y-axis Column", selected_df.columns)

    st.subheader(f"Correlation between **{col1}** and **{col2}**")

    # Plotting
    fig = px.scatter(
        selected_df,
        x=col1,
        y=col2,
        color_discrete_sequence=['#1f77b4'],
        title="Scatter Plot of Selected Columns",
        template="plotly_white"
    )
    fig.update_traces(marker=dict(size=10, line=dict(width=1, color='DarkSlateGrey')))
    fig.update_layout(title_x=0.5)
    st.plotly_chart(fig, use_container_width=True)

except Exception as e:
    st.error(f"❌ Error loading Excel data from link: {e}")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit and Plotly. Designed for civil engineering data insights.")
