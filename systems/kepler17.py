import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exoplanet_engine import analyze_system

# Planet orbiting a hyper-active star with high starspot activity
analyze_system(
    target_name='Kepler-17',
    r_star=1.025,  # 1.02x Solar Radii
    m_star=1.023,  # 1.02x Solar Mass
    quarter=2
)
