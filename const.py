from homeassistant.const import Platform
from datetime import timedelta

DOMAIN = "lds"

CONF_LANGUAGE = "language"
CONF_RESOURCE = "resource"

DEFAULT_LANGUAGE = "eng"
DEFAULT_RESOURCE = "Come, Follow Me"

PLATFORMS = [Platform.SENSOR]
DEFAULT_TIMEOUT = 120
DEFAULT_REFRESH_RATE = timedelta(minutes=10)