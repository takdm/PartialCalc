# PartialCalc: Calculate Partial Roll Weights
#
# This script calculates the weight of a partial roll based on user input for full roll footage, full roll weight, partial footage, and number of lanes.
#
# Usage: Run the script and follow the prompts to enter the required values.

def main():
    # Prompt user for the full roll footage (in feet)
    print("Enter full roll footage:")
    fullfeet = int(input())

    # Prompt user for the full roll weight
    print("Enter full roll weight:")
    fullweight = int(input())

    # Prompt user for the partial roll footage (rounded, in feet)
    print("Enter partial footage (rounded):")
    partfootage = int(input())

    # Prompt user for the number of lanes
    print("Enter amount of lanes:")
    lanes = int(input())

    # Calculate the weight of the partial roll
    partialweight = fullweight / fullfeet * partfootage

    # Output the results
    print("Your per roll partial weight is", partialweight)
    print("Your partials total at", lanes * partialweight)

    input()

# Call the main function to execute the script
if __name__ == "__main__":
    main()