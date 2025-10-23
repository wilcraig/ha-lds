"""Constants for the LDS integration."""
from datetime import timedelta
from homeassistant.const import Platform

DOMAIN = "lds"
VERSION = "3.0.1"

CONF_LANGUAGE = "language"
DEFAULT_LANGUAGE = "eng"

PLATFORMS = [Platform.SENSOR]
DEFAULT_TIMEOUT = 120
DEFAULT_REFRESH_RATE = timedelta(hours=1)

# Integration info for UI display
INTEGRATION_INFO = {
    "name": "Church of Jesus Christ of Latter-day Saints",
    "version": VERSION,
    "documentation": "https://github.com/wilcraig/ha-lds",
    "issue_tracker": "https://github.com/wilcraig/ha-lds/issues",
}

# Sensor types
SENSOR_TYPES = {
    "scripture": {
        "name": "Daily Scripture",
        "icon": "mdi:book-open-page-variant",
        "description": "Daily scripture reading",
    },
    "quote": {
        "name": "Daily Quote",
        "icon": "mdi:format-quote-open",
        "description": "Inspirational quote from church leaders",
    },
    "come_follow_me": {
        "name": "Come Follow Me",
        "icon": "mdi:book-education",
        "description": "Current Come Follow Me lesson",
    },
    "inspirational": {
        "name": "Inspirational Image",
        "icon": "mdi:image-text",
        "description": "Inspirational image with quote",
    },
}
