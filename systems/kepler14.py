import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exoplanet_engine import analyze_system

# Planet in a visual binary star system configuration
analyze_system(
    target_name='Kepler-14',
    r_star=2.048,  # Highly evolved star (2.04x Solar Radii)
    m_star=1.512,  # 1.51x Solar Mass
    quarter=2
)
