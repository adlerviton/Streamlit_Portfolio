import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os
import matplotlib.dates as mdates

# Load Data
# df = pd.read_csv("data/clean_data_rates.csv")
# import the data
df = pd.read_csv("data/base_data_rates.csv", parse_dates=["Date"])
# drop 2 Mo and 4 Mo
df.drop(["1 Mo", "2 Mo", "4 Mo", "20 Yr", "30 Yr"], axis=1, inplace=True)
# drop na values
df.dropna(inplace=True)
dates = df["Date"]

# Get metrics for data
first_day = dates[0]
last_day = dates[len(df)]
total_days = len(df)
mean = df["6 Mo"].mean()
std = df["6 Mo"].std()


# Create Sidebar for Tabs
add_sidebar = st.sidebar.selectbox(
    "Tabs",
    (
        "Objectives and Background",
        "Data",
        "Machine Learning Algorithm",
        "Results",
        "Conclusions",
    ),
)

# Uses if statements to define each tab
if add_sidebar == "Objectives and Background":  # COMPLETED
    # The tab for objectives and background
    # contains all writing and markdown
    st.title("Interest Rate Modeling")
    st.write("Streamlit App created by Adler Viton")
    st.write("Analysis done by Adler Viton, Andrew Kroening, and Jeremy Tan")
    st.header("Objectives and Background")
    st.subheader("Research Motivation")
    st.markdown(
        "- Interest rate yield curves are a critical component of the overall economic picture of an economy"
    )
    st.markdown(
        "- Accurately predicting these rates is essential for banks to manage investment decisions and risk"
    )
    st.markdown(
        "- Major, unforeseen rate swings could have severe consequences for small banks, and potentially catastrophic effects if mismanaged by larger banks"
    )
    st.markdown(
        "- We attempt to build a 20-year forecast from a variety of models trained on historical interest rate data"
    )
    st.markdown(
        """
    <style>
    [data-testid="stMarkdownContainer"] ul{
        padding-left:40px;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )
    st.subheader("Research Question")
    st.write("For specified forward prediction ranges:")
    st.markdown(
        "- Is it possible to produce a realistic prediction for the interest rate yield curve into the future based on historical data?"
    )
    st.markdown(
        "- Does the addition of other economic data positively influence the predictions?"
    )
    st.write("Lookback Ranges:")
    st.markdown("- 1 day")
    st.markdown("- 1 month")
    st.markdown("- 1 year")
    st.markdown("- 1 decade")
    st.markdown(
        """
    <style>
    [data-testid="stMarkdownContainer"] ul{
        padding-left:40px;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )


if add_sidebar == "Data":  # NOT COMPLETED
    # Tab for Interest Rate Data and S&P Data
    # Should have the dataframe and a time series plot
    st.title("Interest Rate Data Utilized")
    st.write("Model uses data aggregated by moving averages for different windows.")

    # Show Metrics as 5 across
    c1, c2, c3, c4, c5 = st.columns(5)
    columns = [c1, c2, c3, c4, c5]
    c1.metric("Start Year", "1990")
    c2.metric("End Year", "2023")
    c3.metric("Total Days", total_days)
    c4.metric("Mean", round(mean, 3))
    c5.metric("6-month-average Standard Deviation", round(std, 3))

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(12, 8))

    # Loop through the non-date columns and plot them
    for i in range(1, len(df.columns)):
        ax.plot(
            df["Date"], df.iloc[:, i], label=df.columns[i], alpha=0.7, linewidth=0.75
        )

    # Set the X axis label to be more readable
    ax.set_xticks(df["Date"])
    ax.set_xticklabels(df["Date"], rotation=45)

    # Set major locator to show ticks annually
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

    # Set ylim
    ax.set_ylim(0, 13)

    # Set the title and axis labels
    ax.set_title("Interest Rates")
    ax.set_xlabel("Date")
    ax.set_ylabel("Interest Rate")

    # Set the legend
    ax.legend(loc="upper left")
    st.pyplot(fig)

    # Include the DataFrame
    # Year selection dropdown
    years = ["All Years"] + sorted(df["Date"].dt.year.unique())
    selected_year = st.selectbox("Select Year", years)

    # Filter the DataFrame based on the selected year
    if selected_year != "All Years":
        filtered_df = df[df["Date"].dt.year == selected_year]
    else:
        filtered_df = df  # Show data for all years

    # Set 'Date' column as the index
    filtered_df_display = filtered_df.set_index("Date")

    # Remove time component from the index (Date) column when displaying the DataFrame
    filtered_df_display.index = filtered_df_display.index.strftime("%Y-%m-%d")

    # Display the filtered DataFrame without the index column
    st.write(filtered_df_display)

if add_sidebar == "Machine Learning Algorithm":  # NOT COMPLETED
    # Should have an explanation of what algorithm is
    # And experimental design
    st.title("Interest Rate Forecasting Machine Learning Algorithm")
    if st.button("Hit me"):
        st.write("nothing here yet")
    else:
        st.write("Experimental Design")

if add_sidebar == "Results":
    # Should show results for the model
    st.title("Interest Rate Modeling Results")
    st.write("Placeholder plot for now")
    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)

    st.pyplot(fig)
