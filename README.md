# Topsis-Vansh-102316118

## 📌 TOPSIS - Technique for Order of Preference by Similarity to Ideal Solution

TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) is a multi-criteria decision-making method used to rank alternatives based on multiple criteria.

The best alternative is the one that:
- Has the shortest distance from the ideal best solution
- Has the farthest distance from the ideal worst solution

This project provides a command-line implementation of the TOPSIS method in Python.

---

## 📦 Installation

### Install from PyPI

```bash
pip install Topsis-Vansh-102316118
```

### Install Locally (from project directory)

```bash
pip install .
```

---

## 🚀 Usage

### Command Line

```bash
topsis <input_file> <weights> <impacts> <output_file>
```

### Parameters

- `input_file` → CSV file containing alternatives and criteria
- `weights` → Comma-separated numeric weights (e.g., `"1,1,1,1,1"`)
- `impacts` → Comma-separated impacts:
  - `+` for benefit criteria
  - `-` for cost criteria
- `output_file` → Output CSV file containing results

---

### Example

```bash
topsis data.csv "1,1,1,1,1" "+,+,-,+,+" result.csv
```

---

## 🐍 Python API Usage

You can also use the package inside Python:

```python
from topsis.topsis import topsis

topsis(
    "data.csv",
    ["1", "1", "1", "1", "1"],
    ["+", "+", "-", "+", "+"],
    "result.csv"
)
```

---

## 📄 Input Format

- The first column must contain alternative names.
- Remaining columns must contain numeric criteria values.
- No missing values are allowed.

### Example Input File

```csv
Object,Criteria1,Criteria2,Criteria3,Criteria4,Criteria5
Option1,25,50,12,200,45
Option2,30,60,10,180,50
Option3,20,45,15,220,40
```

---

## 📤 Output Format

The output CSV file includes:

- Original data
- `Topsis Score` (value between 0 and 1; higher is better)
- `Rank` (1 indicates the best alternative)

### Example Output

```csv
Object,Criteria1,Criteria2,Criteria3,Criteria4,Criteria5,Topsis Score,Rank
Option1,25,50,12,200,45,0.534,3
Option2,30,60,10,180,50,0.782,1
Option3,20,45,15,220,40,0.654,2
```

---

## ⚠️ Validation Checks

The program validates:

- Number of weights must match number of criteria
- Number of impacts must match number of criteria
- Impacts must be either `+` or `-`
- Criteria columns must contain numeric values only

---

## 🛠 Technologies Used

- Python
- NumPy
- Pandas
- setuptools

---


