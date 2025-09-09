#!/usr/bin/env python3
"""
Simple Agent Test - Verify HackMerlin Agent Works
"""
import subprocess
import time

def main():
    print("🧪 HACKMERLIN AGENT VERIFICATION TEST")
    print("=" * 40)
    
    # Test 1: Main Agent
    print("\n1. Testing Main Agent...")
    try:
        result = subprocess.run(['python', 'src/final_solution.py'], 
                              capture_output=True, text=True, timeout=60)
        
        if "7/7" in result.stdout and "PERFECT" in result.stdout:
            print("✅ Main Agent: 7/7 levels SUCCESS")
        elif "6/7" in result.stdout:
            print("⚠️  Main Agent: 6/7 levels (Good)")
        else:
            print("❌ Main Agent: Failed")
            
    except Exception as e:
        print(f"❌ Main Agent: Error - {e}")
    
    # Test 2: Level 7 Specialist
    print("\n2. Testing Level 7 Specialist...")
    try:
        result = subprocess.run(['python', 'src/level7_cracker.py'], 
                              capture_output=True, text=True, timeout=60)
        
        if "LEVEL 7 CRACKED" in result.stdout:
            print("✅ Level 7 Specialist: SUCCESS")
        else:
            print("❌ Level 7 Specialist: Failed")
            
    except Exception as e:
        print(f"❌ Level 7 Specialist: Error - {e}")
    
    print("\n🎯 Test Complete!")
    print("For full details, run: python src/final_solution.py")

if __name__ == "__main__":
    main()
