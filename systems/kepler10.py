import sys
import os

# Allow Python to see the main directory folder
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exoplanet_engine import analyze_system

# Run calculation using unique Kepler-10 metrics
analyze_system(
    target_name='Kepler-10B',
    r_star=1.056,  # Solar Radius
    m_star=0.913,  # Solar Mass
    quarter=3
)