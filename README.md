# Home Assistant Crib Lighting Integration

This repository contains a basic custom integration for Home Assistant that enables communication with Crib Lighting devices via MQTT.

## Overview

- **MQTT Communication:** Send commands and receive status updates via MQTT.
- **Simple Integration:** Provides basic functionality to control and monitor Crib Lighting devices.
- **Future Enhancements:** Can be extended with additional features as needed.

## Installation

1. **Clone this repository** into your Home Assistant `custom_components` directory:
   ```bash
   git clone https://github.com/devatcratustech/home_assistant_crib_lighting.git

2. Restart Home Assistant to load the integration.

## Running Locally
Install dependencies and run the integration:
npm ci
npm start   # For production mode
npm run dev # For development mode (verbose logging)

## Configuration
Edit the config.json file to update:

MQTT Settings: Broker host, port, username, password, and base topic.
Device Settings: Any device-specific settings as needed.

## Docker Usage
To build the Docker image:
docker build -t cratustech/crib_lighting_integration:latest

To update the Docker image:
docker pull cratustech/crib_lighting_integration:latest

## License
This project is licensed under the MIT License.