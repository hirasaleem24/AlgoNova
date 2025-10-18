import { getComparison, simulatePayment } from "./api.js";

document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("payment-form");
  const compareBtn = document.getElementById("compare-btn");
  const result = document.getElementById("result");
  const comparison = document.getElementById("comparison-result");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const recipient = document.getElementById("recipient").value;
    const amount = document.getElementById("amount").value;
    const currency = document.getElementById("currency").value;

    result.innerHTML = "⏳ Processing payment...";
    const data = await simulatePayment(recipient, amount, currency);
    result.innerHTML = `
      ✅ You just sent ${amount} ${currency} to ${recipient}.<br>
      💱 FX Rate: 500 NGN/USD<br>
      💵 Fees: 2 USD<br>
      💰 Total Cost: ${parseFloat(amount) + 2} USD<br>
      🧾 <a href="#">Download Receipt</a>
    `;
  });

  compareBtn.addEventListener("click", async () => {
    const comparisonData = await getComparison();
    comparison.textContent = JSON.stringify(comparisonData, null, 2);
  });
});
