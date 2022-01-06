# Covid

## Simulator for coronavirus spread

## Running the Simulator
###### https://3b1b.github.io/manim/getting_started/quickstart.html
0. `manimgl covid.py IntroducePlot` or `manimgl covid.py <name of animation>`

## Using Poetry

0. `make install` to install all dependencies
0. `poetry shell`
0. `poetry exit` when you are finished

### Adding Python Dependencies

0. use [poetry](https://python-poetry.org/) to track python deps
0. to install a new dep run `poetry add <your_dep>` or `poetry add <dep> --dev`
0. you can also modify the pyproject.toml directly, then run `poetry lock --no-update`


## Setup

### Mac (M1)

 * Install [brew](https://brew.sh/)
 * Install some [manin dependencies](https://azarzadavila-manim.readthedocs.io/en/latest/installation/mac.html)

 * Install cairo
   ```bash
   brew install cairo
   ```

 * Install pangocairo
   ```bash
   brew install pango
   ```

 * Install ffmpeg
   ```bash
   brew install ffmpeg
   ```

 * Install latex (MacTeX)
   ```bash
   brew install mactex
   ```

<h2> :books: Refrences</h2>
<ul>
  <li><p>Grant Sanderson, Covid git repo</p>
      <p>Available: https://github.com/3b1b/videos/blob/master/_2020/covid.py</p>
  </li>
</ul>
