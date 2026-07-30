"""
Luxury Claymorphism + Glassmorphism CSS injection.
Designed for a Canva-grade, high-end UX.
"""
def load_clay_glass_css() -> str:
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
        
        * { font-family: 'Inter', sans-serif; }
        
        /* Global Dark Background */
        .stApp {
            background: #0E1117;
            color: #E6E6E6;
        }
        
        /* Glassmorphism Panel */
        .glass-panel {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 24px;
            padding: 24px;
            margin-bottom: 20px;
        }
        
        /* Claymorphism Card (Soft 3D Matte) */
        .clay-card {
            background: #161B22;
            border-radius: 24px;
            padding: 24px;
            box-shadow: 12px 12px 24px rgba(0, 0, 0, 0.8),
                        -6px -6px 12px rgba(255, 255, 255, 0.04);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            border: 1px solid rgba(255, 255, 255, 0.03);
        }
        .clay-card:hover {
            transform: translateY(-4px);
            box-shadow: 16px 16px 32px rgba(0, 0, 0, 0.9),
                        -8px -8px 16px rgba(255, 255, 255, 0.06);
        }
        
        /* Glowing Badges for AR */
        .badge-critical {
            background: rgba(255, 0, 0, 0.85);
            color: white;
            padding: 4px 14px;
            border-radius: 20px;
            font-weight: 700;
            font-size: 0.75rem;
            letter-spacing: 0.5px;
            box-shadow: 0 0 15px rgba(255, 0, 0, 0.4);
            display: inline-block;
        }
        .badge-warning {
            background: rgba(255, 204, 0, 0.85);
            color: #111;
            padding: 4px 14px;
            border-radius: 20px;
            font-weight: 700;
            font-size: 0.75rem;
            letter-spacing: 0.5px;
            box-shadow: 0 0 15px rgba(255, 204, 0, 0.4);
            display: inline-block;
        }
        
        /* Clay Button */
        .stButton button {
            background: #6C63FF;
            color: white;
            border: none;
            border-radius: 16px;
            padding: 10px 24px;
            font-weight: 600;
            box-shadow: 8px 8px 16px rgba(0, 0, 0, 0.5), -4px -4px 8px rgba(255, 255, 255, 0.05);
            transition: all 0.2s ease;
        }
        .stButton button:hover {
            transform: scale(1.02);
            background: #7B74FF;
            box-shadow: 10px 10px 20px rgba(0, 0, 0, 0.6);
        }

        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 12px;
            background: transparent;
        }
        .stTabs [data-baseweb="tab"] {
            background: #161B22;
            border-radius: 16px;
            padding: 8px 20px;
            color: #A0A0A0;
            box-shadow: 4px 4px 8px rgba(0,0,0,0.4);
        }
        .stTabs [aria-selected="true"] {
            background: #6C63FF;
            color: white;
            box-shadow: 0 0 20px rgba(108, 99, 255, 0.3);
        }
        
        /* WebRTC Container */
        .webrtc-container {
            border-radius: 24px;
            overflow: hidden;
            box-shadow: 12px 12px 24px rgba(0,0,0,0.7);
            border: 1px solid rgba(255,255,255,0.05);
        }
    </style>
    """
