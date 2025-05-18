from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity, DataUpdateCoordinator
from datetime import timedelta
from .get_data import get_current_data
from .const import DOMAIN, CONF_LANGUAGE, CONF_RESOURCE
import logging

_LOGGER = logging.getLogger(__name__)
SCAN_INTERVAL = timedelta(hours=1)

async def async_setup_entry(hass, entry, async_add_entities):
  """Set up LDS Scripture from a config entry"""
  language = entry.data[CONF_LANGUAGE]
  resource = entry.data[CONF_RESOURCE]

  coordinator = LDSDataUpdateCoordinator(hass, language, resource)
  await coordinator.async_config_entry_first_refresh()

  async_add_entities([LDSSensor(coordinator, language, resource)])

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
    return await self.hass.async_add_executor_job(get_current_data, self.language, self.resource)

class LDSSensor(CoordinatorEntity, SensorEntity):
  _attr_has_entity_name = True

  def __init__(self, coordinator, language, resource):
    super().__init__(coordinator)
    self._attr_name = f"LDS {resource.title()} ({language})"
    self._attr_unique_id = f"lds_scripture_{resource}_{language}"

  @property
  def state(self):
    return self.coordinator.data.get("title", "Unavailable")

  @property
  def extra_state_attributes(self):
    return self.coordinator.data
