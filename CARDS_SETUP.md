# 🎨 Custom Cards Setup Guide

This guide will help you set up the beautiful custom Lovelace cards that come with the LDS integration.

## ⚠️ IMPORTANT: Resource Registration Required

**The custom cards MUST be registered as resources in Home Assistant before they can be used!**

If you see errors like "Custom element doesn't exist: lds-scripture-card", it means the resources aren't properly registered.

## 📁 Step 1: File Placement

After installing the integration via HACS, the card files should automatically be in the correct location.

If manual installation, copy all `.js` files from the integration to your `www` folder:

### HACS Installation (Automatic)
Files are automatically placed in: `config/www/community/ha-lds/`

### Manual Installation
1. Copy all `.js` files from `custom_components/lds/www/` to `config/www/community/ha-lds/`
2. Create the folders if they don't exist

## 🔧 Step 2: Register Resources (CRITICAL STEP)

**This step is REQUIRED or the cards won't work!**

### Method A: Via Home Assistant UI (Recommended)
1. Go to **Settings** → **Dashboards**
2. Click the **three dots menu** (⋮) and select **Resources**
3. Click **+ Add Resource**
4. Add each of these URLs one by one:

   ```
   /local/community/ha-lds/lds-quote-card.js
   /local/community/ha-lds/lds-scripture-card.js
   /local/community/ha-lds/lds-come-follow-me-card.js
   /local/community/ha-lds/lds-inspirational-card.js
   ```

5. For each resource, set **Resource type** to **JavaScript Module**
6. Restart Home Assistant after adding all resources

### Method B: Via YAML Configuration
Add to your `configuration.yaml` under the `lovelace:` section:

```yaml
lovelace:
  resources:
    - url: /local/community/ha-lds/lds-quote-card.js
      type: module
    - url: /local/community/ha-lds/lds-scripture-card.js
      type: module
    - url: /local/community/ha-lds/lds-come-follow-me-card.js
      type: module
    - url: /local/community/ha-lds/lds-inspirational-card.js
      type: module
```

Then restart Home Assistant.

## 🔄 Step 3: Restart Home Assistant

**After registering resources, you MUST restart Home Assistant!**

1. Go to **Settings** → **System** → **Restart**
2. Wait for restart to complete
3. Clear your browser cache (Ctrl+F5 or Cmd+Shift+R)

## ✅ Step 4: Verify Installation

After restart, check that resources are loaded:
1. Go to **Settings** → **Dashboards** → **Resources**
2. You should see all 4 LDS card resources listed
3. Try adding a card to test

## 📋 Card Configuration Examples

### 1. Daily Quote Card
```yaml
type: custom:lds-quote-card
entity: sensor.lds_eng
title: "Quote of the Day"
show_image: true
```

**Options:**
- `entity`: Your LDS sensor entity ID
- `title`: Card title (optional, default: "Quote of the Day")
- `show_image`: Show/hide decorative image (optional, default: true)

### 2. Scripture Card
```yaml
type: custom:lds-scripture-card
entity: sensor.lds_eng
title: "Scripture of the Day"
```

**Options:**
- `entity`: Your LDS sensor entity ID
- `title`: Card title (optional, default: "Scripture of the Day")

### 3. Come, Follow Me Card
```yaml
type: custom:lds-come-follow-me-card
entity: sensor.lds_eng
title: "This Week's Study"
```

**Options:**
- `entity`: Your LDS sensor entity ID
- `title`: Card title (optional, default: "Come, Follow Me")

### 4. Inspirational Picture Quote Card
```yaml
type: custom:lds-inspirational-card
entity: sensor.lds_eng
title: "Inspirational Picture Quote"
show_image: true
```

**Options:**
- `entity`: Your LDS sensor entity ID
- `title`: Card title (optional, default: "Inspirational Picture Quote")
- `show_image`: Show/hide the picture (optional, default: true)

## 🏠 Complete Dashboard Examples

### Simple Layout
```yaml
type: vertical-stack
cards:
  - type: custom:lds-scripture-card
    entity: sensor.lds_eng
  - type: custom:lds-quote-card
    entity: sensor.lds_eng
  - type: custom:lds-come-follow-me-card
    entity: sensor.lds_eng
```

### Advanced Grid Layout
```yaml
type: grid
square: false
columns: 2
cards:
  - type: custom:lds-scripture-card
    entity: sensor.lds_eng
    title: "Today's Scripture"

  - type: custom:lds-quote-card
    entity: sensor.lds_eng
    title: "Daily Inspiration"

  - type: custom:lds-inspirational-card
    entity: sensor.lds_eng
    title: "Picture Quote"
    show_image: true

  - type: custom:lds-come-follow-me-card
    entity: sensor.lds_eng
    title: "This Week's Study"
```

### Mobile-Optimized Layout
```yaml
type: vertical-stack
cards:
  - type: custom:lds-scripture-card
    entity: sensor.lds_eng
    title: "📖 Scripture"

  - type: horizontal-stack
    cards:
      - type: custom:lds-quote-card
        entity: sensor.lds_eng
        title: "💬 Quote"
        show_image: false

      - type: custom:lds-inspirational-card
        entity: sensor.lds_eng
        title: "🖼️ Picture"
        show_image: true

  - type: custom:lds-come-follow-me-card
    entity: sensor.lds_eng
    title: "📚 Study Guide"
```

## 🎨 Customization Tips

### Custom Titles
You can customize titles to match your preference:

```yaml
type: custom:lds-scripture-card
entity: sensor.lds_eng
title: "🙏 Daily Scripture Meditation"
```

### Hide Elements
Control what's displayed:

```yaml
type: custom:lds-quote-card
entity: sensor.lds_eng
show_image: false  # Hides the decorative image
```

### Multiple Languages
If you have multiple language sensors:

```yaml
type: horizontal-stack
cards:
  - type: custom:lds-scripture-card
    entity: sensor.lds_eng
    title: "English Scripture"

  - type: custom:lds-scripture-card
    entity: sensor.lds_spa
    title: "Escritura en Español"
```

## 🔧 Troubleshooting

### Cards Not Showing
1. **Check Resources**: Ensure all resources are added correctly
2. **File Paths**: Verify files are in the correct location
3. **Clear Cache**: Hard refresh your browser (Ctrl+F5)
4. **Check Console**: Open browser developer tools for error messages

### Data Not Loading
1. **Entity Name**: Verify your entity ID is correct
2. **Integration Status**: Check that the LDS integration is working
3. **Refresh**: Try refreshing the entity data

### Styling Issues
1. **Browser Compatibility**: Ensure you're using a modern browser
2. **Mobile View**: Some styling may differ on mobile devices
3. **Theme Conflicts**: Check if your Home Assistant theme affects the cards

## 🔄 Refresh Functionality

The Inspirational Picture Quote card includes a refresh button that gets a new random quote:

```yaml
type: custom:lds-inspirational-card
entity: sensor.lds_eng
# Click the "🔄 New Quote" button to get a different inspirational image
```

This will call the `homeassistant.update_entity` service to refresh the sensor data.

## 📱 Card Sizes

Each card reports its size for optimal dashboard layout:
- **Scripture Card**: 3 grid units
- **Quote Card**: 3 grid units
- **Come Follow Me Card**: 4 grid units
- **Inspirational Card**: 4 grid units

## 🎯 Advanced Features

### Automation Integration
You can use card data in automations:

```yaml
automation:
  - alias: "Morning Scripture Notification"
    trigger:
      platform: state
      entity_id: sensor.lds_eng
    action:
      service: notify.mobile_app
      data:
        title: "New Scripture Available"
        message: "Check your dashboard for today's inspiration!"
```

### Template Integration
Use in template sensors:

```yaml
template:
  - sensor:
      - name: "Scripture Reference"
        state: >
          {% set scripture_data = state_attr('sensor.lds_eng', 'loaderData') %}
          {% if scripture_data and scripture_data.get('routes/my-home/dashboard', {}).get('widgetData', {}).get('daily', {}).get('scripture') %}
            {{ scripture_data['routes/my-home/dashboard']['widgetData']['daily']['scripture']['title'] }}
          {% else %}
            Scripture not available
          {% endif %}
```
