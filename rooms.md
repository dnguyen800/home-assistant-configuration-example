# Rooms View

[Home](home.md) | [Media](media.md) | [Rooms](rooms.md) | [Cameras](cameras.md) | [Comics](comics.md) | [System](system.md) | [Floor Plan](floorplan.md) 

![Rooms View](https://github.com/dnguyen800/home-assistant-configuration-example/blob/master/images/rooms.png?raw=true)


## Components in this View
0) **Lovelace Layout Card** - Backend card that provides more control in how to organize your Lovelace cards in a readable format, versus the previous method of using vertical and horizontal stacks. You define the columns and choose where to insert breaks, thus maximizing screen space. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/ui-lovelace.yaml#L384-L386) | [Github](https://github.com/thomasloven/lovelace-layout-card) |

1) **Compact Custom Header** - Reduces the height of the original HA header, saving precious space needed on small tablets like the Fire HD8. Also adds a clock. To use the header with the layout card or stack card, it must be placed within the layout card, not outside. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/ui-lovelace.yaml#L387-L390) | [Github](https://github.com/maykar/compact-custom-header/) |

2) **Lights** - Uses standard Lovelace Entities card to display lights. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/ui-lovelace.yaml#L391-L409) |
    * **Slider Entity Row** adds a brightness slider to light entities. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/ui-lovelace.yaml#L396-L409) | [Github](https://github.com/thomasloven/lovelace-slider-entity-row) |

3) **Alarm Panel** - I used a demo alarm panel in this example. But you can use an MQTT alarm panel if your alarm is within SmartThings. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/ui-lovelace.yaml#L419-L420) | [HA Component](https://www.home-assistant.io/components/demo/) |

4) **Fans** - I used a demo fan entity in this example. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/ui-lovelace.yaml#L410-L417) | [HA Component](https://www.home-assistant.io/components/demo/) |
    * **Monster Card** is used to include all fan entities in the card. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/ui-lovelace.yaml#L410-L417) | [Github](https://community.home-assistant.io/t/lovelace-bringing-back-entity-filter-monster-card/58701) |

5) **Locks** - I used a demo lock entity in this example. To make it look nice, try using Picture Elements Lovelace card! | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/ui-lovelace.yaml#L421-L428) | [HA Component](https://www.home-assistant.io/components/demo/) |
    * **Monster Card** is used to include all lock entities in the card. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/ui-lovelace.yaml#L421-L428) | [Github](https://community.home-assistant.io/t/lovelace-bringing-back-entity-filter-monster-card/58701) |
