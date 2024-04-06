import streamlit as st
from backend import get_data
import plotly.express as px
from datetime import datetime

st.title("Weather forecast App")
city = st.text_input("Enter City Name:")
days = st.slider("Choose Number of Days:", min_value=1, max_value=5)
option = st.selectbox("Select Data", ("Temperature", "Sky Conditions"))
st.subheader(f"{option} in {city.title()} for the next {days} days")

# Data from backend
if city:
    try:
        filtered_data = get_data(city, days)

        if option == "Temperature":
            # Graph - x- values, y values
            dates = [i["dt"] for i in filtered_data]
            temps = [i["main"]["temp"] for i in filtered_data]
            dates_formatted = [datetime.fromtimestamp(date) for date in dates]

            # generate fig for graph
            figure = px.line(x=dates_formatted, y=temps, labels={"x": "Dates", "y": "Temp (deg C)"})
            st.plotly_chart(figure)
        elif option == "Sky Conditions":
            sky_conditions = [i["weather"][0]["main"] for i in filtered_data]
            images = {"Clear": "images_weather/clear.png", "Clouds": "images_weather/cloud.png",
                      "Rain": "images_weather/rain.png", "Snow": "images_weather/snow.png"}
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=100)
    except KeyError:
        st.error("Please enter a valid city.")
