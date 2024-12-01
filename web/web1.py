from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie

#Find more emojis here:https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title='My webpage', page_icon=':tada:', layout='wide')

def load_lottieur1(ur1):
    r = requests.get(ur1)
    if r.status_code != 200:
        return None
    return r.json()

#--- USE LOCAL CSS---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

#--- LOAD ASSETS ---
lottie_coding = ('https://lottie.host/7f4cdad1-9cb1-4689-a98a-a7cd26b6e29c/w2IpF8UQ4A.json')
img_christmas = Image.open('images/christmas.png')

#--- HEADER SECTION ---
with st.container():
    st.subheader("Hi, I'm Panch(with an a)")
    st.title("An EX LOL PRO player")
    st.write("I'm doing side quests now🥷")
    st.write('[This is literally me btw ->](https://www.youtube.com/shorts/-r2Z9ZFFork)')

#--- WHAT I DO ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do(as a sigma male🤫)")
        st.write('##')
        st.write(
            """
            - I'm looks maxing🥶
            - I drink water😈
            - I don't answer my calls😮‍💨
            - Also study sometimes🤓
            """
        )
        st.write('[Also me ->](https://www.youtube.com/shorts/lWS1vQKJER4)')
    with right_column:
        st_lottie(lottie_coding, height=400, key='coding')

#--- CHRISTMAS ---
with st.container():
    st.write("---")
    st.header('Christmas is coming🎅')
    image_coulumn, text_column = st.columns((1, 2))
    with image_coulumn:
        st.image(img_christmas)
    with text_column:
        st.write('[If you were a good boy this year click this link -->](https://www.youtube.com/watch?v=S-bwNgwIcsM)')
        st.write('[If you were a bad boy this year click this link -->](https://www.youtube.com/watch?v=41KB61r7p0w)')

#--- CONTACT ---
with st.container():
    st.write("---")
    st.header("Let's be sigmas together🐺!")
    st.write('##')

    #https://formsubmit.co
    contact_form = """
    <form action="https://formsubmit.co/panostrmpks@gmail.com" method="POST">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder ="Your name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your message here" required></textarea>
         <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()