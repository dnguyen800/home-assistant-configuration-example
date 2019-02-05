# Comics View

[Home](home.md) | [Media](media.md) | [Rooms](rooms.md) | [Cameras](cameras.md) | [Comics](comics.md) | [System](system.md) | [Floor Plan](floorplan.md) 

![Comics View](https://github.com/dnguyen800/home-assistant-configuration-example/blob/master/images/comics.png?raw=true)


## Components in this View
Note: I set 'panel: true' to use the entire width of the screen.

0) **Vertical and Horizontal Stacks to use full screen width** - Before I discovered the @thomasloven Layout card, I used a mix of vertical and horizontal stack cards to achieve the current look. I recommend using Layout card instead, but here is an example of doing it the other way. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/ui-lovelace.yaml#L474-L477) | [HA Lovelace Card](https://www.home-assistant.io/lovelace/vertical-stack/) | [Github Layout Card](https://github.com/thomasloven/lovelace-layout-card) |

1) **Compact Custom Header** - Reduces the height of the original HA header, saving precious space needed on small tablets like the Fire HD8. Also adds a clock. To use the header with the layout card or stack card, it must be placed within the layout card, not outside. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/ui-lovelace.yaml#L474-L477) | [Github](https://github.com/maykar/compact-custom-header/) |

2) **Comics Cards** - I use the custom Useful Markdown card to display the image URL of web comics. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/ui-lovelace.yaml#L468-L491) | [Github](https://github.com/thomasloven/lovelace-useful-markdown-card) |
    * **Web Comic sensor** required to pull the image address of webcomics. I wrote it myself, and just barely works for my needs :) | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/5e66cbe66cb2a99654a92176c7f2fb4b5d4b2c46/configuration/config/sensors.yaml#L7-L17) | [Github](https://github.com/dnguyen800/Webcomic-Sensor) |

