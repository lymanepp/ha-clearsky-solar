from homeassistant.components.sensor import (
    SensorEntity,
    SensorEntityDescription,
    SensorDeviceClass,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import UnitOfIrradiance
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DHI, DNI, GHI, DOMAIN
from .coordinator import ClearskyCoordinator
from .entity import ClearskySolarEntity


class ClearskySolarSensor(ClearskySolarEntity, SensorEntity):
    """Representation of Clearsky Solar Irradiance sensor (GHI, DNI, etc.)."""

    def __init__(self, coordinator: ClearskyCoordinator, desc: SensorEntityDescription):
        """Initialize the sensor with the DataUpdateCoordinator and sensor description."""
        super().__init__(coordinator)
        self.entity_description = desc
        self._attr_unique_id = f"{DOMAIN}_{desc.key}"

    @property
    def native_value(self) -> float | None:
        """Return the current value from the coordinator data."""
        if self.coordinator.data:
            return self.coordinator.data.get(self.entity_description.key)
        return None


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the Clearsky Solar sensors from config entry."""
    coordinator: ClearskyCoordinator = hass.data[DOMAIN]
    async_add_entities([ClearskySolarSensor(coordinator, desc) for desc in SENSOR_DESCRIPTIONS])


SENSOR_DESCRIPTIONS = [
    SensorEntityDescription(
        key=GHI,
        name="Clearsky GHI",
        device_class=SensorDeviceClass.IRRADIANCE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement=UnitOfIrradiance.WATTS_PER_SQUARE_METER,
        suggested_display_precision=1,
    ),
    SensorEntityDescription(
        key=DNI,
        name="Clearsky DNI",
        device_class=SensorDeviceClass.IRRADIANCE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement=UnitOfIrradiance.WATTS_PER_SQUARE_METER,
        suggested_display_precision=1,
    ),
    SensorEntityDescription(
        key=DHI,
        name="Clearsky DHI",
        device_class=SensorDeviceClass.IRRADIANCE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement=UnitOfIrradiance.WATTS_PER_SQUARE_METER,
        suggested_display_precision=1,
    ),
]
