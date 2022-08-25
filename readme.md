# PDF To Speech

<style>
p {text-align: center;}
</style>

<p>
                         ||-------------------------------------------------------||
                         ||.--.    .-._                        .----.             ||
                         |||==|____| |H|___            .---.___|""""|_____.--.___ ||
                         |||  |====| | |xxx|_          |+++|=-=|_  _|-=+=-|==|---|||
                         |||==|    | | |   | \         |   |   |_\/_|Jane |  | ^ |||
                         |||  |    | | |   |\ \   .--. |   |=-=|_/\_|-=+=-|  | ^ |||
                         |||  |    | | |   |_\ \_( oo )|   |   |    |Eyre |  | ^ |||
                         |||==|====| |H|xxx|  \ \ |''| |+++|=-=|""""|-=+=-|==|---|||
                         ||`--^----'-^-^---'   `-' ""  '---^---^----^-----^--^---^||
                         ||-------------------------------------------------------||
                         ||-------------------------------------------------------||
                         ||               ___                   .-.__.-----. .---.||
                         ||              |===| .---.   __   .---| |XX|<(*)>|_|^^^|||
                         ||         ,  /(|   |_|III|__|''|__|:x:|=|  |     |=| Q |||
                         ||      _a'{ / (|===|+|   |++|  |==|   | |  |Beach| | R |||
                         ||      '/\\/ _(|===|-|   |  |''|  |:x:|=|  |Music| | Y |||
                         ||_____  -\{___(|   |-|   |  |  |  |   | |  |     | | Z |||
                         ||       _(____)|===|+|[I]|DK|''|==|:x:|=|XX|<(*)>|=|^^^|||
                         ||              `---^-^---^--^--'--^---^-^--^-----^-^---^||
                         ||-------------------------------------------------------||
                         ||_______________________________________________________|| 
                        
</p>
<!-- 
                         ||-------------------------------------------------------||
                         ||.--.    .-._                        .----.             ||
                         |||==|____| |H|___            .---.___|""""|_____.--.___ ||
                         |||  |====| | |xxx|_          |+++|=-=|_  _|-=+=-|==|---|||
                         |||==|    | | |   | \         |   |   |_\/_|Jane |  | ^ |||
                         |||  |    | | |   |\ \   .--. |   |=-=|_/\_|-=+=-|  | ^ |||
                         |||  |    | | |   |_\ \_( oo )|   |   |    |Eyre |  | ^ |||
                         |||==|====| |H|xxx|  \ \ |''| |+++|=-=|""""|-=+=-|==|---|||
                         ||`--^----'-^-^---'   `-' ""  '---^---^----^-----^--^---^||
                         ||-------------------------------------------------------||
                         ||-------------------------------------------------------||
                         ||               ___                   .-.__.-----. .---.||
                         ||              |===| .---.   __   .---| |XX|<(*)>|_|^^^|||
                         ||         ,  /(|   |_|III|__|''|__|:x:|=|  |     |=| Q |||
                         ||      _a'{ / (|===|+|   |++|  |==|   | |  |Beach| | R |||
                         ||      '/\\/ _(|===|-|   |  |''|  |:x:|=|  |Music| | Y |||
                         ||_____  -\{___(|   |-|   |  |  |  |   | |  |     | | Z |||
                         ||       _(____)|===|+|[I]|DK|''|==|:x:|=|XX|<(*)>|=|^^^|||
                         ||              `---^-^---^--^--'--^---^-^--^-----^-^---^||
                         ||-------------------------------------------------------||
                         ||_______________________________________________________|| -->

## Overview

PDF to Speech is a Python application that allows users to convert pdf to audio. With a quick and easy setup process, the user will be listening to their favorite story or article within minutes.

## How to Use PDF to Speech

### Setup and Installation

The first step to setting up PDF to Speech is to install the necessary packages from requirements.txt by simply running `pip3 install requirements.txt`.

You will then need to download a pdf of your choice and add it to the `pdf` folder.

### Running PDF to Speech

There are two options when running PDF to Speech. First, as the name suggests, you can turn your pdf into text and playback the converted audio. With this first option, all you need to do is simply run `python3 main.py`. The audio will begin to play immediately through your speakers.

The second option is to convert the pdf into a text file and skip the audio playback. If you opt for this option, the argument `--text` needs to be added after the script name, so run `python3 main.py --text`. After running the program, a `.txt` file containing the converted pdf to text will appear in the `pdf` folder under the same name as the original pdf.
