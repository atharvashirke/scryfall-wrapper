
# scryfall_wrapper

The easiest way to get fresh data on every Magic the Gathering card for your software in a simple and intuitive way.



## Installation

Install scryfall_wrapper with pip.

```bash
  pip install scryfall-wrapper
```
    
## Usage/Examples

```python
from scryfall_wrapper import *

# Easily fetch data from scryfall with string search args
sol_ring = Card("Sol Ring") 

# Get up to date prices with a single method
price = sol_ring.price()

# Along with support for almost any type of data scryfall has
cmc = sol_ring.cmc
artist = sol_ring.artist
rarity = sol_ring.rarity
set_code = sol_ring.set

# Get data on collections of cards with one call
every_reprint = sol_ring.reprints()

# Use Card_Set objects to represent a set of MTG and related data
commander_legends = Card_Set("CMR")
all_cmr_cards = commander_legends.cards()




## Authors

- [@atharvashirke](https://www.github.com/atharvashirke)

