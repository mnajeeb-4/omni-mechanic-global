"""
Groq LLM Brain. The centralized reasoning engine for OmniMechanic.
"""
import streamlit as st
from groq import Groq

class GroqBrain:
    def __init__(self):
        self.client = Groq(api_key=st.secrets["GROQ_API_KEY"])
        self.system_prompts = {
            "auto": "You are an expert Automotive Mechanic with 40 years of experience.",
            "moto": "You are a world-class Motorcycle diagnostic specialist.",
            "electrical": "You are a Master Electrician specialized in wiring and PCBs.",
            "home": "You are an elite Appliance Repair Technician.",
            "plumbing": "You are a Senior Plumber and HVAC engineer."
        }

    def get_response(self, domain: str, user_query: str, vision_context: str, audio_context: str) -> str:
        """Send a comprehensive context to Groq for reasoning."""
        system_prompt = self.system_prompts.get(domain, "You are a general mechanical AI.")
        
        prompt = f"""
        {system_prompt}
        
        The user is showing a live feed of a machine.
        Vision Context (AR Detections): {vision_context}
        Audio Context (Acoustic Analysis): {audio_context}
        
        User Question: {user_query}
        
        Please respond in the following strict format:
        1. **The Fault**: Identify the exact issue.
        2. **The Fix**: Provide a step-by-step repair process.
        3. **Exact Tools Needed**: List specific tools from the OmniMechanic database.
        Always prioritize safety protocols.
        """
        
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                model="llama-3.3-70b-versatile",
                temperature=0.3,
                max_tokens=1024,
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            return f"⚠️ Groq API Error: {str(e)}. Please check your API key."
