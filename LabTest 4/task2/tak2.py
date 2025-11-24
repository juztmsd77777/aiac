import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# 1️⃣ Load dataset
data = pd.read_csv("sales_data.csv")
print("✅ Original Dataset:\n", data, "\n")

# 2️⃣ Handle missing values
# Fill missing transaction_amount with mean value
data["transaction_amount"].fillna(data["transaction_amount"].mean(), inplace=True)

# Fill missing customer names with 'Unknown'
data["customer_name"].fillna("Unknown", inplace=True)

print("✅ After Handling Missing Values:\n", data, "\n")

# 3️⃣ Normalize transaction_amount using Min-Max scaling
min_max_scaler = MinMaxScaler()
data["transaction_minmax"] = min_max_scaler.fit_transform(data[["transaction_amount"]])

# 4️⃣ Normalize transaction_amount using Standard Scaler (Z-score normalization)
standard_scaler = StandardScaler()
data["transaction_standard"] = standard_scaler.fit_transform(data[["transaction_amount"]])

print("✅ After Normalization:\n", data, "\n")

# 5️⃣ Save cleaned data
data.to_csv("cleaned_sales_data.csv", index=False)
print("💾 Cleaned and normalized data saved to 'cleaned_sales_data.csv'")
