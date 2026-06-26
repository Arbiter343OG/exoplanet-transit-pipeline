import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exoplanet_engine import analyze_system

# Circumbinary Star System (Analytical Anomaly Target)
analyze_system(
    target_name='Kepler-16',
    r_star=0.648,  # Primary star radius
    m_star=0.689,  # Primary star mass
    quarter=10
)
