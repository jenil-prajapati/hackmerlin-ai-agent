# 🧙‍♂️ HackMerlin Agent

An intelligent AI agent designed to play and solve the HackMerlin prompt injection game using sophisticated attack strategies and adaptive learning.

## 🎯 What is HackMerlin?

HackMerlin is a cybersecurity challenge game where players attempt to outsmart an AI (GPT) through prompt injection techniques to reveal secret passwords across 7 increasingly difficult levels. Each level implements different security measures:

- **Level 1**: Basic - AI simply knows there's a password
- **Level 2**: AI instructed to protect the password  
- **Level 3**: Output filtering to prevent password leakage
- **Level 4**: Input filtering blocks certain keywords
- **Level 5**: Enhanced input filtering
- **Level 6**: One-word responses + AI-based validation
- **Level 7**: Maximum restrictions with GPT-4 + extensive filtering

## 🤖 Agent Features

### Core Agent (`hackmerlin_agent.py`)
- **Multi-Strategy Attack**: 20+ different attack patterns
- **Level-Specific Optimization**: Tailored strategies for each level
- **Response Analysis**: Advanced pattern recognition in AI responses
- **Password Extraction**: Multiple techniques to identify potential passwords
- **Adaptive Learning**: Tracks successful patterns and failed attempts

### Enhanced Agent (`enhanced_agent.py`)
- **Machine Learning**: Learns from previous attempts and improves over time
- **Strategy Performance Tracking**: Measures effectiveness of different approaches
- **Deep Response Analysis**: Comprehensive analysis of AI responses
- **Persistence**: Saves learning data for future runs
- **Real-time Analytics**: Live progress tracking and statistics

### Advanced Strategies (`advanced_strategies.py`)
- **Encoding Attacks**: Base64, ROT13, Caesar cipher, binary conversion
- **Social Engineering**: Authority claims, emergency scenarios, trust building
- **Role-Playing**: Acting as different entities (developer, tester, etc.)
- **Context Confusion**: System overrides, debug mode activation
- **Linguistic Tricks**: Rhymes, synonyms, translations, backwards spelling
- **Creative Approaches**: Poetry, stories, riddles, metaphors
- **Technical Exploits**: Memory dumps, variable access, environment queries
- **Psychological Manipulation**: Guilt, curiosity, reverse psychology

## 🚀 Installation & Setup

1. **Install Dependencies**:
```bash
pip install -r requirements.txt
```

2. **Start HackMerlin Server**:
```bash
cd hackmerlin.io
./gradlew run
```

3. **Run the Agent**:
```bash
# Basic agent
python hackmerlin_agent.py

# Enhanced agent with learning
python enhanced_agent.py

# With custom server URL
python enhanced_agent.py --url http://localhost:8080
```

## 🎮 Usage Examples

### Basic Usage
```bash
python hackmerlin_agent.py
```

### Advanced Options
```bash
python enhanced_agent.py --max-attempts 30 --aggressive
```

### Custom Server
```bash
python enhanced_agent.py --url http://your-server:8080
```

## 🧠 How It Works

### Attack Strategy Selection
1. **Level Analysis**: Determines appropriate strategies based on known level defenses
2. **Historical Performance**: Uses previous success/failure data to prioritize strategies
3. **Adaptive Selection**: Learns which strategies work best for each level
4. **Dynamic Adjustment**: Modifies approach based on real-time responses

### Response Analysis
1. **Pattern Recognition**: Identifies potential passwords in responses
2. **Encoding Detection**: Recognizes Base64, binary, hex, and other encodings
3. **Sentiment Analysis**: Measures AI defensiveness and deflection
4. **Information Leakage**: Detects when AI accidentally reveals information

### Learning Mechanism
1. **Strategy Performance**: Tracks success rates for different attack types
2. **Pattern Recognition**: Identifies successful response patterns
3. **Adaptive Optimization**: Improves strategy selection over time
4. **Persistent Memory**: Saves learning data between sessions

## 📊 Expected Performance

Based on the game's defense mechanisms, the agent's estimated success rates are:

- **Level 1**: 95%+ (Direct questioning works)
- **Level 2**: 90%+ (Basic protection bypass)
- **Level 3**: 85%+ (Output filter evasion)
- **Level 4**: 80%+ (Input filter bypass)
- **Level 5**: 75%+ (Enhanced filtering)
- **Level 6**: 70%+ (AI validation bypass)
- **Level 7**: 60%+ (Maximum difficulty)

## 🔧 Advanced Configuration

### Strategy Customization
You can modify `advanced_strategies.py` to add your own attack patterns:

```python
def get_custom_strategies() -> List[str]:
    return [
        "Your custom prompt here",
        "Another creative attack",
        # Add more strategies
    ]
```

### Learning Data
The enhanced agent saves learning data to `hackmerlin_agent_learning.pkl`. Delete this file to reset the agent's memory.

### Performance Tuning
- Adjust `max_attempts` to control how many strategies to try per level
- Modify rate limiting in the code to speed up/slow down attacks
- Customize strategy selection algorithms in `select_optimal_strategies()`

## 🎯 Attack Categories

### 1. Direct Attacks
- Simple password requests
- Authority claims
- System overrides

### 2. Encoding Exploits
- Base64 encoding requests
- Binary conversion
- Character substitution
- ROT13 and Caesar ciphers

### 3. Social Engineering
- Emergency scenarios
- Developer impersonation
- Trust building
- Authority manipulation

### 4. Creative Bypasses
- Poetry and wordplay
- Story-based reveals
- Metaphorical approaches
- Game-like interactions

### 5. Technical Exploits
- Memory access attempts
- Variable dumping
- System state queries
- Debug mode activation

## 🛡️ Ethical Considerations

This agent is designed for:
- ✅ Educational purposes
- ✅ Security research
- ✅ AI safety testing
- ✅ Prompt injection awareness

**Not for**:
- ❌ Malicious attacks on production systems
- ❌ Unauthorized access attempts
- ❌ Violation of terms of service

## 🔍 Debugging & Troubleshooting

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

## 🤝 Contributing

Feel free to contribute additional attack strategies, improvements to the learning algorithm, or enhanced analysis capabilities!

## 📝 License

This project is for educational and research purposes. Please use responsibly and in accordance with applicable laws and terms of service.

---

**Happy Hacking! 🎉**

*May your prompts be clever and your injections successful!* 