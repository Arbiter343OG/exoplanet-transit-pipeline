import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exoplanet_engine import analyze_system

# Run pipeline for a Habitable Zone target
analyze_system(
    target_name='Kepler-22',
    r_star=0.979,  # 0.97x Solar Radii
    m_star=0.970,  # 0.97x Solar Mass
    quarter=12     # Quarter 12 captures a longer window necessary for wider orbits
)
