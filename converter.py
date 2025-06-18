def scale_scores(scores, new_min, new_max):
    """
    Scales a list of scores to a new minimum and maximum range.
    """
    old_min = min(scores)
    old_max = max(scores)

    # Avoid division by zero if all scores are the same
    if old_max == old_min:
        return [new_min] * len(scores)

    old_range = old_max - old_min
    new_range = new_max - new_min

    scaled_list = [
        (((score - old_min) * new_range) / old_range) + new_min for score in scores
    ]
    return scaled_list


# Original scores [ADJUST]
original_scores = [
    83,
    83,
    93,
    83,
    78,
    78,
    78,
    78,
    97,
    78,
    78,
    78,
    78,
    78,
    78,
    90,
    87,
    78,
    90,
    78,
    83,
]

# Define the new range [ADJUST]
new_minimum = 78
new_maximum = 85

converted_scores = scale_scores(original_scores, new_minimum, new_maximum)

# Option 1: Round to the nearest integer
rounded_scores = [round(score) for score in converted_scores]
# Option 2: Round down
# rounded_scores = [math.floor(score) for score in converted_scores]
# Option 3: Round up
# rounded_scores = [math.ceil(score) for score in converted_scores]

# Print the results

# for old, new in zip(original_scores, rounded_scores):
#     print(f"Original: {old} -> Scaled: {new:.2f}")

for new in rounded_scores:
    # print(f"{new:.2f}")
    print(new)
