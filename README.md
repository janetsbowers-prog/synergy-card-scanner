# Synergy Card Scanner 🎫

A mobile-friendly web app to help Synergy cardholders quickly scan their card numbers and check balances during the Costco refund process.

## Background

Synergy Cards company declared bankruptcy. Costco is offering refunds for unused balances on cards purchased at their warehouses. This app helps streamline the process by quickly scanning card numbers with AI.

## Features

- 📸 Camera scanning or image upload
- 🤖 AI-powered card number extraction  
- ✏️ Editable field to verify/fix the number
- 🔗 Direct link to check balance at cardbalance.cc
- 📱 Mobile-optimized interface
- 🎯 Simple, focused, no-database design

## How to Use

1. Open app on your phone
2. Scan or upload photo of your Synergy card
3. Verify the card number (edit if needed)
4. Click "Check Balance" to go to cardbalance.cc
5. Print or screenshot balance for Costco refund

## Costco Refund Process

1. Check your card balance using this tool
2. Take the balance info to any Costco warehouse
3. Request refund at customer service
4. Costco will refund the remaining balance

## Tech Stack

- Flask (Python web framework)
- Anthropic Claude Vision API (card scanning)
- HTML5/CSS/JavaScript (frontend)
- No database needed!

## Deployment

Configured for easy Heroku deployment:
- No database costs!
- Just needs ANTHROPIC_API_KEY environment variable
- Uses shared API credit pool

---

Built to help Synergy cardholders get their refunds! 💚

**This is a free community tool. Not affiliated with Synergy Cards or Costco.**
