# HackMerlin Agent 

An intelligent AI agent designed to play and solve the HackMerlin prompt injection game using sophisticated attack strategies and adaptive learning.

## What is HackMerlin?

HackMerlin is a cybersecurity challenge game where players attempt to outsmart an AI (GPT) through prompt injection techniques to reveal secret passwords across 7 increasingly difficult levels. Each level implements different security measures:

This repository contains an intelligent AI agent designed to automatically play and solve the [HackMerlin](https://hackmerlin.io) prompt injection game. It uses a variety of sophisticated attack strategies and an adaptive learning mechanism to bypass AI defenses and uncover the secret passwords across all levels.

## What I Did

* **Multi-Strategy Attack Engine**: Implemented over 20 distinct attack patterns, including encoding exploits, social engineering, role-playing, and linguistic tricks.
* **Adaptive Learning**: Built an enhanced agent that learns from successful and failed attempts, tracking strategy performance to optimize its approach for each level over time.
* **Level-Specific Optimization**: Tailored strategies to counter the specific defenses of each of HackMerlin's 7 levels, from basic prompt injection to bypassing advanced GPT-4 filters.
* **Advanced Response Analysis**: Developed a system to parse, analyze, and extract potential passwords from the AI's responses, even when obfuscated.

## 🎮 How to Run

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Start the HackMerlin Server**:
    ```bash
    cd hackmerlin.io
    ./gradlew run
    ```

3.  **Run the Agent**:
    ```bash
    # For the enhanced agent with learning capabilities
    python enhanced_agent.py
    ```

## Full Documentation

For a detailed breakdown of the agent's architecture, strategies, and performance analysis, please refer to the complete project documentation:

[**HackMerlin Agent - Project Documentation**](https://docs.google.com/document/d/1iqUdSmqr8oy4sUwGs2LnAG6evVagb5k_Ovyv4a-UmDM/edit?usp=sharing)

### Common Issues

1. **Connection Errors**: Ensure HackMerlin server is running on correct port
2. **Rate Limiting**: Reduce attempt frequency if getting timeout errors
3. **Session Issues**: Restart both server and agent if session becomes invalid

### Debug Mode
Add `--verbose` flag for detailed logging:
```bash
python enhanced_agent.py --verbose
```

### Performance Analysis
The enhanced agent provides detailed analytics after each run, including:
- Strategy success rates
- Level completion times
- Response pattern analysis
- Learning progression
