# ============================================
# Exercise 1: Check if a number is prime
# ============================================

def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


print(is_prime(7))
print(is_prime(12))


# ============================================
# Exercise 2: Check if all items are unique
# ============================================

def all_unique(lst):
    return len(lst) == len(set(lst))


print(all_unique([1, 2, 3, 4]))
print(all_unique([1, 2, 2, 4]))


# ============================================
# Exercise 3: Check if all items have same data type
# ============================================

def same_data_type(lst):
    first_type = type(lst[0])

    for item in lst:
        if type(item) != first_type:
            return False

    return True


print(same_data_type([1, 2, 3]))
print(same_data_type([1, "2", 3]))


# ============================================
# Exercise 4: Check if a variable name is valid
# ============================================

def is_valid_variable(variable):
    return variable.isidentifier()


print(is_valid_variable("first_name"))
print(is_valid_variable("123name"))
print(is_valid_variable("my_variable"))


# ============================================
# Exercise 5: Most Spoken Languages
# ============================================

from data.countries_data import countries_data

def most_spoken_languages(n):
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

    return sorted_languages[:n]


print(most_spoken_languages(10))
print(most_spoken_languages(20))


# ============================================
# Exercise 6: Most Populated Countries
# ============================================

def most_populated_countries(n):
    countries = sorted(
        countries_data,
        key=lambda x: x["population"],
        reverse=True
    )

    result = []

    for country in countries[:n]:
        result.append({
            "country": country["name"],
            "population": country["population"]
        })

    return result


print(most_populated_countries(10))
print(most_populated_countries(20))
