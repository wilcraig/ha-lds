import logging
import arrow
from async_timeout import timeout

from .get_data import get_current_data
from .const import (
    DOMAIN, 
    PLATFORMS, 
    DEFAULT_TIMEOUT, 
    DEFAULT_REFRESH_RATE,
    CONF_LANGUAGE,
)

from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.const import CONF_NAME

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, entry):
  _LOGGER.debug("Forwarding LDS config entry to sensor platform")
  
  #hass.data.setdefault(DOMAIN, {})[entry.entry_id] = entry.data
  hass.data.setdefault(DOMAIN, {})
  coordinator = LDSDataUpdateCoordinator(
    hass, entry.data, entry
  )
  
  await coordinator.async_refresh()
  
  hass.data[DOMAIN][entry.entry_id] = {
      "coordinator": coordinator,
  }
  
  hass.async_create_task(
    hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
  )
  return True

async def async_unload_entry(hass, entry):
  unload_ok = await hass.config_entries.async_forward_entry_unload(entry, "sensor")
  if unload_ok:
    hass.data[DOMAIN].pop(entry.entry_id)
  return unload_ok
  
class LDSDataUpdateCoordinator(DataUpdateCoordinator):
    data_cache = {}
    last_update = {}
    c_cache = {}
    
    def __init__(self, hass, config, entry: ConfigEntry=None):
        self.name = config.get(CONF_NAME, DOMAIN)
        self.language = config[CONF_LANGUAGE]
        self.config = config
        self.hass = hass
        self.entry = entry
        
        super().__init__(hass, _LOGGER, name=self.name, update_interval=DEFAULT_REFRESH_RATE)
        _LOGGER.debug(
            "%s: Using default refresh rate (%s)", self.name, self.update_interval
        )
        
    async def _async_update_data(self):
        async with timeout(DEFAULT_TIMEOUT):
            try:
                data = await self.async_update_display_data(self.config, self.hass)
            except Exception as error:
                _LOGGER.debug("%s: Error updating data: %s", self.name, error)
                _LOGGER.debug("%s: Error type: %s", self.name, type(error).__name__)
                _LOGGER.debug("%s: Additional information: %s", self.name, str(error))
                
                raise UpdateFailed(error) from error
            return data
            
    async def async_update_display_data(self, config, hass) -> dict:
        sensor_name = self.name
        lang = self.language
        
        key = lang
        
        data = await get_current_data(self.hass, language=self.language)
        self.data_cache[key] = data
        self.last_update[key] = arrow.now().format(arrow.FORMAT_W3C)
        
        _LOGGER.debug("Coordinator fetched data type=%s data=%s", type(data), data)
        
        return data
