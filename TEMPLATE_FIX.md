# Template Error Fix

## Issue
Users were experiencing template errors when trying to access sensor data:
```
Error while processing template: UndefinedError: 'None' has no attribute 'loaderData'
```

## Root Cause
The documentation examples were using incorrect template syntax to access the sensor data:

**Incorrect (causing errors):**
```yaml
{{ state_attr('sensor.lds_eng', 'state')['loaderData']['routes/my-home/dashboard']['widgetData']['daily']['scripture']['text'] }}
```

**Problems:**
1. Trying to access `['state']` attribute that doesn't exist
2. No null checking for when the sensor hasn't loaded data yet
3. Fragile template that breaks if any part of the data structure is missing

## Solution
Updated all templates to use correct syntax with proper null checking:

**Correct (robust):**
```yaml
{% set scripture_data = state_attr('sensor.lds_eng', 'loaderData') %}
{% if scripture_data and scripture_data.get('routes/my-home/dashboard', {}).get('widgetData', {}).get('daily', {}).get('scripture') %}
  {% set scripture = scripture_data['routes/my-home/dashboard']['widgetData']['daily']['scripture'] %}
  {{ scripture.text }}
  - {{ scripture.title }}
{% else %}
  Scripture not available at this time.
{% endif %}
```

## Key Changes

### 1. Removed Incorrect 'state' Access
- **Before:** `state_attr('sensor.lds_eng', 'state')['loaderData']`
- **After:** `state_attr('sensor.lds_eng', 'loaderData')`

### 2. Added Null Checking
- Check if `loaderData` exists before accessing nested properties
- Use `.get()` method with default values for safe navigation
- Provide fallback messages when data isn't available

### 3. Better Template Structure
- Set variables first for readability
- Use conditional blocks to handle missing data gracefully
- Provide meaningful error messages to users

## Files Updated
- `README.md` - Fixed automation examples
- `CARDS_SETUP.md` - Fixed template sensor examples

## Custom Cards
The custom Lovelace cards were already using correct syntax with safe navigation:
```javascript
const scripture = data?.loaderData?.['routes/my-home/dashboard']?.widgetData?.daily?.scripture;
```

## Testing
After this fix:
- ✅ Templates no longer throw `UndefinedError`
- ✅ Graceful handling when sensor is loading
- ✅ Meaningful messages when data is unavailable
- ✅ Robust templates that work across different data states

## Best Practices for LDS Integration Templates

### Always Use Safe Navigation
```yaml
{% set data = state_attr('sensor.lds_eng', 'loaderData') %}
{% if data and data.get('routes/my-home/dashboard', {}).get('widgetData', {}).get('daily', {}).get('scripture') %}
  # Access data safely here
{% else %}
  # Provide fallback
{% endif %}
```

### Check Entity State First
```yaml
{% if states('sensor.lds_eng') not in ['unavailable', 'unknown'] %}
  # Process data
{% else %}
  Integration is loading...
{% endif %}
```

### Provide Meaningful Fallbacks
Instead of showing errors, provide helpful messages:
- "Loading scripture..."
- "Data not available at this time"
- "Please check integration status"
