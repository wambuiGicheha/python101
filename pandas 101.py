import pandas as pd
pd.set_option("max_colwidth", 120)
pd.DataFrame(
    data=data['meta']['view'].values(),
    index=data['meta']['view'].keys(),
    columns=["value"]
)
print(pd)
