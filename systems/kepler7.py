import sys
import os

# Allow Python to look into the main parent directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exoplanet_engine import analyze_system

# Run pipeline using unique Kepler-7 structural parameters
analyze_system(
    target_name='Kepler-7',
    r_star=1.966,  # Significantly larger than our Sun (1.96x Solar Radii)
    m_star=1.347,  # More massive (1.34x Solar Mass)
    quarter=2
)
