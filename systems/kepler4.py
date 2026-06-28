import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exoplanet_engine import analyze_system

# High-density "Hot Neptune" candidate
analyze_system(
    target_name='Kepler-4',
    r_star=1.492,  # 1.49x Solar Radii
    m_star=1.092,  # 1.09x Solar Mass
    quarter=2
)
