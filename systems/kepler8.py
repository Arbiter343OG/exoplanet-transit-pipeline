import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exoplanet_engine import analyze_system

# Run pipeline using unique Kepler-8 structural parameters
analyze_system(
    target_name='Kepler-8',
    r_star=1.486,  # 1.48x Solar Radii
    m_star=1.213,  # 1.21x Solar Mass
    quarter=2
)
