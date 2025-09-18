# 🏛️ Church of Jesus Christ of Latter-day Saints Integration for Home Assistant

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=wilcraig&repository=ha-lds&category=integration)

A comprehensive Home Assistant integration that brings inspirational content from The Church of Jesus Christ of Latter-day Saints directly to your smart home dashboard.

## ✨ Features

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

### Manual Installation

1. Download the latest release
2. Extract the `lds` folder to `<config>/custom_components/`
3. Restart Home Assistant

## ⚙️ Configuration

1. Go to **Settings** → **Devices & Services**
2. Click **"+ Add Integration"**
3. Search for **"Church of Jesus Christ of Latter-day Saints"**
4. Configure your preferred language (default: English)
5. Complete the setup

## 🎨 Lovelace Cards Setup

### 1. Add Resources
First, add the card resources to your Lovelace configuration:

```yaml
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
          {{ state_attr('sensor.lds_eng', 'state')['loaderData']['routes/my-home/dashboard']['widgetData']['daily']['scripture']['text'] }}

          - {{ state_attr('sensor.lds_eng', 'state')['loaderData']['routes/my-home/dashboard']['widgetData']['daily']['scripture']['title'] }}
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

          {{ state_attr('sensor.lds_eng', 'state')['loaderData']['routes/my-home/dashboard']['widgetData']['cfm']['title'] }}

          Study dates: {{ state_attr('sensor.lds_eng', 'state')['loaderData']['routes/my-home/dashboard']['widgetData']['cfm']['dateRange'] }}
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
