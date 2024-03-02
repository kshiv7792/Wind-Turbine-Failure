
import streamlit as st
import pickle
import numpy as np
model = pickle.load(open('model_final.pkl','rb'))



st.set_page_config(
    page_title="Prediction App",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
)

from PIL import Image
image = Image.open('img.jpg')

st.image(image,
      use_column_width=True)


def predict_failure(Wind_speed, Power, Nacelle_ambient_temperature, Generator_bearing_temperature,Gear_oil_temperature, Ambient_temperature, Rotor_Speed,Nacelle_temperature, Generator_speed,Yaw_angle,Wind_direction,Gear_box_inlet_temperature, Bearing_temperature,Wheel_hub_temperature):
	
	input=np.array([[Wind_speed, Power, Nacelle_ambient_temperature, Generator_bearing_temperature,Gear_oil_temperature, Ambient_temperature, Rotor_Speed,Nacelle_temperature,        	Generator_speed,Yaw_angle,Wind_direction,Gear_box_inlet_temperature, Bearing_temperature,Wheel_hub_temperature]]).astype(np.float64)
	prediction = model.predict(input)
    	
	return (prediction)


def main():
    #st.title("Wind Turbine Failure Prediction")
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Wind Turbine Failure Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)

    Wind_speed = st.text_input("Wind_speed")
    Power = st.text_input("Power")
    Nacelle_ambient_temperature = st.text_input("Nacelle_ambient_temperature")
    Generator_bearing_temperature = st.text_input("Generator_bearing_temperature")
    Gear_oil_temperature = st.text_input("Gear_oil_temperature")
    Ambient_temperature = st.text_input("Ambient_temperature")
    Rotor_Speed = st.text_input("Rotor_Speed")
    Nacelle_temperature = st.text_input("Nacelle_temperature")
    Generator_speed = st.text_input("Generator_speed")
    Yaw_angle = st.text_input("Yaw_angle")
    Wind_direction = st.text_input("Wind_direction")
    Gear_box_inlet_temperature = st.text_input("Gear_box_inlet_temperature")
    Bearing_temperature = st.text_input("Bearing_temperature")
    Wheel_hub_temperature = st.text_input("Wheel_hub_temperature")

    safe_html ="""  
      <div style="background-color:#80ff80; padding:10px >
      <h2 style="color:white;text-align:center;"> The Abalone is young</h2>
      </div>
    """
    warn_html ="""  
      <div style="background-color:#F4D03F; padding:10px >
      <h2 style="color:white;text-align:center;"> The Abalone is middle aged</h2>
      </div>
    """
    danger_html="""  
      <div style="background-color:#F08080; padding:10px >
       <h2 style="color:black ;text-align:center;"> The Abalone is old</h2>
       </div>
    """

    if st.button("Predict the failure"):
        output = predict_failure(Wind_speed, Power,Nacelle_ambient_temperature, Generator_bearing_temperature,Gear_oil_temperature,Ambient_temperature,Rotor_Speed,Nacelle_temperature, 	Generator_speed,Yaw_angle,Wind_direction,Gear_box_inlet_temperature, Bearing_temperature,Wheel_hub_temperature)
        st.success(output)

        
if __name__=='__main__':
    main()