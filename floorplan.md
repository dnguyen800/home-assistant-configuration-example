# Floor Plan View

[Readme](README.md) |
[Home View](home.md) |  [Media](media.md) | [Rooms](rooms.md) | [Cameras](cameras.md) | [Comics](comics.md) | [System](system.md) | [**Floor Plan**](floorplan.md) 

![Floor Plan View](https://github.com/dnguyen800/home-assistant-configuration-example/blob/master/images/floorplan.png?raw=true)

The Floor Plan view is similar to the Rooms view, but I use it more because it's easier to process. I can confirm all my doors are closed and lights are off with one glance.

Everything in this floor plan is made of .png images. I use the transparency capability of .png images to create circular icons. Using the out-of-the-box [Lovelace Picture Elements card](https://www.home-assistant.io/lovelace/picture-elements/), I'm able to achieve mostly everything I did in the [@pkozul's](https://github.com/pkozul/ha-floorplan) custom Floorplan, which was amazing but painful to setup. I do miss the cool fan and door animations though.

## Components in this View
Note: I set 'panel: true' to use the entire width of the screen. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/469e949b0f1610091ca03c508d8d9ec6846ba6e4/configuration/ui-lovelace.yaml#L611-L616) |

0) I drew the **Floor Plan** image using an open-source vector graphics application called [Inkscape](https://inkscape.org/). It is very difficult to use, so I recommend using any program you're familiar with, like one of Adobe's graphic design products. If you're lucky, you can find your home's floor plan online. I was able to find a neighbor's floor plan siilar to mine and used that as an outline. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/469e949b0f1610091ca03c508d8d9ec6846ba6e4/configuration/ui-lovelace.yaml#L611) | [Image](https://github.com/dnguyen800/home-assistant-configuration-example/blob/master/configuration/www/images/floorplan/floorplan.png) |


1) **Compact Custom Header** - Reduces the height of the original HA header, saving precious space on small tablets like the Fire HD8. Also adds a clock. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/c464015b67898ab87d38762f3f4858ecddc3ea87/configuration/ui-lovelace.yaml#L507-L510) | [Github](https://github.com/maykar/compact-custom-header/) |

2) **Text** - Displays the time, indoor and outdoor temperature, and anything else I can think of. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/c464015b67898ab87d38762f3f4858ecddc3ea87/configuration/ui-lovelace.yaml#L880-L908) |

3) The **TV Light** uses a gradient image to give the look that the TV is glowing. It automatically appears when the TV and bias lighting is on, by changing the CSS opacity setting. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/c464015b67898ab87d38762f3f4858ecddc3ea87/configuration/ui-lovelace.yaml#L760-L768) | [Image](https://github.com/dnguyen800/home-assistant-configuration-example/blob/master/configuration/www/images/floorplan/tv.png) |

4) The **Light bulb icon** changes when the light is on or off. Pressing on the icon will turn on the light; a long-press will bring up the 'More Info' panel. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/c464015b67898ab87d38762f3f4858ecddc3ea87/configuration/ui-lovelace.yaml#L744-L758) | [Image](https://github.com/dnguyen800/home-assistant-configuration-example/blob/master/configuration/www/images/floorplan/light_on.png) |
    * Icon and color scheme is from [@oakbrad's floor plan](https://community.home-assistant.io/t/share-your-floorplan/21315/146?u=dwinnn), who used [thenounproject.com](https://thenounproject.com/) for icons.



6) **Motion sensors**, 'nuff said. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/c464015b67898ab87d38762f3f4858ecddc3ea87/configuration/ui-lovelace.yaml#L682-L740) | [Image](https://github.com/dnguyen800/home-assistant-configuration-example/blob/master/configuration/www/images/floorplan/motion-on.png) |
    * I created **MQTT binary sensors** to load SmartThings sensors into Home Assistant, but that is no longer needed as of Home Assistant 0.87. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/master/configuration/config/binary_sensors.yaml) |
    * Icon is from [thenounproject.com](https://thenounproject.com/).

7) **Camera**. Clicking on the icon will bring up the live camera view. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/c464015b67898ab87d38762f3f4858ecddc3ea87/configuration/ui-lovelace.yaml#L674-L681) | [Image](https://github.com/dnguyen800/home-assistant-configuration-example/blob/master/configuration/www/images/floorplan/camera.png) |
    * Icon is from [thenounproject.com](https://thenounproject.com/).

8) **Garage door (not pictured) and other door sensors**. I was too lazy to play around with CSS, so I created separate images for open and closed doors. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/c464015b67898ab87d38762f3f4858ecddc3ea87/configuration/ui-lovelace.yaml#L909-L960) | [Image](https://github.com/dnguyen800/home-assistant-configuration-example/blob/master/configuration/www/images/floorplan/front_door_closed.png) |
    * **Door sensors**, see my examples of MQTT binary sensors. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/master/configuration/config/binary_sensors.yaml) |


6) The **Scene Buttons** (on the right) will activate scenes like Movie Theater (living room dims, TV light on), reading (living room lights on), downstairs lights off, upstairs lights off. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/c464015b67898ab87d38762f3f4858ecddc3ea87/configuration/ui-lovelace.yaml#L621-L672) |
    * **Scenes**, see my examples. | [My Config](https://github.com/dnguyen800/home-assistant-configuration-example/blob/master/configuration/config/scenes.yaml) | [HA Component](https://www.home-assistant.io/components/scene/) |
    * Icons are from [thenounproject.com](https://thenounproject.com/).

7) The [Lovelace Picture Elements card](https://www.home-assistant.io/lovelace/picture-elements/) was used to display the floor plan and icons.

## Credits
* Icons are from [thenounproject.com](https://thenounproject.com/), and from various Floorplan examples on the Home Assistant forum [thread](https://community.home-assistant.io/t/share-your-floorplan/21315), thanks [@oakbrad](https://community.home-assistant.io/t/share-your-floorplan/21315/146?u=dwinnn)!

* Car, sofa, washer and dryer are 3D models found on [sketchup.com 3D Warehouse](https://3dwarehouse.sketchup.com/?hl=en)