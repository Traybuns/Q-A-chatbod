import os

# List of required modules
required_modules = [
    "streamlit",
    "langchain",
    "python-dotenv",
    "openai"  # Required for langchain OpenAI integration
]

# Install each module using pip
for module in required_modules:
    os.system(f"pip install {module}")

print("All required modules have been installed.")

