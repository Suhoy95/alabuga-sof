import turtle

def draw_L_system(axiom,
                  rule,
                  depth,
                  delta_angle,
                  length):
    checkpoints = []
    t = turtle.Pen()
    t.left(90)

