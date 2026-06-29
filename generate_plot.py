import os
import sys
import re
import io
import shutil
import contextlib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

print("--- INITIATING ROBUST SYSTEM DATA HARVESTER ---")

# Automatically clear out the cache if a corruption warning happens
def clear_astropy_cache():
    cache_path = os.path.expanduser("~/.lightkurve/cache")
    if os.path.exists(cache_path):
        try:
            shutil.rmtree(cache_path)
            print("🧹 Detected file truncation warning. Automatically cleared local cache for fresh download.")
        except Exception:
            pass

systems_dir = "systems"
if not os.path.exists(systems_dir):
    print(f"Error: Directory '{systems_dir}' not found.")
    sys.exit()

system_files = [f for f in os.listdir(systems_dir) if f.endswith('.py')]
print(f"Found {len(system_files)} individual target scripts to harvest.")

planet_names = []
radii = []
distances = []

# Loop through each target file
for file in sorted(system_files):
    file_path = os.path.join(systems_dir, file)
    output_buffer = io.StringIO()
    
    # Try running the file up to 2 times if a download fails due to truncation
    for attempt in range(2):
        try:
            with contextlib.redirect_stdout(output_buffer):
                with open(file_path, "r") as f:
                    code = f.read()
                    exec(code, {'__file__': file_path, 'sys': sys, 'os': os})
                    
            printed_text = output_buffer.getvalue()
            
            # Check if the terminal output recorded a truncated file error during execution
            if "truncated" in printed_text.lower() or "corrupt" in printed_text.lower():
                clear_astropy_cache()
                output_buffer = io.StringIO() # Reset buffer for retry
                continue
                
            name_match = re.search(r"DATA FOR\s+([\w\-\s]+)|Signature:\s+([\w\-]+)", printed_text, re.IGNORECASE)
            radius_match = re.search(r"Planetary Radius:\s+([\d\.]+)", printed_text)
            distance_match = re.search(r"Orbital Distance\s*\(a\):\s+([\d\.]+)", printed_text)
            
            target_name = (name_match.group(1) or name_match.group(2) if name_match else file.replace('.py', '').capitalize())
            
            if radius_match and distance_match:
                r_val = float(radius_match.group(1))
                a_val = float(distance_match.group(1))
                
                planet_names.append(target_name.strip())
                radii.append(r_val)
                distances.append(a_val)
                print(f"✅ Extracted: {target_name.strip()} -> Radius: {r_val} R_earth, Distance: {a_val} AU")
                break # Success, move to next file
            else:
                print(f"⚠️ Metrics parsing skipped for: {file}")
                break
                
        except Exception as e:
            if "truncated" in str(e).lower() or "fits" in str(e).lower():
                clear_astropy_cache()
                continue # Retry once with fresh cache
            print(f"❌ Automation runtime disruption tracking {file}: {e}")
            break

# Generate Plot
if len(radii) == 0:
    print("Error: No physical data frames could be aggregated.")
    sys.exit()

print("\n--- COMPILING EXOPLANETARY POPULATION PLOT ---")
plt.figure(figsize=(11, 6.5))
scatter = plt.scatter(distances, radii, c=radii, cmap='plasma', s=120, edgecolors='black', alpha=0.85, zorder=3)

for i, txt in enumerate(planet_names):
    plt.annotate(txt, (distances[i], radii[i]), textcoords="offset points", 
                 xytext=(6, 5), fontsize=8, weight='bold', alpha=0.75, zorder=4)

plt.title("Exoplanetary Demographic Survey Matrix (N=30 Targets)", fontsize=13, weight='bold', pad=15)
plt.xlabel("Semi-Major Axis / Orbital Distance ($AU$)", fontsize=11, weight='semibold')
plt.ylabel("Calculated Planetary Radius ($R_{\\oplus}$)", fontsize=11, weight='semibold')
plt.xscale('log')
plt.grid(True, which="both", linestyle="--", alpha=0.4, zorder=1)
cbar = plt.colorbar(scatter)
cbar.set_label("Planetary Size Classification Scale ($R_{\\oplus}$)", fontsize=10, weight='semibold')

plt.axhspan(0.5, 2.0, color='blue', alpha=0.04, label="Rocky / Terrestrial Super-Earth Territory")
plt.axhspan(10.0, 22.0, color='red', alpha=0.04, label="Gas Giant Jovian Landscape Saturated Zone")
plt.legend(loc="upper left", frameon=True, facecolor='white', framealpha=0.95)

output_img = "exoplanet_population_survey.png"
plt.savefig(output_img, dpi=300, bbox_inches='tight')
print(f"📊 Publication composite plot generated and saved as '{output_img}'!")
