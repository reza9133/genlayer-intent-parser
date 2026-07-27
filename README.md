# GenLayer AI Natural Language Intent Parser App

A Web3 application built on **GenLayer (SDK v0.2.17)** that bridges natural human language and smart contract execution. It enables users to submit plain English transaction prompts and leverages multi-validator AI consensus to extract structured, validated transaction intents.

---

## 🌟 Key Features
- **Natural Language Parsing**: Translates raw text prompts (e.g., *"Send 50 USDC to 0x... if ETH is above 3000"*) into executable Web3 actions.
- **Multi-Validator Consensus**: Uses GenLayer's `gl.eq_principle.prompt_non_comparative` to reach consensus among AI validators on action types, parameters, amounts, and execution conditions.
- **Intent-Based Web3 UX**: Provides a foundation for conversational wallets and automated intent execution.
- **On-Chain Tracking**: Stores last-parsed intent states and tracks global request counters directly on-chain.

---

## 🛠️ Tech Stack
- **Smart Contract**: Python (`genlayer` SDK `v0.2.17`)
- **Frontend**: HTML5, Tailwind CSS, JavaScript
- **Network**: GenLayer Testnet

---

## 📁 Repository Structure
