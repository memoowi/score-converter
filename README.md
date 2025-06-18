# Score Scaler & Normalization Script
by [_Memoowi_](https://instagram.com/me_moowi)

A simple yet flexible Python script to perform min-max normalization on a list of scores. It scales the numbers from their original range to a new, specified integer range. This is a common requirement for data preprocessing, adjusting grading schemes, or any scenario where data needs to be mapped to a consistent scale.

---

## Features

- **Min-Max Scaling:** Scales any list of numbers to a new defined range.
- **Integer Output:** Provides options to convert the final scaled scores into integers using different rounding methods (round, floor, or ceiling).
- **Edge Case Handling:** Correctly handles cases where all input scores are identical, avoiding division-by-zero errors.
- **Easy to Customize:** Written in a clear and straightforward manner, making it easy to modify the input data and scaling parameters.

---

## How It Works

The script uses the standard formula for min-max normalization to linearly scale a value from one range to another:

$$
\text{NewValue} = \frac{(\text{OldValue} - \text{OldMin}) \times (\text{NewMax} - \text{NewMin})}{(\text{OldMax} - \text{OldMin})} + \text{NewMin}
$$

Where:
- `OldValue`: The original score to be converted.
- `OldMin`: The minimum value in the original dataset.
- `OldMax`: The maximum value in the original dataset.
- `NewMin`: The desired minimum value for the new range.
- `NewMax`: The desired maximum value for the new range.

---

## Usage

1.  **Prerequisites:** Ensure you have Python 3 installed on your system.

2.  **Clone or Download:**
    Clone this repository or simply download the `converter.py` script.
    ```bash
    git clone https://github.com/memoowi/score-converter.git
    cd score-converter
    ```

3.  **Run the Script:**
    Execute the script from your terminal:
    ```bash
    python converter.py
    ```
    The script will print the original and scaled scores to the console.

## Customization

To use the script for your own data, open `converter.py` and modify the following sections:

1.  **Input Data:**
    Change the `original_scores` list to contain your own numbers.
    ```python
    # Original scores
    original_scores = [10, 20, 45, 60, 95, 100]
    ```

2.  **Target Range:**
    Adjust the `new_minimum` and `new_maximum` variables to define your desired scale.
    ```python
    # Define the new range
    new_minimum = 0
    new_maximum = 100
    ```

3.  **Rounding Method:**
    The script defaults to standard rounding. You can change this by commenting and uncommenting the desired conversion method.
    ```python
    # Option 1: Round to the nearest integer
    rounded_scores = [round(score) for score in converted_scores]

    # Option 2: Round down
    # rounded_scores = [math.floor(score) for score in converted_scores]

    # Option 3: Round up
    # rounded_scores = [math.ceil(score) for score in converted_scores]
    ```

---

## License

This project is open source and available under the [MIT License](LICENSE).