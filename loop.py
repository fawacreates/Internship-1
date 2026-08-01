# ============================================
# 1. Countries containing the word "land"
# ============================================

from data.countries import countries

for country in countries:
    if "land" in country:
        print(country)

# ============================================
# 2. Reverse the fruit list using a loop
# ============================================

fruits = ['banana', 'orange', 'mango', 'lemon']

reversed_fruits = []

for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])

print(reversed_fruits)

# ============================================
# 3. Total number of languages
# ============================================

from data.countries_data import countries_data

languages = []

for country in countries_data:
    languages.extend(country["languages"])

print("Total number of languages:", len(set(languages)))

# ============================================
# 4. Ten most spoken languages
# ============================================

language_count = {}

for country in countries_data:
    for language in country["languages"]:
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1

sorted_languages = sorted(
    language_count.items(),
    key=lambda x: x[1],
    reverse=True
)

print("\nTop 10 Most Spoken Languages:")

for language, count in sorted_languages[:10]:
    print(language, "-", count)

# ============================================
# 5. Ten most populated countries
# ============================================

sorted_population = sorted(
    countries_data,
    key=lambda x: x["population"],
    reverse=True
)

print("\nTop 10 Most Populated Countries:")

for country in sorted_population[:10]:
    print(country["name"], "-", country["population"])
