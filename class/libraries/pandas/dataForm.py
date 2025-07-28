import pandas as pd

data = {
    "calories": [100, 200, 300],
    "Duration": [40, 45, 50]
}

calDAta = pd.DataFrame(data, index=["d1", "d2", "d3"])
print(calDAta)
print(calDAta.loc["d1"])
