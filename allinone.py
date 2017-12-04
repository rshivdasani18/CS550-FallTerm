"""
Rohin Shivdasani
10/29/17
A Block
MandleBrot Set Visualization #1

http://code.activestate.com/recipes/578590-mandelbrot-fractal-using-tkinter/
https://stackoverflow.com/questions/902761/saving-a-numpy-array-as-an-image

Sources:
http://www.cuug.ab.ca/~dewara/mandelbrot/Mandelbrowser.html
https://docs.python.org/2/library/math.html
Ms. Healey's base code
"""


import random
import math
import tkinter
from tkinter import *

def mandelbrot(z, c, count):
	z = z * z + c
	count += 1
	if abs(z) >= 2.0 or count > maxIt-1:
		return count
	return mandelbrot(z, c, count)

def mandelbrotloop(z, c):
	count = 0
	while abs(z) < 2.0 and count < maxIt-1:
		z = z * z + c
		count += 1
	return count


WIDTH = 500
HEIGHT = 500
xmin = -.01
xmax = .01
ymin = .74
ymax = .76
maxIt = 255

window = Tk()
canvas = Canvas(window, width = WIDTH, height = HEIGHT, bg = "#000000")
img = PhotoImage(width = WIDTH, height = HEIGHT)
canvas.create_image((0, 0), image = img, state = "normal", anchor = tkinter.NW)

redrandom = random.randint(0,255)
greenrandom = random.randint(0,255)
bluerandom = random.randint(0,255)


for row in range(HEIGHT):
    for col in range(WIDTH):
        c = complex(xmin + (xmax - xmin) * col / WIDTH, ymin + (ymax - ymin) * row / HEIGHT)
        z = complex(-0.0, -0.0)
        # r = mandelbrot(z, c, 0)
        r = mandelbrotloop(z, c)

        
        rd = hex((r*19)%255)[2:].zfill(2)
        gr = hex((256*0)%255)[2:].zfill(2)
        bl = hex((255*108)%255)[2:].zfill(2)
        
        img.put("#" + rd + gr + bl, (col, row))

canvas.pack()


"""
These are the main changes I made: 

	use random numbers
	experment with color
	change zoom and view window of mandlebrot set

What I did:

	I genrated three distinct random coefficents for rd, gr, bl, and printed them out
	each time I ran the code so that if I liked the color scheme of the image, then I
	could just use those integers as the coefficient. While my final code just uses integer
	coefficent, this image was made possible by using random numbers and recording their values.

Here is what the code looked like before I found a color scheme that I liked:

	for row in range(HEIGHT):
	    for col in range(WIDTH):
	        c = complex(xmin + (xmax - xmin) * col / WIDTH, ymin + (ymax - ymin) * row / HEIGHT)
	        z = complex(-0.0, -0.0)
	        # r = mandelbrot(z, c, 0)
	        r = mandelbrotloop(z, c)

	        
	        rd = hex((r*19)%255)[2:].zfill(2)
	        gr = hex((256*0)%255)[2:].zfill(2)
	        bl = hex((255*108)%255)[2:].zfill(2)
	        
	        img.put("#" + rd + gr + bl, (col, row))


	print(redrandom)
	print(greenrandom)
	print(bluerandom)


Some more good random color combinaitons I found:

254 178 221

255 31 90

95 5 169
"""



xmin = 0.25484
xmax = 0.25485
ymin = -0.0005745
ymax = -0.0005645

window2 = Toplevel()
canvas2 = Canvas(window2, width = WIDTH, height = HEIGHT, bg = "#000000")
img2 = PhotoImage(width = WIDTH, height = HEIGHT)
canvas2.create_image((0, 0), image = img2, state = "normal", anchor = tkinter.NW)

quadvar = 0
quadconstant = 300000

#quadvar = 1 + quadvar
#quadvar = (-1** quadvar)
#quadconstant = quadconstant - 1
#quadco = int(((3*quadvar)**3))


for row in range(HEIGHT):
	for col in range(WIDTH):
		
		c = complex(xmin + (xmax - xmin) * col / WIDTH, ymin + (ymax - ymin) * row / HEIGHT)
		z = complex(-0.0, -0.0)
		# r = mandelbrot(z, c, 0)
		r = mandelbrotloop(z, c)



		quadco = (r*r) - (r)

		cosine = math.cos(r)

		logarithmic = math.log(r)



		rd = hex(int((2*r*(r)))%255)[2:].zfill(2)
		gr = hex(int((quadco))%180)[2:].zfill(2)
		bl = hex(int((logarithmic*r*cosine))%255)[2:].zfill(2)
		img2.put("#" + rd + gr + bl, (col, row))

canvas2.pack()


"""
These are the main changes I made: 

	experment with color
	change zoom and view window of mandlebrot set

What I did:

	experiemnted with colors of rd, gr, and bl by experimenting
	with r (subtracting it, adding it, squaring it, etc.) and experimenting with 
	multiplicaiton coefficients. I landed on a combination of coefficients that results in a 
	very compelling set of colors with very intersting contrasts, namely the green.
	With two of my coefficients, I experimented with the pythons cosine and log, since the values of these fucntions change in unique ways.
	With my other coefficient, I just deicided to use a quadratic function of r, since r seems to have a large impact on the image and quadrartics are cool and smooth.
	experimented extensively with the zoom and view window of mandlebrot set and adjusted decimal place by decimal place to land on a cool spot.
"""



xmin = -2
xmax = 2
ymin = -2
ymax = 2



window3 = Toplevel()
canvas3 = Canvas(window3, width = WIDTH, height = HEIGHT, bg = "#000000")
img3 = PhotoImage(width = WIDTH, height = HEIGHT)
canvas3.create_image((0, 0), image = img3, state = "normal", anchor = tkinter.NW)

smooth = 9999
crazy = 9000000
x=-.9999

for row in range(HEIGHT):
	for col in range(WIDTH):

		smooth = smooth + 150
		texture = int((smooth**.28))
		crazy = crazy - 2
		socrazy = int(crazy/(1-.98))
		c = complex(xmin + (xmax - xmin) * col / WIDTH, ymin + (ymax - ymin) * row / HEIGHT)
		z = complex(-0.0, -0.0)
		# r = mandelbrot(z, c, 0)
		r = mandelbrotloop(z, c)

		while x in range (-1,1):
			x=x+.003
		rd = hex(int((r*(x*texture))%255))[2:].zfill(2)
		gr = hex((4**texture)%255)[2:].zfill(2) #sosmoove
		bl = hex(((205+r)*socrazy)%255)[2:].zfill(2) #socrazy
		img3.put("#" + rd + gr + bl, (col, row))

canvas3.pack()


"""
These are the main changes I made: 

	experment with color
	change zoom and view window of mandlebrot set

What I did:

	experiemnted with colors of rd, gr, and bl. 
	I created a coefficient that got smaller (due to an exponetial function with exponent less that 1) each time the loop ran.
	I used this to create cool horizontal lines to create an old TV set effect thing.
	I did a sort of aysmptotic coefficient that got smaller every time becasue I reduced the numerator arithmetically each time in the loop.
	I used x in a seperate loop just to make an intersting coefficient to couple with the other two coefficients described above.
	The achieved effect took more than two hours of experiemnting with different math functions and these coefficients.
	I also experimented with the zoom and view window of mandlebrot set, concluding that to best dispay this effect, the simple window of domain and range (-1,1) was the best one.
	With this image, I basically created variables that changed geometrically and arithmetically and didn't use predeifned functions.
"""

mainloop()