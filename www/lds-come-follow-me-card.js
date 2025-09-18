class LDSComeFollowMeCard extends HTMLElement {
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
    const cfm = data?.loaderData?.['routes/my-home/dashboard']?.widgetData?.cfm;

    if (!cfm) {
      this.shadowRoot.innerHTML = `
        <ha-card>
          <div class="card-content">
            <p>No Come, Follow Me data available</p>
          </div>
        </ha-card>
      `;
      return;
    }

    const title = this.config.title || 'Come, Follow Me';

    this.shadowRoot.innerHTML = `
      <style>
        ha-card {
          --ha-card-background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
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
        }
        .cfm-date {
          font-size: 1.1em;
          font-weight: 600;
          margin-bottom: 12px;
          text-align: center;
          background: rgba(255,255,255,0.1);
          padding: 8px 16px;
          border-radius: 20px;
          display: inline-block;
          width: 100%;
          box-sizing: border-box;
        }
        .cfm-title {
          font-size: 1.3em;
          font-weight: 600;
          margin-bottom: 12px;
          line-height: 1.3;
          text-align: center;
        }
        .cfm-description {
          font-size: 1.1em;
          margin-bottom: 20px;
          opacity: 0.9;
          text-align: center;
        }
        .cfm-link {
          display: block;
          background: rgba(255,255,255,0.2);
          color: white;
          padding: 12px 20px;
          border-radius: 25px;
          text-decoration: none;
          transition: all 0.3s ease;
          border: 1px solid rgba(255,255,255,0.3);
          text-align: center;
          font-weight: 500;
        }
        .cfm-link:hover {
          background: rgba(255,255,255,0.3);
          transform: translateY(-2px);
        }
        .study-icon {
          width: 50px;
          height: 50px;
          margin: 0 auto 16px;
          background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="50" cy="35" r="15" fill="rgba(255,255,255,0.3)"/><rect x="20" y="55" width="60" height="30" rx="5" fill="rgba(255,255,255,0.3)"/><rect x="25" y="60" width="50" height="3" fill="white"/><rect x="25" y="66" width="45" height="3" fill="white"/><rect x="25" y="72" width="40" height="3" fill="white"/></svg>') center/contain no-repeat;
        }
      </style>
      <ha-card>
        <div class="card-header">${title}</div>
        <div class="card-content">
          <div class="study-icon"></div>
          <div class="cfm-date">${cfm.dateRange}</div>
          <div class="cfm-title">${cfm.title}</div>
          <div class="cfm-description">${cfm.description}</div>
          <a href="https://churchofjesuschrist.org${cfm.url}" target="_blank" class="cfm-link">
            Study This Week's Lesson
          </a>
        </div>
      </ha-card>
    `;
  }

  getCardSize() {
    return 4;
  }
}

customElements.define('lds-come-follow-me-card', LDSComeFollowMeCard);

window.customCards = window.customCards || [];
window.customCards.push({
  type: 'lds-come-follow-me-card',
  name: 'LDS Come Follow Me Card',
  description: 'A beautiful card displaying the weekly Come, Follow Me study material'
});
