import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exoplanet_engine import analyze_system

# Run calculation using unique Kepler-45 metrics
analyze_system(
    target_name='Kepler-45',
    r_star=0.550,
    m_star=0.590,
    quarter=5
)
