import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exoplanet_engine import analyze_system

# First-ever multi-transiting system candidate (Kepler-9b)
analyze_system(
    target_name='Kepler-9',
    r_star=1.023,  # 1.02x Solar Radii
    m_star=1.022,  # 1.02x Solar Mass
    quarter=2
)
