import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Q1) Data Manipulation and cleaning using Numpy and Pandas??
df=pd.read_csv("C:\\Users\\kaziem\\Downloads\\MTA_Key_Performance_Indicators__2008-2021.csv")
df = df.dropna(how='all')
df = df.fillna(0)
df.columns = df.columns.str.lower()
df.columns = df.columns.str.strip()
numeric_cols = df.select_dtypes(include=[np.number]).columns
df.sort_values(by=numeric_cols[0], ascending=False, inplace=True)
mean_values = df[numeric_cols].mean()
median_values = df[numeric_cols].median()
stdev_values = df[numeric_cols].std()
range_values = df[numeric_cols].max() - df[numeric_cols].min()
total_cases = len(df)
exceeded_cases = len(df[df["monthly actual"] > df["monthly target"]])
percentage = (exceeded_cases / total_cases) * 100
print(f"Percentage exceeded is: {percentage:.2f}%")
print("\nMean Values:\n", mean_values)
print("\nMedian Values:\n", median_values)
print("\nStandard Deviation:\n", stdev_values)
print("\nRange (Max - Min):\n", range_values)


#  Q2) What are the KPI trends for top agencies using Multi-Line Chart???
df=pd.read_csv("C:\\Users\\kaziem\\Downloads\\MTA_Key_Performance_Indicators__2008-2021.csv")
df["Period"] = pd.to_datetime(df["Period"], errors="coerce")
df["Year"] = df["Period"].dt.year
top_agencies = df.groupby("Agency Name")["Monthly Actual"].sum().nlargest(3).index
df_filtered = df[df["Agency Name"].isin(top_agencies)]
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_filtered, x="Year", y="Monthly Actual", hue="Agency Name", palette="coolwarm")
plt.xlabel("Year", fontsize=12)
plt.ylabel("Monthly Actual KPI", fontsize=12)
plt.title("Top 3 Agencies KPI Trend", fontsize=14)
plt.xticks(rotation=45)  # Rotate x-axis labels for clarity
plt.legend(title="Agency")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.show()

# Q3) Create a scatter plot comparing Monthly target and Monthly Actual values??
df=pd.read_csv("C:\\Users\\kaziem\\Downloads\\MTA_Key_Performance_Indicators__2008-2021.csv")
df_filtered = df.dropna(subset=["monthly target", "monthly actual"])
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df_filtered["monthly target"], y=df_filtered["monthly actual"], alpha=0.7,
                color="green", edgecolor="black")
plt.xlabel(xlabel="monthly target", fontsize=12, fontweight="bold", color="purple")
plt.ylabel(ylabel="monthly actual", fontsize=12, fontweight="bold", color="red")
plt.title(label="monthly target vs. monthly actual", fontsize=14, fontweight="bold", color="#2E86C1")
plt.grid(visible=True, linestyle="--", alpha=0.5, color="gray")
plt.show()


# Q4) Visualize the proportion of different KPI categories in the dataset using a pie chart???
df=pd.read_csv("C:\\Users\\kaziem\\Downloads\\MTA_Key_Performance_Indicators__2008-2021.csv")
category_counts = df["Indicator Name"].value_counts().head(5)  # Top 5 Indicators
plt.figure(figsize=(5, 5))
plt.pie(category_counts, labels=category_counts.index, autopct="%1.1f%%", startangle=140)
plt.title("Top 5 KPI (Indicator) Distribution", fontsize=14)
plt.show()

# Q5) Make a boxplot over years showing YTD Target and YTD Actual.

df = pd.read_csv("MTA_Key_Performance_Indicators__2008-2021.csv")
data = df[['Period Year', 'YTD Target', 'YTD Actual']].dropna()
melted = pd.melt(
    data,
    id_vars='Period Year',
    value_vars=['YTD Target', 'YTD Actual'],
    var_name='Metric',
    value_name='Value'
)
plt.figure(figsize=(14, 6))
sns.boxplot(x='Period Year', y='Value', hue='Metric', data=melted)
plt.title('Boxplot of YTD Target vs YTD Actual Over Years')
plt.xlabel('Year')
plt.ylabel('Value')
plt.xticks(rotation=45)
plt.legend(title='Metric')
plt.tight_layout()
plt.show()


# Q6)  How has the Collisions with Injury Rate changed over time for Bridges and Tunnels?
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("C:\\Users\\kaziem\\Downloads\\MTA_Key_Performance_Indicators__2008-2021.csv")
df1 = df[(df["Agency Name"] == "Bridges and Tunnels") &
         (df["Indicator Name"] == "Collisions with Injury Rate")].copy()
df1["Period"] = pd.to_datetime(df1["Period"], errors='coerce')
df1 = df1.dropna(subset=["Period", "Monthly Actual"])
df1 = df1.sort_values("Period")
plt.figure(figsize=(14, 6))
sns.lineplot(data=df1, x="Period", y="Monthly Actual", marker="o", linewidth=2, color="steelblue")
plt.title("Monthly Collisions with Injury Rate - Bridges and Tunnels", fontsize=14)
plt.xlabel("Date")
plt.ylabel("Monthly Actual Rate")
plt.grid(True, linestyle="--", alpha=0.5)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Q7) Visualizing KPI trends based on the Desired Change direction using line plot?
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("C:\\Users\\kaziem\\Downloads\\MTA_Key_Performance_Indicators__2008-2021.csv")
df["Period"] = pd.to_datetime(df["Period"], errors="coerce")
df_clean = df.dropna(subset=["Period", "Monthly Actual", "Desired Change"])
df_clean = df_clean.sort_values("Period")
plt.figure(figsize=(14, 6))
sns.lineplot(data=df_clean, x="Period", y="Monthly Actual", hue="Desired Change",
             estimator="mean", ci=None, marker="o", linewidth=2)
plt.title("Trend of Monthly Actual by Desired Change Direction", fontsize=14)
plt.xlabel("Period")
plt.ylabel("Monthly Actual")
plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.legend(title="Desired Change")
plt.show()
