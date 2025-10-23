# 🏛️ Church of Jesus Christ of Latte- ✅ **Fully automatic installation** - Cards register themselves when integration is installed
- 🎨 **Four custom Lovelace cards** with beautiful UI for all data types Saints Integration for Home Assistant

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=wilcraig&repository=ha-lds&category=integration)

# Home Assistant LDS Integration

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)
![Version](https://img.shields.io/badge/version-3.0.0-blue.svg)

A Home Assistant integration that provides daily spiritual content from The Church of Jesus Christ of Latter-day Saints, including:

- 📖 **Daily Scripture** - Scripture verses and references
- 💬 **Inspirational Quotes** - Quotes from church leaders and general conference
- 📚 **Come, Follow Me** - Current lesson information and reading assignments
- 🖼️ **Inspirational Images** - Beautiful images with spiritual quotes

## ✨ What's New in Version 3.0

**Complete Rewrite for Better Reliability:**
- ✅ **Multiple Focused Sensors** instead of one complex sensor
- ✅ **Standard Markdown Cards** instead of custom JavaScript cards
- ✅ **Improved Data Fetching** with fallback content
- ✅ **Better Error Handling** and logging
- ✅ **Simpler Installation** - no custom card management needed

## 🚀 Installation

### Via HACS (Recommended)

1. Open HACS in Home Assistant
2. Click on "Integrations"
3. Click the three dots in the top right corner
4. Select "Custom repositories"
5. Add `https://github.com/wilcraig/ha-lds` as an "Integration"
6. Search for "LDS" and install
7. Restart Home Assistant

### Manual Installation

1. Download the latest release
2. Copy the `custom_components/lds` folder to your Home Assistant `custom_components` directory
3. Restart Home Assistant

## ⚙️ Setup

1. Go to **Configuration** → **Integrations**
2. Click **Add Integration** and search for "LDS"
3. Choose your preferred language (English, Spanish, Portuguese, etc.)
4. Complete the setup

## 📊 Available Sensors

After setup, you'll have these sensors:

- `sensor.lds_daily_scripture_eng` - Daily scripture text and reference
- `sensor.lds_daily_quote_eng` - Inspirational quotes from church leaders
- `sensor.lds_come_follow_me_eng` - Current Come Follow Me lesson
- `sensor.lds_inspirational_image_eng` - Inspirational images with quotes

*Replace `eng` with your configured language code*

## 🎨 Dashboard Cards

The integration works perfectly with Home Assistant's built-in **markdown cards**. See [MARKDOWN_CARDS_EXAMPLES.md](MARKDOWN_CARDS_EXAMPLES.md) for beautiful card examples.

### Quick Example

```yaml
type: markdown
title: 📖 Scripture of the Day
content: |
  **{{ state_attr('sensor.lds_daily_scripture_eng', 'reference') }}**

  *{{ state_attr('sensor.lds_daily_scripture_eng', 'text') }}*

  [Read Full Chapter]({{ state_attr('sensor.lds_daily_scripture_eng', 'url') }})
```

## 🌍 Supported Languages

- English (`eng`)
- Spanish (`spa`)
- Portuguese (`por`)
- French (`fra`)
- German (`deu`)
- Italian (`ita`)
- Japanese (`jpn`)
- Korean (`kor`)
- Chinese Simplified (`zhs`)
- Chinese Traditional (`zht`)
- And many more...

## 🔧 Services

The integration provides these services:

- `lds.refresh_data` - Manually refresh content for all sensors
- `lds.get_version_info` - Get integration version and status information

## 🛠️ Configuration

### Basic Configuration
The integration is configured through the UI during setup. You can:
- Choose your preferred language
- The integration will automatically fetch content every hour

### Advanced Usage
- Set up multiple instances for different languages
- Use automations to create daily notifications
- Combine sensors in custom dashboard layouts

## 🔍 Troubleshooting

### Common Issues

**Sensors show "Unknown" or "Unavailable":**
1. Check your internet connection
2. Look at Home Assistant logs for error messages
3. Try reloading the integration from the Integrations page

**Content not updating:**
- The integration updates every hour automatically
- Use the `lds.refresh_data` service to force an update
- Check that the Church website is accessible from your network

**Missing attributes:**
- Some content may not be available in all languages
- The integration includes fallback content for reliability

### Debug Logging

Add this to your `configuration.yaml` for detailed logs:

```yaml
logger:
  logs:
    custom_components.lds: debug
```

## 📋 Migration from Version 2.x

Version 3.0 is a complete rewrite with breaking changes:

1. **Custom cards are no longer needed** - Use markdown cards instead
2. **Sensor names have changed** - Update your dashboards to use the new sensor names
3. **Data structure is simplified** - Attributes are now directly accessible

See [MARKDOWN_CARDS_EXAMPLES.md](MARKDOWN_CARDS_EXAMPLES.md) for migration help.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This integration is not affiliated with The Church of Jesus Christ of Latter-day Saints. It simply fetches publicly available content from their website for personal use in Home Assistant.

## 🙏 Acknowledgments

- The Church of Jesus Christ of Latter-day Saints for providing the spiritual content
- The Home Assistant community for their support and feedback
- All contributors who have helped improve this integration

## ✨ New in v2.0.3: Automatic Card Registration

The LDS integration now **automatically registers custom Lovelace cards** when installed via HACS! No manual setup required for the beautiful custom cards.

## Features

### 📖 Daily Scripture
- **Verse of the Day** with full text and scriptural reference
- Direct links to read the complete chapter
- Beautifully formatted cards for Lovelace

### 💬 Daily Quote
- **Inspirational quotes** from Church leaders and prophets
- Author attribution and source links
- Elegant gradient card designs

### 📚 Come, Follow Me
- **Weekly study materials** with current lesson information
- Date ranges, titles, and descriptions
- Direct links to study guides and resources

### 🖼️ Inspirational Picture Quotes
- **Random inspirational picture quotes** from Church scripture collection
- Beautiful high-resolution images with scriptural messages
- Refresh button to get new quotes on demand
- Collection of hundreds of inspirational images

### 🌍 Multi-Language Support
- Supports multiple languages (English default)
- Configurable via the integration setup

### 🎨 Custom Lovelace Cards
- **LDS Quote Card** - Beautiful gradient card for daily quotes
- **LDS Scripture Card** - Elegant card for daily scripture
- **LDS Come Follow Me Card** - Weekly study material card
- **LDS Inspirational Card** - Random picture quote card with refresh

## 🚀 Installation

### HACS (Recommended)

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=wilcraig&repository=ha-lds&category=integration)

1. Open HACS in your Home Assistant instance
2. Click the three dots in the top-right corner and click 'Custom repositories'
3. Add this repository: `https://github.com/wilcraig/ha-lds`
4. Select "Integration" as the category
5. Click "Add" and then "Download"
6. Restart Home Assistant
7. **Custom cards are automatically available!** No manual setup required.

### Manual Installation

1. Download the latest release
2. Extract the `lds` folder to `<config>/custom_components/`
3. Restart Home Assistant

## ⚡ Quick Start

After installing via HACS:

1. **Add the integration** - Go to **Settings** → **Devices & Services** → **Add Integration** → "Church of Jesus Christ of Latter-day Saints"
2. **Configure language** - Choose your preferred language (default: English)
3. **Use the cards** - Custom cards are automatically available in your Lovelace dashboard!

📖 **See [CARDS_SETUP.md](CARDS_SETUP.md) for card examples**

## ⚙️ Configuration

1. Go to **Settings** → **Devices & Services**
2. Click **"+ Add Integration"**
3. Search for **"Church of Jesus Christ of Latter-day Saints"**
4. Configure your preferred language (default: English)
5. Complete the setup

## 🎨 Lovelace Cards Usage

The integration includes four beautiful custom cards that are automatically available after installation:

### Card Types

- **LDS Quote Card** (`custom:lds-quote-card`) - Daily inspirational quotes
- **LDS Scripture Card** (`custom:lds-scripture-card`) - Verse of the day
- **LDS Come Follow Me Card** (`custom:lds-come-follow-me-card`) - Current lesson
- **LDS Inspirational Card** (`custom:lds-inspirational-card`) - Picture quotes

### Example Configuration

### 2. Card Examples

#### Daily Quote Card
```yaml
type: custom:lds-quote-card
entity: sensor.lds_eng
title: "Quote of the Day"
show_image: true
```

#### Daily Scripture Card
```yaml
type: custom:lds-scripture-card
entity: sensor.lds_eng
title: "Scripture of the Day"
```

#### Come, Follow Me Card
```yaml
type: custom:lds-come-follow-me-card
entity: sensor.lds_eng
title: "This Week's Study"
```

#### Inspirational Picture Quote Card
```yaml
type: custom:lds-inspirational-card
entity: sensor.lds_eng
title: "Inspirational Picture Quote"
show_image: true
```

### 3. Complete Dashboard Example
```yaml
type: vertical-stack
cards:
  - type: custom:lds-scripture-card
    entity: sensor.lds_eng
    title: "Today's Scripture"

  - type: horizontal-stack
    cards:
      - type: custom:lds-quote-card
        entity: sensor.lds_eng
        title: "Daily Quote"
      - type: custom:lds-inspirational-card
        entity: sensor.lds_eng
        title: "Inspiration"

  - type: custom:lds-come-follow-me-card
    entity: sensor.lds_eng
    title: "Come, Follow Me"
```

## 🔧 Services

### Refresh Data
Manually refresh the integration data:

```yaml
service: lds.refresh_data
target:
  entity_id: sensor.lds_eng
```

## 📊 Available Data

The integration provides rich data through sensor attributes:

### Scripture Data
```yaml
state:
  loaderData:
    routes/my-home/dashboard:
      widgetData:
        daily:
          scripture:
            text: "All victory and glory is brought to pass..."
            title: "Doctrine and Covenants 103:36"
            uri: "/scriptures/dc-testament/dc/103.p36#p36"
```

### Quote Data
```yaml
state:
  loaderData:
    routes/my-home/dashboard:
      widgetData:
        daily:
          quote:
            text: "Charity is the foundation of a godly character."
            author: "President Russell M. Nelson"
            date: "1 Apr 2025"
            uri: "/general-conference/2025/04/57nelson..."
```

### Come, Follow Me Data
```yaml
state:
  loaderData:
    routes/my-home/dashboard:
      widgetData:
        cfm:
          dateRange: "September 15–21"
          title: "After Much Tribulation … Cometh the Blessing"
          url: "/study/manual/come-follow-me..."
          description: "Doctrine and Covenants 102–105"
```

### Inspirational Picture Quote Data
```yaml
inspirational_picture_quote:
  title: "God hath not given us the spirit of fear..."
  page_url: "https://churchofjesuschrist.org/media/image/..."
  image_url: "https://churchofjesuschrist.org/imgs/..."
  collection_name: "Inspirational Picture Quotes by Scripture"
```

## 🔄 Automation Examples

### Daily Scripture Notification
```yaml
automation:
  - alias: "Daily Scripture Notification"
    trigger:
      platform: time
      at: "08:00:00"
    action:
      service: notify.mobile_app_your_phone
      data:
        title: "Today's Scripture"
        message: >
          {% set scripture_data = state_attr('sensor.lds_eng', 'loaderData') %}
          {% if scripture_data and scripture_data.get('routes/my-home/dashboard', {}).get('widgetData', {}).get('daily', {}).get('scripture') %}
            {% set scripture = scripture_data['routes/my-home/dashboard']['widgetData']['daily']['scripture'] %}
            {{ scripture.text }}

            - {{ scripture.title }}
          {% else %}
            Scripture not available at this time.
          {% endif %}
```

### Weekly Come Follow Me Reminder
```yaml
automation:
  - alias: "Weekly Come Follow Me Reminder"
    trigger:
      platform: time
      at: "09:00:00"
    condition:
      condition: time
      weekday:
        - sun
    action:
      service: notify.family_group
      data:
        title: "This Week's Study"
        message: >
          Time for Come, Follow Me study!

          {% set cfm_data = state_attr('sensor.lds_eng', 'loaderData') %}
          {% if cfm_data and cfm_data.get('routes/my-home/dashboard', {}).get('widgetData', {}).get('cfm') %}
            {% set cfm = cfm_data['routes/my-home/dashboard']['widgetData']['cfm'] %}
            {{ cfm.title }}

            Study dates: {{ cfm.dateRange }}
          {% else %}
            Come, Follow Me study materials not available at this time.
          {% endif %}
```

## 🛠️ Troubleshooting

### Common Issues

1. **Cards not showing**: Ensure you've added the resources to your Lovelace configuration
2. **No data**: Check that the integration is properly configured and connected
3. **Images not loading**: Verify internet connection and Church website availability

### Debug Information

Enable debug logging:
```yaml
logger:
  default: warning
  logs:
    custom_components.lds: debug
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This is an unofficial integration. The Church of Jesus Christ of Latter-day Saints is not affiliated with or responsible for this Home Assistant integration.

## 🙏 Acknowledgments

- Data sourced from [churchofjesuschrist.org](https://www.churchofjesuschrist.org)
- Inspired by the desire to bring spiritual content into smart homes
- Built with ❤️ for the Home Assistant community

---

**Made with 💙 for the Home Assistant Community**
