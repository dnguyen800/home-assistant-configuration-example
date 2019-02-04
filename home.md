# Home View

[Home](home.md) | [Media](media.md) | [Rooms](rooms.md) | [Cameras](cameras.md) | [Comics](comics.md) | [System](system.md) | [Floor Plan](floorplan.md) 

![Home View](https://github.com/dnguyen800/home-assistant-configuration-example/blob/master/images/home.PNG?raw=true)

## Components in this View
**Lovelace Layout Card** - Backend card that provides more control in how to organize your Lovelace cards in a readable format, versus the previous method of using vertical and horizontal stacks. You define the columns and choose where to insert breaks, thus maximizing screen space | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/ui-lovelace.yaml#L50-L60) | [Github](https://github.com/thomasloven/lovelace-layout-card) |

1) **Compact Custom Header** - Reduces the height of the original HA header, saving precious space on small tablets like the Fire HD8. Also adds a clock. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/ui-lovelace.yaml#L50-L62) | [Github](https://github.com/maykar/compact-custom-header/) |

2) **Quote of the Day Card** - Displays the quote of the day from brainyquote.com. It can be recreated using HA Picture Elements card, but haven't gotten around to it. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/ui-lovelace.yaml#L61-L62) | [Github](https://github.com/dnguyen800/Quote-of-the-Day-Card) |
    * Requires **Feed Parser sensor** to load RSS feed from brainyquotes.com | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/config/sensors.yaml#L46-L52) | [Github](https://github.com/custom-components/sensor.feedparser) |

3) **Animated Weather Card** - Looks a bit nicer on the tablet than the standard HA weather card.| [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/ui-lovelace.yaml#L84-L86) | [Github](https://community.home-assistant.io/t/custom-animated-weather-card-for-lovelace/58338) |
    * Requires Weather entity, such as **Dark Sky component** | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/configuration.yaml#L82-L85) | [HA Component](https://www.home-assistant.io/components/weather.darksky/) |
    * Requires **Sun component** | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/configuration.yaml#L66-L67) | [HA Component](https://www.home-assistant.io/components/sun/) |


4) **Traffic Map Image** - Uses the Lovelace camera entity to display an image URL that is constantly updated by Google. It's not going to show the very latest traffic, but it's a nice visual to have on the dashboard. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/f4d7474dcface0cd83b7481499a7efd873d8d79e/configuration/ui-lovelace.yaml#L97-L101) |
    * Requires the **Generic IP Camera component** | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/f4d7474dcface0cd83b7481499a7efd873d8d79e/configuration/config/cameras.yaml#L14-L18) | [HA Component](https://www.home-assistant.io/components/camera.generic/) |
    * Requires URL of traffic image obtained from Google | [Google Search](https://www.google.com/search?q=san+francisco+traffic&oq=san+francisco+traffic&aqs=chrome.0.35i39j0l5.2687j0j7&sourceid=chrome&ie=UTF-8) |

5) **Calendar Card** - As titled. It's great addition to a Home UI. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/ui-lovelace.yaml#L63-L67) | [Github](https://github.com/rdehuyss/homeassistant-lovelace-google-calendar-card) |
    * Requires **Google Calendar Event component**. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/configuration.yaml#L106-L109) | [HA Component](https://www.home-assistant.io/components/calendar.google/) |

6) **Air Visual Card** - A card that mimics the look of the cards found on airvisual.com. Background, font color and icons change depending on AQI level. Created by me! | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/ui-lovelace.yaml#L87-L92) | [Github](https://github.com/dnguyen800/Air-Visual-Card) |
    * Requires **Air Visual component**. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/config/sensors.yaml#L19-L25) | [HA Component](https://www.home-assistant.io/components/sensor.airvisual/) |
    * Weather component such as **Dark Sky** is recommended. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/ui-lovelace.yaml#L87-L92) | [HA Component](https://www.home-assistant.io/components/weather.darksky/) |

7) **Mini Media Player Card (TV)** - Combines multiple media players into one. In this case, it combines the LG WebOS TV, XboxOne and Playstation4 media players. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/config/media_players.yaml#L46-L51) | [Github](https://github.com/kalkih/mini-media-player), [HA Component](https://www.home-assistant.io/components/media_player.universal/) 
    * Uses **HA Conditional card** to display the media player only when it is active. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/ui-lovelace.yaml#L104-L117) | [HA Lovelace Card](https://www.home-assistant.io/lovelace/conditional/) | 
    * Uses the **LG WebOS TV Component**. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/config/media_players.yaml#L14-L19) | [HA Component](https://www.home-assistant.io/components/media_player.webostv/) | 
    * Uses the **XboxOne Hass.io add-on**. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/config/media_players.yaml#L36-L38) | [Github](https://github.com/hunterjm/hassio-addons/tree/master/xboxone) |
    * Also uses the **Playstation 4 Hass.io add-on**. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/config/media_players.yaml#L40-L44) | [Github](https://github.com/vkorn/hassio-addons/tree/master/ps4waker) | [Highly Recommended Tutorial](https://community.home-assistant.io/t/playstation-4-ps4-custom-component/16974/73) | 


8) **Slideshow Card** | My Config???? | [Github](https://github.com/zsarnett/slideshow-card) |
    * Requires **custom Folder sensor**. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/config/sensors.yaml#L3-L4) | [Github](https://github.com/zsarnett/slideshow-card) |
    * Requires storing images on a local folder as defined in your YAML file, like \config\www\images\slideshow. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/tree/master/configuration/www/images/slideshow) |

9) **Standard Thermostat card** | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/ui-lovelace.yaml#L93-L95) | [HA Lovelace Card](https://www.home-assistant.io/lovelace/thermostat/) |
    * Requires an **HA thermostat/climate entity**, like Nest or Ecobee. You can also setup a demo thermostat platform to test, like I did in this example. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/configuration.yaml#L124-L125) | [HA Component](https://www.home-assistant.io/components/demo/) |

10) **Mini Media Player Card (Music)** - Displays when Spotify or a Chromecast Built-in Speaker begins playing around the house. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/ui-lovelace.yaml#L63-L67) | [Github](https://github.com/kalkih/mini-media-player) |
    * Uses **HA Conditional card** to display the media player only when it is active. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/ui-lovelace.yaml#L63-L67) |
    * Requires **Universal Media Player entity** to combine multiple music media players into one. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/config/media_players.yaml#L54-L66) | [HA Component](https://www.home-assistant.io/components/media_player.universal/) | 
    * Requires a media player, such as **Chromecast**. Having HA Discovery component enabled will allow HA to automatically detect Chromecasts or Google Home on the network. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/configuration.yaml#L51-L52) | [HA Component](https://www.home-assistant.io/components/cast/) |



