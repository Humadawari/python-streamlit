import streamlit as st


st.header("You can connect with me here")

st.divider()
st.subheader("if you have any questions, you can email me📧")
st.markdown("humadawari@gmail.com")

st.subheader("You can find me here on Linkedin📱")
st.markdown("https://www.linkedin.com/in/huma-dawari-3b35292a4?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app")




linkedin = st.text_input('Enter your linkedin ID:')
if 'https://www.linkedin.com/in' in linkedin:
    st.write(f"confirm your linkedin ID is {linkedin}")

if st.checkbox('Show/Hide'):
    st.text('If you like our website you can visit my other websites just here email me humadawari@gmail.com')




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


