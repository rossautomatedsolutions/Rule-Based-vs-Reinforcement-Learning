import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Model Performance Dashboard", layout="wide")

# Load data
@st.cache_data
def load_data():
    df_all = pd.read_csv("df_all.csv")
    summary_table = pd.read_csv("summary_table.csv", index_col=0)
    sector_model_avg = pd.read_csv("sector_model_avg.csv", index_col=0)
    sector_consistency = pd.read_csv("sector_consistency.csv", index_col=0)
    return df_all, summary_table, sector_model_avg, sector_consistency

df_all, summary_table, sector_model_avg, sector_consistency = load_data()

# --- Streamlit UI ---
st.title("📊 Model Performance Dashboard")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["📈 Overview", "🏆 Sector Leaderboard", "📂 Filter Results", "📤 Export"])

# --- Overview Tab ---
with tab1:
    st.header("Top 2 Model Frequency")
    st.dataframe(summary_table.style.format({'Top 2 %': '{:.1f}'}))

    st.subheader("Boxplot: Total Return (%) by Model")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.boxplot(data=df_all, x="Model", y="Total Return (%)", ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    ax.grid(axis='y')
    st.pyplot(fig)

# --- Sector Leaderboard Tab ---
with tab2:
    st.header("Average Total Return (%) by Sector and Model")
    st.dataframe(sector_model_avg.style.format("{:.2f}"))

    st.subheader("Most Consistent Top Models by Sector")
    st.dataframe(sector_consistency[["Top Model", "Top Model Count"]])

# --- Filter Results Tab ---
with tab3:
    st.header("Explore All Model Results")
    col1, col2 = st.columns(2)

    sectors = df_all['Sector'].dropna().unique()
    models = df_all['Model'].unique()

    selected_sector = col1.selectbox("Select Sector", options=["All"] + sorted(sectors.tolist()))
    selected_model = col2.selectbox("Select Model", options=["All"] + sorted(models.tolist()))

    filtered = df_all.copy()
    if selected_sector != "All":
        filtered = filtered[filtered['Sector'] == selected_sector]
    if selected_model != "All":
        filtered = filtered[filtered['Model'] == selected_model]

    st.write(f"Showing {len(filtered)} rows")
    st.dataframe(filtered)

# --- Export Tab ---
with tab4:
    st.header("Download Data")
    st.download_button("Download All Results (CSV)", df_all.to_csv(index=False), "all_results.csv", "text/csv")
    st.download_button("Download Summary Table", summary_table.to_csv(), "summary_table.csv", "text/csv")
    st.download_button("Download Sector Model Averages", sector_model_avg.to_csv(), "sector_model_avg.csv", "text/csv")
    st.download_button("Download Sector Leaderboard", sector_consistency.to_csv(), "sector_consistency.csv", "text/csv")
