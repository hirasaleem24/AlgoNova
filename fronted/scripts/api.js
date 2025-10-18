const BASE_URL = "http://localhost:8000";

export async function getComparison() {
  const res = await fetch(`${BASE_URL}/compare`);
  return await res.json();
}

export async function simulatePayment(recipient, amount, currency) {
  const res = await fetch(`${BASE_URL}/simulate`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ recipient, amount, currency }),
  });
  return await res.json();
}

