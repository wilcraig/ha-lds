import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_NAME
from .const import DOMAIN, CONF_LANGUAGE, DEFAULT_LANGUAGE, VERSION
import logging

_LOGGER = logging.getLogger(__name__)

# Supported languages with display names
SUPPORTED_LANGUAGES = {
    "eng": "English",
    "spa": "Español (Spanish)",
    "por": "Português (Portuguese)",
    "fra": "Français (French)",
    "deu": "Deutsch (German)",
    "ita": "Italiano (Italian)",
    "jpn": "日本語 (Japanese)",
    "kor": "한국어 (Korean)",
    "zho": "中文 (Chinese)",
}

# Data source versions (for future use)
DATA_SOURCE_VERSIONS = {
    "current": "Current (Latest)",
    "stable": "Stable (Tested)",
    "beta": "Beta (Preview)",
}

class LDSConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
  """Handle a config flow for LDS Scripture."""

  VERSION = 1
  #CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_POLL

  def __init__(self):
    self._data = {}

  async def async_step_user(self, user_input=None):
    _LOGGER.debug("LDS config flow: user step, input=%s", user_input)
    errors = {}

    if user_input is not None:
      # Validate language selection
      if user_input[CONF_LANGUAGE] not in SUPPORTED_LANGUAGES:
        errors[CONF_LANGUAGE] = "invalid_language"
      else:
        self._data.update(user_input)
        return self.async_create_entry(
          title=f"LDS ({SUPPORTED_LANGUAGES[user_input[CONF_LANGUAGE]]})",
          data=self._data
        )

    return self.async_show_form(
      step_id="user",
      data_schema=vol.Schema({
        vol.Required(CONF_NAME, default="Church of Jesus Christ of Latter-day Saints"): str,
        vol.Required(CONF_LANGUAGE, default=DEFAULT_LANGUAGE): vol.In(SUPPORTED_LANGUAGES),
        vol.Optional("data_source", default="current"): vol.In(DATA_SOURCE_VERSIONS),
        vol.Optional("show_version_info", default=True): bool,
      }),
      errors=errors,
      description_placeholders={
        "version": VERSION,
        "supported_languages": ", ".join(SUPPORTED_LANGUAGES.values()),
      }
    )

  async def async_step_reconfigure(self, user_input=None):
    """Handle reconfiguration of the integration."""
    if user_input is not None:
      return self.async_update_reload_and_abort(
        self._get_reconfigure_entry(),
        data_updates=user_input,
      )

    # Get current config
    entry = self._get_reconfigure_entry()
    current_config = entry.data

    return self.async_show_form(
      step_id="reconfigure",
      data_schema=vol.Schema({
        vol.Required(CONF_NAME, default=current_config.get(CONF_NAME, "Church of Jesus Christ of Latter-day Saints")): str,
        vol.Required(CONF_LANGUAGE, default=current_config.get(CONF_LANGUAGE, DEFAULT_LANGUAGE)): vol.In(SUPPORTED_LANGUAGES),
        vol.Optional("data_source", default=current_config.get("data_source", "current")): vol.In(DATA_SOURCE_VERSIONS),
        vol.Optional("show_version_info", default=current_config.get("show_version_info", True)): bool,
      }),
      description_placeholders={
        "version": VERSION,
        "current_language": SUPPORTED_LANGUAGES.get(current_config.get(CONF_LANGUAGE, DEFAULT_LANGUAGE), "Unknown"),
      }
    )
