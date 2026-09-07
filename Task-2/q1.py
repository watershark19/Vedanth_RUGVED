#counting matches in 2008
import pandas as pd

df = pd.read_csv("C:\\Users\\bmved\\OneDrive\\vedupython\\Vedanth_RUGVED\\Task-2\\matches.csv")
print(df.head())

matches_2008 = df[df["season"]==2008]
print(matches_2008)
print(f"The number of matches in 2008 is {len(matches_2008)}")