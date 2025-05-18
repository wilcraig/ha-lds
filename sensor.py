from homeassistant.core import HomeAssistant
from homeassistant.const import CONF_NAME
from homeassistant.helpers.entity import Entity
from homeassistant.config_entries import ConfigEntry
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity, DataUpdateCoordinator
from homeassistant.util import slugify
from datetime import timedelta
from .get_data import get_current_data
from .const import DOMAIN, CONF_LANGUAGE, CONF_RESOURCE

import logging
import async_timeout
from typing import Any

_LOGGER = logging.getLogger(__name__)
SCAN_INTERVAL = timedelta(hours=1)

async def async_setup_entry(hass, entry, async_add_entities):
    """Set up LDS Scripture from a config entry"""
    #   language = entry.data[CONF_LANGUAGE]
    #   resource = entry.data[CONF_RESOURCE]
    
    #   coordinator = LDSDataUpdateCoordinator(hass, language, resource)
    #   await coordinator.async_config_entry_first_refresh()
    
    #   async_add_entities([LDSSensor(coordinator, language, resource)])
    
    async_add_entities([LDSSensor(hass, entry)], True)

class LDSDataUpdateCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, language, resource):
        self.language = language
        self.resource = resource
        super().__init__(
            hass,
            _LOGGER,
            name=f"lds_scripture_{resource}_{language}",
            update_interval=SCAN_INTERVAL
        )

    async def _async_update_data(self):
        try:
            return await self.hass.async_add_executor_job(get_current_data, self.hass, self.language, self.resource)
        except Exception as err:
            raise UpdateFailed(err) from err

class LDSSensor(CoordinatorEntity):
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        _LOGGER.debug("hass.data snapshot: %s", hass.data.get(DOMAIN, {}))
        if entry is not None:
            entry_id = entry.entry_id
            sensor_coordinator = hass.data[DOMAIN][entry_id]["coordinator"]
            super().__init__(sensor_coordinator)
            sensor_name = entry.data[CONF_NAME]
        else:
            sensor_name = config[CONF_NAME]
            entry_id = ""
            sensor_coordinator = hass.data[DOMAIN][sensor_name]["coordinator"]
            super().__init__(sensor_coordinator)
        
        self.coordinator = sensor_coordinator
        self._entry_id = entry_id
        self._name = sensor_name
        
        self._hass = hass
        self._entry = entry
        self._attr_unique_id = f"{entry.entry_id}_scripture"
        self._attr_extra_state_attributes = {
            "language": entry.data[CONF_LANGUAGE],
            "resource": entry.data[CONF_RESOURCE]
        }
        
    @property
    def state(self):
        return getattr(self, "_state", "unavailable")
        
    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        attrs = {}
        
        if self.coordinator.data is None:
            return attrs
            
        data = self.coordinator.data or {}
            
        attrs["dateRange"] = data.get("dateRange", "unknown")
        attrs["title"] = data.get("title", "unknown")
        attrs["url"] = data.get("url", "unknown")
        
        return attrs
        
    async def async_update(self) -> None:
        try:
            async with async_timeout.timeout(10):
                val = await get_current_data(self._hass, language=self._entry.data[CONF_LANGUAGE], resource=self._entry.data[CONF_RESOURCE])
                self._state = val
        except Exception as err:
            _LOGGER.warning("Unable to fetch data: %s", err)
            self._state = "unavailable"

# class LDSSensor(CoordinatorEntity, SensorEntity):
#   _attr_has_entity_name = True

#   def __init__(self, coordinator, language, resource):
#     super().__init__(coordinator)
#     self._attr_name = f"LDS {resource.title()} ({language})"
#     self._attr_unique_id = f"lds_scripture_{resource}_{language}"

#   @property
#   def state(self):
#     return self.coordinator.data.get("title", "Unavailable")

#   @property
#   def extra_state_attributes(self):
#     return self.coordinator.data