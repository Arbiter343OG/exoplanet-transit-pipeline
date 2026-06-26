import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exoplanet_engine import analyze_system

# Run calculation using unique Kepler-12 metrics
analyze_system(
    target_name='Kepler-12',
    r_star=1.483,
    m_star=1.166,
    quarter=2
)
