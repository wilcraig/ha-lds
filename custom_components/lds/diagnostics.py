"""Diagnostics support for LDS integration."""
from __future__ import annotations

from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers import device_registry as dr, entity_registry as er

from .const import DOMAIN, VERSION, INTEGRATION_INFO


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, config_entry: ConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for a config entry."""

    # Get coordinator data
    coordinator = hass.data[DOMAIN][config_entry.entry_id]["coordinator"]

    # Get entity registry info
    entity_registry = er.async_get(hass)
    entities = []
    for entity_entry in er.async_entries_for_config_entry(entity_registry, config_entry.entry_id):
        entities.append({
            "entity_id": entity_entry.entity_id,
            "original_name": entity_entry.original_name,
            "platform": entity_entry.platform,
            "disabled": entity_entry.disabled,
            "hidden": entity_entry.hidden,
        })

    # Get device registry info
    device_registry = dr.async_get(hass)
    devices = []
    for device_entry in dr.async_entries_for_config_entry(device_registry, config_entry.entry_id):
        devices.append({
            "id": device_entry.id,
            "name": device_entry.name,
            "model": device_entry.model,
            "manufacturer": device_entry.manufacturer,
            "sw_version": device_entry.sw_version,
        })

    diagnostics_data = {
        "integration": {
            "domain": DOMAIN,
            "version": VERSION,
            "name": INTEGRATION_INFO["name"],
            "documentation": INTEGRATION_INFO["documentation"],
        },
        "config_entry": {
            "title": config_entry.title,
            "data": {
                # Only include safe config data (no sensitive info)
                "language": config_entry.data.get("language"),
                "name": config_entry.data.get("name"),
                "data_source": config_entry.data.get("data_source", "current"),
                "show_version_info": config_entry.data.get("show_version_info", True),
            },
            "options": dict(config_entry.options),
            "version": config_entry.version,
            "state": config_entry.state.value,
        },
        "coordinator": {
            "last_update_success": coordinator.last_update_success,
            "last_exception": str(coordinator.last_exception) if coordinator.last_exception else None,
            "update_interval": str(coordinator.update_interval),
            "data_keys": list(coordinator.data.keys()) if coordinator.data else [],
            "last_update_success_time": coordinator.last_update_success_time.isoformat() if coordinator.last_update_success_time else None,
        },
        "entities": entities,
        "devices": devices,
        "runtime_data": {
            "data_available": coordinator.data is not None,
            "data_size": len(str(coordinator.data)) if coordinator.data else 0,
            "has_scripture": bool(coordinator.data and coordinator.data.get("loaderData", {}).get("routes/my-home/dashboard", {}).get("widgetData", {}).get("daily", {}).get("scripture")),
            "has_quote": bool(coordinator.data and coordinator.data.get("loaderData", {}).get("routes/my-home/dashboard", {}).get("widgetData", {}).get("daily", {}).get("quote")),
            "has_cfm": bool(coordinator.data and coordinator.data.get("loaderData", {}).get("routes/my-home/dashboard", {}).get("widgetData", {}).get("cfm")),
            "has_inspirational": bool(coordinator.data and coordinator.data.get("inspirational_picture_quote")),
        }
    }

    return diagnostics_data
