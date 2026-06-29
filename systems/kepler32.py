import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exoplanet_engine import analyze_system
analyze_system('Kepler-32', r_star=0.430, m_star=0.540, quarter=3)
