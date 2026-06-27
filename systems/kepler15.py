import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exoplanet_engine import analyze_system

# High-density, metal-rich gas giant ("Heavy Jupiter")
analyze_system(
    target_name='Kepler-15',
    r_star=0.992,  # 0.99x Solar Radii
    m_star=1.018,  # 1.01x Solar Mass
    quarter=2
)
