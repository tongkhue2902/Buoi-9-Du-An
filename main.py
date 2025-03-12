import streamlit as st
import os
st.set_page_config(page_title = "Tiếng động vật")
st.title("Tiếng các con vật")
def url(file):
  f = os.getcwd()
  return f + "/" + file
col1, col2, col3 = st.columns(3)

with col1:
  b1 = st.button("Bấm để nghe tiếng con chó")
if b1:
  dog = "https://dogagingproject.org/_next/image?url=https%3A%2F%2Fcontent.dogagingproject.org%2Fwp-content%2Fuploads%2F2020%2F11%2Fhelena-lopes-S3TPJCOIRoo-unsplash-scaled.jpg&w=1200&q=75"
  st.image(dog, caption = "Con chó")
  
  st.audio(url("dog.mp3"))
  
  vid1 = "https://www.youtube.com/watch?v=lycJwHNdYug"
  st.video(vid1)

with col2:
  b2 = st.button("Bấm để nghe tiếng con mèo")
if b2:
  cat = "https://images.pexels.com/photos/10520684/pexels-photo-10520684.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
  st.image(cat, caption = "Con mèo")

  st.audio(url("cat.wav"))

  vid2 = "https://www.youtube.com/watch?v=WRlSx_qpFk8"
  st.video(vid2)

with col3:
  b3 = st.button("Bấm để nghe tiếng con vịt")
if b3:
  duck = "https://images.unsplash.com/photo-1465153690352-10c1b29577f8?q=80&w=1430&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
  st.image(duck, caption = "Con vịt")

  st.audio(url("duck.mp3"))

  vid3 = "https://www.youtube.com/watch?v=e90eWYPNtJ8"
  st.video(vid3)
