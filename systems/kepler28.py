import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exoplanet_engine import analyze_system
analyze_system('Kepler-28', r_star=0.710, m_star=0.750, quarter=2)
