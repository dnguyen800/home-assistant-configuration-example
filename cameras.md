# Cameras View

[Home](home.md) | [Media](media.md) | [Rooms](rooms.md) | [Cameras](cameras.md) | [Comics](comics.md) | [System](system.md) | [Floor Plan](floorplan.md) 

![Cameras View](https://github.com/dnguyen800/home-assistant-configuration-example/blob/master/images/cameras.png?raw=true)


## Components in this View
Note: I set 'panel: true' to use the entire width of the screen.

0) **Lovelace Layout Card** - Backend card that provides more control in how to organize your Lovelace cards in a readable format, versus the previous method of using vertical and horizontal stacks. You define the columns and choose where to insert breaks, thus maximizing screen space. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/ui-lovelace.yaml#L449-L451) | [Github](https://github.com/thomasloven/lovelace-layout-card) |

1) **Compact Custom Header** - Reduces the height of the original HA header, saving precious space needed on small tablets like the Fire HD8. Also adds a clock. To use the header with the layout card or stack card, it must be placed within the layout card, not outside. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/ui-lovelace.yaml#L452-L455) | [Github](https://github.com/maykar/compact-custom-header/) |

2) **Cameras** - I use the Lovelace Picture Entity card to display some internet cameras. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/ui-lovelace.yaml#L446-L462) | [HA Lovelace Card](https://www.home-assistant.io/lovelace/picture-entity/) |
    * **Generic Camera Component** used to display internet cameras. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/7a63a37ee0b22a8af947cab6a3688eba5ad6efe3/configuration/config/cameras.yaml#L6-L18) | [HA Component](https://www.home-assistant.io/components/camera.generic/) |
