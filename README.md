# 🌐 AlgoNova

A hybrid **Algorand-based wallet simulation** demonstrating **instant USDC TestNet transfers**, **traditional vs blockchain comparisons**, and **P2P freelancer payments**.

---

## 🚀 Features
- FastAPI backend with core simulation logic  
- JS frontend for user interaction and wallet simulation  
- Real-time comparison between Traditional vs Algorand payments  
- Simple UI to send, swap, or simulate payments  

---

## 🧩 Core Functionalities

### 1️⃣ `comparison.py`
Compares **traditional vs blockchain** performance:
- Fees (6% vs <1%)  
- Settlement (2–5 days vs 4 seconds)  
- Simulates processing via `time.sleep(3)`  

### 2️⃣ `transaction_flow.py`
Simulates end-to-end payment:
- Client sends USDC to freelancer (TestNet)  
- Instant confirmation  
- Placeholder for real on-chain Algorand integration  

---

## ⚙️ Setup

### Clone Repository
```bash
git clone https://github.com/<your-username>/algonova.git
cd algonova
