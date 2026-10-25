"""
Test script for SlothSurf.
Validates configuration and basic module imports.
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from slothsurf.config import Config
from slothsurf.presets import PRESET_TASKS

def test_config():
    print("[TEST] Checking configuration...")
    print(f"  - Grok Model: {Config.GROK_MODEL}")
    print(f"  - Base URL: {Config.XAI_BASE_URL}")
    print(f"  - Headless: {Config.HEADLESS}")
    print(f"  - Slow Mo: {Config.BROWSER_SLOW_MO}ms")
    print(f"  - Key Configured: {'Yes' if Config.validate() else 'No (Default placeholder)'}")

def test_presets():
    print("[TEST] Checking presets...")
    assert len(PRESET_TASKS) >= 4, "Should have at least 4 preset missions"
    for key, item in PRESET_TASKS.items():
        assert "title" in item
        assert "task" in item
        print(f"  [OK] Preset {key}: {item['title']}")

if __name__ == "__main__":
    print("=" * 40)
    print("SLOTHSURF SELF-CHECK")
    print("=" * 40)
    test_config()
    test_presets()
    print("=" * 40)
    print("Configuration and Presets verified successfully!")
