import board
# from kmk.modules.encoder import EncoderHandler

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.tapdance import TapDance
from kmk.modules.combos import Combos, Chord, Sequence
from kmk.modules.holdtap import HoldTap

layers = Layers()
combos = Combos()

keyboard = KMKKeyboard()

keyboard.modules.append(layers)
keyboard.modules.append(MouseKeys())
keyboard.modules.append(TapDance())
keyboard.modules.append(combos)
keyboard.modules.append(HoldTap())

keyboard.extensions.append(MediaKeys())
#                          0           1          2         3         4         5          6          7         8         9         10         11
keyboard.col_pins = (board.GP0, board.GP1, board.GP2,board.GP3,board.GP4,board.GP5, board.GP6,board.GP7,board.GP8,board.GP9,board.GP10,board.GP11)
keyboard.row_pins = (board.GP21, board.GP20,board.GP19,board.GP18, board.GP16)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.coord_mapping = [ 
     0,  1,  2,  3,  4,  5,        6,  7,  8,  9, 10, 11,
    12, 13, 14, 15, 16, 17,       18, 19, 20, 21, 22, 23,
    24, 25, 26, 27, 28, 29,       30, 31, 32, 33, 34, 35,
    36, 37, 38, 39, 40, 41,       42, 43, 44, 45, 46, 47,
        
                49, 50, 51,       56, 57, 58,
                    53, 52,       55, 54
     ]

# Combos
combos.combos = [
    Sequence((KC.LWIN, KC.W), KC.LALT(KC.F4)),
]
# TapDance: 
# hold to momentarly activate layer 1, tap for permanent layert 1
# tap once and then hold to momentarly activate layer 2, tap twice for permanent layert 2
L2L3 = KC.TD(
    KC.MO(2),
    KC.MO(3)
)

# HoldTap: KC.HT(key_tapped, key_held)
LALT = KC.HT(KC.NO, KC.LALT)

keyboard.keymap = [
    [                                              
                                                         ####### MAIN #######

KC.GRV,   KC.N1,    KC.N2,     KC.N3,    KC.N4,    KC.N5,                 KC.N6,    KC.N7,    KC.N8,    KC.N9,     KC.N0,    KC.MINUS,
KC.TAB,   KC.Q,     KC.W,      KC.E,     KC.R,     KC.T,                  KC.Y,     KC.U,     KC.I,     KC.O,      KC.P,     KC.EQUAL,
KC.ESC,   KC.A,     KC.S,      KC.D,     KC.F,     KC.G,                  KC.H,     KC.J,     KC.K,     KC.L,      KC.SCLN,  KC.ENT,
KC.LCTRL, KC.Z,     KC.X,      KC.C,     KC.V,     KC.B,                  KC.N,     KC.M,     KC.COMM,  KC.DOT,    KC.SLSH,  KC.BSPC,
 
                               KC.SPC,   LALT,     KC.MEH,                L2L3,     KC.RSFT,  KC.MO(1),    
                                         KC.BSPC,  KC.LWIN,               KC.DEL,   KC.RALT
    ],
                                                                                                        
    [
                                                      ####### SYMBOLS #######

KC.F11,   KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F5,                 KC.F6,    KC.F7,    KC.F8,    KC.F9,    KC.F10,   KC.F12,
KC.TRNS,  KC.QUOT,  KC.LABK,  KC.RABK,  KC.DQUO,  KC.DOT,                KC.DLR,   KC.AT,    KC.LBRC,  KC.RBRC,  KC.PERC,  KC.EQUAL,
KC.TRNS,  KC.EXLM,  KC.MINS,  KC.PLUS,  KC.EQUAL, KC.HASH,               KC.PIPE,  KC.UNDS,  KC.LPRN,  KC.RPRN,  KC.COLN,  KC.DQUO,
KC.TRNS,  KC.CIRC,  KC.SLASH, KC.ASTR,  KC.BSLASH,KC.GRV,                KC.TILD,  KC.AMPR,  KC.LCBR,  KC.RCBR,  KC.QUES,  KC.DEL,
 
                              KC.TRNS,  KC.TRNS,  KC.TRNS,               KC.TO(0),  KC.TRNS,  KC.TRNS,     
                                        KC.TRNS,  KC.TRNS,               KC.TRNS,   KC.TRNS
    ],

    [
             ####### NUMERICAL #######                                                  ###### NAVIGATION ########

KC.MUTE,  KC.NO,    KC.MPRV,  KC.MPLY,  KC.MNXT,  KC.RESET,              KC.BRID,  KC.BRIU,  KC.PGUP,   KC.NO,    KC.NO,   KC.NO,
KC.VOLU,  KC.MINUS, KC.N7,    KC.N8,    KC.N9,    KC.SLASH,              KC.HOME,  KC.PGDN,  KC.UP,     KC.PGUP,  KC.P,    KC.NO,
KC.VOLD,  KC.PLUS,  KC.N4,    KC.N5,    KC.N6,    KC.ASTR,               KC.HOME,  KC.LEFT,  KC.DOWN,   KC.RIGHT, KC.END,  KC.NO,
KC.TRNS,  KC.N0,    KC.N1,    KC.N2,    KC.N3,    KC.DEL,                KC.NO,    KC.NO,    KC.PGDN,   KC.NO,    KC.NO,   KC.NO,
 
                              KC.TRNS,  KC.TRNS,  KC.TRNS,               KC.TO(0), KC.TRNS,  KC.ENT,     
                                        KC.TRNS,  KC.TRNS,               KC.TRNS,  KC.TRNS
    ],
    
[
                                                      ####### MOUSE #######

KC.NO,    KC.NO,    KC.NO,     KC.NO,     KC.NO,     KC.NO,              KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,    
KC.NO,    KC.NO,    KC.NO,     KC.MB_BTN4,KC.MB_BTN5,KC.NO,              KC.NO,    KC.NO,    KC.MS_UP, KC.NO,    KC.NO,    KC.NO,    
KC.ESC,   KC.NO,    KC.MB_LMB, KC.MB_MMB, KC.MB_RMB, KC.NO,              KC.NO,    KC.MS_LT, KC.MS_DN, KC.MS_RT, KC.NO,    KC.NO,    
KC.TRNS,  KC.NO,    KC.NO,     KC.NO,     KC.NO,     KC.NO,              KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,    

                              KC.NO,    KC.MW_UP,    KC.NO,              KC.TO(0), KC.NO,    KC.NO,
                                        KC.MW_DN,    KC.NO,              KC.NO,    KC.NO,
]

]


if __name__ == '__main__':
    keyboard.go()