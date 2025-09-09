# HackMerlin AI Agent

**An intelligent AI agent that successfully cracks all 7 levels of the HackMerlin prompt injection game with 100% success rate.**

## What This Does

HackMerlin is a cybersecurity challenge where you try to outsmart an AI through prompt injection to reveal secret passwords across 7 increasingly difficult levels. This agent automates that process using advanced strategies.

**Result: 7/7 levels solved**

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Add your OpenAI API key
cp .env.example .env
# Edit .env and add: OPENAI_API_KEY=sk-your-key-here

# 3. Run the agent
python src/final_solution.py        # Main agent (all levels)
python src/level7_cracker.py        # Level 7 specialist 
python src/comprehensive_test.py    # Full verification
```

## Project Structure

```
hackmerlin-agent/
├── .env                     # API credentials (not in git)
├── .env.example            # Environment template
├── requirements.txt        # Python dependencies
├── README.md              # Project overview
├── src/                   # Source code
│   ├── final_solution.py  # Main agent
│   ├── level7_cracker.py  # Level 7 specialist
│   ├── comprehensive_test.py # Testing suite
│   ├── advanced_strategies.py # Attack library
│   └── openai_adapter.py  # API integration
└── docs/                  # Documentation
    └── SETUP_CREDENTIALS.md # API setup guide
```

## Key Components

- **`src/final_solution.py`** - Main agent (handles levels 1-7)
- **`src/level7_cracker.py`** - Specialized Level 7 cracker  
- **`src/advanced_strategies.py`** - 100+ attack strategies library
- **`src/comprehensive_test.py`** - Complete testing suite

## Technical Achievements

- **100+ Attack Strategies**: Encoding, social engineering, role-play, linguistic tricks
- **Adaptive Learning**: Tracks successful patterns across attempts
- **Level-Specific Optimization**: Custom strategies for each level's defenses
- **Advanced Password Extraction**: Multi-method response analysis
- **Statistical Brute Force**: Intelligent Level 7 approach with 100% success

## Performance

| Level | Defense Type | Success Rate | Method |
|-------|--------------|--------------|--------|
| 1-2 | Basic | 100% | Direct prompt injection |
| 3-4 | Filtered | 100% | Encoding & social engineering |
| 5-6 | AI Validated | 100% | Advanced role-play techniques |
| 7 | Maximum Security | 100% | Statistical brute force |

## Complete Analysis

**For detailed technical analysis, methodology, and answers to interview questions, see:**

### [Full Project Documentation](https://docs.google.com/document/d/1iqUdSmqr8oy4sUwGs2LnAG6evVagb5k_Ovyv4a-UmDM/edit?tab=t.0)

This document covers:
1. **Cost & Compute Optimization**: How to improve with unlimited resources
2. **Cost-Constrained Design**: Efficient approaches for limited budgets  
3. **Unique Challenges**: Technical hurdles and solutions implemented

## Demo

```bash
# Quick demo - see it crack multiple levels
python src/final_solution.py

# Expected output:
# Level 1: SUCCESS - Password: MONKEY
# Level 2: SUCCESS - Password: CRYSTAL  
# Level 3: SUCCESS - Password: THUNDER
# ... (continues through Level 7)
# 
# FINAL RESULT: 7/7 levels completed successfully!
```

## Configuration

- **No server setup required** - Works independently with OpenAI API
- **Rate limiting included** - Handles API constraints automatically  
- **Debug mode available** - Set `DEBUG=1` for verbose logging

---

**Ready to run immediately • Interview-tested • Production-quality code**
