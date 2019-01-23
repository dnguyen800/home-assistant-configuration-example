"""

Example from:
https://developers.home-assistant.io/docs/en/creating_platform_example_sensor.html

"""
from datetime import timedelta
import logging
import voluptuous as vol



from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import PLATFORM_SCHEMA

REQUIREMENTS = ['bs4']         # Python libraries or modules needed for this sensor
# DEPENDENCIES = ['mqtt']   # Other Home Assistant Components needed for this sensor to work.

import re                           # Regular expresssion object. Allows search using wildcards
import requests                     # Sends HTTP request to website and saves the data
from bs4 import BeautifulSoup       # Parses the HTML data into a Python object

__version__ = '0.0.1'
_LOGGER = logging.getLogger(__name__)


# CONF_VARIABLE_NAME = 'variable_name_listed_in_configuration_yaml'
CONF_NAME = 'name'
CONF_URL = 'url'
CONF_REFRESH = 'refresh'

DEFAULT_REFRESH = 360

ATTR_COMIC_URL = 'url'

SCAN_INTERVAL = timedelta(hours=1)

# Validate the sensor's user-defined configuration specified in configuration.yaml
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_NAME): cv.string,
    vol.Required(CONF_URL): cv.string,
    vol.Optional(CONF_REFRESH,
                 default=DEFAULT_REFRESH): cv.positive_int,
})

def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup the sensor platform."""
    _LOGGER.info("setup_platform called for Webcomic")   
    add_devices([ComicSensor(hass, config)])


class ComicSensor(Entity):
    """Representation of a Sensor."""
    def __init__(self, hass, config):
        """Initialize the sensor and variables."""      
        self._name = config[CONF_NAME]
        self._url = config[CONF_URL]
        self._state = None
        # This is where the comic URL data will be stored.
        self._comic_url = None
        self.update()


    def check_url(self, c):
        """Checks URL for issues, such as incompleteness, or whitespaces"""
        try:
            if c['src'][0:4] == 'http':                                         
                self._comic_url = c['src'].replace(" ", "%20")
                self._state = "URL found"
            else:                      
                self._comic_url = (self._url + c['src']).replace(" ", "%20")
                self._state = "URL found"
        except:
            self._state = None
            self._comic_url = None

    
    def update(self):
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """      
        user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        r = requests.get(self._url, headers=user_agent)
        soup = BeautifulSoup(r.text, 'html.parser')
        comic = soup.find_all(id=re.compile("comic"))
        for c in comic:
            self.check_url(c)
            if self._state is None:
                for i in c.find_all('img'):
                    self.check_url(i)


    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def url(self):
        return self._url

    @property
    def comic_url(self):
        return self._comic_url
    
    @property
    def device_state_attributes(self):
        """Return the state attributes"""      
        return{ATTR_COMIC_URL: self._comic_url}
