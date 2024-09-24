import streamlit as st
import plotly.express as px
from backend import get_data


st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days",min_value=1,max_value=5, help="Select the number of forecast days")
option = st.selectbox("Select data to view", ("Temperature","Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    filtered_data = get_data(place,days)

    if option == "Temperature":
        temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
        dates= [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates,y=temperatures,labels = {"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    if option == "Sky":
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                  "Rain": "images/rain.png", "Snow": "images/snow.png"}

        # Extract sky conditions and corresponding dates
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        image_paths = [images[condition] for condition in sky_conditions]
        dates = [dict["dt_txt"] for dict in filtered_data]

        # Display images in a grid with 5 columns per row
        for i in range(0, len(image_paths), 5):
            cols = st.columns(5)  # Create 5 columns for each row
            for j in range(5):
                if i + j < len(image_paths):  # Ensure we don't go out of range
                    with cols[j]:
                        st.image(image_paths[i + j], width=115)  # Display the image
                        st.write(dates[i + j])  # Display the corresponding date and time below the image
    st.markdown("<br><br>", unsafe_allow_html=True)  # Add two line breaks for space
    st.markdown('Created by **<span style="color:darkblue;">Dario Galvagno</span>**', unsafe_allow_html=True)

