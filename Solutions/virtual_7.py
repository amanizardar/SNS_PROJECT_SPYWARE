

import tkinter as Tkinter
import pyautogui
import random


x=3
z=" "
def if_else(store_key_frame,k):
 	
	if len(k)<=x:
		fitting_this_button = Tkinter.Button(store_key_frame, text=k, width=2, height=2)
	else:
		fitting_this_button = Tkinter.Button(store_key_frame, text=k.center(5,' '), height=2)
	if z in k:
		fitting_this_button['state']='disable'

	return fitting_this_button

def initialize(self):
	fitting_all_keys = Tkinter.Frame(self)
	fitting_all_keys.pack(side='left',expand='yes',fill='both',padx=10,pady=10,ipadx=10,ipady=10)
	return fitting_all_keys


def sec_initialize(fitting_all_keys,Functionalities_of_that):
	fitting_this_subset = Tkinter.LabelFrame(fitting_all_keys)
	fitting_this_subset.pack(Functionalities_of_that)
	return fitting_this_subset

def third_initialize(fitting_this_subset):
	store_key_frame = Tkinter.Frame(fitting_this_subset)
	store_key_frame.pack(side='top',expand='yes',fill='both')
	return store_key_frame

def initialize_colours(fitting_this_button):
	fitting_this_button['relief']="ridge"
	fitting_this_button['bg']="black"
	fitting_this_button['fg']="white"


list_of_keys = [
			('esc', 'F1', 'F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12'),
			('`',',','.','/','-','=','\\','[',']','backspace'),
			('~','!','@','#','$','%','^','&','*','(',')','_','+','|'),
			('tab','i','w','e','d','x','y','g','q','b','p','{','}',";",'\''),
			('capslock','l','s','r','n','h','j','k','a',':',"\"","enter"),
			('z','t','c','v','o','u','m','<','>','?',"shift"),
			( "win",'space  ','alt','ctrl'),

			("printscreen","scrolllock","pause"),
			("insert","home","pageup"),
			("delete","end","pagedown"),
			("numlock","/","*"),
			("7","8","9","+"),
			("4","5","6","-"),
			("1","2","3","0"),
			(".","enter"),
			("up",),
			("right","down","left"),

]

all_keys =[ 
[

	[
		("1st"),
		({'side':'top','expand':'yes','fill':'both'}),
		[
			(random.sample(list_of_keys[0], len(list_of_keys[0]))),
			(random.sample(list_of_keys[2], len(list_of_keys[2]))),
			(random.sample(list_of_keys[1], len(list_of_keys[1]))),
			(random.sample(list_of_keys[4], len(list_of_keys[4]))),
			(random.sample(list_of_keys[3], len(list_of_keys[3]))),
			(random.sample(list_of_keys[5], len(list_of_keys[5]))),
			(random.sample(list_of_keys[6], len(list_of_keys[6]))),

		]
	]
],
[
	[          
		("2nd"),
		({'side':'top','expand':'yes','fill':'both'}),
		[
			
			(random.sample(list_of_keys[7], len(list_of_keys[7]))),
			(random.sample(list_of_keys[8], len(list_of_keys[8]))),
			(random.sample(list_of_keys[9], len(list_of_keys[9]))),
			(random.sample(list_of_keys[10], len(list_of_keys[10]))),
			(random.sample(list_of_keys[11], len(list_of_keys[11]))),
			(random.sample(list_of_keys[12], len(list_of_keys[12]))),
			(random.sample(list_of_keys[13], len(list_of_keys[13]))),
			(random.sample(list_of_keys[14], len(list_of_keys[14]))),
			(random.sample(list_of_keys[15], len(list_of_keys[15]))),
			(random.sample(list_of_keys[16], len(list_of_keys[16]))),
		]
	],
],
]

class MY_keyboard(Tkinter.Frame):
	def __init__(self, *args, **kwargs):
		Tkinter.Frame.__init__(self, *args, **kwargs)
		self.layout_creation()


	def layout_creation(self):
		for collection_of_keys in all_keys:
			
			fitting_all_keys=initialize(self)
			# print(type(collection_of_keys))

			for name_of_that_layer, Functionalities_of_that, subset_of_keys in collection_of_keys:
				fitting_this_subset=sec_initialize(fitting_all_keys,Functionalities_of_that)
				
				for key_bunch in subset_of_keys:
				
					store_key_frame=third_initialize(fitting_this_subset)
					for k in key_bunch:
						k=k.lower()
					
						fitting_this_button=if_else(store_key_frame,k)
						
						initialize_colours(fitting_this_button)

						fitting_this_button['command']=lambda q=k.lower(): self.Pressed_functionality(q)
						fitting_this_button.pack(side='left',fill='both',expand='yes')
		return

	def Pressed_functionality(self, event):
		pyautogui.press(event)
		return

class shiting_window_fun:
	def __init__(self, main_window, label):
		self.main_window = main_window
		self.label = label

	def Fun_for_moving_window(self, kwargs):
		w,h = (self.main_window.winfo_reqwidth(), self.main_window.winfo_reqheight())
		(x,y) = (kwargs.x_root, kwargs.y_root)
		self.main_window.geometry("%dx%d+%d+%d" % (w,h,x,y))
		return

def main():
	main_window = Tkinter.Tk(className="Antilogger MY_keyboard by Diksha & Aman")
	main_window.overrideredirect(True)
	main_window.wait_visibility(main_window)
	main_window.wm_attributes('-alpha',0.8)

	k=MY_keyboard(main_window, bg="blue")
	
	that_frame = Tkinter.Frame(main_window)
	title_bar_t=Tkinter.Label(that_frame, text="Antilogger MY_keyboard by Diksha & Aman", bg="royalblue")
	title_bar_t.pack(side='left',expand="yes", fill="both")

	shifter = shiting_window_fun(main_window, title_bar_t)
	title_bar_t.bind("<B1-Motion>", shifter.Fun_for_moving_window)
	Tkinter.Button(that_frame, text="[X]", command= main_window.destroy).pack(side='right')
	that_frame.pack(side='top', expand='yes',fill='both')
	k.pack(side='top')
	main_window.mainloop()
	return

if __name__=='__main__':
	main()
