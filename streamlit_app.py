import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

model = data["model"]
nationalities = data["nationalities"]
clubs = data["clubs"]
nationalities_list = data["nationalities_list"]
clubs_list = data["clubs_list"]
te_nationalities = data["te_nationalities"]
te_clubs = data["te_clubs"]

body_types = (
    "Lean",
    "Stocky",
    "Normal",
)

st.write(
    """
    # Sports Prediction

    A Machine Learning App that predicts the Overall Ranking of FIFA 19 Players 
    based on a collection of detailed attributes for every player.

    """
)

st.write('Please enter player attributes to predict their overall ranking:')

st.subheader('Profile')
f1=st.number_input('Age',16,45)
f29 = st.selectbox("Nationality", nationalities_list)
f30 = st.selectbox("Club", clubs_list)
f6=st.number_input('Value',0,200000000,1000000,1000000)
f16=st.number_input('Wage',0,1000000,0,1000)
f10=st.number_input('Release Clause',0,300000000,1000000,1000000)
f7=st.number_input('Special',700,2500,700,100)
f25 = st.selectbox("Body Type", body_types)
f24=st.slider('International Reputation', 1, 5)
f4=st.slider('Potential', 50, 100)

st.subheader('Position')
f23=st.slider('Striker', 0, 100)
f2=st.slider('Left Striker', 0, 100)
f9=st.slider('Right Striker', 0, 100)
f15=st.slider('Center Back', 0, 100)
f22=st.slider('Left Center Back', 0, 100)
f8=st.slider('Right Center Back', 0, 100)
f14=st.slider('Right Back', 0, 100)
f17=st.slider('Left Back', 0, 100)
f18=st.slider('Right Wing-Back', 0, 100)
f20=st.slider('Central Defensive Midfielder', 0, 100)
f19=st.slider('Right Defensive Midfielder', 0, 100)
f21=st.slider('Left Defensive Midfielder', 0, 100)

st.subheader('Skills')
f11=st.slider('GKDiving', 0, 100)
f12=st.slider('LongShots', 0, 100)
f13=st.slider('Reactions', 10, 100)
f28=st.slider('Aggression', 10, 100)
f3=st.slider('Volleys', 0, 100)
f5=st.slider('Dribbling', 0, 100)

# Prediction
ok = st.button('Predict Overall Ranking')

if f25 == 'Lean':
    f25 = 1
    f26 = 0
    f27 = 0
elif f25 == 'Stocky':
    f25 = 0
    f26 = 1
    f27 = 0
elif f25 == "Normal":
    f25 = 0
    f26 = 0
    f27 = 1

if ok:
    X_test=[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21,f22,f23,f24,f25,f26,f27,f28,f29,f30]
    
    def te_nationalities():
        if X_test[28] in nationalities.index:
            X_test[28]=int(nationalities.loc[X_test[28]])
    
    def te_clubs():
        if X_test[29] in clubs.index:
            X_test[29]=int(clubs.loc[X_test[29]])
    
    te_nationalities=te_nationalities()
    te_clubs=te_clubs()
    
    X_test=np.array(X_test).reshape(1,-1)

    overall = model.predict(X_test)
    st.subheader(f"The estimated overall ranking is {overall[0]:.2f}")