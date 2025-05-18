import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_NAME
from .const import DOMAIN, CONF_LANGUAGE, CONF_RESOURCE, DEFAULT_LANGUAGE, DEFAULT_RESOURCE
import logging

_LOGGER = logging.getLogger(__name__)

class LDSConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
  """Handle a config flow for LDS Scripture."""

  VERSION = 1
  #CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_POLL

  def __init__(self):
    self._data = {}

  async def async_step_user(self, user_input=None):
    _LOGGER.debug("LDS config flow: user step, input=%s", user_input)

    if user_input is not None:
      self._data.update(user_input)
      return self.async_create_entry(title="Church of Jesus Christ of Latter-day Saints", data=self._data)

    return self.async_show_form(
      step_id="user",
      data_schema=vol.Schema({
        vol.Required(CONF_NAME, default="Church of Jesus Christ of Latter-day Saints"): str,
        vol.Required(CONF_LANGUAGE, default=DEFAULT_LANGUAGE): str,
        vol.Required(CONF_RESOURCE, default=DEFAULT_RESOURCE): vol.In(["Come, Follow Me"])
      })
    )