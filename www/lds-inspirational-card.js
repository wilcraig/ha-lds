class LDSInspirationalCard extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
  }

  setConfig(config) {
    if (!config.entity) {
      throw new Error('You need to define an entity');
    }
    this.config = config;
  }

  set hass(hass) {
    this._hass = hass;
    this.render();
  }

  render() {
    const entity = this._hass.states[this.config.entity];
    if (!entity) {
      this.shadowRoot.innerHTML = `
        <ha-card>
          <div class="card-content">
            <p>Entity ${this.config.entity} not found.</p>
          </div>
        </ha-card>
      `;
      return;
    }

    const data = entity.attributes;
    const inspirational = data?.inspirational_picture_quote;

    if (!inspirational) {
      this.shadowRoot.innerHTML = `
        <ha-card>
          <div class="card-content">
            <p>No inspirational quote data available</p>
            <button onclick="this.getRootNode().host.refreshQuote()">Get New Quote</button>
          </div>
        </ha-card>
      `;
      return;
    }

    const title = this.config.title || 'Inspirational Picture Quote';
    const showImage = this.config.show_image !== false;

    this.shadowRoot.innerHTML = `
      <style>
        ha-card {
          --ha-card-background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
          color: #333;
          border-radius: 15px;
          overflow: hidden;
          box-shadow: 0 8px 25px rgba(0,0,0,0.15);
          position: relative;
        }
        .card-header {
          background: rgba(255,255,255,0.3);
          padding: 16px;
          text-align: center;
          font-size: 1.2em;
          font-weight: 500;
          border-bottom: 1px solid rgba(255,255,255,0.4);
        }
        .card-content {
          padding: 0;
          position: relative;
        }
        .image-container {
          position: relative;
          width: 100%;
          height: 300px;
          overflow: hidden;
        }
        .inspirational-image {
          width: 100%;
          height: 100%;
          object-fit: cover;
          transition: transform 0.3s ease;
        }
        .inspirational-image:hover {
          transform: scale(1.05);
        }
        .image-overlay {
          position: absolute;
          bottom: 0;
          left: 0;
          right: 0;
          background: linear-gradient(transparent, rgba(0,0,0,0.7));
          padding: 20px;
          color: white;
        }
        .quote-title {
          font-size: 1.1em;
          font-weight: 600;
          margin-bottom: 12px;
          text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }
        .action-buttons {
          padding: 16px;
          display: flex;
          gap: 12px;
          justify-content: center;
          background: rgba(255,255,255,0.1);
        }
        .action-button {
          background: rgba(255,255,255,0.9);
          color: #333;
          border: none;
          padding: 8px 16px;
          border-radius: 20px;
          text-decoration: none;
          font-weight: 500;
          transition: all 0.3s ease;
          cursor: pointer;
          display: inline-flex;
          align-items: center;
          gap: 8px;
        }
        .action-button:hover {
          background: white;
          transform: translateY(-2px);
          box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }
        .refresh-button {
          background: #4facfe;
          color: white;
        }
        .refresh-button:hover {
          background: #3d8bfe;
        }
        .no-image {
          padding: 40px 20px;
          text-align: center;
          background: rgba(255,255,255,0.3);
        }
        .no-image h3 {
          margin: 0 0 12px 0;
          color: #333;
        }
        .collection-badge {
          position: absolute;
          top: 12px;
          right: 12px;
          background: rgba(255,255,255,0.9);
          color: #333;
          padding: 4px 8px;
          border-radius: 12px;
          font-size: 0.8em;
          font-weight: 500;
        }
      </style>
      <ha-card>
        <div class="card-header">${title}</div>
        <div class="card-content">
          ${showImage && inspirational.image_url ? `
            <div class="image-container">
              <img src="${inspirational.image_url}" alt="${inspirational.title}" class="inspirational-image" />
              <div class="collection-badge">${inspirational.collection_name}</div>
              <div class="image-overlay">
                <div class="quote-title">${inspirational.title}</div>
              </div>
            </div>
          ` : `
            <div class="no-image">
              <h3>${inspirational.title}</h3>
              <p>${inspirational.collection_name}</p>
            </div>
          `}
          <div class="action-buttons">
            <button class="action-button refresh-button" onclick="this.getRootNode().host.refreshQuote()">
              🔄 New Quote
            </button>
            <a href="${inspirational.page_url}" target="_blank" class="action-button">
              🔗 View Original
            </a>
          </div>
        </div>
      </ha-card>
    `;
  }

  refreshQuote() {
    // Call the sensor update service to get a new quote
    this._hass.callService('homeassistant', 'update_entity', {
      entity_id: this.config.entity
    });
  }

  getCardSize() {
    return 4;
  }
}

customElements.define('lds-inspirational-card', LDSInspirationalCard);

window.customCards = window.customCards || [];
window.customCards.push({
  type: 'lds-inspirational-card',
  name: 'LDS Inspirational Picture Card',
  description: 'A beautiful card displaying random inspirational picture quotes from the Church'
});
