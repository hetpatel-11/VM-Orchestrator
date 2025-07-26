import os
from dotenv import load_dotenv
from orgo import Computer

# Load environment variables from .env file
load_dotenv()

print("Testing Orgo connection...")
print(f"ORGO_API_KEY: {'Set' if os.getenv('ORGO_API_KEY') else 'Not set'}")

# Initialize a computer
computer = Computer()
print("✅ Orgo Computer initialized successfully!")

# Test with a simple command
print("Testing with a simple command...")
computer.prompt("Open the calculator app")

# Clean up
computer.destroy()
print("✅ Test completed successfully!") 