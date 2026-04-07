"""
Main Entry Point for Statistical Engine
"""

import json
import os
import sys

# Add src directory to path
BASE_DIR = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(BASE_DIR, 'src'))

from stat_engine import StatEngine
from monte_carlo import simulate_crashes, run_full_analysis


def load_salary_data():
    path = os.path.join(BASE_DIR, 'data', 'sample_salaries.json')
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Missing file: {path}")
        return None


def analyze_salary_data():
    data = load_salary_data()
    if not data:
        return

    salaries = data['salaries']
    engine = StatEngine(salaries)
    s = engine.get_summary()

    print("\n=== SALARY ANALYSIS ===")
    print(f"{data['description']} ({data['year']}) [{len(salaries)} entries]\n")

    print("Summary:")
    for k in ['count', 'mean', 'median', 'mode', 'min', 'max', 'range']:
        print(f"{k.capitalize():<10}: {s[k]}")

    print("\nVariance / Std Dev:")
    print(f"Population: {s['variance_population']:.2f} / {s['std_dev_population']:.2f}")
    print(f"Sample:     {s['variance_sample']:.2f} / {s['std_dev_sample']:.2f}")

    print("\nOutliers:")
    for label in ['outliers_2std', 'outliers_3std']:
        vals = s[label]
        print(f"{label}: {len(vals)} → {sorted(vals) if vals else 'None'}")


def demonstrate_monte_carlo():
    print("\n=== MONTE CARLO (Crash Simulation) ===")
    p = 0.045

    for days in [10, 100, 10000]:
        crashes, obs = simulate_crashes(days)
        print(f"{days:>6} days → crashes: {crashes}, observed: {obs:.4f}, error: {abs(obs-p)*100:.2f}%")

    print("\n" + run_full_analysis(seed=42))


def main():
    print("\n=== STATISTICAL ENGINE DEMO ===")
    analyze_salary_data()
    demonstrate_monte_carlo()

    print("\nRun tests with:")
    print("  python -m unittest discover -s tests")


if __name__ == "__main__":
    main()