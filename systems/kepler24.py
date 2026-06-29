import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exoplanet_engine import analyze_system
analyze_system('Kepler-24', r_star=1.210, m_star=0.980, quarter=2)
