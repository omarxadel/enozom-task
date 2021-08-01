import pandas as pd
import hashlib as hl

df = pd.read_csv('data.csv')
result = ''

for i in range(len(df)):
    if not i % 2:
        result += str(df.iloc[i][2])
hashed_result = hl.md5(result.encode())
hashed_result = (hashed_result.hexdigest()).upper()

print(result)
print(hashed_result)
