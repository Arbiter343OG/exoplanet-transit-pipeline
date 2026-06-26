import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exoplanet_engine import analyze_system

# Run pipeline for a highly compact multi-planet system
analyze_system(
    target_name='Kepler-11',
    r_star=1.065,  # 1.06x Solar Radii
    m_star=0.961,  # 0.96x Solar Mass
    quarter=6
)
