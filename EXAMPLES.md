# 📊 Example Dashboard Configurations

Here are some pre-built dashboard configurations you can use as inspiration or copy directly.

## 🏠 Complete LDS Dashboard

```yaml
title: "LDS Daily Inspiration"
path: "lds-inspiration"
icon: "mdi:church"
cards:
  # Header Card
  - type: markdown
    content: |
      # 🏛️ Daily Spiritual Inspiration
      *Strengthening faith through daily study and reflection*

      ---

  # Main Content Grid
  - type: grid
    square: false
    columns: 2
    cards:
      # Today's Scripture
      - type: custom:lds-scripture-card
        entity: sensor.lds_eng
        title: "📖 Today's Scripture"

      # Daily Quote
      - type: custom:lds-quote-card
        entity: sensor.lds_eng
        title: "💬 Inspirational Quote"
        show_image: true

      # Come Follow Me (spans full width)
      - type: custom:lds-come-follow-me-card
        entity: sensor.lds_eng
        title: "📚 This Week's Come, Follow Me"
        grid_columns: 2
        grid_rows: 1

  # Inspirational Picture Quote
  - type: custom:lds-inspirational-card
    entity: sensor.lds_eng
    title: "🖼️ Inspirational Picture Quote"
    show_image: true

  # Quick Actions
  - type: entities
    title: "🔧 Quick Actions"
    show_header_toggle: false
    entities:
      - entity: sensor.lds_eng
        name: "LDS Integration Status"
        icon: "mdi:church"
      - type: call-service
        name: "🔄 Refresh All Data"
        service: lds.refresh_data
        service_data:
          entity_id: sensor.lds_eng
        icon: "mdi:refresh"
      - type: call-service
        name: "🔄 Update Entity"
        service: homeassistant.update_entity
        service_data:
          entity_id: sensor.lds_eng
        icon: "mdi:update"

  # Study Links
  - type: markdown
    content: |
      ## 🔗 Helpful Study Links

      - [📖 Scriptures](https://www.churchofjesuschrist.org/scriptures)
      - [🎥 General Conference](https://www.churchofjesuschrist.org/general-conference)
      - [📚 Come, Follow Me](https://www.churchofjesuschrist.org/study/come-follow-me)
      - [🖼️ Media Library](https://www.churchofjesuschrist.org/media)
      - [🏛️ Temples](https://www.churchofjesuschrist.org/temples)
```

## 📱 Mobile-First Dashboard

```yaml
title: "LDS Mobile"
path: "lds-mobile"
icon: "mdi:cellphone"
cards:
  # Compact Scripture
  - type: custom:lds-scripture-card
    entity: sensor.lds_eng
    title: "📖 Scripture"

  # Horizontal Quote and Picture
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

  # Come Follow Me
  - type: custom:lds-come-follow-me-card
    entity: sensor.lds_eng
    title: "📚 Study"

  # Quick refresh button
  - type: button
    tap_action:
      action: call-service
      service: lds.refresh_data
      service_data:
        entity_id: sensor.lds_eng
    entity: sensor.lds_eng
    name: "Refresh Content"
    icon: "mdi:refresh"
    show_state: false
```

## 🏡 Family Dashboard Section

```yaml
# Add this to your existing family dashboard
cards:
  # Family Study Section Header
  - type: markdown
    content: |
      ## 👨‍👩‍👧‍👦 Family Study Time

  # Study Materials
  - type: vertical-stack
    cards:
      - type: custom:lds-scripture-card
        entity: sensor.lds_eng
        title: "Family Scripture Study"

      - type: custom:lds-come-follow-me-card
        entity: sensor.lds_eng
        title: "Family Home Evening Lesson"

  # Inspirational Content
  - type: horizontal-stack
    cards:
      - type: custom:lds-quote-card
        entity: sensor.lds_eng
        title: "Family Inspiration"
      - type: custom:lds-inspirational-card
        entity: sensor.lds_eng
        title: "Picture to Share"
```

## 🌅 Morning Routine Dashboard

```yaml
title: "Morning Inspiration"
path: "morning-lds"
icon: "mdi:weather-sunny"
cards:
  # Good Morning Header
  - type: markdown
    content: |
      # 🌅 Good Morning!
      *Start your day with spiritual nourishment*

      **{{ now().strftime('%A, %B %d, %Y') }}**

  # Today's Spiritual Food
  - type: custom:lds-scripture-card
    entity: sensor.lds_eng
    title: "🙏 Morning Scripture Meditation"

  - type: custom:lds-quote-card
    entity: sensor.lds_eng
    title: "💡 Today's Inspiration"
    show_image: true

  # Study Reminder
  - type: conditional
    conditions:
      - entity: binary_sensor.workday_sensor
        state: "on"
    card:
      type: markdown
      content: |
        ## 📖 Don't Forget
        - Read today's Come, Follow Me
        - Family prayer before work
        - Share inspiration with someone

  # Weekly Study
  - type: custom:lds-come-follow-me-card
    entity: sensor.lds_eng
    title: "📅 This Week's Focus"
```

## 🎯 Study Focus Dashboard

```yaml
title: "Deep Study"
path: "lds-study"
icon: "mdi:book-open-page-variant"
cards:
  # Study Session Header
  - type: markdown
    content: |
      # 📚 Deep Scripture Study
      *"Search the scriptures; for in them ye think ye have eternal life"*

  # Current Study Materials
  - type: vertical-stack
    cards:
      - type: custom:lds-scripture-card
        entity: sensor.lds_eng
        title: "Current Scripture Focus"

      - type: custom:lds-come-follow-me-card
        entity: sensor.lds_eng
        title: "Weekly Study Guide"

  # Study Tools
  - type: entities
    title: "📖 Study Tools"
    entities:
      - type: weblink
        url: "https://www.churchofjesuschrist.org/scriptures"
        name: "Scripture Library"
        icon: "mdi:book"
      - type: weblink
        url: "https://www.churchofjesuschrist.org/study/general-conference"
        name: "General Conference"
        icon: "mdi:microphone"
      - type: weblink
        url: "https://www.churchofjesuschrist.org/media"
        name: "Media Library"
        icon: "mdi:multimedia"

  # Reflection Space
  - type: markdown
    content: |
      ## 🤔 Study Questions
      - What principle did I learn today?
      - How can I apply this in my life?
      - What questions do I have?
      - How did I feel the Spirit?

  # Inspirational Close
  - type: custom:lds-inspirational-card
    entity: sensor.lds_eng
    title: "Study Inspiration"
    show_image: true
```

## 🎨 Minimalist Dashboard

```yaml
title: "LDS Simple"
path: "lds-simple"
icon: "mdi:leaf"
cards:
  # Clean, simple layout
  - type: custom:lds-scripture-card
    entity: sensor.lds_eng
    title: "Scripture"

  - type: custom:lds-quote-card
    entity: sensor.lds_eng
    title: "Quote"
    show_image: false

  - type: custom:lds-come-follow-me-card
    entity: sensor.lds_eng
    title: "Study"

  # Simple refresh
  - type: button
    tap_action:
      action: call-service
      service: homeassistant.update_entity
      service_data:
        entity_id: sensor.lds_eng
    entity: sensor.lds_eng
    icon: "mdi:refresh"
    show_state: false
    show_name: false
```

## 🌍 Multi-Language Dashboard

```yaml
title: "LDS Multi-Language"
path: "lds-languages"
icon: "mdi:translate"
cards:
  # Language Tabs Header
  - type: markdown
    content: |
      # 🌍 Multi-Language Study
      *Choose your preferred language*

  # English Section
  - type: vertical-stack
    title: "English"
    cards:
      - type: markdown
        content: "## 🇺🇸 English"
      - type: custom:lds-scripture-card
        entity: sensor.lds_eng
        title: "English Scripture"
      - type: custom:lds-quote-card
        entity: sensor.lds_eng
        title: "English Quote"

  # Spanish Section (if configured)
  - type: vertical-stack
    title: "Español"
    cards:
      - type: markdown
        content: "## 🇪🇸 Español"
      - type: custom:lds-scripture-card
        entity: sensor.lds_spa
        title: "Escritura en Español"
      - type: custom:lds-quote-card
        entity: sensor.lds_spa
        title: "Cita en Español"

  # Come Follow Me (common for all languages)
  - type: custom:lds-come-follow-me-card
    entity: sensor.lds_eng
    title: "📚 Come, Follow Me / Ven, Sígueme"
```

## ⚡ Quick Setup Copy-Paste

For quick setup, here's a minimal working dashboard:

```yaml
# Paste this into a new dashboard
title: "LDS Dashboard"
path: "lds"
icon: "mdi:church"
cards:
  - type: custom:lds-scripture-card
    entity: sensor.lds_eng
  - type: custom:lds-quote-card
    entity: sensor.lds_eng
  - type: custom:lds-come-follow-me-card
    entity: sensor.lds_eng
  - type: custom:lds-inspirational-card
    entity: sensor.lds_eng
```

## 🔧 Customization Tips

### Custom Colors
While the cards have built-in gradients, you can modify them by editing the CSS in the card files.

### Custom Icons
Add custom icons to your dashboard sections:
- 📖 `mdi:book-open-page-variant`
- 💬 `mdi:comment-quote`
- 🏛️ `mdi:church`
- 📚 `mdi:book-multiple`
- 🖼️ `mdi:image-frame`

### Performance Tips
- Use `show_image: false` on mobile for faster loading
- Limit the number of cards per view for better performance
- Use conditional cards to show content only when needed

Remember to replace `sensor.lds_eng` with your actual LDS sensor entity ID!
