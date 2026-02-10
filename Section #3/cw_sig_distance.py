## cw_sig_distance.py
## DATE: 2/8/2025
## OBJ: To see how far
## a 10 watt 6m CW signal
## can travel.
##=======================
## Repeat Interval: 30s
## Transmitter: Yaesu FT-710 (160m-6m)
## Receiver: Wouxun KG-UV7D (6m/2m)
##=======================

##=VARIABLE BANK==============================
receiver = "Wouxun KG-UV7D"
transmitter = "Yaesu FT-710"
repeat_interval = "30 (seconds)"
receiver_band_range = "160 meters to 6 meters"
transmitter_band_range = "6 meters to 2 meters"
maximum_distance_heard = "15 miles"
transmitter_mode = "CW (Continous Wave)"
transmitter_power = "10 watt"
morse_code_speed = "15 WPM (Words Per Minute)"
##============================================

print("The reciever used for this project is the", receiver, '''and the transmitter is the
    ''', transmitter, ". "'''The transmitter's band range is''', transmitter_band_range, '''while
    the receiver's band range is''', receiver_band_range, ".", "The transmitter repeated the", transmitter_power,
      transmitter_mode, "signal, with a speed at", morse_code_speed, '''It is estimated that the transmitted signal was
      heard up to''', maximum_distance_heard, ".")
      


