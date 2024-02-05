import streamlit as st



st.subheader("You can find YouTube links of programming languages here🎥")
st.divider()

st.subheader(" ✔PYTHON PROGRAMMING LANGUAGE")
st.markdown("https://youtube.com/playlist?list=PLsyeobzWx|7poL9JTVyndKe62ieoN-MZ3&si=3L6WE00kapjKzrNQ")

st.subheader(" ✔JAVASCRIPT PROGRAMMING LANGUAGE")
st.markdown("https://youtu.be/W6NZfCO5SIk?si=TMFTtLJyBxV9RebM")

st.subheader(" ✔C++ PROGRAMMING LANGUAGE")
st.markdown("https://youtu.be/ZzaPdXTrSb8?si=XuuYInARv-GajSkm")

st.subheader(" ✔JAVA PROGRAMMING LANGUAGE")
st.markdown("https://youtu.be/eIrMbAQSU34?si=jTQr8JCZTInWBv0-")

st.subheader(" ✔C PROGRAMMING LANGUAGE")
st.markdown("https://youtu.be/KJgsSFOSQv0?si=ilZY__mb2-YMdGE-")

st.subheader(" ✔RUBY PROGRAMMING LANGUAGE")
st.markdown("https://youtu.be/t_ispmWmdjY?si=EFw4MAdJnr-eGd7G")
st.subheader(" ✔C# PROGRAMMING LANGUAGE")
st.markdown("https://youtu.be/gfkTfcpWqAY?si=sWxboAp00HMRBOmj")
st.markdown(
    "In short, a programming language is the way in which a computer programmer talks to a device. If you know how to speak one of these languages and there are hundreds you can create a program that can perform tasks. These can range from the very simple, like a script that moves a file from one place to another, to the very complex, like rendering a 3D world in a video game.")

message = st.text_area('Give your Experience about Coding')



col1, col2 = st.sidebar.columns(2)

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


