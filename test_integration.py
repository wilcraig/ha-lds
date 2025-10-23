#!/usr/bin/env python3
"""Simple test script to validate the modified LDS integration functions."""

import asyncio
import sys
import os

# Add the custom components directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'custom_components', 'lds'))

try:
    from get_data import LDSDataFetcher
    print("✅ Successfully imported LDSDataFetcher")
except ImportError as e:
    print(f"❌ Import error: {e}")
    sys.exit(1)

class MockHass:
    """Mock Home Assistant object for testing."""

    def async_add_executor_job(self, func, *args, **kwargs):
        """Mock executor job."""
        return func(*args, **kwargs)

async def test_functions():
    """Test the modified functions."""
    print("\n🧪 Testing modified LDS integration functions...")

    # Create fetcher instance
    fetcher = LDSDataFetcher("eng")
    mock_hass = MockHass()

    print("\n📖 Testing daily scripture...")
    try:
        scripture = await fetcher.get_daily_scripture(mock_hass)
        print(f"✅ Scripture: {scripture['reference']}")
        print(f"   Text: {scripture['text'][:100]}...")
        print(f"   URL: {scripture['url']}")
    except Exception as e:
        print(f"❌ Scripture error: {e}")

    print("\n💬 Testing daily quote...")
    try:
        quote = await fetcher.get_daily_quote(mock_hass)
        print(f"✅ Quote: {quote['author']}")
        print(f"   Text: {quote['text'][:100]}...")
        print(f"   Source: {quote['source']}")
    except Exception as e:
        print(f"❌ Quote error: {e}")

    print("\n🖼️ Testing inspirational image...")
    try:
        image = await fetcher.get_inspirational_image(mock_hass)
        print(f"✅ Image: {image['title']}")
        print(f"   Collection: {image['collection']}")
        print(f"   Has image URL: {'Yes' if image['image_url'] else 'No'}")
    except Exception as e:
        print(f"❌ Image error: {e}")

    print("\n📚 Testing Come Follow Me...")
    try:
        cfm = await fetcher.get_come_follow_me(mock_hass)
        print(f"✅ CFM: {cfm['title']}")
        print(f"   Reading: {cfm['reading']}")
        print(f"   Dates: {cfm['date_range']}")
    except Exception as e:
        print(f"❌ CFM error: {e}")

if __name__ == "__main__":
    print("🚀 Starting LDS Integration Test")
    asyncio.run(test_functions())
    print("\n✅ Test completed!")
