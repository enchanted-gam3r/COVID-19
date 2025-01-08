# # import streamlit as st
# import pandas as pd

# data = pd.read_csv("dataset.csv")
# # print(data[["1/22/20", "1/23/20"]])
# print(data.loc["China"])


# import pandas as pd

# # Reading the CSV file into a DataFrame

# # Accessing the row labeled "China"
# china_rows = data[data["Country/Region"] == "China"]
# # Printing the row
# print(china_rows)


import pandas as pd
import streamlit as st
from gemma import *

st.title("Covid 19 Analysis")
st.subheader("Worldwide Covid cases (Scatter plot)")

data = pd.read_csv("newdata.csv")
data.fillna(0, inplace=True)
st.map(data)

nameOfCountry = st.text_input("Enter the name of the country")

if(nameOfCountry):
    rowData = data[data["Country/Region"] == nameOfCountry]
    countryData = rowData.iloc[:, 4:]
    countryData = countryData.T
    countryData.columns = [nameOfCountry]
    countryData.index = pd.to_datetime(countryData.index)
    st.line_chart(countryData)

    st.subheader("Conclusion from the data: ")
    response = getAIData(countryData)
    st.write(response)
    # print(response)

else:
    st.write("Some error occured")


st.subheader("Comparison between growth rates")
country1 = st.text_input("Enter the name of the country", placeholder="Country name 1")
country2 = st.text_input("Enter the name of another country", placeholder="Country name 2")

if country1 and country2:
    st.write(f"Country 1: {country1}")
    st.write(f"Country 2: {country2}")

    # Filter data for the first country
    rowData1 = data[data["Country/Region"] == country1]
    countryData1 = rowData1.iloc[:, 4:].T
    countryData1.columns = [country1]
    countryData1.index = pd.to_datetime(countryData1.index)

    # Filter data for the second country
    rowData2 = data[data["Country/Region"] == country2]
    countryData2 = rowData2.iloc[:, 4:].T
    countryData2.columns = [country2]
    countryData2.index = pd.to_datetime(countryData2.index)

    # Combine both countries' data into one DataFrame
    combinedData = pd.concat([countryData1, countryData2], axis=1)

    # Plot the combined data
    st.line_chart(combinedData)
    st.subheader("Conclusion from the data: ")
    response = secondFun(combinedData)
    st.write(response)
