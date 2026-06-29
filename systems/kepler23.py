import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exoplanet_engine import analyze_system
analyze_system('Kepler-23', r_star=1.520, m_star=1.110, quarter=2)
