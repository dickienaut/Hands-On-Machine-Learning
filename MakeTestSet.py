import hashlib
from HousingDataDL import fetch_housing_data, load_housing_data
from sklearn.model_selection import train_test_split




fetch_housing_data()
df = load_housing_data()
train_set, test_set = train_test_split(df, test_size=0.2, random_state=41)
