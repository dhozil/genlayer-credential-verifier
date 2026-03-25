# 🎓 CredentialVerifier — On-Chain Credential & Certificate Verifier

A trustless, AI-powered system for verifying academic degrees and professional certifications on the GenLayer blockchain.

> "No more fake degrees. No more manual calls to HR departments. Just on-chain truth."

---

## 🔍 The Problem

Fake credentials cost the global economy over $1 billion annually:
- 1 in 3 job applicants misrepresent their qualifications
- Manual verification takes days and requires institutional cooperation
- Centralized services (LinkedIn, Credly) are trusted but single points of failure
- Traditional smart contracts cannot read a credential page and evaluate it

## ✅ The Solution

CredentialVerifier uses GenLayer's AI validators to:
1. Fetch the credential URL directly on-chain (no oracle needed)
2. Cross-reference with publicly available issuer data
3. Reach consensus across multiple independent LLM validators
4. Store the result permanently on-chain as tamper-proof proof

---

## ⚙️ Verification Flow
Anyone deploys contract
    └─> __init__() — no parameters needed

Call verify() with:
    └─> credential_url: public URL to the credential
    └─> holder_name: full name of the credential holder
    └─> expected_issuer: name of the issuing institution
    └─> credential_type: type of credential

Validators fetch the credential URL
    └─> Each validator's LLM evaluates:
          - Does the name on the credential match the holder?
          - Is the issuer the expected institution?
          - Does the credential type match?
    └─> Validators reach consensus via Equivalence Principle
    └─> State → "verified: ..." ✅ or "rejected: ..." ❌

Call get_state() to read the result

---

## 📋 Contract Methods

| Method | Type | Description |
|---|---|---|
| __init__() | Deploy | Initialize contract — no parameters needed |
| verify(credential_url, holder_name, expected_issuer, credential_type) | ✍️ Write | Trigger AI-based verification |
| get_state() | 👁️ Read | Returns verification result and explanation |

---

## 🚀 Quick Deploy (GenLayer Studio)

1. Go to [studio.genlayer.com](https://studio.genlayer.com)
2. Create new contract → paste credential_verifier.py
3. Deploy — no parameters needed
4. Call `verify` (Write) with:
credential_url  → "https://www.credly.com/badges/example-badge"
holder_name     → "Your Full Name"
expected_issuer → "Amazon Web Services"
credential_type → "AWS Certified Solutions Architect"
5. Call `get_state` (Read) to see the AI verdict

---

## 💡 Supported Credential Types

| Credential | URL Source Examples |
|---|---|
| University Degree | University verification portal, LinkedIn Education |
| AWS / Google / Azure Certification | Credly badge URL, certification portal |
| Bootcamp Certificate | Certificate public link (Coursera, Udemy, etc.) |
| Professional License | Public license registry URL |
| Online Course Completion | Coursera / edX certificate URL |

---

## 🌍 Real-World Applications

- Employers verifying candidates before making job offers
- DAOs gating governance roles behind verified credentials
- DeFi protocols requiring professional certifications for access
- Universities issuing tamper-proof diplomas on-chain
- Freelance platforms building verified skill profiles

---

## 🧪 Testnet Deployment

Network: GenLayer Testnet Bradbury  
Contract Address: *(update after deployment)*  
Transaction Hash: *(update after deployment)*

---

## 📄 License

MIT — free to use, fork, and build upon.

---

## 🏗️ Built With

- [GenLayer](https://genlayer.com) — AI-native blockchain
- [GenVM Python SDK](https://docs.genlayer.com) — Intelligent Contract framework
- Built as part of the [GenLayer Incentivized Builder Program](https://portal.genlayer.foundation)
