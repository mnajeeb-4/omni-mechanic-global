"""
The Global Tool Encyclopedia. Massive dictionary for all mechanic domains.
"""
TOOLS_DB = {
    "Diagnostic Multimeter": {
        "domain": ["electrical", "auto", "hvac"],
        "icon_url": "https://img.icons8.com/color/96/multimeter.png",
        "description": "Measures voltage, current, and resistance in circuits.",
        "usage": "Set dial to Vdc, connect probes in parallel to test live wires."
    },
    "Torque Wrench": {
        "domain": ["auto", "moto", "heavy"],
        "icon_url": "https://img.icons8.com/color/96/torque-wrench.png",
        "description": "Applies exact torque to bolts to prevent overtightening.",
        "usage": "Set the required Nm value, click when torque is reached."
    },
    "Bearing Puller": {
        "domain": ["auto", "moto", "hvac", "heavy"],
        "icon_url": "https://img.icons8.com/color/96/puller.png",
        "description": "Removes stuck bearings, gears, and pulleys from shafts.",
        "usage": "Attach jaw grips to the bearing, tighten the central screw."
    },
    "Vernier Caliper": {
        "domain": ["auto", "moto", "heavy", "electrical"],
        "icon_url": "https://img.icons8.com/color/96/caliper.png",
        "description": "Precision tool for measuring internal/external dimensions.",
        "usage": "Slide the jaws, read main and vernier scale combined."
    },
    "Pipe Wrench": {
        "domain": ["plumbing", "hvac"],
        "icon_url": "https://img.icons8.com/color/96/pipe-wrench.png",
        "description": "Heavy-duty adjustable wrench for gripping and turning pipes.",
        "usage": "Set jaws to pipe size, turn counterclockwise to loosen."
    },
    "Digital Clamp Meter": {
        "domain": ["electrical", "hvac", "auto"],
        "icon_url": "https://img.icons8.com/color/96/clamp-meter.png",
        "description": "Measures AC current without breaking the circuit.",
        "usage": "Clamp around a single wire, read the amperage."
    },
    "Screwdriver Set": {
        "domain": ["all"],
        "icon_url": "https://img.icons8.com/color/96/screwdriver.png",
        "description": "Essential for loosening/tightening various fasteners.",
        "usage": "Match the tip (Phillips/Flat) to the screw head."
    }
}

def get_tools_for_domain(domain: str):
    """Filter tools based on the active mechanic domain."""
    return {k: v for k, v in TOOLS_DB.items() if domain in v["domain"] or "all" in v["domain"]}
