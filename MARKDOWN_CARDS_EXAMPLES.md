# LDS Integration - Markdown Card Examples

The LDS integration now provides clean, focused sensors that work perfectly with Home Assistant's built-in markdown cards. This approach is much more reliable than custom cards and integrates seamlessly with all dashboard types.

## Available Sensors

After setting up the integration, you'll have these sensors available:

- `sensor.lds_daily_scripture_eng` - Daily scripture with text and reference
- `sensor.lds_daily_quote_eng` - Inspirational quotes from church leaders
- `sensor.lds_come_follow_me_eng` - Current Come Follow Me lesson info
- `sensor.lds_inspirational_image_eng` - Inspirational images with quotes

*Replace `eng` with your configured language code*

## Markdown Card Examples

### 1. Daily Scripture Card

```yaml
type: markdown
title: 📖 Scripture of the Day
content: |
  **{{ state_attr('sensor.lds_daily_scripture_eng', 'reference') }}**

  *{{ state_attr('sensor.lds_daily_scripture_eng', 'text') }}*

  [Read Full Chapter]({{ state_attr('sensor.lds_daily_scripture_eng', 'url') }})

  *Updated: {{ state_attr('sensor.lds_daily_scripture_eng', 'date') }}*
card_mod:
  style: |
    ha-card {
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
      border-radius: 15px;
    }
```

### 2. Daily Quote Card

```yaml
type: markdown
title: 💬 Inspirational Quote
content: |
  > {{ state_attr('sensor.lds_daily_quote_eng', 'text') }}

  **— {{ state_attr('sensor.lds_daily_quote_eng', 'author') }}**

  *{{ state_attr('sensor.lds_daily_quote_eng', 'source') }}*

  [Read More]({{ state_attr('sensor.lds_daily_quote_eng', 'url') }})
card_mod:
  style: |
    ha-card {
      background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
      color: white;
      border-radius: 15px;
    }
```

### 3. Come Follow Me Card

```yaml
type: markdown
title: 📚 Come, Follow Me
content: |
  ## {{ state_attr('sensor.lds_come_follow_me_eng', 'title') }}

  **Reading:** {{ state_attr('sensor.lds_come_follow_me_eng', 'reading') }}

  **Dates:** {{ state_attr('sensor.lds_come_follow_me_eng', 'date_range') }}

  [View Lesson]({{ state_attr('sensor.lds_come_follow_me_eng', 'url') }})
card_mod:
  style: |
    ha-card {
      background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
      color: white;
      border-radius: 15px;
    }
```

### 4. Inspirational Image Card

```yaml
type: markdown
title: 🖼️ Inspirational Image
content: |
  {% if state_attr('sensor.lds_inspirational_image_eng', 'image_url') %}
  ![{{ state_attr('sensor.lds_inspirational_image_eng', 'title') }}]({{ state_attr('sensor.lds_inspirational_image_eng', 'image_url') }})
  {% endif %}

  **{{ state_attr('sensor.lds_inspirational_image_eng', 'title') }}**

  *{{ state_attr('sensor.lds_inspirational_image_eng', 'collection') }}*

  [View Original]({{ state_attr('sensor.lds_inspirational_image_eng', 'page_url') }})
card_mod:
  style: |
    ha-card {
      background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
      color: white;
      border-radius: 15px;
    }
```

### 5. Simple All-in-One Card

```yaml
type: markdown
title: ⛪ LDS Daily Content
content: |
  ## Scripture: {{ state_attr('sensor.lds_daily_scripture_eng', 'reference') }}
  {{ state_attr('sensor.lds_daily_scripture_eng', 'text') }}

  ---

  ## Quote of the Day
  > {{ state_attr('sensor.lds_daily_quote_eng', 'text') }}

  **— {{ state_attr('sensor.lds_daily_quote_eng', 'author') }}**

  ---

  ## Come Follow Me
  **{{ state_attr('sensor.lds_come_follow_me_eng', 'title') }}**
  Reading: {{ state_attr('sensor.lds_come_follow_me_eng', 'reading') }}
```

### 6. Entity Card Alternative

For a simpler approach, you can also use entity cards:

```yaml
type: entity
entity: sensor.lds_daily_scripture_eng
name: Daily Scripture
icon: mdi:book-open-page-variant
```

```yaml
type: entity
entity: sensor.lds_daily_quote_eng
name: Daily Quote
icon: mdi:format-quote-open
```

## Dashboard Layout Example

Here's a complete dashboard view combining all the cards:

```yaml
type: vertical-stack
cards:
  - type: horizontal-stack
    cards:
      - type: markdown
        title: 📖 Scripture
        content: |
          **{{ state_attr('sensor.lds_daily_scripture_eng', 'reference') }}**

          {{ state_attr('sensor.lds_daily_scripture_eng', 'text') }}
      - type: markdown
        title: 💬 Quote
        content: |
          > {{ state_attr('sensor.lds_daily_quote_eng', 'text') }}

          **— {{ state_attr('sensor.lds_daily_quote_eng', 'author') }}**
  - type: markdown
    title: 📚 Come, Follow Me
    content: |
      ## {{ state_attr('sensor.lds_come_follow_me_eng', 'title') }}
      **Reading:** {{ state_attr('sensor.lds_come_follow_me_eng', 'reading') }}
      **Dates:** {{ state_attr('sensor.lds_come_follow_me_eng', 'date_range') }}
```

## Customization Tips

1. **Card Styling**: Use `card_mod` (requires the card-mod custom component) to add beautiful gradients and styling
2. **Conditional Display**: Use Home Assistant's conditional logic to show/hide cards based on data availability
3. **Automation**: Create automations to send notifications with daily content
4. **Multiple Languages**: Set up multiple integration instances for different languages

## Benefits Over Custom Cards

- ✅ **More Reliable**: No dependency on custom JavaScript files
- ✅ **Better Performance**: Native Home Assistant rendering
- ✅ **Mobile Friendly**: Works perfectly on all devices and apps
- ✅ **Easy Customization**: Full control over styling and layout
- ✅ **Standard Integration**: Uses normal Home Assistant patterns
- ✅ **Future Proof**: Won't break with Home Assistant updates

## Troubleshooting

If sensor data appears as "Unknown" or attributes are missing:

1. Check that the integration is properly configured
2. Look at the Home Assistant logs for any error messages
3. Try reloading the integration from the Integrations page
4. Verify your internet connection is working

The integration includes fallback data, so you should always see some content even if the church website is temporarily unavailable.
