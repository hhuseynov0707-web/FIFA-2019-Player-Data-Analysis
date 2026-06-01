import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ── 1. Load Data ───────────────────────────────────────────────────────────────
df = pd.read_csv("Fifa 2019.csv")
print("Shape:", df.shape)
print(df.head())

# ── 2. Clean Columns ───────────────────────────────────────────────────────────
df.drop(columns=["Unnamed: 0"], inplace=True, errors="ignore")

print("\nColumn names:")
print(df.columns.tolist())

print("\nBasic stats:")
print(df.describe(include=[np.number]))

# ── 3. Parse Market Value ──────────────────────────────────────────────────────
print("\nSample raw values:")
print(df["Value"].head(10))

# Remove € symbol
df["Value"] = df["Value"].str.replace("€", "", regex=False)

# Extract multiplier (M or K)
df["multiplier"] = df["Value"].str.extract("([MK])")

# Extract numeric part
df["number"] = (
    df["Value"]
    .str.replace("M", "", regex=False)
    .str.replace("K", "", regex=False)
)
df["number"] = pd.to_numeric(df["number"], errors="coerce")

# Map multiplier to actual factor
df["multiplier"] = df["multiplier"].map({"M": 1_000_000, "K": 1_000})

# Compute real value; fill missing with 0
df["real_value"] = df["number"] * df["multiplier"]
df["real_value"] = df["real_value"].fillna(0)

# Check for nulls in key columns
print("\nNull counts in key columns:")
print(df[["Age", "Preferred Foot", "Position", "Potential", "Overall", "International Reputation"]].isnull().sum())

# ── 4. Age Distribution ────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

sns.histplot(data=df, x="Age", kde=False, bins=20, ax=axes[0])
axes[0].set_title("Player Age Distribution (Histogram)")

sns.kdeplot(data=df, x="Age", fill=True, ax=axes[1])
axes[1].set_title("Player Age Distribution (KDE)")

plt.tight_layout()
plt.show()

# ── 5. Preferred Foot Analysis ─────────────────────────────────────────────────
print("\nPreferred Foot counts:")
print(df["Preferred Foot"].value_counts())

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Count plot
sns.countplot(data=df, x="Preferred Foot", ax=axes[0])
axes[0].set_title("Preferred Foot Count")

# Pie chart
df["Preferred Foot"].value_counts().plot.pie(
    autopct="%1.1f%%",
    startangle=90,
    colors=["lightblue", "lightgreen"],
    ax=axes[1],
)
axes[1].set_title("Preferred Foot Distribution")
axes[1].set_ylabel("")

# Average market value by foot
ortalama_qiymet_ayaq = df.groupby("Preferred Foot")["real_value"].mean()
print("\nAverage market value by foot:")
print(ortalama_qiymet_ayaq)

ortalama_qiymet_ayaq.plot(kind="bar", color=["blue", "orange"], ax=axes[2])
axes[2].set_title("Average Market Value by Foot")
axes[2].set_ylabel("Average Value (€)")
axes[2].tick_params(axis="x", rotation=0)

plt.tight_layout()
plt.show()

# ── 6. Position × Foot Breakdown ───────────────────────────────────────────────
fig, axes = plt.subplots(2, 1, figsize=(14, 14))

sns.countplot(data=df, x="Position", hue="Preferred Foot", ax=axes[0])
axes[0].set_title("Player Count by Position and Foot")
axes[0].tick_params(axis="x", rotation=90)

sns.boxplot(data=df, x="Position", y="real_value", hue="Preferred Foot", ax=axes[1])
axes[1].set_title("Market Value by Position and Foot (Boxplot)")
axes[1].tick_params(axis="x", rotation=90)
axes[1].legend(title="Preferred Foot")

plt.tight_layout()
plt.show()

# ── 7. International Reputation × Potential ────────────────────────────────────
print("\nUnique Reputation levels:", df["International Reputation"].unique())

fig, axes = plt.subplots(1, 3, figsize=(18, 6))

sns.scatterplot(data=df, x="International Reputation", y="Potential", ax=axes[0])
axes[0].set_title("Reputation vs Potential (Scatter)")

sns.stripplot(
    data=df,
    x="International Reputation",
    y="Potential",
    hue="Preferred Foot",
    jitter=True,
    dodge=True,
    ax=axes[1],
)
axes[1].set_title("Reputation vs Potential by Foot (Strip)")
axes[1].legend(title="Preferred Foot")

sns.boxplot(data=df, x="International Reputation", y="Potential", ax=axes[2])
axes[2].set_title("Reputation vs Potential (Boxplot)")

plt.tight_layout()
plt.show()

# ── 8. Potential × Overall Rating ──────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

sns.lineplot(data=df, x="Potential", y="Overall", ax=axes[0])
axes[0].set_title("Potential vs Overall (Lineplot)")

sns.scatterplot(data=df, x="Potential", y="Overall", hue="Preferred Foot", ax=axes[1])
axes[1].set_title("Potential vs Overall by Foot (Scatter)")

plt.tight_layout()
plt.show()

# ── 9. Summary Dashboard (2×2) ─────────────────────────────────────────────────
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 15))

# Plot 1: Stripplot
sns.stripplot(
    data=df,
    x="International Reputation",
    y="Potential",
    hue="Preferred Foot",
    jitter=True,
    dodge=True,
    ax=axes[0, 0],
)
axes[0, 0].set_title("1. Reputation, Potential, Foot (Stripplot)")
axes[0, 0].get_legend().remove()

# Plot 2: Boxplot
sns.boxplot(data=df, x="International Reputation", y="Potential", ax=axes[0, 1])
axes[0, 1].set_title("2. Reputation vs Potential (Boxplot)")

# Plot 3: Lineplot
sns.lineplot(data=df, x="Potential", y="Overall", ax=axes[1, 0])
axes[1, 0].set_title("3. Potential vs Overall (Lineplot)")

# Plot 4: Scatterplot
sns.scatterplot(data=df, x="Potential", y="Overall", hue="Preferred Foot", ax=axes[1, 1])
axes[1, 1].set_title("4. Potential, Overall, Foot (Scatter)")

plt.tight_layout()
plt.show()