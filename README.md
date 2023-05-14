# Unnest Components

*Filter > Unnest Components* (de: *Komponenten entpacken*) ‘unpacks’, ‘unnests’ or ‘flattens’ components, i.e. it decomposes composites step by step until there is only one level of composition. You may need this for satisfying some fontbakery tests in TTF exports, if you are in a situation where this is required for your project. Nested components are not bad per se.

This filter only makes sense for TrueType exports (.ttf or TT-flavored .woff and .woff2). It has no effect on CFF exports (.otf or CFF-flavored .woff and .woff2) because PostScript-based fonts have no components.

## Custom Parameter
 
You can have the filter run at export time with a custom parameter. This can be useful for automatically fixing interpolations. To do so, go to *File > Font Info > Exports,* select an instance, add a *Custom Parameter* with the plus button, choose *Filter* from the menu that pops up, and write `UnnestComponents` in the filter value.


## Installation

*Unnest Components* is [available in the Glyphs&nbsp;3 Plugin Manager](glyphsapp3://showplugin/Unnest%20Components). Click on the *Install* button next to it and restart Glyphs.

The filter requires Glyphs 3.2 or later. It may work in previous version, though. If it does not, upgrade your Glyphs installation.

# License

Copyright 2022 Rainer Erich Scheichelbauer (@mekkablue). Builds on template code by Georg Seifert (@schriftgestalt) and Jan Gerner (@yanone). Help for the conversion into the plug-in by Rainer Erich Scheichelbauer (@mekkablue).

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

See the License file included in this repository for further details.
