class LDSQuoteCard extends HTMLElement {
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
    const quote = data?.loaderData?.['routes/my-home/dashboard']?.widgetData?.daily?.quote;

    if (!quote) {
      this.shadowRoot.innerHTML = `
        <ha-card>
          <div class="card-content">
            <p>No quote data available</p>
          </div>
        </ha-card>
      `;
      return;
    }

    const title = this.config.title || 'Quote of the Day';
    const showImage = this.config.show_image !== false;

    this.shadowRoot.innerHTML = `
      <style>
        ha-card {
          --ha-card-background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
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
        .quote-text {
          font-size: 1.3em;
          line-height: 1.4;
          margin-bottom: 20px;
          font-style: italic;
          position: relative;
        }
        .quote-text:before {
          content: '"';
          font-size: 3em;
          position: absolute;
          left: -20px;
          top: -10px;
          opacity: 0.3;
        }
        .quote-text:after {
          content: '"';
          font-size: 3em;
          position: absolute;
          right: -20px;
          bottom: -30px;
          opacity: 0.3;
        }
        .quote-author {
          font-size: 1.1em;
          font-weight: 500;
          margin-bottom: 8px;
        }
        .quote-date {
          font-size: 0.9em;
          opacity: 0.8;
          margin-bottom: 16px;
        }
        .quote-link {
          display: inline-block;
          background: rgba(255,255,255,0.2);
          color: white;
          padding: 8px 16px;
          border-radius: 20px;
          text-decoration: none;
          transition: all 0.3s ease;
          border: 1px solid rgba(255,255,255,0.3);
        }
        .quote-link:hover {
          background: rgba(255,255,255,0.3);
          transform: translateY(-2px);
        }
        .church-image {
          width: 40px;
          height: 40px;
          margin: 0 auto 16px;
          background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="50" cy="50" r="45" fill="rgba(255,255,255,0.3)"/><path d="M30 70 L50 30 L70 70 Z" fill="white"/></svg>') center/contain no-repeat;
        }
      </style>
      <ha-card>
        <div class="card-header">${title}</div>
        <div class="card-content">
          ${showImage ? '<div class="church-image"></div>' : ''}
          <div class="quote-text">${quote.text}</div>
          <div class="quote-author">${quote.author}</div>
          <div class="quote-date">${quote.date}</div>
          <a href="https://churchofjesuschrist.org${quote.uri}" target="_blank" class="quote-link">
            Read Full Talk
          </a>
        </div>
      </ha-card>
    `;
  }

  getCardSize() {
    return 3;
  }
}

customElements.define('lds-quote-card', LDSQuoteCard);

window.customCards = window.customCards || [];
window.customCards.push({
  type: 'lds-quote-card',
  name: 'LDS Quote Card',
  description: 'A beautiful card displaying the LDS daily quote'
});
