import streamlit as st
import pickle
import numpy as np
from PIL import Image
model=pickle.load(open('model.pkl','rb'))


def predict_forest(EmotionalAdjustment,IntegrityControl,IntellectualEfficiency,InterpersonalRelationships):
    input=np.array([[EmotionalAdjustment,IntegrityControl,IntellectualEfficiency,InterpersonalRelationships]]).astype(np.float64)
    prediction=model.predict_proba(input)
    pred='{0:.{1}f}'.format(prediction[0][0], 4)
    return float(pred)
image = Image.open('image1.png')
from PIL import Image

def main():
    st.image(image,width=400,height=250)
    html_temp = """
    <div style="background-color:#000099 ;padding:10px">
    <h2 style="color:white;text-align:center;">Predictive Staffing Model</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.text('Enter these values of a particular Candidate from their 16PF score')
    EmotionalAdjustment = st.text_input("EmotionalAdjustment")
    IntegrityControl = st.text_input("IntegrityControl")
    IntellectualEfficiency = st.text_input("IntellectualEfficiency")
    InterpersonalRelationships = st.text_input("InterpersonalRelationships")
    safe_html="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h1 style="color:white;text-align:center;"> You can place this person in top 10 CTA Stations</h1>
       <h2 style="color:white;text-align:center;">Red/Purple/Brown Lines Belmont</h2>
       <h2 style="color:white;text-align:center;">Clark/Lake Station (Brown Pink Orange Purple & Green)</h2>
       <h2 style="color:white;text-align:center;">Blue Line Pulaski Station</h2>
       <h2 style="color:white;text-align:center;">South Shop Bravo-Bone Yard</h2>
       <h2 style="color:white;text-align:center;">Red Line 79th Street Station</h2>
       <h2 style="color:white;text-align:center;">Red Line Jackson Station</h2>
       <h2 style="color:white;text-align:center;">63rd Street Lower Rail Yard</h2>
       <h2 style="color:white;text-align:center;">Blue Line O'Hare Station</h2>
       <h2 style="color:white;text-align:center;">Red Line 69th Street Station</h2>
       <h2 style="color:white;text-align:center;">Skokie Rail Yard</h2>
       </div>
    """
    danger_html="""  
      <div style="background-color:#F08080;padding:10px >
       <h1 style="color:black ;text-align:center;"> You can't Hire this person | CTA stations with low Crime Rate</h1>
       <h2 style="color:white;text-align:center;">Washington/Wabash Station (Brown, Pink, Orange, Purple & Green)</h2>
       <h2 style="color:white;text-align:center;">Red Line Garfield Station</h2>
       <h2 style="color:white;text-align:center;">Red Line Clark/Division Station</h2>
       <h2 style="color:white;text-align:center;">Pink/Green Clinton Station</h2>
       <h2 style="color:white;text-align:center;">Orange Line Pulaski Station</h2>
       <h2 style="color:white;text-align:center;">LaSalle/Van Buren (Brown,Pink,Orange & Purple)</h2>
       <h2 style="color:white;text-align:center;">Coal Yard</h2>
       <h2 style="color:white;text-align:center;">Red Line Sox-35th Station</h2>
       <h2 style="color:white;text-align:center;"> West Shop</h2>
       <h2 style="color:white;text-align:center;">Blue Line Cicero Station</h2>
       </div>
    """

    if st.button("Predict"):
        output=predict_forest(EmotionalAdjustment,IntegrityControl,IntellectualEfficiency,InterpersonalRelationships)
        #st.success('The probability of not hiring a Person is {}'.format(output))

        if output > 0.5:
            st.markdown(danger_html,unsafe_allow_html=True)
        else:
            st.markdown(safe_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()