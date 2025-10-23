"""LDS integration sensors."""
from datetime import timedelta, datetime
import logging
from typing import Any

from homeassistant.components.sensor import SensorEntity, SensorDeviceClass
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_NAME
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity, DataUpdateCoordinator, UpdateFailed

from .const import DOMAIN, CONF_LANGUAGE, VERSION, INTEGRATION_INFO
from .get_data import LDSDataFetcher

_LOGGER = logging.getLogger(__name__)
SCAN_INTERVAL = timedelta(hours=1)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up LDS sensors based on a config entry."""
    coordinator = hass.data[DOMAIN][entry.entry_id]["coordinator"]

    sensors = [
        LDSScriptureSensor(coordinator, entry),
        LDSQuoteSensor(coordinator, entry),
        LDSComeFollowMeSensor(coordinator, entry),
        LDSInspirationalImageSensor(coordinator, entry),
    ]

    async_add_entities(sensors, True)


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


class LDSBaseSensor(CoordinatorEntity, SensorEntity):
    """Base class for LDS sensors."""

    def __init__(self, coordinator: LDSDataUpdateCoordinator, entry: ConfigEntry, sensor_type: str):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self.entry = entry
        self.sensor_type = sensor_type
        self._language = entry.data[CONF_LANGUAGE]

        # Generate unique ID
        self._attr_unique_id = f"lds_{sensor_type}_{self._language}"

        # Device info
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, f"lds_{self._language}")},
            name=f"LDS Integration ({self._language.upper()})",
            manufacturer="Church of Jesus Christ of Latter-day Saints",
            model="Scripture & Study Content",
            sw_version=VERSION,
            configuration_url=INTEGRATION_INFO["documentation"],
        )

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return additional state attributes."""
        attrs = {
            "language": self._language,
            "integration_version": VERSION,
            "last_updated": self.coordinator.last_update_success,
        }

        if self.coordinator.data and self.sensor_type in self.coordinator.data:
            data = self.coordinator.data[self.sensor_type]
            attrs.update(data)

        return attrs


class LDSScriptureSensor(LDSBaseSensor):
    """Sensor for daily scripture."""

    def __init__(self, coordinator: LDSDataUpdateCoordinator, entry: ConfigEntry):
        """Initialize the scripture sensor."""
        super().__init__(coordinator, entry, "scripture")
        self._attr_name = f"LDS Daily Scripture ({self._language.upper()})"
        self._attr_icon = "mdi:book-open-page-variant"

    @property
    def state(self) -> str:
        """Return the state of the sensor."""
        if self.coordinator.data and "scripture" in self.coordinator.data:
            scripture_data = self.coordinator.data["scripture"]
            return scripture_data.get("reference", "Unknown")
        return "unavailable"

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return additional state attributes."""
        attrs = super().extra_state_attributes

        if self.coordinator.data and "scripture" in self.coordinator.data:
            scripture_data = self.coordinator.data["scripture"]
            attrs.update({
                "text": scripture_data.get("text"),
                "reference": scripture_data.get("reference"),
                "url": scripture_data.get("url"),
                "date": scripture_data.get("date"),
            })

        return attrs


class LDSQuoteSensor(LDSBaseSensor):
    """Sensor for inspirational quotes."""

    def __init__(self, coordinator: LDSDataUpdateCoordinator, entry: ConfigEntry):
        """Initialize the quote sensor."""
        super().__init__(coordinator, entry, "quote")
        self._attr_name = f"LDS Daily Quote ({self._language.upper()})"
        self._attr_icon = "mdi:format-quote-open"

    @property
    def state(self) -> str:
        """Return the state of the sensor."""
        if self.coordinator.data and "quote" in self.coordinator.data:
            quote_data = self.coordinator.data["quote"]
            return quote_data.get("author", "Unknown")
        return "unavailable"

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return additional state attributes."""
        attrs = super().extra_state_attributes

        if self.coordinator.data and "quote" in self.coordinator.data:
            quote_data = self.coordinator.data["quote"]
            attrs.update({
                "text": quote_data.get("text"),
                "author": quote_data.get("author"),
                "source": quote_data.get("source"),
                "url": quote_data.get("url"),
                "date": quote_data.get("date"),
            })

        return attrs


class LDSComeFollowMeSensor(LDSBaseSensor):
    """Sensor for Come Follow Me lessons."""

    def __init__(self, coordinator: LDSDataUpdateCoordinator, entry: ConfigEntry):
        """Initialize the Come Follow Me sensor."""
        super().__init__(coordinator, entry, "come_follow_me")
        self._attr_name = f"LDS Come Follow Me ({self._language.upper()})"
        self._attr_icon = "mdi:book-education"

    @property
    def state(self) -> str:
        """Return the state of the sensor."""
        if self.coordinator.data and "come_follow_me" in self.coordinator.data:
            lesson_data = self.coordinator.data["come_follow_me"]
            return lesson_data.get("title", "Unknown")
        return "unavailable"

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return additional state attributes."""
        attrs = super().extra_state_attributes

        if self.coordinator.data and "come_follow_me" in self.coordinator.data:
            lesson_data = self.coordinator.data["come_follow_me"]
            attrs.update({
                "title": lesson_data.get("title"),
                "reading": lesson_data.get("reading"),
                "date_range": lesson_data.get("date_range"),
                "url": lesson_data.get("url"),
                "fetched_date": lesson_data.get("fetched_date"),
            })

        return attrs


class LDSInspirationalImageSensor(LDSBaseSensor):
    """Sensor for inspirational images."""

    def __init__(self, coordinator: LDSDataUpdateCoordinator, entry: ConfigEntry):
        """Initialize the inspirational image sensor."""
        super().__init__(coordinator, entry, "inspirational")
        self._attr_name = f"LDS Inspirational Image ({self._language.upper()})"
        self._attr_icon = "mdi:image-text"

    @property
    def state(self) -> str:
        """Return the state of the sensor."""
        if self.coordinator.data and "inspirational" in self.coordinator.data:
            image_data = self.coordinator.data["inspirational"]
            return image_data.get("title", "Unknown")
        return "unavailable"

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return additional state attributes."""
        attrs = super().extra_state_attributes

        if self.coordinator.data and "inspirational" in self.coordinator.data:
            image_data = self.coordinator.data["inspirational"]
            attrs.update({
                "title": image_data.get("title"),
                "image_url": image_data.get("image_url"),
                "page_url": image_data.get("page_url"),
                "collection": image_data.get("collection"),
                "date": image_data.get("date"),
            })

        return attrs
