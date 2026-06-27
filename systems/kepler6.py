import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exoplanet_engine import analyze_system

# Massive, classic Hot Jupiter
analyze_system(
    target_name='Kepler-6',
    r_star=1.391,  # 1.39x Solar Radii
    m_star=1.082,  # 1.08x Solar Mass
    quarter=2
)
