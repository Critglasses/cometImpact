# CometImpact
A simulation of heat diffusion after a comet impacts the earth

The program creates a mesh-grid which is given inital conditions for "heat" and "diffusivity" in each "layer". The layers themselves signify the different depths in the Earth, which have different values for diffusivity, with the last layer signifying outer space. 

After the meshgrid is created, a "comet" or an object of certain size and temperature at a certain position on the mesh-grid is formed. The position determines where the heat will diffuse from, which in the case places it at the edge of the earths last layer. 

This comet's heat diffusing into the earth is animated with the **`animation.FuncAnimation`** function, which calls the **'animate'** function for each frame of the animation. The **'animate'** function updates the values for the heat from the comet for each frame, which radiates out in a circular manner, eventually slowing down due to added exponential term **'np.exp(-1e-17 * t)'**. 

The animation is then showed over a timespan specified by the amount of frames in the animation.FuncAnimation function.


