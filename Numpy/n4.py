import pandas as pd

data = {
    "Name": ["A", "B", "C", "D"],
    "Marks": [80, 65, 90, 75]
}

df = pd.DataFrame(data)

print(df[df["Marks"] > 75])
