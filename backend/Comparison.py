import time

traditional = {"fee": "6%", "settlement": "2-5 days"}
algorand = {"fee": "<1%", "settlement": "4 seconds"}

def display_comparison():
    print("\n💡 VALUE COMPARISON:")
    print("------------------------------------------------")
    print("Traditional Payment:")
    print(f"  Transaction Fees: {traditional['fee']}")
    print(f"  Settlement Time:  {traditional['settlement']}")
    print("\nBlockchain Payment (Algorand):")
    print(f"  Transaction Fees: {algorand['fee']}")
    print(f"  Settlement Time:  {algorand['settlement']}")
    print("------------------------------------------------")

print("Simulating Transaction Comparison...\n")
time.sleep(3)
display_comparison()
