import streamlit as st
import pandas as pd
import seaborn as sns
import altair as alt
data = pd.read_csv("Clean_dataset.csv")
df = pd.DataFrame(data)

# Streamlit app with sidebar
st.title("Retail Data Analysis")

# Sidebar with interactive widgets
st.sidebar.subheader("Select Options")
selected_store = st.sidebar.selectbox("Select Store", df['Store'].unique())
selected_dept = st.sidebar.selectbox("Select Department", df['Dept'].unique())
selected_year = st.sidebar.selectbox("Select Year", df['Year'].unique())


# Filter data based on selected options
filtered_df = df[(df['Store'] == selected_store) & (df['Dept'] == selected_dept) & (df['Year'] == selected_year)]


# 1. Bar Plot - Weekly Sales by Store
st.subheader("Weekly Sales by Store")
st.bar_chart(filtered_df.groupby('Store')['Weekly_Sales'].sum())

import streamlit as st
import matplotlib.pyplot as plt

st.subheader("Weekly Sales Distribution By Department")

# Create an Altair chart
chart = alt.Chart(filtered_df).mark_boxplot().encode(
    x='Dept:O',  # Assuming 'Dept' is a categorical variable
    y='Weekly_Sales:Q'  # Assuming 'Weekly_Sales' is a quantitative variable
).properties(width=600, height=300)

# Display the Altair chart using st.altair_chart
st.altair_chart(chart, use_container_width=True)

import streamlit as st
import pandas as pd
import altair as alt

# Assuming 'filtered_df' is your DataFrame

st.subheader("Top 10 Average Weekly Sales By Week")

# Calculate the top 10 average weekly sales by week
top10_week = pd.pivot_table(filtered_df, values="Weekly_Sales", index="Week_Number").sort_values(by='Weekly_Sales', ascending=False).head(10)

# Create an Altair chart
chart = alt.Chart(top10_week.reset_index()).mark_circle(color='orange').encode(
    x='Weekly_Sales:Q',
    y='Week_Number:O',  # Assuming 'Week_Number' is a categorical variable
    tooltip=['Week_Number:O', 'Weekly_Sales:Q']
).properties(width=600, height=300)

# Display the Altair chart using st.altair_chart
st.altair_chart(chart, use_container_width=True)


# Assuming 'filtered_df' is your DataFrame

st.subheader("Weekly Sales During Holidays")
df1 = filtered_df[(filtered_df['IsHoliday'] != 'No Holiday') | (filtered_df['Week_Number'] == 22)]
holidaymarkdown = pd.pivot_table(df1, values='Weekly_Sales', columns='Year', index="Week_Number")

# Display the bar chart using st.bar_chart
st.bar_chart(holidaymarkdown, use_container_width=True)

# Display the line chart using st.line_chart
st.line_chart(holidaymarkdown, use_container_width=True)



# Assuming 'filtered_df' is your DataFrame

st.subheader("Weekly Sales Distribution by IsHoliday")

# Create an Altair chart for the boxplot
chart = alt.Chart(filtered_df).mark_boxplot().encode(
    x='IsHoliday:N',
    y='Weekly_Sales:Q',
    color='IsHoliday:N',
    tooltip=['IsHoliday:N', 'Weekly_Sales:Q']
).properties(width=400, height=300)

# Display the Altair chart using st.altair_chart
st.altair_chart(chart, use_container_width=True)


# Assuming 'filtered_df' is your DataFrame

st.subheader("MarkDown1 Trends Over Weeks and Years")

# Create a line chart using st.line_chart
chart_data = pd.pivot_table(filtered_df, values="MarkDown1", columns="Year", index="Week_Number").reset_index()
st.line_chart(chart_data.set_index('Week_Number'), use_container_width=True)



# Assuming 'filtered_df' is your DataFrame

st.subheader("MarkDown2 Trends Over Weeks and Years")

# Create a line chart using st.line_chart
chart_data = pd.pivot_table(filtered_df, values="MarkDown2", columns="Year", index="Week_Number").reset_index()
st.line_chart(chart_data.set_index('Week_Number'), use_container_width=True)

# Assuming 'filtered_df' is your DataFrame

st.subheader("MarkDown3 Trends Over Weeks and Years")

# Create a line chart using st.line_chart
chart_data = pd.pivot_table(filtered_df, values="MarkDown3", columns="Year", index="Week_Number").reset_index()
st.line_chart(chart_data.set_index('Week_Number'), use_container_width=True)

# Assuming 'filtered_df' is your DataFrame

st.subheader("MarkDown4 Trends Over Weeks and Years")

# Create a line chart using st.line_chart
chart_data = pd.pivot_table(filtered_df, values="MarkDown4", columns="Year", index="Week_Number").reset_index()
st.line_chart(chart_data.set_index('Week_Number'), use_container_width=True)

# Assuming 'filtered_df' is your DataFrame

st.subheader("MarkDown5 Trends Over Weeks and Years")

# Create a line chart using st.line_chart
chart_data = pd.pivot_table(filtered_df, values="MarkDown5", columns="Year", index="Week_Number").reset_index()
st.line_chart(chart_data.set_index('Week_Number'), use_container_width=True)

# Assuming 'filtered_df' is your DataFrame

st.subheader("Weekly Sales Trends Over Weeks and Years based on Fuel Price")

# Create a line chart for Weekly Sales based on Fuel Price using st.line_chart
fuel_price_data = pd.pivot_table(filtered_df, values="Weekly_Sales", index="Fuel_Price").reset_index()
st.line_chart(fuel_price_data.set_index('Fuel_Price'), use_container_width=True)




# Assuming 'filtered_df' is your DataFrame

st.subheader("Bar Chart of Weekly Sales by CPI")

# Calculate mean Weekly Sales for each CPI value
mean_sales_by_cpi = filtered_df.groupby('CPI')['Weekly_Sales'].mean().reset_index()

# Create a bar chart using st.bar_chart
st.bar_chart(mean_sales_by_cpi.set_index('CPI'))


# Assuming 'filtered_df' is your DataFrame

st.subheader("Scatter Plot of Weekly Sales vs. Unemployment")

# Create an Altair chart for the scatter plot
scatter_chart_data = filtered_df[['Unemployment', 'Weekly_Sales']]

chart = alt.Chart(scatter_chart_data).mark_circle().encode(
    x='Unemployment:Q',
    y='Weekly_Sales:Q',
    tooltip=['Unemployment:Q', 'Weekly_Sales:Q']
).properties(width=600, height=400)

# Display the Altair chart using st.altair_chart
st.altair_chart(chart, use_container_width=True)

# 4. Table - Display Raw Data
show_raw_data = st.checkbox("Show Raw Data")
if show_raw_data:
    st.subheader("Raw Data")
    st.write(filtered_df)


st.write("Explore the visualizations above.")
