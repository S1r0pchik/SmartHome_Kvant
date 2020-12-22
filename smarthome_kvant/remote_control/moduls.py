def try_to_connect():
	pyb = pyboard.Pyboard('COM7', 115200)
	pyb.enter_raw_repl()

def connecting():
		pyb.exec_("from pyb import Pin")
		pyb.exec_("p_out = [Pin(i, Pin.OUT_PP) for i in ('D3','D5','D6') ]")

def off_led():
	pyb.exec_("p_out[0].off()")
	pyb.exec_("p_out[1].off()")
	pyb.exec_("p_out[2].off()")

def on_led():
	pyb.exec_("p_out[0].on()")
	pyb.exec_("p_out[1].on()")
	pyb.exec_("p_out[2].on()")