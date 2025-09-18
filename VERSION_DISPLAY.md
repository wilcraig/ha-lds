# 🔢 Version Display Configuration Guide

This guide shows you how the LDS integration displays version information in the Home Assistant UI and how to configure the version dropdown options.

## 📊 Version Information in Home Assistant UI

### Integration Page Display
When you go to **Settings** → **Devices & Services** → **LDS Integration**, you'll see:

- **Integration Name**: Church of Jesus Christ of Latter-day Saints
- **Version**: 2.0.0
- **Documentation**: Link to GitHub repository
- **Issue Tracker**: Link to GitHub issues

### Device Information
Each language configuration creates a device with:
- **Device Name**: LDS Integration (ENG)
- **Manufacturer**: Church of Jesus Christ of Latter-day Saints
- **Model**: Scripture & Study Content
- **Software Version**: 2.0.0
- **Configuration URL**: Links to documentation

### Sensor Attributes
Each sensor includes version metadata:

```yaml
# Sensor: sensor.lds_eng
state: "up"
attributes:
  integration_version: "2.0.0"
  integration_name: "Church of Jesus Christ of Latter-day Saints"
  language: "eng"
  documentation: "https://github.com/wilcraig/ha-lds"
  issue_tracker: "https://github.com/wilcraig/ha-lds/issues"
  last_updated: "2025-09-18T10:30:00+00:00"
  # ... plus all the LDS content data
```

## 🌍 Language Dropdown Configuration

### Supported Languages
The integration now includes a proper language dropdown with these options:

```yaml
Languages Available:
- English (eng)
- Español - Spanish (spa)
- Português - Portuguese (por)
- Français - French (fra)
- Deutsch - German (deu)
- Italiano - Italian (ita)
- 日本語 - Japanese (jpn)
- 한국어 - Korean (kor)
- 中文 - Chinese (zho)
```

### Configuration UI
When setting up the integration, users see:

1. **Integration Name** - Friendly name field
2. **Language** - Dropdown with language options
3. **Data Source Version** - Dropdown with options:
   - Current (Latest) - *Recommended*
   - Stable (Tested) - *More reliable*
   - Beta (Preview) - *Experimental features*
4. **Show Version Info** - Checkbox to include version data

## 🔧 Advanced Configuration Options

### Data Source Versions
The integration supports multiple data source versions:

```yaml
Data Source Options:
- current: "Current (Latest)" - Gets the newest content
- stable: "Stable (Tested)" - Uses tested, reliable content
- beta: "Beta (Preview)" - Experimental features and content
```

### Reconfiguration Support
Users can reconfigure without removing the integration:
- Go to integration settings
- Click "Configure"
- Update language, data source, or other options
- Integration reloads with new settings

## 📈 Version Services

### Get Version Information Service
```yaml
service: lds.get_version_info
target:
  entity_id: sensor.lds_eng
```

**Response includes:**
```yaml
integration_version: "2.0.0"
integration_name: "Church of Jesus Christ of Latter-day Saints"
documentation: "https://github.com/wilcraig/ha-lds"
issue_tracker: "https://github.com/wilcraig/ha-lds/issues"
domain: "lds"
entity_state: "up"
entity_id: "sensor.lds_eng"
entity_attributes: {...}
```

### Refresh Data Service
```yaml
service: lds.refresh_data
target:
  entity_id: sensor.lds_eng  # Optional, defaults to all LDS entities
```

## 🎨 Dashboard Version Display

### Version Info Card
```yaml
type: entities
title: "🔢 LDS Integration Info"
entities:
  - entity: sensor.lds_eng
    name: "Status"
    icon: "mdi:church"
  - type: attribute
    entity: sensor.lds_eng
    attribute: integration_version
    name: "Version"
    icon: "mdi:tag"
  - type: attribute
    entity: sensor.lds_eng
    attribute: language
    name: "Language"
    icon: "mdi:translate"
  - type: attribute
    entity: sensor.lds_eng
    attribute: last_updated
    name: "Last Updated"
    icon: "mdi:clock"
```

### Version Badge in Custom Cards
You can add version info to your custom cards:

```yaml
type: custom:lds-scripture-card
entity: sensor.lds_eng
title: "Scripture (v{{ state_attr('sensor.lds_eng', 'integration_version') }})"
```

## 🔍 Diagnostics and Troubleshooting

### Built-in Diagnostics
The integration provides comprehensive diagnostics at:
**Settings** → **Devices & Services** → **LDS Integration** → **Download Diagnostics**

Includes:
- Integration version and configuration
- Entity and device information
- Coordinator status and timing
- Data availability status
- Error logs and exceptions

### Debug Information Template
```yaml
type: markdown
content: |
  ## 🔍 LDS Integration Debug Info

  **Version:** {{ state_attr('sensor.lds_eng', 'integration_version') }}
  **Status:** {{ states('sensor.lds_eng') }}
  **Language:** {{ state_attr('sensor.lds_eng', 'language') }}
  **Last Updated:** {{ state_attr('sensor.lds_eng', 'last_updated') }}

  **Data Available:**
  - Scripture: {{ 'Yes' if state_attr('sensor.lds_eng', 'loaderData') else 'No' }}
  - Quote: {{ 'Yes' if state_attr('sensor.lds_eng', 'inspirational_picture_quote') else 'No' }}

  **Quick Actions:**
  - [Refresh Data](javascript:void(0))
  - [Get Version Info](javascript:void(0))
```

## 🚀 Automation with Version Info

### Version Change Notification
```yaml
automation:
  - alias: "LDS Integration Version Update"
    trigger:
      platform: state
      entity_id: sensor.lds_eng
      attribute: integration_version
    action:
      service: notify.mobile_app
      data:
        title: "LDS Integration Updated"
        message: >
          LDS Integration has been updated to version
          {{ state_attr('sensor.lds_eng', 'integration_version') }}
```

### Health Check Automation
```yaml
automation:
  - alias: "LDS Integration Health Check"
    trigger:
      platform: time
      at: "08:00:00"
    condition:
      condition: state
      entity_id: sensor.lds_eng
      state: "unavailable"
    action:
      service: lds.refresh_data
      target:
        entity_id: sensor.lds_eng
```

## 🔧 Custom Version Dropdown (Advanced)

For developers wanting to add more version options:

### Update const.py
```python
# Additional data source versions
DATA_SOURCE_VERSIONS = {
    "current": "Current (Latest)",
    "stable": "Stable (Tested)",
    "beta": "Beta (Preview)",
    "legacy_v1": "Legacy v1.x Compatible",
    "custom": "Custom Source URL",
}
```

### Update config_flow.py
```python
# Add custom URL field when "custom" is selected
if user_input.get("data_source") == "custom":
    return self.async_show_form(
        step_id="custom_source",
        data_schema=vol.Schema({
            vol.Required("custom_url"): str,
        })
    )
```

## 📊 Version Compatibility Matrix

| HA Version | LDS Integration | Features |
|------------|----------------|----------|
| 2023.7+    | 2.0.0+        | Full features, diagnostics |
| 2023.1+    | 1.5.0+        | Basic features, no diagnostics |
| 2022.12+   | 1.0.0+        | Core functionality only |

## 🎯 Summary

The LDS integration now provides comprehensive version information:

✅ **Integration page displays version and links**
✅ **Device page shows software version**
✅ **Sensor attributes include version metadata**
✅ **Language dropdown with proper options**
✅ **Data source version selection**
✅ **Built-in diagnostics and debugging**
✅ **Version-aware services and automation**
✅ **Reconfiguration without reinstall**

Users get a professional integration experience with full version transparency and easy configuration management!
