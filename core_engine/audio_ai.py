"""
Acoustic analysis module using Librosa.
Detects bearing squeaks, misfires, and excessive pitch deviations.
"""
import librosa
import numpy as np

class AudioAI:
    def analyze_audio_data(self, audio_bytes: bytes, sample_rate: int = 22050) -> dict:
        """Analyze audio chunk (bytes) for mechanical faults."""
        try:
            # Convert bytes to numpy array (floats)
            y = np.frombuffer(audio_bytes, dtype=np.int16).astype(np.float32) / 32768.0
            if len(y) == 0:
                return {"fault": "No audio detected", "severity": "HEALTHY"}
            
            # 1. Pitch Deviation
            pitches, magnitudes = librosa.piptrack(y=y, sr=sample_rate)
            pitch = pitches[magnitudes.argmax(axis=0)]
            pitch = pitch[pitch > 0]
            if len(pitch) > 0:
                deviation = np.std(pitch) / np.mean(pitch) * 100
            else:
                deviation = 0.0

            # 2. High Frequency Bearing Noise
            fft = np.abs(librosa.stft(y))
            freqs = librosa.fft_frequencies(sr=sample_rate)
            high_freq_mask = freqs > 2000
            high_ratio = np.sum(fft[high_freq_mask, :]) / np.sum(fft) if np.sum(fft) > 0 else 0
            
            if deviation > 15.0:
                return {"fault": "Severe Engine Misfire / Unstable RPM", "severity": "CRITICAL"}
            elif high_ratio > 0.35:
                return {"fault": "Bearing Squeak / High-freq wear", "severity": "WARNING"}
            else:
                return {"fault": "Healthy Mechanical Range", "severity": "HEALTHY"}
        except Exception as e:
            return {"fault": "Audio processing error", "severity": "HEALTHY", "error": str(e)}
