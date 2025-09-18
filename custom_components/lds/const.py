from homeassistant.const import Platform
from datetime import timedelta

DOMAIN = "lds"
VERSION = "2.0.1"

CONF_LANGUAGE = "language"

DEFAULT_LANGUAGE = "eng"

PLATFORMS = [Platform.SENSOR]
DEFAULT_TIMEOUT = 120
DEFAULT_REFRESH_RATE = timedelta(minutes=10)

# Integration info for UI display
INTEGRATION_INFO = {
    "name": "Church of Jesus Christ of Latter-day Saints",
    "version": VERSION,
    "documentation": "https://github.com/wilcraig/ha-lds",
    "issue_tracker": "https://github.com/wilcraig/ha-lds/issues",
}
