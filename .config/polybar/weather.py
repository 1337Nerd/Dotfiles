#!/usr/bin/env python
# Modified from https://github.com/Chaosteil/dotfiles/tree/master/polybar/.config/polybar

import json
import urllib
import urllib.parse
import urllib.request
import os

def main():
    try:
        weather = json.loads(urllib.request.urlopen(
            'https://api.openweathermap.org/data/2.5/weather?q=GroveCity,oh&appid=c3ec0e268239d674fbe215f89868ee73&units=imperial')
            .read())
        desc = weather['weather'][0]['description'].capitalize()
        temp = int(float(weather['main']['temp']))
        return '{}, {} F'.format(desc, temp)
    except:
        return '!'


if __name__ == "__main__":
    print(main())
