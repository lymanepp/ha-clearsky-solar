# Clearsky Solar Integration for Home Assistant

[![HACS Badge](https://img.shields.io/badge/HACS-Default-41BDF5.svg?style=for-the-badge)](https://github.com/hacs/integration)

Clearsky Solar provides calculated sensors for Home Assistant. This integration uses the `pvlib` library to estimate the sensor values:

> Anderson, K., Hansen, C., Holmgren, W., Jensen, A., Mikofski, M., and Driesse, A. “pvlib python: 2023 project update.” Journal of Open Source Software, 8(92), 5994, (2023). DOI: [10.21105/joss.05994](https://doi.org/10.21105/joss.05994)

---

## Sensors

### Clearsky DHI
**Diffuse Horizontal Irradiance (DHI):**
The portion of solar radiation that reaches the earth indirectly due to scattering by water vapor, aerosols, and clouds.

**Unit:** Watts per square meter (W/m²).

### Clearsky DNI
**Direct Normal Irradiance (DNI):**
The portion of solar radiation that reaches the earth directly from the sun.

**Unit:** Watts per square meter (W/m²).

### Clearsky GHI
**Global Horizontal Irradiance (GHI):**
The total solar radiation per unit area measured on a horizontal surface on the earth. GHI is the sum of two components:
- Direct Normal Irradiance (DNI)
- Diffuse Horizontal Irradiance (DHI)

**Formula:**
![GHI Formula](https://latex.codecogs.com/svg.image?\pagecolor{white}\text{GHI}=\text{DHI}+(\text{DNI}\cdot\cos(\alpha_{\text{zenith}})))

**Unit:** Watts per square meter (W/m²).

---

## Usage

To use Clearsky Solar, follow the documentation for your preferred setup method.

### UI/Frontend (Config Flow)
- Access the integration setup via the Home Assistant UI.

---

## Installation

### Using [HACS](https://hacs.xyz/) (Recommended)
1. Open HACS in Home Assistant.
2. Go to the **Integrations** section.
3. Search for **Clearsky Solar** and install the integration.
4. Restart Home Assistant.

### Manual Installation
1. Clone the repository or download the source code:
    ```bash
    git clone https://github.com/lymanepp/ha-clearsky-solar.git
    cd ha-clearsky-solar
    # If you want a specific version, check out its tag:
    # e.g., git checkout 1.0.0
    ```

2. Copy the `custom_components` folder into your Home Assistant configuration directory:
    ```bash
    cp -r custom_components $hacs_config_folder
    ```
    Alternatively, extract the `custom_components` folder from the source release and place it in your Home Assistant configuration directory.

3. Restart Home Assistant.

---

## Additional Notes

- Check the [project repository](https://github.com/lymanepp/ha-clearsky-solar) for updates or troubleshooting information.
