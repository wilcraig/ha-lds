"""The LDS integration."""
import logging
from datetime import timedelta, datetime

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import DOMAIN, PLATFORMS, CONF_LANGUAGE
from .get_data import LDSDataFetcher
from .services import async_setup_services, async_unload_services

_LOGGER = logging.getLogger(__name__)
SCAN_INTERVAL = timedelta(hours=1)


class LDSDataUpdateCoordinator(DataUpdateCoordinator):
    """Coordinator for LDS data updates."""

    def __init__(self, hass: HomeAssistant, language: str):
        """Initialize the coordinator."""
        self.language = language
        self.fetcher = LDSDataFetcher(language)
        
        super().__init__(
            hass,
            _LOGGER,
            name=f"lds_{language}",
            update_interval=SCAN_INTERVAL,
        )

    async def _async_update_data(self):
        """Fetch data from LDS sources."""
        try:
            data = {}
            data["scripture"] = await self.fetcher.get_daily_scripture(self.hass)
            data["quote"] = await self.fetcher.get_daily_quote(self.hass)
            data["come_follow_me"] = await self.fetcher.get_come_follow_me(self.hass)
            data["inspirational"] = await self.fetcher.get_inspirational_image(self.hass)
            data["last_updated"] = datetime.now().isoformat()
            
            _LOGGER.debug("Successfully fetched LDS data for language: %s", self.language)
            return data
            
        except Exception as err:
            _LOGGER.error("Error fetching LDS data: %s", err)
            raise UpdateFailed(f"Error communicating with LDS API: {err}") from err


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up LDS from a config entry."""
    _LOGGER.debug("Setting up LDS integration for language: %s", entry.data[CONF_LANGUAGE])

    # Initialize the coordinator
    coordinator = LDSDataUpdateCoordinator(hass, entry.data[CONF_LANGUAGE])

    # Fetch initial data
    await coordinator.async_config_entry_first_refresh()

    # Store coordinator in hass data
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = {
        "coordinator": coordinator,
    }

    # Setup services
    await async_setup_services(hass)

    # Forward entry setup to platforms
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    _LOGGER.debug("Unloading LDS integration for language: %s", entry.data[CONF_LANGUAGE])

    # Unload platforms
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

    if unload_ok:
        # Remove entry from hass data
        hass.data[DOMAIN].pop(entry.entry_id)

        # Unload services if this is the last entry
        if not hass.data[DOMAIN]:
            await async_unload_services(hass)

    return unload_ok


async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Reload config entry."""
    await async_unload_entry(hass, entry)
    await async_setup_entry(hass, entry)
