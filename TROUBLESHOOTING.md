# 🔧 Troubleshooting Common Issues

## Custom Element Doesn't Exist Errors

### Error Message:
```
Configuration error
Custom element doesn't exist: lds-scripture-card.
```

### Cause:
The custom cards haven't been registered as resources in Home Assistant.

### Solution:

#### 1. Verify File Location
Check that card files exist in `config/www/community/ha-lds/`:
- `lds-quote-card.js`
- `lds-scripture-card.js`
- `lds-come-follow-me-card.js`
- `lds-inspirational-card.js`

#### 2. Register Resources
Go to **Settings** → **Dashboards** → **Resources** and add:
```
/local/community/ha-lds/lds-quote-card.js (JavaScript Module)
/local/community/ha-lds/lds-scripture-card.js (JavaScript Module)
/local/community/ha-lds/lds-come-follow-me-card.js (JavaScript Module)
/local/community/ha-lds/lds-inspirational-card.js (JavaScript Module)
```

#### 3. Restart Home Assistant
**Required after adding resources!**

#### 4. Clear Browser Cache
Press Ctrl+F5 (Windows) or Cmd+Shift+R (Mac)

## Sensor Errors

### Error Message:
```
AttributeError: 'LDSDataUpdateCoordinator' object has no attribute 'last_update_success_time'
```

### Cause:
Incorrect attribute name in sensor code.

### Solution:
This is fixed in version 2.0.1+. Update the integration through HACS.

## Template Errors

### Error Message:
```
UndefinedError: 'None' has no attribute 'loaderData'
```

### Cause:
Template trying to access data before sensor has loaded.

### Solution:
Use safe templates with null checking:

**Bad:**
```yaml
{{ state_attr('sensor.lds_eng', 'state')['loaderData']['routes/my-home/dashboard']['widgetData']['daily']['scripture']['text'] }}
```

**Good:**
```yaml
{% set scripture_data = state_attr('sensor.lds_eng', 'loaderData') %}
{% if scripture_data and scripture_data.get('routes/my-home/dashboard', {}).get('widgetData', {}).get('daily', {}).get('scripture') %}
  {{ scripture_data['routes/my-home/dashboard']['widgetData']['daily']['scripture']['text'] }}
{% else %}
  Scripture loading...
{% endif %}
```

## Integration Not Loading Data

### Symptoms:
- Sensor shows "unavailable" or "unknown"
- Cards show "No data available"
- Attributes are empty

### Troubleshooting:

#### 1. Check Network Connectivity
The integration fetches data from churchofjesuschrist.org

#### 2. Check Logs
Go to **Settings** → **System** → **Logs** and search for "lds"

#### 3. Manually Refresh
Call the `lds.refresh_data` service:
```yaml
service: lds.refresh_data
target:
  entity_id: sensor.lds_eng
```

#### 4. Check Integration Status
Go to **Settings** → **Devices & Services** → **LDS Integration**

## Card Display Issues

### Cards Not Showing Data
1. Check that sensor has data: `sensor.lds_eng` should not be "unavailable"
2. Verify entity ID in card configuration matches your sensor
3. Check browser console for JavaScript errors (F12)

### Cards Not Styling Correctly
1. Clear browser cache
2. Check that all resources are loaded
3. Verify card files are not corrupted

### Images Not Loading
1. Check network connectivity to churchofjesuschrist.org
2. Verify image URLs in sensor attributes
3. Check Content Security Policy settings

## Installation Issues

### HACS Installation Fails
1. Verify HACS is properly installed
2. Check that repository URL is correct: `https://github.com/wilcraig/ha-lds`
3. Restart Home Assistant after installation

### Manual Installation Issues
1. Verify file structure:
   ```
   config/
   ├── custom_components/
   │   └── lds/
   │       ├── __init__.py
   │       ├── manifest.json
   │       ├── sensor.py
   │       └── ... (other files)
   └── www/
       └── community/
           └── ha-lds/
               ├── lds-quote-card.js
               └── ... (other cards)
   ```

2. Check file permissions
3. Restart Home Assistant after copying files

## Dependency Issues

### Error Message:
```
Unable to install package requests==2.31.0: No solution found when resolving dependencies
```

### Solution:
Update to version 2.0.1+ which fixes dependency conflicts.

## Getting Help

### Before Asking for Help:
1. Check this troubleshooting guide
2. Update to the latest version
3. Check the logs for specific error messages
4. Try restarting Home Assistant

### Where to Get Help:
- [GitHub Issues](https://github.com/wilcraig/ha-lds/issues)
- Home Assistant Community Forum
- Provide full error messages and logs when asking for help

## Useful Diagnostic Commands

### Check Sensor Status
```yaml
# Developer Tools → States
# Look for: sensor.lds_eng
```

### Refresh Data Manually
```yaml
service: lds.refresh_data
target:
  entity_id: sensor.lds_eng
```

### Get Version Info
```yaml
service: lds.get_version_info
target:
  entity_id: sensor.lds_eng
```

### Template Testing
Use **Developer Tools** → **Template** to test templates safely:
```yaml
{{ state_attr('sensor.lds_eng', 'loaderData') }}
```
