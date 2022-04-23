from ..paths import OUTPUT_BASE_DIR, create_if_not_exists
from .dataset import df as dataset
from .dataset import full_str

path = create_if_not_exists(f"{OUTPUT_BASE_DIR}/config")

with open(f"{path}/print1.txt", "w") as f:
    f.write(f"{dataset.__str__()}\n")

with open(f"{path}/print2.txt", "w") as f:
    f.write(f"{full_str(dataset)}\n")
