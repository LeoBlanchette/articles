import argparse

# Constants
SHEKELS_PER_MINA = 60
MINAS_PER_TALENT = 60
SHEKELS_PER_TALENT = SHEKELS_PER_MINA * MINAS_PER_TALENT
STANDARD_WEIGHT = 1  # shekel

def convert_to_shekels(amount, unit):
    if unit == 's':
        return amount
    elif unit == 'm':
        return amount * SHEKELS_PER_MINA
    elif unit == 't':
        return amount * SHEKELS_PER_TALENT
    else:
        raise ValueError("Invalid unit. Use 's' for shekels, 'm' for minas, or 't' for talents.")

def divine_accounting(entrusted, returned):
    gain_ratio = returned / entrusted if entrusted != 0 else 0
    divided = (entrusted / STANDARD_WEIGHT) * gain_ratio
    return gain_ratio, divided

def main():
    parser = argparse.ArgumentParser(description='Divine Accounting Calculator')
    parser.add_argument('-e', '--entrusted', type=float, required=True, help='Amount entrusted')
    parser.add_argument('-r', '--returned', type=float, required=True, help='Amount returned')
    parser.add_argument('-u', '--unit', choices=['s', 'm', 't'], default='s', help='Unit: s (shekel), m (mina), t (talent)')
    
    args = parser.parse_args()

    entrusted_shekels = convert_to_shekels(args.entrusted, args.unit)
    returned_shekels = convert_to_shekels(args.returned, args.unit)

    gain_ratio, divided_value = divine_accounting(entrusted_shekels, returned_shekels)

    print("\nDivine Accounting Process:")
    print(f"  Entrusted (C): {entrusted_shekels} shekels")
    print(f"  Returned: {returned_shekels} shekels")
    print(f"  Gain Ratio (R): {gain_ratio:.2f}")
    print(f"  Standard Weight (W): {STANDARD_WEIGHT} shekel")
    print(f"  Calculation: D = (C ÷ W) × R")
    print(f"  Final Divided Value (D): {divided_value:.2f} shekels")

    if gain_ratio > 1:
        print("  Outcome: Faithful steward. Increase granted.")
    elif gain_ratio == 1:
        print("  Outcome: No gain, no loss. Maintenance only.")
    else:
        print("  Outcome: Unfaithful steward. Reduction expected.")

if __name__ == '__main__':
    main()
