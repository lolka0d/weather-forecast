import streamlit as st
import plotly.express as px

from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} in {place}")

if place:
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict_["main"]["temp"] / 10  for dict_ in filtered_data]
            dates = [dict_["dt_txt"] for dict_ in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)
        else:
            filtered_data = [dict_["weather"][0]["main"] for dict_ in filtered_data]
            image_paths = [f"images/{i}.png" for i in filtered_data]
            st.image(image_paths, width=115)
    except KeyError:
        st.write("This place doesn't exist!")
