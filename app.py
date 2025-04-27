import streamlit as st

def main():
    st.title("User Details Form")

    # Create input fields
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", min_value=0, max_value=120)
    email = st.text_input("Enter your email:")

    # Submit button
    if st.button("Submit"):
        st.success("Details Submitted Successfully!")
        st.write("### Here are the details you entered:")
        st.write(f"**Name:** {name}")
        st.write(f"**Age:** {age}")
        st.write(f"**Email:** {email}")

if __name__ == "__main__":
    main()

