

import streamlit as st
import os

# Directory to save audio recordings
SAVE_DIR = "recording"
os.makedirs(SAVE_DIR, exist_ok=True)

# Initialize session state for navigation and audio data
if "page" not in st.session_state:
    st.session_state.page = "Home"

if "recorded_file" not in st.session_state:
    st.session_state.recorded_file = None

if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None

# Navigation function
def navigate_to(page_name):
    st.session_state.page = page_name

# Page content
if st.session_state.page == "Home":
    st.title("Audio Dashboard")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Record File", use_container_width=True):
            navigate_to("Record")  # Navigate to Record page

    with col2:
        if st.button("Browse File", use_container_width=True):
            navigate_to("Browse")  # Navigate to Browse page

elif st.session_state.page == "Record":
    st.title("Record Audio")
    st.write("Press the start button to record audio:")

    # Use st.audio_input for recording audio
    audio_bytes = st.audio_input("Record your audio", key="audio_input")

    if audio_bytes:
        # Ensure audio_bytes is properly extracted if it is an UploadedFile
        if hasattr(audio_bytes, "read"):
            audio_bytes = audio_bytes.read()  # Extract bytes

        # Save the audio file to disk if needed
        file_path = os.path.join(SAVE_DIR, "recorded_audio.wav")
        with open(file_path, "wb") as f:
            f.write(audio_bytes)

        st.session_state.recorded_file = file_path
        st.audio(audio_bytes, format="audio/wav")  # Play the recorded audio
        st.success(f"Recording saved as {file_path}.")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back to Home", use_container_width=True):
            navigate_to("Home")

    with col2:
        if st.button("Audio Process", use_container_width=True):
            navigate_to("Process")

elif st.session_state.page == "Browse":
    st.title("Upload an Audio File")
    uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3", "m4a"])
    if uploaded_file is not None:
        # Extract bytes from the uploaded file
        audio_bytes = uploaded_file.read()

        # Save the uploaded file for processing
        file_path = os.path.join(SAVE_DIR, "uploaded_audio.wav")
        with open(file_path, "wb") as f:
            f.write(audio_bytes)

        st.session_state.uploaded_file = file_path
        st.audio(audio_bytes, format="audio/wav", autoplay=True)
        st.success(f"Audio file uploaded and saved as {file_path}!")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back to Home", use_container_width=True):
            navigate_to("Home")

    with col2:
        if st.button("Audio Process", use_container_width=True):
            navigate_to("Process")

elif st.session_state.page == "Process":
    st.title("Audio Processing")
    
    if st.session_state.recorded_file or st.session_state.uploaded_file:
        st.write("Processing the following audio files:")

        # Display and process the recorded file
        if st.session_state.recorded_file:
            st.audio(st.session_state.recorded_file, format="audio/wav")
            st.success("Recorded audio is processed.")

        # Display and process the uploaded file
        if st.session_state.uploaded_file:
            st.audio(st.session_state.uploaded_file, format="audio/wav")
            st.success("Uploaded audio is processed.")
    else:
        st.warning("No audio file available for processing. Please record or upload an audio file first.")

    if st.button("Back to Home", use_container_width=True):
        navigate_to("Home")
