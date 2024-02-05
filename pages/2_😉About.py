import streamlit as st


st.subheader("Hello, I am Huma Dawari and here I teach you programming languages, here you can find information about programming and if you "
          "want to download streamlit, you can rfer to this website. And if you want to learn, then you can register here, Thank you😊 ")



st.divider()
# video
vid = open('Untitled 19_1080p.mp4', 'rb').read()
st.video(vid)


col1, col2 = st.columns(2)

with col1:
    st.write("coding")
    st.text("Coding is the process of transforming "
            "computer instructions into a form a computer"
            " can understand. Every website and app operates "
            "because programmers write code. However,"
            " you do not have to work in technology to use coding. "
            "In fact, job hunters can find most coding "
            "jobs outside of the tech industry.")



with col2:
    st.write("programmer")
    st.text("A computer programmer, "
            "sometimes referred to as a software developer,"
            " a software engineer, a programmer or a coder, "
            "is a person who creates computer programs.")
