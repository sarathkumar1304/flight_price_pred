from datetime import timedelta
from datetime import datetime
import streamlit as st
import pickle
import pandas as pd
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Project", "About Me"],
        icons=["house", "app-indicator", "person-video3"],
        menu_icon="cast",
        default_index=0,
    )

model = pickle.load(open("flight_rf.pkl", "rb"))
if selected == "Home":
    st.image(
        "https://lh3.googleusercontent.com/-5ZEa4w2GiXs/YcGpSsrOt4I/AAAAAAAACV4/SmKjOWuFL_galichmeWZBMsY9VIIGzv7gCNcBGAsYHQ/w1600/219-2190735_abstract-stained-background-seamless-video-color-light%2Bcopy.webp")
    st.title("FLIGHT PRICE PREDICTION")
    st.subheader("WELCOME ALL :heart:")

if selected == "Project":
    st.image(
        "https://lh3.googleusercontent.com/-5ZEa4w2GiXs/YcGpSsrOt4I/AAAAAAAACV4/SmKjOWuFL_galichmeWZBMsY9VIIGzv7gCNcBGAsYHQ/w1600/219-2190735_abstract-stained-background-seamless-video-color-light%2Bcopy.webp")
    st.title("FLIGHT PRICE PREDICTION")
    st.subheader("WELCOME ALL :heart:")
    with st.form("my form"):
        date_dep = st.date_input("Select Depture Date and Month", min_value=datetime.now())
        Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").month)

        Dep_hour = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").minute)

        date_arr = st.date_input("Select Arrival Date And Month", max_value=datetime.now() + timedelta(days=4))
        Arrival_hour = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").minute)

        dur_hour = abs(Arrival_hour - Dep_hour)
        dur_min = abs(Arrival_min - Dep_min)
        Total_stops = st.number_input("No of stops", 0, 4)
        airline = st.selectbox("Select Airline", ["Jet_Airways", "IndiGo",
                                                  "Air_India",
                                                  "Multiple_carriers",
                                                  "SpiceJet",
                                                  "Vistara",
                                                  "GoAir",
                                                  "Multiple_carriers_Premium_economy",
                                                  "Jet_Airways_Business",
                                                  "Vistara_Premium_economy",
                                                  "Trujet"])
        if airline == "Jet_Airways":
            Jet_Airways = 1
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
        elif airline == "IndiGo":
            Jet_Airways = 0
            IndiGo = 1
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
        elif airline == "Air_India":
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif airline == "Multiple_carriers":
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
        elif airline == "SpiceJet":
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif airline == "Vistara":
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif airline == "GoAir":
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 1
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
        elif airline == "Multiple_carriers_Premium_economy":
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 1
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
        elif airline == "Jet_Airways_Business":
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 1
            Vistara_Premium_economy = 0
            Trujet = 0
        elif airline == "Vistara_Premium_economy":
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 1
            Trujet = 0
        elif airline == "Trujet":
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 1
        else:
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        source = st.selectbox("Select From", ["Delhi",
                                              "Kolkata",
                                              "Mumbai",
                                              "Chennai"])
        if source == "Delhi":
            s_Delhi = 1
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0
        elif source == "Kolkata":
            s_Delhi = 0
            s_Kolkata = 1
            s_Mumbai = 0
            s_Chennai = 0
        elif source == "Mumbai":
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 1
            s_Chennai = 0
        elif source == "Chennai":
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 1
        else:
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0
        source_des = st.selectbox("Select Desingnation", ["Cochin",
                                                          "Delhi",
                                                          "Banglore",
                                                          "Hyderabad",
                                                          "Kolkata"])
        if source_des == "Cochin":
            d_Cochin = 1
            d_Delhi = 0
            d_Banglore = 0
            d_Hyderabad = 0
            d_Kolkata = 0
        elif source_des == "Delhi":
            d_Cochin = 0
            d_Delhi = 1
            d_Banglore = 0
            d_Hyderabad = 0
            d_Kolkata = 0
        elif source_des == "Banglore":
            d_Cochin = 0
            d_Delhi = 0
            d_Banglore = 1
            d_Hyderabad = 0
            d_Kolkata = 0
        elif source_des == "Hyderabad":
            d_Cochin = 0
            d_Delhi = 0
            d_Banglore = 0
            d_Hyderabad = 1
            d_Kolkata = 0
        elif source_des == "Kolkata":
            d_Cochin = 0
            d_Delhi = 0
            d_Banglore = 0
            d_Hyderabad = 0
            d_Kolkata = 1
        else:
            d_Cochin = 0
            d_Delhi = 0
            d_Banglore = 0
            d_Hyderabad = 0
            d_Kolkata = 0
        button = st.form_submit_button("predict")
        if button:
            prediction = model.predict([[
                Total_stops,
                Journey_day,
                Journey_month,
                Dep_hour,
                Dep_min,
                Arrival_hour,
                Arrival_min,
                dur_hour,
                dur_min,
                Air_India,
                GoAir,
                IndiGo,
                Jet_Airways,
                Jet_Airways_Business,
                Multiple_carriers,
                Multiple_carriers_Premium_economy,
                SpiceJet,
                Trujet,
                Vistara,
                Vistara_Premium_economy,
                s_Chennai,
                s_Delhi,
                s_Kolkata,
                s_Mumbai,
                d_Cochin,
                d_Delhi,
                d_Hyderabad,
                d_Kolkata,
                d_Banglore
            ]])

            output = round(prediction[0], 0)

            st.success("Your Flight price Rs.{}".format(output))

if selected == "About Me":
    st.header("Hi, I am R.sarath kumar:wave:")
    st.subheader("A Newbie Data Scientist Aspirer  From Bsc Biotech Background")
    st.write("I am passionate about learning python to be more efficient and effective in **AI and ML Projects**")
    st.write("Check out my other projects in GitHub : https://github.com/sarathkumar1304")





