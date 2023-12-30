import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy as sp

fig = plt.figure()
num = 200 #Number of pixels and calculated values in meshgrid
L = 7000e3 #Size of graph and so on
ax = plt.axes(xlim=(0, L), ylim=(0, L))
x = y = np.linspace(0, L, num = num) #change num for pixels
x, y = np.meshgrid(x, y)
timetravel = 1e15              #Changes time-scale

u = 3e5           #Temperature of comet
rmax = 9e4           #Changes size of comet
begPos = 6.369e6/np.sqrt(2) #Position of comet impact
r = np.sqrt((x+0.001) ** 2 + (y+0.001) ** 2)
rcomet = np.sqrt((x - begPos) ** 2 + (y - begPos) ** 2) #Specific radial position

radius = [0.001, 1000e3, 3000e3, 6400e3, 6470e3,  10000e3] #Radius of temperaturezones
aEarth = np.zeros((num, num))
tempEarth = np.zeros((num, num))
a = [1e-5, 5e-5, 1e-6, 5e-6, 1e-10] #diffusivity for different layers
#a = [10, 5, 1, 2]
temp = [7000, 3800, 2000, 500,  0] #temperature for the different layers



for i in range(len(radius) - 1):  #Creates meshgrids for diffusivity and temperature of the earth and for space
   aEarth[(r >= radius[i]) & (r < radius[i + 1])] = a[i]
   tempEarth[(r >= radius[i]) & (r < radius[i + 1])] = temp[i]

z = tempEarth + (1/2)*u*(sp.special.erf((rmax - rcomet)/(np.sqrt(4*aEarth*0.001 + 0.001)))-(sp.special.erf((-rmax - rcomet)/(np.sqrt(4*aEarth*0.001 + 0.001)))))
map = ax.pcolormesh(x, y, z, vmin = 0, vmax = 1e4, shading = 'gouraud', cmap = plt.cm.jet)

def animate(count):  #Animates the comet's heat-spread
   t = count * timetravel
   z = tempEarth + ((1/2)*u*(sp.special.erf((rmax - rcomet)/np.sqrt(4*aEarth*t+1e-9))-(sp.special.erf((-rmax - rcomet)/np.sqrt(4*aEarth*t+1e-9))))) * np.exp(-1e-17 * t)
   map.set_array(z.ravel())
   ax.set_title(f'y(x) at time={round(t/(60*60*24*365*1e6), 0)} million years')
   return map,



plt.colorbar(map, label = "Temperature [Kelvin]")
plt.ylabel('y [m]')
plt.xlabel('x [m]')

anim = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit= False)  #Calls animate and creates a plot

"""fingif = animation.PillowWriter(fps = 30)
anim.save("CometImpact.gif", writer = fingif)"""  #Enable this and comment out anim to save a gif instead


#plt.show()


