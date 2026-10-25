import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file from project root
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

class Config:
    XAI_API_KEY: str = os.getenv("XAI_API_KEY", "")
    GROK_MODEL: str = os.getenv("GROK_MODEL", "grok-2-vision-1212")
    HEADLESS: bool = os.getenv("HEADLESS", "false").lower() in ("true", "1", "yes")
    BROWSER_SLOW_MO: int = int(os.getenv("BROWSER_SLOW_MO", "1000"))
    XAI_BASE_URL: str = "https://api.x.ai/v1"

    @classmethod
    def validate(cls) -> bool:
        """Check if an API key is provided."""
        if not cls.XAI_API_KEY or cls.XAI_API_KEY == "your_xai_api_key_here":
            return False
        return True
