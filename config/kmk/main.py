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
from kmk.modules.capsword import CapsWord
from kmk.modules.split import Split, SplitType, SplitSide

layers = Layers()
combos = Combos()

split = Split(
    # split_side=SplitSide.RIGHT,
    split_flip=False,  # If both halves are the same, but flipped, set this True
    # split_side=None,  # Sets if this is to SplitSide.LEFT or SplitSide.RIGHT, or use EE hands
    split_type=SplitType.UART,  # Defaults to UART
    split_target_left=False,  # Assumes that left will be the one on USB. Set to False if it will be the right
    uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
    data_pin=board.GP0,  # The primary data pin to talk to the secondary device with
    data_pin2=board.GP1,  # Second uart pin to allow 2 way communication
    uart_flip=True,  # Reverses the RX and TX pins if both are provided
    use_pio=True,  # Use RP2040 PIO implementation of UART. Required if you want to use other pins than RX/TX
)

keyboard = KMKKeyboard()

keyboard.extensions.append(MediaKeys())

keyboard.modules.append(layers)
keyboard.modules.append(MouseKeys())
keyboard.modules.append(TapDance())
keyboard.modules.append(combos)
keyboard.modules.append(HoldTap())
keyboard.modules.append(CapsWord())
keyboard.modules.append(split)

#                          0           1          2         3         4         5          6          7         8         9         10         11
#keyboard.col_pins = (board.GP0, board.GP1, board.GP2,board.GP3,board.GP4,board.GP5, board.GP6,board.GP7,board.GP8,board.GP9,board.GP10,board.GP11)
keyboard.col_pins = (board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15)
keyboard.row_pins = (board.GP16, board.GP17,board.GP18,board.GP19, board.GP20)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.coord_mapping = [ 
     0,  1,  2,  3,  4,  5,        30, 31, 32, 33, 34, 35, 
     6,  7,  8,  9, 10, 11,        36, 37, 38, 39, 40, 41,
    12, 13, 14, 15, 16, 17,        42, 43, 44, 45, 46, 47,
    18, 19, 20, 21, 22, 23,        48, 49, 50, 51, 52, 53,
        25, 26, 27,                        56, 57, 58, 
            29, 28,                        55, 54 
     ]

xxxxxxxx = KC.NO
________ = KC.TRNS

# Combos
combos.combos = [
    Sequence((KC.LWIN, KC.W), KC.LALT(KC.F4)),
    Chord((KC.LALT, KC.RSFT), KC.CW),           # CapsWord on lalt and rshift
]

# TapDance: 
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
 
                               KC.SPC,   LALT,     KC.ENT,                L2L3,     KC.RSFT,  KC.MO(1),    
                                         KC.BSPC,  KC.LWIN,               KC.DEL,   KC.RALT
],
[
                                                      ####### SYMBOLS #######

KC.F11,   KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F5,                 KC.F6,    KC.F7,    KC.F8,    KC.F9,    KC.F10,   KC.F12,
________, KC.QUOT,  KC.LABK,  KC.RABK,  KC.DQUO,  KC.DOT,                KC.DLR,   KC.AT,    KC.LBRC,  KC.RBRC,  KC.PERC,  KC.EQUAL,
________, KC.EXLM,  KC.MINS,  KC.PLUS,  KC.EQUAL, KC.HASH,               KC.PIPE,  KC.UNDS,  KC.LPRN,  KC.RPRN,  KC.COLN,  KC.DQUO,
________, KC.CIRC,  KC.SLASH, KC.ASTR,  KC.BSLASH,KC.GRV,                KC.TILD,  KC.AMPR,  KC.LCBR,  KC.RCBR,  KC.QUES,  KC.DEL,
 
                              ________, ________, ________,              KC.TO(0),  ________, ________,    
                                        ________, ________,              ________,  ________
],
[
             ####### NUMERICAL #######                                                  ###### NAVIGATION ########

KC.MUTE,  xxxxxxxx, KC.MPRV,  KC.MPLY,  KC.MNXT,  KC.RESET,              KC.BRID,  KC.BRIU,  KC.PGUP,   xxxxxxxx, KC.NO,   KC.NO,
KC.VOLU,  KC.MINUS, KC.N7,    KC.N8,    KC.N9,    KC.SLASH,              KC.HOME,  KC.PGDN,  KC.UP,     KC.PGUP,  KC.P,    KC.NO,
KC.VOLD,  KC.PLUS,  KC.N4,    KC.N5,    KC.N6,    KC.ASTR,               KC.HOME,  KC.LEFT,  KC.DOWN,   KC.RIGHT, KC.END,  KC.NO,
________, KC.N0,    KC.N1,    KC.N2,    KC.N3,    KC.DEL,                xxxxxxxx, xxxxxxxx, KC.PGDN,   xxxxxxxx, KC.NO,   KC.NO,
 
                              ________, ________, ________,              KC.TO(0), ________, KC.ENT,     
                                        ________, ________,              ________, ________
],
[
                                                      ####### MOUSE #######

xxxxxxxx, xxxxxxxx, xxxxxxxx,  xxxxxxxx,  xxxxxxxx,  xxxxxxxx,           xxxxxxxx, xxxxxxxx, xxxxxxxx, xxxxxxxx, xxxxxxxx, KC.NO,
xxxxxxxx, xxxxxxxx, xxxxxxxx,  KC.MB_BTN4,KC.MB_BTN5,xxxxxxxx,           xxxxxxxx, xxxxxxxx, KC.MS_UP, xxxxxxxx, xxxxxxxx, KC.NO,
KC.ESC,   xxxxxxxx, KC.MB_LMB, KC.MB_MMB, KC.MB_RMB, xxxxxxxx,           xxxxxxxx, KC.MS_LT, KC.MS_DN, KC.MS_RT, xxxxxxxx, KC.NO,
________, xxxxxxxx, xxxxxxxx,  xxxxxxxx,  xxxxxxxx,  xxxxxxxx,           xxxxxxxx, xxxxxxxx, xxxxxxxx, xxxxxxxx, xxxxxxxx, KC.NO,

                               xxxxxxxx,  KC.MW_UP,  xxxxxxxx,           KC.TO(0), xxxxxxxx, KC.NO,
                                          KC.MW_DN,  xxxxxxxx,           xxxxxxxx, KC.NO
]
]


if __name__ == '__main__':
    keyboard.go()