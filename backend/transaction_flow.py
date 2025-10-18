import time

def simulate_transaction(recipient, amount, currency="USDC"):
    print("\n🔁 Simulating Transaction Flow...")
    print(f"Client sending {amount} {currency} to {recipient}...")
    time.sleep(3)
    print("✅ Transaction confirmed on Algorand TestNet!")
    print(f"Freelancer {recipient} received {amount} {currency} instantly.")
    print("------------------------------------------------")
    print("FX Rate: 500 NGN/USD | Fees: 2 USD | Total Cost: 1002 USD")
    print("Download receipt → [Simulated]")
    print("Send another payment → [Simulated]\n")

simulate_transaction("Precious N.", 1000)
