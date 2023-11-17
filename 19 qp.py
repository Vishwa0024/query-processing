
import pandas as pd
data = {
 "Year": [1986, 1986, 1985, 1986, 1987],
 "WHO region": ["Western Pacific", "Americas", "Africa", "Americas", "Americas"],
 "Country": ["Viet Nam", "Uruguay", "Cte d'Ivoire", "Colombia", "Saint Kitts and Nevis"],
 "Beverage Types": ["Wine", "Other", "Wine", "Beer", "Beer"],
 "Display Value": [0.00, 0.50, 1.62, 4.27, 1.98]
}
df = pd.DataFrame(data)
print(df.head())
print('\nShape of the dataframe: ',df.shape)
print('\nNumber of rows: ',df.shape[0])
print('\nNumber of column: ',df.shape[1])
print("\nExtract Column Names:")
print(df.columns)
