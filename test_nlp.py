import sys
import os

# Add the project root to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

try:
    # Try importing the chatbot
    from smarthire_ai.app.nlp.train import NLPChatbot
    
    # Initialize the chatbot
    chatbot = NLPChatbot()
    print("✅ Successfully imported and initialized NLPChatbot!")
    
    # Test a simple prediction
    test_input = "Tell me about your experience with Python"
    print(f"\nTesting with input: '{test_input}'")
    
    # This assumes your NLPChatbot has a predict method - adjust if needed
    if hasattr(chatbot, 'predict'):
        response = chatbot.predict(test_input)
        print(f"Response: {response}")
    else:
        print("Note: The predict method is not available in the current implementation.")
    
    print("\n✅ Test completed successfully!")
    
except Exception as e:
    print(f"❌ Error: {str(e)}")
    print("\nTroubleshooting steps:")
    print(f"1. Current working directory: {os.getcwd()}")
    print(f"2. Python path: {sys.path}")
    print(f"3. Files in project root: {os.listdir(project_root)}")
    print("\nPlease ensure the project structure is correct and all required packages are installed.")
