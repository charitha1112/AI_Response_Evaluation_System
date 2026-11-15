import streamlit as st
import requests

st.set_page_config(
    page_title="AI Response Evaluation System",
    page_icon="🤖",
    layout="centered"
)

st.title("AI Response Evaluation System")
st.write("Submit an AI-generated response for evaluation.")

# Input fields
question = st.text_area("Enter your Question")

ai_response = st.text_area("Enter AI Response")

reference_answer = st.text_area(
    "Optional: Reference Answer"
)

source = st.text_area(
    "Optional: Source Information"
)

# Submit button
if st.button("Submit for Evaluation"):

    if not question.strip() or not ai_response.strip():
        st.error("Please enter both the question and AI response.")

    else:
        # Prepare input data
        payload = {
            "question": question,
            "ai_response": ai_response,
            "reference_answer": reference_answer or None,
            "source": source or None
        }

        try:
            # Send data to FastAPI
            response = requests.post(
                "http://127.0.0.1:8000/evaluate",
                json=payload,
                timeout=10
            )

            if response.status_code == 200:
                st.success("Input successfully sent to FastAPI!")

                st.subheader("Backend Response")
                st.json(response.json())

            else:
                st.error(f"API Error: {response.status_code}")

        except requests.exceptions.ConnectionError:
            st.error("Cannot connect to FastAPI. Check whether the backend is running.")

        except requests.exceptions.Timeout:
            st.error("The backend took too long to respond.")