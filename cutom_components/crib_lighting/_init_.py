"""Home Assistant Lighting Displays - Custom Integration."""
from homeassistant.core import HomeAssistant

DOMAIN = "lighting_displays"

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Lighting Displays integration."""
    hass.states.async_set(f"{DOMAIN}.status", "initialized")
    return True
