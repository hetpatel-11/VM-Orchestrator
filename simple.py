import os
from dotenv import load_dotenv
from orgo import Computer

# Load environment variables from .env file
load_dotenv()

# Print debug information
print("Loading environment variables...")
print(f"ORGO_API_KEY: {'Set' if os.getenv('ORGO_API_KEY') else 'Not set'}")
print(f"ANTHROPIC_API_KEY: {'Set' if os.getenv('ANTHROPIC_API_KEY') else 'Not set'}")

# Initialize a computer
print("Initializing Orgo Computer...")
computer = Computer(project_id="yourcomputerid", api_key=os.getenv('ORGO_API_KEY', 'your_orgo_api_key_here'))
print("Orgo Computer initialized successfully!")

# Let Claude control the computer with natural language
print("Sending command to Orgo...")
computer.prompt("Open Firefox and search for pictures of cats")

# Clean up when done
print("Cleaning up...")
computer.destroy()
print("Done!")
