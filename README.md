# CHMR
# Projectile motion 
Funtionality to study projectile motion.

## Tutorial
In this tutorial we will see how to use some of the funcutions of `projectiles` to study projectile motion.

Consider the following problem:

An object is launched at a velocity of $20 m/s$ in a direction making an angle of $25°$ upward with the horizontal.

    a) What is the maximum height reached by the object?
    b) What is the total flight time (between launch and touching the ground) of the object?
    c) What is the horizontal range (maximum x above ground) of the object?

First we import the relevent library.
```python
import projectiles as pjt
```
In order, to calculate the maximum height we will have to convert the angle given to radians as followed:
```python
>>> angle_in_radians = pjt.convert_degrees_to_radians(angle_in_degrees = 25)
>>> angle_in_radians
    0.4363323129985824
```

Since,we have the initial velocity and, now, the angle in radians. We can calculate the maxiumum height using the `maximum_height` function in `projectiles`. 
```Python
>>> time_at_maximum_height = pjt.time_at_maximum_height(
    initial_velocity = 20,
     angle = angle_in_radians
    )
```
This gives us:
``` python
>>> time_at_maximum_height
 0.862486248450407 s
```
Solving the first part a) of the problem.

In order to solve the part b) of the problem, we use the `time_of_flight` function in `Projectiles`. We know the inital velocity $20m/s$ and angle (`angle_in_radians`).

Running the following funtion will give us:
```python
>>> time_of_flight = pjt.time_of_flight(
    initial_veolcity = 20,
    angle = angle_in_radians
    )
>>> time_of_flight 
    1.724972496900814 s
```
To solve part c) of the problem we use the `horizontal_range`  function. The initial velocity and angle is the same. We calaculate the horizontal range by doing the following:
```python 
>>> horizontal_range = pjt.horizontal_range(
    inital_velcity = 20,
    angle = angle_in_radians
    )
>>> horizontal_range
    31.267120127305226 m
```

## How to guides

###  How to convert degrees into radians

Given an angle in degrees, we can obtain the corresponding angle in radians using the following `projectiles.convert_degrees_to_radians` function.
```python
>>> import projectiles as pjt
>>> pjt.convert_degrees_to_radians(angle_in_degrees = 60)
    1.0471975511965976
```

### How to compute time at maximum height
Given the initial velocity in $m/s$ and the angle in radians, we can compute the time at maximum height as follows:
```python
>>> import projectiles as pjt
>>> pjt.time_at_maximum_height(initial_velocity = 20,angle = 1.05)
    1.7702514808041159 s
```
### How to compute maximum height
Given the initial velocity in $m/s$ and the angle in radians, we can calculate the time at maximum height the following way:
```python
>>> import projectiles as pjt
>>> pjt.maximum_height(initial_velocity = 20,angle = 1.05)
    15.35557249591691 m
```

### How to compute time of flight
Given the initial velocity in $m/s$ and the angle in radians, we can compute the time of flight using the following method:
```python
>>> import projectiles as pjt
>>> pjt.time_of_flight(initial_velocity = 20,angle = 1.05)
    3.5405029616082317 s
```
### How to compute horizontal range
Given the initial velocity in $m/s$ and the angle in radians, we can compute the horizontal as followed:
```python
>>> import projectiles as pjt
>>> pjt.horizontal_range(initial_velocity = 20,angle = 1.05)
    35.23303537342342 m
```
### How to plot the projectile motion graph
Given the initial velocity in $m/s$ and the angle in radians, we can obtain a graph of the whole motion to visualies the dispacement of both axis using the following:
```python
>>> import projectiles as pjt
>>> pjt.plot_projectile_motion(initial_velocity = 20,angle = 1.05)
```
This gives us the following graph:

![projectile motion graph](https://i.ibb.co/q9yrjFp/Screenshot-2022-05-08-at-02-46-23.png)

## Explantion

### Converting degrees to radians
The library `numpy` in `projectiles` is used to find sine of an angle, therefore the angle must be in radians. Since $2π$ is equivalent to $360°$, to convert the angle in degrees to radians we multiply the angle by the following:
$$
\frac{π}{180}
$$
which gives the corresponding angle in radians.

### Overview of the motion in plane of the projectile.

When an object is projected at an angle, it moves simtaniously in the vertial and horizontal direction. 


The vertical velocity is given by:
$$
 Vy = V0sinθ
$$
denoted as $Vy$.

THe horizontal velocity is given by:
$$
Vx = V0cosθ
$$
denoted as $Vx$.

Where $V0$ is the inital velocity at an angle and $θ$ is the angle from the horizon in radians.

As we are working in a drag free enviroment, the only for acting on the partical is gravity $g$, can be aproximated by $9.8 m/s ^ 2.$

For projectile motion, we are able to calculate the following:

- The time is taken to reach from start to end point.
- The time taken to reach maximum height.
- The maximum height reached during the motion.
- The horizontal distance covered from start to end point.


  

The time taken to reach maximum height is calculated by:
$$
t = \frac{Vy * sinθ}{g}
$$
where, $Vy$ is the vertial component of the inital velocity, $θ$ is the angle from the horizon in radians and $g$ is the accelration due to gravity.


The time is taken to reach from start to end point is calculated by: 
$$ 
 t0=2\frac{Vy * sinθ}{g}
$$
where, $Vy$ is the vertial component of the inital velocity, $θ$ is the angle from the horizon in radians and $g$ is the accelration due to gravity.Given that the particle is projected at ground level.

The maximum height reached during the motion in calculated by:
$$ 
V0sinθ * t - \frac{g * t ^ 2}{2}
$$
where $t$ is the time taken to reach maximum height, $V0$ is the inital velocity, $θ$ is the angle from the horizon in radians and $g$ is the accelration due to gravity.

The horizontal distance covered from start to end point is calculated by:
$$ 
\frac{V0 ^ 2 sin2θ}{g}
$$
where, $V0$ is the inital velocity, $θ$ is the angle from the horizon in radians and $g$ is the accelration due to gravity.



## Reference
### List of functionailty
The following is a list of functions written in `projetiles` using the input taken in breakets.
- angle_in_radians(angle_in_degrees)
- time_at_maximum_height(initial_velocity, angle)
- time_of_flight(initial_velocity, angle)
- maximum_height(initial_velocity, angle)
- horizontal_range
- plot_projectile_motion

## Bibliography
For some background information of projectile motion we recommend the following:
- Projectile motion in 2D https://www.khanacademy.org/science/physics/two-dimensional-motion/two-dimensional-projectile-mot/a/what-is-2d-projectile-motion
  
- Maximum height formula: https://dewwool.com/maximum-height-of-a-projectile-formula/

- 
