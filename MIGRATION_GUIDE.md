# LDS Integration v3.0 - Migration Guide

## 🚨 Breaking Changes

Version 3.0 is a complete rewrite that removes the dependency on custom cards and provides a much more reliable experience using standard Home Assistant components.

## What Changed

### ❌ Removed
- Custom JavaScript cards (`lds-quote-card.js`, `lds-scripture-card.js`, etc.)
- Complex web scraping of the church's internal website structure
- Frontend resource registration
- Single complex sensor with nested data

### ✅ Added
- Multiple focused sensors for each content type
- Standard markdown card examples
- Improved error handling and fallback content
- Better data structure and reliability
- Simplified installation process

## Migration Steps

### 1. Remove Old Custom Cards

If you have the old custom cards installed:

1. Remove these lines from your Lovelace resources:
   ```yaml
   - url: /local/community/ha-lds/lds-quote-card.js
     type: module
   - url: /local/community/ha-lds/lds-scripture-card.js
     type: module
   - url: /local/community/ha-lds/lds-come-follow-me-card.js
     type: module
   - url: /local/community/ha-lds/lds-inspirational-card.js
     type: module
   ```

2. Delete the old files from `www/community/ha-lds/` (optional but recommended)

### 2. Update Your Dashboard Cards

#### Old Custom Card (v2.x):
```yaml
type: custom:lds-quote-card
entity: sensor.lds_eng
title: Quote of the Day
show_image: true
```

#### New Markdown Card (v3.0):
```yaml
type: markdown
title: 💬 Quote of the Day
content: |
  > {{ state_attr('sensor.lds_daily_quote_eng', 'text') }}

  **— {{ state_attr('sensor.lds_daily_quote_eng', 'author') }}**

  [Read More]({{ state_attr('sensor.lds_daily_quote_eng', 'url') }})
```

### 3. Sensor Name Changes

#### Old Sensors (v2.x):
- `sensor.lds_eng` (with all data in attributes)

#### New Sensors (v3.0):
- `sensor.lds_daily_scripture_eng`
- `sensor.lds_daily_quote_eng`
- `sensor.lds_come_follow_me_eng`
- `sensor.lds_inspirational_image_eng`

### 4. Data Structure Changes

#### Old Structure (v2.x):
```yaml
# sensor.lds_eng attributes
loaderData:
  routes/my-home/dashboard:
    widgetData:
      daily:
        quote:
          text: "Quote text"
          author: "Author name"
        scripture:
          text: "Scripture text"
          title: "Reference"
```

#### New Structure (v3.0):
```yaml
# sensor.lds_daily_quote_eng attributes
text: "Quote text"
author: "Author name"
source: "General Conference"
url: "https://..."
date: "2024-10-23"

# sensor.lds_daily_scripture_eng attributes
text: "Scripture text"
reference: "John 3:16"
url: "https://..."
date: "2024-10-23"
```

## Complete Migration Example

### Before (v2.x):
```yaml
# Dashboard card
type: custom:lds-quote-card
entity: sensor.lds_eng
title: Daily Quote

# Automation
automation:
  - alias: "Morning LDS Quote"
    trigger:
      platform: time
      at: "08:00:00"
    action:
      service: notify.mobile_app
      data:
        message: >
          {{ state_attr('sensor.lds_eng', 'loaderData')['routes/my-home/dashboard']['widgetData']['daily']['quote']['text'] }}
          - {{ state_attr('sensor.lds_eng', 'loaderData')['routes/my-home/dashboard']['widgetData']['daily']['quote']['author'] }}
```

### After (v3.0):
```yaml
# Dashboard card
type: markdown
title: 💬 Daily Quote
content: |
  > {{ state_attr('sensor.lds_daily_quote_eng', 'text') }}

  **— {{ state_attr('sensor.lds_daily_quote_eng', 'author') }}**

  [Read More]({{ state_attr('sensor.lds_daily_quote_eng', 'url') }})

# Automation
automation:
  - alias: "Morning LDS Quote"
    trigger:
      platform: time
      at: "08:00:00"
    action:
      service: notify.mobile_app
      data:
        message: >
          {{ state_attr('sensor.lds_daily_quote_eng', 'text') }}
          - {{ state_attr('sensor.lds_daily_quote_eng', 'author') }}
```

## Why This Change?

### Problems with v2.x:
- ❌ Custom cards broke frequently with HA updates
- ❌ Complex web scraping was fragile and unreliable
- ❌ Mobile app compatibility issues
- ❌ Difficult to customize styling
- ❌ Performance issues with JavaScript rendering

### Benefits of v3.0:
- ✅ Standard HA components are future-proof
- ✅ Much more reliable data fetching
- ✅ Works perfectly on all devices
- ✅ Easy to style with card-mod
- ✅ Better performance and loading times
- ✅ Simpler maintenance and updates

## Getting Help

If you need help migrating:

1. Check the [MARKDOWN_CARDS_EXAMPLES.md](MARKDOWN_CARDS_EXAMPLES.md) file for card examples
2. Look at the updated [README.md](README.md) for full documentation
3. Open an issue on GitHub if you encounter problems

## Rollback (Not Recommended)

If you absolutely need to rollback to v2.x:

1. Downgrade to version 2.0.3 via HACS
2. Re-add the custom card resources
3. Update your dashboard cards back to custom cards

However, we strongly recommend staying on v3.0 for the improved reliability and future-proofing.
