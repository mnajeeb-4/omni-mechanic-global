"""
WebRTC Pipeline for live video/audio streaming.
Coordinates VisionAI, AudioAI, and GroqBrain.
"""
import cv2
import av
import numpy as np
from streamlit_webrtc import WebRtcMode, webrtc_streamer
import streamlit as st
import threading
import queue

class OmniWebRTCProcessor:
    def __init__(self, vision_ai, audio_ai, groq_brain, domain):
        self.vision_ai = vision_ai
        self.audio_ai = audio_ai
        self.groq_brain = groq_brain
        self.domain = domain
        self.audio_queue = queue.Queue()
        self.last_detections = []
        self.last_audio_result = {"fault": "Listening..."}

    def recv_video(self, frame: av.VideoFrame) -> av.VideoFrame:
        """Video Callback: Process frame with YOLO, draw boxes, return to Streamlit."""
        img = frame.to_ndarray(format="bgr24")
        img, detections = self.vision_ai.process_frame(img)
        self.last_detections = detections
        return av.VideoFrame.from_ndarray(img, format="bgr24")

    def recv_audio(self, frame: av.AudioFrame) -> av.AudioFrame:
        """Audio Callback: Send bytes to AudioAI for processing."""
        self.audio_queue.put(frame.to_ndarray().tobytes())
        return frame

    def process_queued_audio(self):
        """Background thread to flush audio buffer to AI."""
        while True:
            try:
                audio_data = self.audio_queue.get(timeout=0.1)
                self.last_audio_result = self.audio_ai.analyze_audio_data(audio_data)
            except queue.Empty:
                pass

def render_live_stream(domain: str):
    vision_ai = core_engine.vision_ai.VisionAI()
    audio_ai = core_engine.audio_ai.AudioAI()
    groq_brain = core_engine.groq_llm_brain.GroqBrain()
    
    processor = OmniWebRTCProcessor(vision_ai, audio_ai, groq_brain, domain)
    
    # Start audio background thread
    threading.Thread(target=processor.process_queued_audio, daemon=True).start()

    webrtc_ctx = webrtc_streamer(
        key=f"omnimechanic-{domain}",
        mode=WebRtcMode.SENDRECV,
        video_processor_factory=lambda: processor.recv_video,
        audio_processor_factory=lambda: processor.recv_audio,
        rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
        media_stream_constraints={"video": True, "audio": True},
    )

    # Display Live Context Panels
    col_viz, col_audio, col_groq = st.columns([2, 1, 1])
    
    with col_viz:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.subheader("🔴 Live AR Overlay")
        if webrtc_ctx.state.playing:
            st.success("Stream is LIVE")
        else:
            st.warning("Press 'Start Diagnostics' to initiate stream.")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col_audio:
        st.markdown('<div class="clay-card">', unsafe_allow_html=True)
        st.subheader("🎧 Live Acoustic")
        result = processor.last_audio_result
        severity = result.get("severity", "HEALTHY")
        badge_class = "badge-critical" if severity == "CRITICAL" else "badge-warning" if severity == "WARNING" else ""
        st.markdown(f"**Status:** {result.get('fault', 'Analyzing...')} <span class='{badge_class}'>{severity}</span>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_groq:
        st.markdown('<div class="clay-card">', unsafe_allow_html=True)
        st.subheader("🤖 Copilot")
        user_question = st.text_input("Ask the AI (e.g., 'How do I fix this?')")
        if st.button("Get Fix Instructions", use_container_width=True):
            context = f"Detected: {processor.last_detections}. Audio: {result}"
            with st.spinner("Thinking like a master mechanic..."):
                response = groq_brain.get_response(domain, user_question, context, str(result))
            st.markdown(response)
        st.markdown('</div>', unsafe_allow_html=True)
