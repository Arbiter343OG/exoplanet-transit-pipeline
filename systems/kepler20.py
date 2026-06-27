import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exoplanet_engine import analyze_system

# Packed multi-planet system target (Kepler-20b)
analyze_system(
    target_name='Kepler-20',
    r_star=0.944,  # 0.94x Solar Radii
    m_star=0.912,  # 0.91x Solar Mass
    quarter=2
)
