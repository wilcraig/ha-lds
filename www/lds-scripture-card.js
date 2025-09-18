class LDSScriptureCard extends HTMLElement {
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
    const scripture = data?.loaderData?.['routes/my-home/dashboard']?.widgetData?.daily?.scripture;

    if (!scripture) {
      this.shadowRoot.innerHTML = `
        <ha-card>
          <div class="card-content">
            <p>No scripture data available</p>
          </div>
        </ha-card>
      `;
      return;
    }

    const title = this.config.title || 'Scripture of the Day';

    this.shadowRoot.innerHTML = `
      <style>
        ha-card {
          --ha-card-background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
          color: white;
          border-radius: 15px;
          overflow: hidden;
          box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        }
        .card-header {
          background: rgba(255,255,255,0.1);
          padding: 16px;
          text-align: center;
          font-size: 1.2em;
          font-weight: 500;
          border-bottom: 1px solid rgba(255,255,255,0.2);
        }
        .card-content {
          padding: 24px;
          text-align: center;
        }
        .scripture-text {
          font-size: 1.2em;
          line-height: 1.5;
          margin-bottom: 20px;
          font-family: Georgia, serif;
          position: relative;
        }
        .scripture-reference {
          font-size: 1.1em;
          font-weight: 600;
          margin-bottom: 16px;
          letter-spacing: 0.5px;
        }
        .scripture-link {
          display: inline-block;
          background: rgba(255,255,255,0.2);
          color: white;
          padding: 8px 16px;
          border-radius: 20px;
          text-decoration: none;
          transition: all 0.3s ease;
          border: 1px solid rgba(255,255,255,0.3);
        }
        .scripture-link:hover {
          background: rgba(255,255,255,0.3);
          transform: translateY(-2px);
        }
        .book-icon {
          width: 40px;
          height: 40px;
          margin: 0 auto 16px;
          background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect x="25" y="20" width="50" height="60" rx="5" fill="rgba(255,255,255,0.3)"/><rect x="30" y="25" width="40" height="2" fill="white"/><rect x="30" y="30" width="35" fill="white" height="2"/><rect x="30" y="35" width="30" height="2" fill="white"/></svg>') center/contain no-repeat;
        }
      </style>
      <ha-card>
        <div class="card-header">${title}</div>
        <div class="card-content">
          <div class="book-icon"></div>
          <div class="scripture-text">${scripture.text}</div>
          <div class="scripture-reference">${scripture.title}</div>
          <a href="https://churchofjesuschrist.org${scripture.uri}" target="_blank" class="scripture-link">
            Read Full Chapter
          </a>
        </div>
      </ha-card>
    `;
  }

  getCardSize() {
    return 3;
  }
}

customElements.define('lds-scripture-card', LDSScriptureCard);

window.customCards = window.customCards || [];
window.customCards.push({
  type: 'lds-scripture-card',
  name: 'LDS Scripture Card',
  description: 'A beautiful card displaying the LDS daily scripture'
});
