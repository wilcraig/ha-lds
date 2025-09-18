"""Services for the LDS integration."""
import logging
from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.helpers.service import async_extract_referenced_entity_ids

from .const import DOMAIN, VERSION, INTEGRATION_INFO

_LOGGER = logging.getLogger(__name__)

async def async_setup_services(hass: HomeAssistant) -> None:
    """Set up services for the LDS integration."""

    async def refresh_entity_data(call: ServiceCall) -> None:
        """Refresh data for specified LDS entities."""
        entity_ids = async_extract_referenced_entity_ids(hass, call)

        if not entity_ids.referenced:
            # If no entities specified, refresh all LDS entities
            entity_ids = [
                entity_id for entity_id in hass.states.async_entity_ids()
                if entity_id.startswith("sensor.lds_")
            ]
        else:
            entity_ids = list(entity_ids.referenced)

        # Update each entity
        for entity_id in entity_ids:
            if entity_id.startswith("sensor.lds_"):
                await hass.services.async_call(
                    "homeassistant",
                    "update_entity",
                    {"entity_id": entity_id}
                )
                _LOGGER.info("Refreshed entity: %s", entity_id)

    async def get_version_info(call: ServiceCall) -> dict:
        """Get version and integration information."""
        entity_ids = async_extract_referenced_entity_ids(hass, call)

        version_info = {
            "integration_version": VERSION,
            "integration_name": INTEGRATION_INFO["name"],
            "documentation": INTEGRATION_INFO["documentation"],
            "issue_tracker": INTEGRATION_INFO["issue_tracker"],
            "domain": DOMAIN,
        }

        if entity_ids.referenced:
            entity_id = list(entity_ids.referenced)[0]
            entity = hass.states.get(entity_id)
            if entity:
                version_info["entity_state"] = entity.state
                version_info["entity_attributes"] = dict(entity.attributes)
                version_info["entity_id"] = entity_id

        _LOGGER.info("Retrieved version info: %s", version_info)
        return version_info

    # Register the services
    hass.services.async_register(
        DOMAIN,
        "refresh_data",
        refresh_entity_data,
        schema=None
    )

    hass.services.async_register(
        DOMAIN,
        "get_version_info",
        get_version_info,
        schema=None,
        supports_response=True
    )

    _LOGGER.info("LDS services registered successfully")


async def async_unload_services(hass: HomeAssistant) -> None:
    """Unload services for the LDS integration."""
    hass.services.async_remove(DOMAIN, "refresh_data")
    hass.services.async_remove(DOMAIN, "get_version_info")
    _LOGGER.info("LDS services unloaded")
