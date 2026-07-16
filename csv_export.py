import pandas as pd

def export_csv(city):

    df = pd.DataFrame([city])

    return df.to_csv(index=False).encode("utf-8")