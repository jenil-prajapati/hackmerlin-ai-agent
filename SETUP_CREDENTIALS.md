# 🔑 Quick Credential Setup Guide

## **Option 1: Azure OpenAI (Production)**

### 1. Get Azure Account
```bash
# Sign up at: https://portal.azure.com
# Free tier includes $200 credit
```

### 2. Request Access
```bash
# Apply at: https://aka.ms/oai/access
# Usually takes 1-7 days for approval
```

### 3. Configure HackMerlin
```yaml
# Edit: hackmerlin.io/backend/src/main/resources/application.yml
merlin:
  azure:
    key: your-azure-openai-api-key
    url: https://your-resource-name.openai.azure.com
```

---

## **Option 2: OpenAI API (Immediate)**

### 1. Get OpenAI API Key
```bash
# Sign up at: https://platform.openai.com
# Go to API Keys → Create new key
# Copy the key (starts with sk-)
```

### 2. Configure Environment
```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your actual API key:
# OPENAI_API_KEY=sk-your-actual-api-key-here
```

Alternative: Set as environment variable
```bash
export OPENAI_API_KEY="sk-your-openai-api-key-here"
```

### 3. Use Our Adapter
```bash
# The agent can use regular OpenAI API through our adapter
# No server modification needed!
```

---

## **Option 3: Free Local Testing**

### Use Mock Mode (No API Required)
```bash
cd hackmerlin-agent
python mock_test.py
# Full functionality demonstration without API costs
```

---

## **Recommended Approach:**

1. **Start with Mock Testing** (immediate, free)
2. **Get OpenAI API key** (quick, works immediately)  
3. **Request Azure OpenAI** (best for production, takes time)

---

## **Cost Estimates:**

- **Mock Testing**: Free
- **OpenAI API**: ~$0.01-0.10 per game session
- **Azure OpenAI**: Similar pricing, more enterprise features

---

## **Next Steps:**

Choose your approach and I'll help you configure it! 