# LDS Integration - Markdown Card Examples

The LDS integration provides comprehensive church content that works perfectly with Home Assistant's built-in markdown cards. This approach is much more reliable than custom cards and integrates seamlessly with all dashboard types.

## Available Data

The integration now fetches data from the church's My Home page and provides:

- **Daily Scripture** - Scripture passages with references and links
- **Inspirational Quotes** - Quotes from church leaders and content
- **Come Follow Me** - Current lesson information
- **Inspirational Images** - Pictures with inspiring quotes
- **Church News Headlines** - Latest newsroom articles with images
- **Featured Content** - Highlighted church content and resources

All data is available through the `sensor.lds_data` entity with appropriate attributes.

## Basic Card Examples

### 1. Daily Scripture Card

```yaml
type: markdown
title: 📖 Scripture of the Day
content: |
  **{{ state_attr('sensor.lds_data', 'scripture')['reference'] }}**

  *{{ state_attr('sensor.lds_data', 'scripture')['text'] }}*

  [Read More]({{ state_attr('sensor.lds_data', 'scripture')['url'] }})

  *Updated: {{ state_attr('sensor.lds_data', 'scripture')['date'] }}*
```

### 2. Daily Quote Card

```yaml
type: markdown
title: 💬 Inspirational Quote
content: |
  > {{ state_attr('sensor.lds_data', 'quote')['text'] }}

  **— {{ state_attr('sensor.lds_data', 'quote')['author'] }}**

  *{{ state_attr('sensor.lds_data', 'quote')['source'] }}*

  [Read More]({{ state_attr('sensor.lds_data', 'quote')['url'] }})
```

### 3. Come Follow Me Card

```yaml
type: markdown
title: 📚 Come, Follow Me
content: |
  ## {{ state_attr('sensor.lds_data', 'come_follow_me')['title'] }}

  **Reading:** {{ state_attr('sensor.lds_data', 'come_follow_me')['reading'] }}

  **Dates:** {{ state_attr('sensor.lds_data', 'come_follow_me')['date_range'] }}

  [View Lesson]({{ state_attr('sensor.lds_data', 'come_follow_me')['url'] }})
```

### 4. Inspirational Image Card

```yaml
type: markdown
title: 🖼️ Inspirational Image
content: |
  ### {{ state_attr('sensor.lds_data', 'inspirational')['title'] }}

  {% if state_attr('sensor.lds_data', 'inspirational')['image_url'] %}
  <img src="{{ state_attr('sensor.lds_data', 'inspirational')['image_url'] }}" alt="{{ state_attr('sensor.lds_data', 'inspirational')['title'] }}" style="width: 100%; border-radius: 8px;">
  {% endif %}

  *From: {{ state_attr('sensor.lds_data', 'inspirational')['collection'] }}*

  [View Full Size]({{ state_attr('sensor.lds_data', 'inspirational')['page_url'] }})
```

## New: Church News Summary Card

```yaml
type: markdown
title: 📰 Church News Headlines
content: |
  ### Latest Church News

  {% for headline in state_attr('sensor.lds_data', 'newsroom_headlines') %}
  {% if loop.index <= 5 %}

  #### {{ headline.title }}

  {% if headline.image_url %}
  <img src="{{ headline.image_url }}" alt="{{ headline.title }}" style="width: 100%; max-height: 200px; object-fit: cover; border-radius: 8px; margin-bottom: 10px;">
  {% endif %}

  {{ headline.description }}

  {% if headline.publish_date %}
  *Published: {{ headline.publish_date }}*
  {% endif %}

  [Read Full Article]({{ headline.link_url }})

  ---

  {% endif %}
  {% endfor %}
```

## New: Featured Content Card

```yaml
type: markdown
title: ⭐ Featured Church Content
content: |
  ### Featured Content

  {% for item in state_attr('sensor.lds_data', 'featured_content') %}
  {% if loop.index <= 3 %}

  #### {{ item.title }}

  {% if item.pretitle %}
  *{{ item.pretitle }}*
  {% endif %}

  {% if item.image_url %}
  <img src="{{ item.image_url }}" alt="{{ item.title }}" style="width: 100%; max-height: 250px; object-fit: cover; border-radius: 8px; margin-bottom: 10px;">
  {% endif %}

  {{ item.description }}

  [Learn More]({{ item.link_url }})

  ---

  {% endif %}
  {% endfor %}
```

## Compact Layout Examples

### Compact News Card (Single Column)

```yaml
type: markdown
title: Church News
content: |
  {% for headline in state_attr('sensor.lds_data', 'newsroom_headlines') %}
  {% if loop.index <= 3 %}

  **{{ headline.title }}**

  {{ headline.description[:150] }}{% if headline.description|length > 150 %}...{% endif %}

  [Read More]({{ headline.link_url }})

  {% if not loop.last %}---{% endif %}

  {% endif %}
  {% endfor %}
```

### Featured Content Grid Card

```yaml
type: markdown
title: Featured Content
content: |
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">

  {% for item in state_attr('sensor.lds_data', 'featured_content') %}
  {% if loop.index <= 4 %}

  <div style="border: 1px solid #ddd; border-radius: 8px; padding: 15px; background: #f9f9f9;">

  {% if item.image_url %}
  <img src="{{ item.image_url }}" alt="{{ item.title }}" style="width: 100%; height: 150px; object-fit: cover; border-radius: 4px; margin-bottom: 10px;">
  {% endif %}

  **{{ item.title }}**

  {% if item.pretitle %}
  *{{ item.pretitle }}*
  {% endif %}

  {{ item.description[:100] }}{% if item.description|length > 100 %}...{% endif %}

  [Learn More]({{ item.link_url }})

  </div>

  {% endif %}
  {% endfor %}

  </div>
```

## All-in-One LDS Dashboard Card

```yaml
type: markdown
title: ⛪ LDS Daily Dashboard
content: |
  ## Daily Scripture

  ### {{ state_attr('sensor.lds_data', 'scripture')['reference'] }}

  {{ state_attr('sensor.lds_data', 'scripture')['text'] }}

  [Read More]({{ state_attr('sensor.lds_data', 'scripture')['url'] }})

  ---

  ## Inspirational Quote

  > {{ state_attr('sensor.lds_data', 'quote')['text'] }}

  **—{{ state_attr('sensor.lds_data', 'quote')['author'] }}**

  ---

  ## Come Follow Me

  **{{ state_attr('sensor.lds_data', 'come_follow_me')['title'] }}**
  *{{ state_attr('sensor.lds_data', 'come_follow_me')['reading'] }}*

  [Study Guide]({{ state_attr('sensor.lds_data', 'come_follow_me')['url'] }})

  ---

  ## Latest Church News

  {% for headline in state_attr('sensor.lds_data', 'newsroom_headlines') %}
  {% if loop.index <= 2 %}

  **{{ headline.title }}**
  {{ headline.description[:120] }}{% if headline.description|length > 120 %}...{% endif %}
  [Read More]({{ headline.link_url }})

  {% endif %}
  {% endfor %}
```

## Dashboard Layout Examples

### Complete Dashboard View

```yaml
type: vertical-stack
cards:
  - type: horizontal-stack
    cards:
      - type: markdown
        title: 📖 Scripture
        content: |
          **{{ state_attr('sensor.lds_data', 'scripture')['reference'] }}**

          {{ state_attr('sensor.lds_data', 'scripture')['text'][:200] }}...

          [Read More]({{ state_attr('sensor.lds_data', 'scripture')['url'] }})
      - type: markdown
        title: 💬 Quote
        content: |
          > {{ state_attr('sensor.lds_data', 'quote')['text'][:150] }}...

          **— {{ state_attr('sensor.lds_data', 'quote')['author'] }}**
  - type: horizontal-stack
    cards:
      - type: markdown
        title: � Church News
        content: |
          {% for headline in state_attr('sensor.lds_data', 'newsroom_headlines') %}
          {% if loop.index <= 2 %}
          **{{ headline.title }}**
          [Read More]({{ headline.link_url }})
          {% if not loop.last %}---{% endif %}
          {% endif %}
          {% endfor %}
      - type: markdown
        title: ⭐ Featured
        content: |
          {% for item in state_attr('sensor.lds_data', 'featured_content') %}
          {% if loop.index <= 2 %}
          **{{ item.title }}**
          [Learn More]({{ item.link_url }})
          {% if not loop.last %}---{% endif %}
          {% endif %}
          {% endfor %}
```

## Styling with card-mod

If you have the `card-mod` custom component installed, you can add beautiful styling:

```yaml
type: markdown
title: 📖 Scripture of the Day
content: |
  **{{ state_attr('sensor.lds_data', 'scripture')['reference'] }}**

  *{{ state_attr('sensor.lds_data', 'scripture')['text'] }}*

  [Read More]({{ state_attr('sensor.lds_data', 'scripture')['url'] }})
card_mod:
  style: |
    ha-card {
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
      border-radius: 15px;
      box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
```

## Benefits of This Approach

- ✅ **Comprehensive Content**: Access to scriptures, quotes, news, and featured content
- ✅ **Real-time Updates**: Fresh content from the church's My Home page
- ✅ **Rich Media**: Images and proper formatting for enhanced visual appeal
- ✅ **Flexible Display**: Multiple card layouts for different needs
- ✅ **Mobile Friendly**: Responsive design that works on all devices
- ✅ **Future Proof**: Uses standard Home Assistant patterns

## Troubleshooting

If data appears as "Unknown" or attributes are missing:

1. Check the Home Assistant logs for error messages
2. Verify the integration is properly loaded
3. Test your internet connection to churchofjesuschrist.org
4. Try reloading the integration from the Integrations page

The integration includes comprehensive fallback data, so you should always see some content even if the church website is temporarily unavailable.
