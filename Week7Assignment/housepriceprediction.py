import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv(os.path.abspath("./house_price_regression_dataset.csv"))
house_price_df = df[['Square_Footage', 'House_Price']]
print("Initial dataset:")
print(house_price_df.head())

print("Cleaned dataset:")
df_cleaned = house_price_df.dropna()
df_cleaned['House_Price'] = df_cleaned['House_Price'].round(2)
print(df_cleaned.head())

plt.scatter(df_cleaned['Square_Footage'], df_cleaned['House_Price'], color='orange', label='Data Points')
plt.xlabel('Square_Footage')
plt.ylabel('House_Price')
plt.title('Scatter Plot of Square_Footage vs House_Price')
plt.grid(True)
plt.show()

x=df_cleaned[['Square_Footage']]
y=df_cleaned['House_Price']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=12)

model = LinearRegression()
model.fit(x_train, y_train)
print(f"intercept (b₀): {model.intercept_}")
print(f"coefficient (b₁): {model.coef_}")
y_pred = model.predict(x_test)

print("Mean squared error:\n")
print(mean_squared_error(y_test, y_pred))
print("R2 Score:\n")
print(r2_score(y_test, y_pred))

plt.scatter(x_test, y_test, color='orange', marker='+', label='Original')
plt.plot(x_test, y_pred, color='red', label='Predicted')
plt.xlabel("Square Footage")
plt.ylabel('House Price')
plt.title('Prediction of House Price via Linear Regression')
plt.grid(True)
plt.show()


