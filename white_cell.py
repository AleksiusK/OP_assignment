import math
from decimal import *
getcontext().prec = 10

## Using the decimal again for this, as it's quite easy way to work
## around the floating point errors.

def white_cell_bounces(x1 : Decimal, x2: Decimal, y1: Decimal, y2: Decimal):
    """
    This function calculates the number of bounces for the given white cell with the equation 4x**2 + y**2 = 100.
    Takes in the coordinates of the incoming line and the first point where the line intersects the ellipse (x2, y2).
    Updates the coordinates based on the laser reflection function, and ends when the exit point is reached.
    """
    # Get the slope for the first line. Return 1 if there is no change in x direction, as this means
    # the line is vertical and thus bounces back
    bounces = 1
    # Initialize the default values for the ellips
    while (x2 < -0.01 or x2 > 0.01) and y2 < 10.01:
        x1, x2, y1, y2 = laser_reflection(x1, x2, y1, y2)
        # For debugging purposes: check if the coordinates have not changed.
        if (round(x2, 5) == round(x1, 5)) and (round(y2, 5) == round(y1, 5)):
            print(f"An error in the code: ({round(x2, 2)}, {round(y2,2)})")
            print(f"On iteration: {bounces}")
            raise ValueError
        bounces += 1

    return bounces

def laser_reflection(x1: Decimal, x2: Decimal, y1: Decimal, y2: Decimal):

    # Tangent to ellipse. Notice that this is not a general equation, as the
    # task was to work with only the 4x**2 + y**2 = 100 ellipse.
    tangent_slope = -4 * (x2 / y2)
    # Deflection on sloping mirror y = mx + c.

    # If the incoming line is vertical, the slope cannot be defined. Thus, check for this- otherwise, the results
    # will be incorrect. Originally noticed this while testing, as there seemed to be "double values", e.g. the coordinates
    # did not change between two bounces.
    if round(x2 - x1, 5) != 0:
        
        # Slope for the incoming line
        k1 = (y2 - y1) / (x2 - x1)
        k2 = Decimal(math.tan(Decimal(math.pi) - Decimal(math.atan(k1)) + 2 * Decimal(math.atan(tangent_slope))))
    else:
        # Incase the incoming line is vertical, the reflection angle is defined as the angle between the slope of the tangent
        # and the x- axis.
        k2 = Decimal(math.tan(Decimal(math.pi) - 2 * Decimal(math.atan(tangent_slope))))
    # Define the rest of the line's equation.
    b = y2 - k2 * x2
    # If we input the equation of the line to the equation of the ellipse (4x**2 + (kx + b)**2 = 100), we get a quadratic equation, shown below.
    x2_1 = -(2 * Decimal(math.sqrt(25 * (k2**2 + 4) - b**2)) + b*k2) / (k2**2 + 4)
    x2_2 = (2 * Decimal(math.sqrt(25 * (k2**2 + 4) - b**2)) - b*k2) / (k2**2 + 4)
    # Switch the x1 and x2 coordinates
    x1 = x2
    y1 = y2
    # Re- define the x2 and y2 coordinates by determining the intersection point. The line will intersect the ellipse at two points, one being the x1 y1 coordinate. We check for
    # equality on this basis and choose the other point.
    if round(x1 - x2_1, 5) == 0:
        x2 = x2_2
    else:
        x2 = x2_1
    # y2 is defined by the line's equation
    y2 = k2 * x2 + b

    return x1, x2, y1, y2




print(white_cell_bounces(Decimal(0.0), Decimal(1.4), Decimal(10.1), Decimal(-9.6)))
