from pathlib import Path
from pytest_bdd import scenarios
from sil_tests_i.steps import *

features_path = Path(__file__).parent / "features"

for feature_file in features_path.rglob("*.feature"):
    print(f"Loading feature: {feature_file}")
    scenarios(str(feature_file))
