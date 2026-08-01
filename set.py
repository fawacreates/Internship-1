# 1. Convert ages to a set and compare lengths
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages_set = set(ages)

print("Length of list:", len(ages))
print("Length of set:", len(ages_set))

if len(ages) > len(ages_set):
    print("The list is bigger.")
elif len(ages) < len(ages_set):
    print("The set is bigger.")
else:
    print("Both have the same length.")

# 2. Difference between string, list, tuple and set

print("\nString: Stores text. Immutable (cannot be changed).")
print("List: Ordered, mutable collection. Allows duplicate values.")
print("Tuple: Ordered, immutable collection. Allows duplicate values.")
print("Set: Unordered, mutable collection of unique values. Does not allow duplicates.")

# 3. Count unique words in a sentence

sentence = "I am a teacher and I love to inspire and teach people."

# Remove the period and split into words
words = sentence.replace(".", "").split()

unique_words = set(words)

print("Words:", words)
print("Unique Words:", unique_words)
print("Number of unique words:", len(unique_words))
