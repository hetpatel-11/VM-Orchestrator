import os
os.environ["ORGO_API_KEY"] = os.getenv('ORGO_API_KEY', 'your_orgo_api_key_here')
os.environ["ANTHROPIC_API_KEY"] = os.getenv('ANTHROPIC_API_KEY', 'your_anthropic_api_key_here')