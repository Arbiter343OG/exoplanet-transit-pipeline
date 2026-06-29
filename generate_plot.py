import os
import sys
import re
import io
import contextlib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

print("--- INITIATING SYSTEM DATA HARVESTER ---")

# Step 1: Dynamically find all system scripts inside your directory
systems_dir = "systems"
if not os.path.exists(systems_dir):
    print(f"Error: Directory '{systems_dir}' not found.")
    sys.exit()

system_files = [f for f in os.listdir(systems_dir) if f.endswith('.py')]
print(f"Found {len(system_files)} individual target scripts to harvest.")

# Data capture lists
planet_names = []
radii = []
distances = []

# Step 2: Loop through each file and capture its printed terminal output stream
for file in sorted(system_files):
    file_path = os.path.join(systems_dir, file)
    
    # Setup standard text container to catch terminal output
    output_buffer = io.StringIO()
    
    try:
        # Silently run the target script file while stealing its printed results text
        with contextlib.redirect_stdout(output_buffer):
            with open(file_path, "r") as f:
                code = f.read()
                # Execute script body locally within its own context block
                exec(code, {'__file__': file_path, 'sys': sys, 'os': os})
                
        printed_text = output_buffer.getvalue()
        
        # Step 3: Extract calculated physics values using RegEx (Regular Expressions)
        name_match = re.search(r"DATA FOR\s+([\w\-\s]+)|Signature:\s+([\w\-]+)", printed_text, re.IGNORECASE)
        radius_match = re.search(r"Planetary Radius:\s+([\d\.]+)", printed_text)
        distance_match = re.search(r"Orbital Distance\s*\(a\):\s+([\d\.]+)", printed_text)
        
        # Fallback target name resolver using file string configurations
        target_name = (name_match.group(1) or name_match.group(2) if name_match else file.replace('.py', '').capitalize())
        
        if radius_match and distance_match:
            r_val = float(radius_match.group(1))
            a_val = float(distance_match.group(1))
            
            planet_names.append(target_name.strip())
            radii.append(r_val)
            distances.append(a_val)
            print(f"✅ Extracted: {target_name.strip()} -> Radius: {r_val} R_earth, Distance: {a_val} AU")
        else:
            print(f"⚠️ Metrics parsing skipped for: {file} (Check data string matching rules)")
            
    except Exception as e:
        print(f"❌ Automation runtime disruption tracking {file}: {e}")

# Step 4: Generate Publication-Grade Cumulative Scatter Plot
if len(radii) == 0:
    print("Error: No physical data frames could be aggregated. Exiting visual compiler.")
    sys.exit()

print("\n--- COMPILING EXOPLANETARY POPULATION PLOT ---")
plt.figure(figsize=(11, 6.5))

# Plot data tracks with a clean color gradient map based on planet scale sizes
scatter = plt.scatter(distances, radii, c=radii, cmap='plasma', s=120, edgecolors='black', alpha=0.85, zorder=3)

# Add clear annotation text offsets for each individual dataset node
for i, txt in enumerate(planet_names):
    plt.annotate(txt, (distances[i], radii[i]), textcoords="offset points", 
                 xytext=(6, 5), fontsize=8, weight='bold', alpha=0.75, zorder=4)

# Apply formal astronomical scientific axis scaling metrics
plt.title("Exoplanetary Demographic Survey Matrix (N=30 Targets)", fontsize=13, weight='bold', pad=15)
plt.xlabel("Semi-Major Axis / Orbital Distance ($AU$)", fontsize=11, weight='semibold')
plt.ylabel("Calculated Planetary Radius ($R_{\\oplus}$)", fontsize=11, weight='semibold')

# Set a log-scale on X axis to cleanly spread out very close planets from wide ones (like Kepler-22b)
plt.xscale('log')
plt.grid(True, which="both", linestyle="--", alpha=0.4, zorder=1)

# Include color tracking index legend scale bar on side profile margin layout
cbar = plt.colorbar(scatter)
cbar.set_label("Planetary Size Classification Scale ($R_{\\oplus}$)", fontsize=10, weight='semibold')

# Add subtle shading sectors to isolate physical structural regions
plt.axhspan(0.5, 2.0, color='blue', alpha=0.04, label="Rocky / Terrestrial Super-Earth Territory")
plt.axhspan(10.0, 22.0, color='red', alpha=0.04, label="Gas Giant Jovian Landscape Saturated Zone")
plt.legend(loc="upper left", frameon=True, facecolor='white', framealpha=0.95)

# Save visualization array layout into working folder path
output_img = "exoplanet_population_survey.png"
plt.savefig(output_img, dpi=300, bbox_inches='tight')
print(f"📊 Publication composite plot generated and saved as '{output_img}'!")
