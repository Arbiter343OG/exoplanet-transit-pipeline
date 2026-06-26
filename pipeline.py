import os
import lightkurve as lk

# --- FIX FOR THE TCL ERROR ---
import matplotlib
matplotlib.use('Agg') # Tells Python to save the plot directly without opening a popup window
# -----------------------------

import matplotlib.pyplot as plt
import numpy as np
from astropy import units as u
from astropy.constants import G

print("--- EXOPLANET PIPELINE STARTING ---")

# 1. Download NASA Kepler Data
print("Fetching target light curves from NASA Archive...")
search_result = lk.search_lightcurve('Kepler-10', author='Kepler', quarter=3)
lc = search_result.download().remove_nans().flatten()

# 2. Run Periodogram Analysis
print("Running Box Least Squares period search algorithm...")
periodogram = lc.to_periodogram(method='bls', period=np.linspace(0.5, 5, 10000))
best_period = periodogram.period_at_max_power
best_t0 = periodogram.transit_time_at_max_power
print(f"Detected Orbital Period: {best_period:.4f}")

# 3. Fold and Bin Data
folded_lc = lc.fold(period=best_period, epoch_time=best_t0)
binned_lc = folded_lc.bin(time_bin_size=0.01)

# 4. Core Physics Calculations
R_star = 1.056 * u.R_sun
M_star = 0.913 * u.M_sun

delta_f = 1.0 - np.min(binned_lc.flux.value)
R_planet = (R_star * np.sqrt(delta_f)).to(u.R_earth)

period_seconds = best_period.to(u.s)
m_star_kg = M_star.to(u.kg)
a_meters = ((G * m_star_kg * (period_seconds**2)) / (4 * np.pi**2))**(1/3)
a_au = a_meters.to(u.au)

print("\n================== RESULTS ==================")
print(f"Transit Light Dip Depth: {delta_f:.6f}")
print(f"Calculated Planetary Radius: {R_planet:.2f} Earth Radii")
print(f"Calculated Orbital Distance (a): {a_au:.4f} AU")
print("=============================================\n")

# 5. Save the Diagnostic Plot Locally
print("Generating light curve visualization...")
plt.figure(figsize=(10, 5))
plt.plot(folded_lc.time.value, folded_lc.flux.value, 'k.', alpha=0.2, label='Raw Observations')
plt.plot(binned_lc.time.value, binned_lc.flux.value, 'r.', markersize=8, label='Binned Transit Profile')
plt.title(f"Folded Light Curve: Kepler-10b")
plt.xlabel("Time Since Mid-Transit (Days)")
plt.ylabel("Normalized Flux")
plt.xlim(-0.2, 0.2)
plt.legend()
plt.grid(True)

# Instead of just showing it on screen, we save it as an image file in your project folder
output_filename = "kepler10b_transit_profile.png"
plt.savefig(output_filename, dpi=300)
print(f"Plot saved successfully as '{output_filename}'!")
 