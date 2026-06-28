import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exoplanet_engine import analyze_system

# Classic, highly irradiated Jovian planet
analyze_system(
    target_name='Kepler-5',
    r_star=1.793,  # Large F-type star (1.79x Solar Radii)
    m_star=1.374,  # 1.37x Solar Mass
    quarter=2
)
