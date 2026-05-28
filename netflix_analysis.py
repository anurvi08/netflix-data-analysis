import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Title": ["Wednesday", "Money Heist", "Stranger Things", "Squid Game", "Extraction", "Dark", "Lucifer"],

    "Type": ["TV Show", "TV Show", "TV Show", "TV Show", "Movie", "TV Show", "TV Show"],

    "Genre": ["Horror", "Crime", "Sci-Fi", "Thriller", "Action", "Sci-Fi", "Crime"],

    "Year": [2022, 2017, 2016, 2021, 2020, 2019, 2021]
}

df = pd.DataFrame(data)

print("Netflix Dataset:")
print(df)

content_count = df["Type"].value_counts()

print("Movies vs TV Shows:")
print(content_count)

most_common_genre = df["Genre"].mode()[0]

print("Most Common Genre:")
print(most_common_genre)

latest_content = df[df["Year"] == df["Year"].max()]

print("Latest Content:")
print(latest_content)

content_count.plot(kind="bar")

plt.xlabel("Content Type")
plt.ylabel("Count")
plt.title("Netflix Content Distribution")

plt.show()

df.to_csv("netflix_report.csv", index=False)

print("Netflix Report Saved")