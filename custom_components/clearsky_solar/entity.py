from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .coordinator import ClearskyCoordinator


class ClearskySolarEntity(CoordinatorEntity[ClearskyCoordinator]):
    """Base entity for Clearsky Solar sensors."""

    def __init__(self, coordinator: ClearskyCoordinator):
        """Initialize the base entity."""
        super().__init__(coordinator)
        self._attr_should_poll = False
