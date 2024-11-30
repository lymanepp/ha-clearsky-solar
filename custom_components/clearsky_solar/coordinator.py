import logging
import pandas as pd
from pvlib.location import Location
from datetime import datetime, timezone
from typing import Dict
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from homeassistant.core import HomeAssistant
from .const import DHI, DNI, GHI, UPDATE_INTERVAL

_LOGGER = logging.getLogger(__name__)


class ClearskyCoordinator(DataUpdateCoordinator[dict[str, float]]):
    """Handles updating Clearsky solar irradition estimates."""

    def __init__(self, hass: HomeAssistant):
        """Initialize the coordinator with location."""
        self._location = Location(hass.config.latitude, hass.config.longitude)

        super().__init__(
            hass,
            _LOGGER,
            name="clearsky_solar_data",
            update_method=self.async_update_clearsky_estimates,
            update_interval=UPDATE_INTERVAL,
        )

    async def async_update_clearsky_estimates(self) -> Dict[str, float]:
        """Fetch clearsky data asynchronously and store it."""
        current_time = datetime.now(tz=timezone.utc)
        times = pd.DatetimeIndex([current_time])

        estimates = self._location.get_clearsky(times)
        return {key: estimates[key].iloc[0] for key in [GHI, DNI, DHI]}
