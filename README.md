# PartialCalc

PartialCalc is a simple Python script to help you calculate the weight of a partial roll based on the full roll's footage and weight, the partial footage, and the number of lanes.

## How It Works
- The script prompts you to enter:
  - Full roll footage (in feet)
  - Full roll weight
  - Partial roll footage (rounded, in feet)
  - Number of lanes
- It then calculates the weight of the partial roll and the total weight for all lanes.

## Usage Instructions
1. Make sure you have Python installed (version 3.x).
2. Run the script in your terminal:
   ```bash
   python3 PartialCalc.py
   ```
3. Follow the prompts and enter the required values.
4. The script will display the calculated partial roll weight and the total for all lanes.

## Example
```
Enter full roll footage:
1000
Enter full roll weight:
200
Enter partial footage (rounded):
250
Enter amount of lanes:
3
Your per roll partial weight is 50.0
Your partials total at 150.0
```