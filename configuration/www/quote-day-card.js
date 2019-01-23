class QuoteDayCard extends HTMLElement {

    constructor() {
      super();
      this.attachShadow({ mode: 'open' });
    }
  
    setConfig(config) {
      if (!config.entity) {
        throw new Error('Please define an entity.');
      }
      const root = this.shadowRoot;
      if (root.lastChild) root.removeChild(root.lastChild);
  
      const cardConfig = Object.assign({}, config);
      if (!cardConfig.title) {
        cardConfig.title = `Quote of the Day`;
      } 
      
    


      const card = document.createElement('ha-card');
      const content = document.createElement('div');
      const style = document.createElement('style');

      style.textContent = `
            ha-card {
              /* sample css */
            }

            body {
              margin: 0;
              font-family: Arial, Helvetica, sans-serif;
            }

            .quotecontainer {
              position: relative;
              width: 100%;
            }
          
            .quotecenter {
              margin: auto;
              width: 90%;
              position: absolute;
              text-align: center;
              padding: 1px;

              line-height: 1;
              top: 50%;
              left: 50%;
              transform: translate(-50%, -50%);
              color: white;

            }
          
            .quotecontainer img { 
              display: block;
              margin-left: auto;
              margin-right: auto;
              width: 100%;
              height: auto;
            }
            `;
             


      content.innerHTML = `
      <div id='content'>
      </div>
      `;
      
      if (config.show_title) {
        card.header = cardConfig.title;
      }
      card.appendChild(content);
      card.appendChild(style);
      root.appendChild(card);
      this._config = cardConfig;
    }
  
 
    set hass(hass) {
      const config = this._config;
      const root = this.shadowRoot;
      const card = root.lastChild;
      this.myhass = hass;
      let card_content = ''
      let quote_content = ``
      card_content += `<div class="quotecontainer">
        <img src="/local/bg.jpg" style="width:100%">
        <div class="quotecenter">`;
       
      if (hass.states[config.entity]) {
        const quoteList = hass.states[config.entity].attributes;
   
        for (let quote in quoteList) {
          if (quote !== "friendly_name" && quote !== "icon" && quote !== "homebridge_hidden" && !quote_content) {
            quote_content += `  <h1 style="font-size:1.8vw">${quoteList[quote]['summary']}</h1>`;
            quote_content += `  <h3 style="font-size:1.3vw">${quoteList[quote]['title']}</h3>`;

          }
        }
        card_content += quote_content
        card_content += `</div></div>` 

      };
      root.lastChild.hass = hass;
      root.getElementById('content').innerHTML = card_content;

      
    }
    getCardSize() {
      return 1;
    }
}
  
customElements.define('quote-day-card', QuoteDayCard);