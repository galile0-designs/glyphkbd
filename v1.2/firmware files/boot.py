import board

from kmk.bootcfg import bootcfg

bootcfg(
    sense=board.GP1,
    source=board.GP11,
    cdc=False,
    consumer_control=True,
    keyboard=True,
    midi=True,
    mouse=True,
    nkro=False,
    pan=False,
    storage=False,
)
