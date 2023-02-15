import json
import streamlit as st
from streamlit_lottie import st_lottie
import pyttsx3
col1, col2 = st.columns(2)
with col1:
    st.markdown("""## Basic Chat bot by Sudhanshu""")
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
with col1:
    lottie_now = load_lottiefile("file/code.json")
st_lottie(lottie_now,speed=1,reverse=False,loop=True,quality="low",height=300,key=None,)
st.success("Hi! Myself Jaisu")
engine = pyttsx3.init()

def speak(text):
 engine.say(text)
engine.runAndWait()
s="Myself Jaisu, Just an innocent Software user-interface"
speak(s)
suu = st.text_input("How can i help you")

if suu == "Hi":
    data = "Hi myself Jaisu, I'm Basically a ChatBot"
elif suu == "How are you":
    data = "I'm fine how are you"
else:
    data = "I don't understand, what you want to say."
response = data
st.write("Jaisu")
st.success(response)
speak(response)

