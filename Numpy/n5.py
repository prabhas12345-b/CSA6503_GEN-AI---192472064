import pandas as pd

data = {
    "Marks": [70, 80, 90, 85, 95]
}

df = pd.DataFrame(data)

print(df.describe())
