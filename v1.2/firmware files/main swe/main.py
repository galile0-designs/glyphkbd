# glyph v1 kmk firmware main

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

keyboard.col_pins = (
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP5,
    board.GP6,
    board.GP7,
    board.GP8,
    board.GP20,
    board.GP21,
    board.GP22,
    board.GP23,
    board.GP24,
    board.GP25,
    board.GP26,
    board.GP27,
)

keyboard.row_pins = (
    board.GP11,
    board.GP12,
    board.GP13,
    board.GP14,
    board.GP15,
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())


Å = KC.RALT(KC.W)
Ö = KC.RALT(KC.P)   
Ä = KC.RALT(KC.Q)

keyboard.keymap = [

	# base layer
    [
	##########-##########-##########-##########-##########-##########-##########-##########-##########-##########-##########-##########-##########-##########-##########-##########
        KC.ESC,    KC.N1,     KC.N2,     KC.N3,     KC.N4,     KC.N5,     KC.N6,     KC.N7,     KC.N8,     KC.N9,     KC.N0,     KC.MINS,   KC.BSPC,   KC.INS,    KC.HOME,   KC.PGUP, 
	KC.TAB,    KC.Q,      KC.W,      KC.E,      KC.R,      KC.T,      KC.Y,      KC.U,      KC.I,      KC.O,      KC.P,      KC.LBRC,   KC.RBRC,   KC.DEL,    KC.END,    KC.PGDN, 
	KC.CAPS,   KC.A,      KC.S,      KC.D,      KC.F,      KC.G,      KC.H,      KC.J,      KC.K,      KC.L,      KC.SCLN,   KC.QUOT,   KC.ENT,    KC.NO,     KC.NO,     KC.NO,   
	KC.LSFT,   KC.BSLS,   KC.Z,      KC.X,      KC.C,      KC.V,      KC.B,      KC.N,      KC.M,      KC.COMM,   KC.DOT,    KC.SLSH,   KC.RSFT,   KC.NO,     KC.UP,     KC.NO,   
	KC.LCTL,   KC.NO,     KC.LGUI,   KC.LALT,   KC.MO(1),  KC.SPC,    KC.NO,     KC.SPC,    KC.MO(3),  KC.RALT,   KC.RGUI,   KC.MO(2),  KC.RCTL,   KC.LEFT,   KC.DOWN,   KC.RGHT, 

    ],

	# function layer
    [
	##########-##########-##########-##########-##########-##########-##########-##########-##########-##########-##########-##########-##########-##########-##########-##########
        KC.NO,     KC.F1,     KC.F2,     KC.F3,     KC.F4,     KC.F5,     KC.F6,     KC.F7,     KC.F8,     KC.F9,     KC.F10,    KC.F11,    KC.F12,    KC.PSCR,   KC.SLCK,   KC.BRK,     
	KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     
	KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     
	KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     
	KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.TRNS,   KC.NO,     KC.NO,     KC.NO,     KC.TRNS,   KC.NO,     KC.NO,     KC.TRNS,   KC.NO,     KC.NO,     KC.NO,     KC.NO,     

    ],

	# media layer
    [
	##########-##########-##########-##########-##########-##########-##########-##########-##########-##########-##########-##########-##########-##########-##########-##########
	KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.VOLU,     
	KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.MPLY,   KC.NO,     KC.VOLD,     
	KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     
	KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     
	KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.TRNS,   KC.NO,     KC.NO,     KC.NO,     KC.TRNS,   KC.NO,     KC.NO,     KC.TRNS,   KC.NO,     KC.NO,     KC.NO,     KC.NO,     

    ],

	# symbol layer
    [
	##########-##########-##########-##########-##########-##########-##########-##########-##########-##########-##########-##########-##########-##########-##########-##########
        KC.GRV,    KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.EQL,    KC.PPLS,   KC.NO,     KC.NO,     KC.NO,     KC.NO,     
        KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     Å,         KC.NO,     KC.NO,     KC.NO,     KC.NO,     
	KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     Ö,         Ä,         KC.NO,     KC.NO,     KC.NO,     KC.NO,   
	KC.LSFT,   KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.RSFT,   KC.NO,     KC.NO,     KC.NO,     
	KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.TRNS,   KC.NO,     KC.NO,     KC.NO,     KC.TRNS,   KC.NO,     KC.NO,     KC.TRNS,   KC.NO,     KC.NO,     KC.NO,     KC.NO,     

    ],

]

if __name__ == "__main__":
    keyboard.go()
