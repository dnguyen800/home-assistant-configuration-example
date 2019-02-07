# Floor Plan View

[Home](home.md) | [Media](media.md) | [Rooms](rooms.md) | [Cameras](cameras.md) | [Comics](comics.md) | [System](system.md) | [Floor Plan](floorplan.md) 

![Floor Plan View](https://github.com/dnguyen800/home-assistant-configuration-example/blob/master/images/floorplan.png?raw=true)

The Floor Plan view is similar to the Rooms view, but I use it more because it's easier to process. I can confirm all my doors are closed and lights are off with one glance.

Everything in this floor plan is made of .png images. I use the transparency capability of .png images to create circular icons. Using the out-of-the-box Lovelace Picture Elements card, I'm able to achieve mostly everything I did in the [@pkozul's](https://github.com/pkozul/ha-floorplan) custom Floorplan, which was amazing but painful to setup. I do miss the cool fan and door animations though.

## Components in this View
Note: I set 'panel: true' to use the entire width of the screen. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/c464015b67898ab87d38762f3f4858ecddc3ea87/configuration/ui-lovelace.yaml#L495-L500) |

0) I drew the **Floor Plan** using an open-source vector graphics application called [Inkscape](https://inkscape.org/). It is very difficult to use, so I recommend using any program you're familiar with, like one of Adobe's graphic design products. If you're lucky, you can find your home's floor plan online. I was able to find a neighbor's floor plan siilar to mine and used that as an outline. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/master/configuration/www/images/floorplan/floorplan.png) |

1) **Compact Custom Header** - Reduces the height of the original HA header, saving precious space on small tablets like the Fire HD8. Also adds a clock. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/c464015b67898ab87d38762f3f4858ecddc3ea87/configuration/ui-lovelace.yaml#L507-L510) | [Github](https://github.com/maykar/compact-custom-header/) |

2) **Text** - Displays the time, indoor and outdoor temperature, and anything else I can think of. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/c464015b67898ab87d38762f3f4858ecddc3ea87/configuration/ui-lovelace.yaml#L880-L908) |

3) The **TV Light** uses a gradient image to give the look that the TV is glowing. It automatically appears when the TV and bias lighting is on, by changing the CSS opacity setting. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/c464015b67898ab87d38762f3f4858ecddc3ea87/configuration/ui-lovelace.yaml#L760-L768) |

4) The **Light bulb icon** changes when the light is on or off. Pressing on the icon will turn on the light; a long-press will bring up the 'More Info' panel. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/c464015b67898ab87d38762f3f4858ecddc3ea87/configuration/ui-lovelace.yaml#L744-L758) | [Image](https://github.com/dnguyen800/home-assistant-configuration-example/blob/master/configuration/www/images/floorplan/light_on.png) |
    * Icon and color scheme is from [@oakbrad's floor plan](https://community.home-assistant.io/t/share-your-floorplan/21315/146?u=dwinnn), who used [thenounproject.com](https://thenounproject.com/) for icons.



6) **Motion sensors**. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/c464015b67898ab87d38762f3f4858ecddc3ea87/configuration/ui-lovelace.yaml#L682-L740) |

7) **Camera**. Clicking on the icon will bring up the live camera view. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/c464015b67898ab87d38762f3f4858ecddc3ea87/configuration/ui-lovelace.yaml#L674-L681) |

8) **Garage door (not pictured) and other door sensors**. I was too lazy to play around with CSS, so I created separate images for open and closed doors. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/c464015b67898ab87d38762f3f4858ecddc3ea87/configuration/ui-lovelace.yaml#L909-L960) |


6) **Scene Buttons** to the right will activate scenes, like Movie Theater (living room dims, TV light on), reading (living room lights on), downstairs lights off, upstairs lights off

## Credits
* Icons are from [thenounproject.com](https://thenounproject.com/), and from various Floorplan examples on the Home Assistant forum [thread](https://community.home-assistant.io/t/share-your-floorplan/21315), thanks [@oakbrad](https://community.home-assistant.io/t/share-your-floorplan/21315/146?u=dwinnn)!

* Car, sofa, washer and dryer are 3D models found on sketchup.com community
