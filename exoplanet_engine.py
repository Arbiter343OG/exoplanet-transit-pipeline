import os
import lightkurve as lk
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from astropy import units as u
from astropy.constants import G

def analyze_system(target_name, r_star, m_star, quarter):
    print(f"\n⚡ Executing Core Analysis Engine for {target_name}...")
    
    # 1. Download NASA Data
    search_result = lk.search_lightcurve(target_name, author='Kepler', quarter=quarter)
    lc = search_result.download().remove_nans().flatten()
    
    # 2. Period Search
    periodogram = lc.to_periodogram(method='bls', period=np.linspace(0.5, 5, 10000))
    best_period = periodogram.period_at_max_power
    best_t0 = periodogram.transit_time_at_max_power
    
    # 3. Fold Data
    folded_lc = lc.fold(period=best_period, epoch_time=best_t0)
    binned_lc = folded_lc.bin(time_bin_size=0.01)
    
    # 4. Compute Astrophysical Metrics
    delta_f = 1.0 - np.min(binned_lc.flux.value)
    r_planet = (r_star * u.R_sun * np.sqrt(delta_f)).to(u.R_earth)
    
    period_seconds = best_period.to(u.s)
    m_star_kg = (m_star * u.M_sun).to(u.kg)
    a_meters = ((G * m_star_kg * (period_seconds**2)) / (4 * np.pi**2))**(1/3)
    a_au = a_meters.to(u.au)
    
    # Print Results
    print(f"================== {target_name.upper()} DATA ==================")
    print(f"Detected Orbital Period: {best_period:.4f}")
    print(f"Calculated Planetary Radius: {r_planet:.2f} Earth Radii")
    print(f"Calculated Orbital Distance (a): {a_au:.4f} AU")
    print("=================================================\n")
    
    # 5. Generate and Save Plot
    plt.figure(figsize=(8, 4))
    plt.plot(folded_lc.time.value, folded_lc.flux.value, 'k.', alpha=0.1)
    plt.plot(binned_lc.time.value, binned_lc.flux.value, 'r.', markersize=6)
    plt.title(f"Transit Signature: {target_name}")
    plt.xlabel("Time (Days)")
    plt.ylabel("Flux")
    plt.xlim(-0.2, 0.2)
    plt.grid(True)
    
    # Save chart cleanly inside your working directory
    filename = f"{target_name.lower().replace('-', '')}_transit.png"
    plt.savefig(filename, dpi=150)
    plt.close()
    print(f" Saved structural plot as '{filename}'!")
