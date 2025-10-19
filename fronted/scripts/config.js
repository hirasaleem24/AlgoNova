// =============================================
// 🌐 AlgoNova Configuration File (config.js)
// =============================================
// This file centralizes environment variables and network configuration
// for both frontend (UI) and backend (FastAPI + Algorand SDK).

export const config = {
  // -----------------------------------------
  // 🚀 Project Information
  // -----------------------------------------
  appName: "AlgoNova",
  environment: process.env.NODE_ENV || "development",

  // -----------------------------------------
  // 🌐 API Endpoints
  // -----------------------------------------
  backendBaseUrl: process.env.API_BASE_URL || "http://localhost:8000/api",
  frontendBaseUrl: process.env.FRONTEND_URL || "http://localhost:3000",

  // -----------------------------------------
  // 💰 Algorand TestNet Configuration
  // -----------------------------------------
  algod: {
    server: process.env.ALGOD_SERVER || "https://testnet-api.algonode.cloud",
    port: process.env.ALGOD_PORT || "",
    token:
      process.env.ALGOD_TOKEN ||
      "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    network: "TestNet",
  },

  // -----------------------------------------
  // 🪙 USDC TestNet Asset Details
  // -----------------------------------------
  usdc: {
    asaId: Number(process.env.USDC_ASA_ID) || 31566704, // Standard TestNet USDC ASA
    symbol: "USDC",
    decimals: 6,
  },

  // -----------------------------------------
  // 👤 Wallets (For Demo Purposes Only)
  // Replace with your TestNet accounts for real demo
  // -----------------------------------------
  wallets: {
    sender: {
      address: process.env.SENDER_ADDRESS || "REPLACE_WITH_SENDER_TESTNET_ADDRESS",
      mnemonic:
        process.env.WALLET_MNEMONIC_SENDER ||
        "replace this with your 25-word mnemonic for sender account",
    },
    receiver: {
      address: process.env.RECEIVER_ADDRESS || "REPLACE_WITH_RECEIVER_TESTNET_ADDRESS",
      mnemonic:
        process.env.WALLET_MNEMONIC_RECEIVER ||
        "replace this with your 25-word mnemonic for receiver account",
    },
  },

  // -----------------------------------------
  // 💳 Transaction Settings
  // -----------------------------------------
  transactionDefaults: {
    defaultAmount: Number(process.env.DEFAULT_AMOUNT) || 1000,
    currency: process.env.DEFAULT_CURRENCY || "USD",
    fxRate: Number(process.env.FX_RATE) || 500, // Example: 1 USD = 500 NGN
    transactionFeeUsd: Number(process.env.TRANSACTION_FEE_USD) || 2,
  },

  // -----------------------------------------
  // 🧾 UI & Display Options
  // -----------------------------------------
  ui: {
    enableSimulationMode:
      process.env.ENABLE_SIMULATION_MODE === "True" ||
      process.env.ENABLE_SIMULATION_MODE === "true" ||
      true,
    showTransactionLogs:
      process.env.SHOW_TRANSACTION_LOGS === "True" ||
      process.env.SHOW_TRANSACTION_LOGS === "true" ||
      true,
  },
};

// -----------------------------------------
// 🧩 Utility: Display Config Summary (Optional)
// -----------------------------------------
export function printConfigSummary() {
  console.log("🚀 AlgoNova Config Summary:");
  console.table({
    Environment: config.environment,
    Algorand_Network: config.algod.network,
    Backend_API: config.backendBaseUrl,
    USDC_ASA_ID: config.usdc.asaId,
    FX_Rate: `${config.transactionDefaults.fxRate} NGN/USD`,
  });
}
