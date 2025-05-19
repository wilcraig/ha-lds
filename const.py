from homeassistant.const import Platform
from datetime import timedelta

DOMAIN = "lds"

CONF_LANGUAGE = "language"

DEFAULT_LANGUAGE = "eng"

PLATFORMS = [Platform.SENSOR]
DEFAULT_TIMEOUT = 120
DEFAULT_REFRESH_RATE = timedelta(minutes=10)