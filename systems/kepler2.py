import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exoplanet_engine import analyze_system
analyze_system('Kepler-2', r_star=1.521, m_star=1.258, quarter=2)
