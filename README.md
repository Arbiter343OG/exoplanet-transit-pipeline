# Multi-Target Computational Astrophysics Pipeline: Exoplanet Transit Analysis

An open-source, automated data processing pipeline built in Python to extract raw stellar photometry data from NASA space telescope archives, isolate subtle planetary signatures via signal processing algorithms, and solve Newtonian/Keplerian mechanics equations to calculate key planetary physical and orbital metrics.

---

## 🌌 Core Scientific Methodology & Physics Engine

This project implements the **Transit Photometry Method** to study exoplanetary properties based on the geometric configurations of stellar eclipses.

### 1. Geometric Extraction of Planetary Radius ($R_p$)
When an exoplanet transits its host star, the structural flux reduction—or transit depth ($\Delta F$)—is mathematically defined as the ratio of the cross-sectional area of the planet's disk to that of the star:

$$\Delta F = \frac{F_{\text{unobscured}} - F_{\text{transit}}}{F_{\text{unobscured}}} = \left(\frac{R_p}{R_s}\right)^2$$

By isolating the minimum normalized flux value within the folded time-series array, the engine extracts the true physical size of the world relative to Earth ($R_{\oplus}$):

$$R_p = R_s \sqrt{\Delta F}$$

### 2. Solving for Semi-Major Axis ($a$) via Kepler's Third Law
Once the Box Least Squares (BLS) periodogram isolates the periodic transit interval ($T$), the planet's average orbital distance (semi-major axis) is resolved by matching centrifugal and gravitational parameters:

$$T^2 = \frac{4\pi^2}{G M_s} a^3 \implies a = \left(\frac{G M_s T^2}{4\pi^2}\right)^{1/3}$$

Where $G$ represents the Gravitational Constant:

$$G = 6.674 \times 10^{-11} \text{ m}^3 \text{ kg}^{-1} \text{ s}^{-2}$$

And $M_s$ represents the cataloged mass of the target star.


---

## 🛠️ Software Architecture & Project Topology

The codebase transitions away from static notebooks into a scalable, production-style architecture. A centralized, parametrizable processing module is imported by independent system wrappers to cleanly segregate target profiles.

```text
physics_passion_project/
│
├── exoplanet_engine.py      # Core framework: Downloads NASA flux files, executes BLS models, runs physics equations
├── .gitignore               # Excludes virtual environments and raw image artifacts from repository pollution
└── systems/                 # Target-specific research scripts wrapping custom stellar data
    ├── kepler4.py           # Discovers Kepler-4b: Dense, close-in "Hot Neptune" (~4.1 R_earth)
    ├── kepler5.py           # Discovers Kepler-5b: Highly irradiated, hot Jovian world (~15.2 R_earth)
    ├── kepler6.py           # Discovers Kepler-6b: A high-mass sub-stellar Hot Jupiter (~14.3 R_earth)
    ├── kepler7.py           # Discovers Kepler-7b: One of the lowest-density, "fluffiest" gas giants cataloged
    ├── kepler8.py           # Discovers Kepler-8b: A massive gas giant orbiting a hot, rapidly rotating F-type star
    ├── kepler9.py           # Discovers Kepler-9b: A resonant, multi-planetary massive gas giant
    ├── kepler10.py          # Discovers Kepler-10b: A dense, hyper-close rocky Super-Earth (~1.5 R_earth)
    ├── kepler11.py          # Discovers Kepler-11b: Processes signals from a highly compact, multi-planet system
    ├── kepler12.py          # Discovers Kepler-12b: A low-density, inflated gas giant ("Hot Jupiter")
    ├── kepler14.py          # Discovers Kepler-14b: Massive planet tracking inside binary background light noise
    ├── kepler15.py          # Discovers Kepler-15b: A dense, core-concentrated metallic "Heavy Jupiter"
    ├── kepler16.py          # Discovers Kepler-16b: An analytical anomaly testing binary-star orbital mathematics
    ├── kepler17.py          # Discovers Kepler-17b: Jovian planet cross-cutting high-activity stellar starspots
    ├── kepler20.py          # Discovers Kepler-20b: A compressed, close-in Super-Earth in a tight system
    ├── kepler22.py          # Discovers Kepler-22b: Explores the habitable zone boundaries of a G-type star
    └── kepler45.py          # Discovers Kepler-45b: An exoplanet transiting a small M-dwarf star

```

---

## 📈 Empirical Database & Analytical Findings

Executing the modular script catalog returns a highly diverse exoplanetary demographic profile across 16 distinct systems:

| Target System | Stellar Radius ($R_{\odot}$) | Stellar Mass ($M_{\odot}$) | Detected Period (Days) | Calculated Radius ($R_{\oplus}$) | Calculated Distance ($AU$) | Target Profile Classification |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Kepler-10b** | 1.056 | 0.913 | 0.8375 | ~1.51 | 0.0168 | Ultra-Short Period Rocky Super-Earth |
| **Kepler-12b** | 1.483 | 1.166 | 4.4379 | ~19.06 | 0.0553 | Inflated Low-Density "Hot Jupiter" |
| **Kepler-7b** | 1.966 | 1.347 | 4.8855 | ~16.22 | 0.0624 | Extremely Evolved "Fluffy" Gas Giant |
| **Kepler-8b** | 1.486 | 1.213 | 3.5225 | ~15.61 | 0.0479 | Rapid-Orbit Massive Gas Giant |
| **Kepler-6b** | 1.391 | 1.082 | 3.2347 | ~14.30 | 0.0435 | High-Mass Sub-Stellar Hot Jupiter |
| **Kepler-9b** | 1.023 | 1.022 | 19.243 | ~9.42 | 0.1432 | Resonant Multi-Planetary Gas Giant |
| **Kepler-15b** | 0.992 | 1.018 | 4.9429 | ~10.91 | 0.0574 | Core-Concentrated "Heavy Jupiter" |
| **Kepler-20b** | 0.944 | 0.912 | 3.6961 | ~1.85 | 0.0454 | Highly Compressed Close-In Super-Earth |
| **Kepler-4b**  | 1.492 | 1.092 | 3.2135 | ~4.05 | 0.0437 | Dense Intermediate Hot Neptune |
| **Kepler-5b**  | 1.793 | 1.374 | 3.5485 | ~15.15 | 0.0507 | Irradiated High-Temperature Jovian Planet |
| **Kepler-14b** | 2.048 | 1.512 | 6.7901 | ~12.41 | 0.0781 | Binary-System High-Mass Gas Giant |
| **Kepler-17b** | 1.025 | 1.023 | 1.4857 | ~14.62 | 0.0260 | Hot Jupiter Orbiting Active Starspot Star |
| **Kepler-11b** | 1.065 | 0.961 | 10.304 | ~1.80 | 0.0911 | Highly Compact Multi-Planet System Target |
| **Kepler-16b** | 0.648 | 0.689 | 228.78 | ~8.43 | 0.6920 | Analytical Anomaly: Circumbinary World |
| **Kepler-22b** | 0.979 | 0.970 | 289.86 | ~2.38 | 0.8491 | Habitable Zone Liquid-Water Candidate |
| **Kepler-45b** | 0.550 | 0.590 | 2.4552 | ~4.21 | 0.0271 | M-Dwarf Transiting Jovian World |



## 🚀 Execution Instructions

### Local Environment Setup
To clone this project and build the research dependencies inside an isolated virtual environment, execute the following commands in your shell:

```bash
# Clone the repository
git clone https://github.com
cd exoplanet-transit-pipeline

# Install specialized astrophysical analysis and scientific computing libraries
pip install lightkurve astropy matplotlib numpy
```

### Running System Discovery Analysis
To independently query NASA's servers for raw stellar records, process light-curve algorithms, and evaluate planetary characteristics for any target system, invoke its script wrapper:

```bash
python systems/kepler10.py
```

*Note: The engine leverages a headless `Agg` backend interface configuration within Matplotlib to avoid runtime window processing conflicts, directly exporting phase-folded signal profiles as high-fidelity diagnostic `.png` assets locally.*
