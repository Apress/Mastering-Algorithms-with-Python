import math
import matplotlib.pyplot as plt
plt.figure()
def draw_line(x1, y1, x2, y2):
    plt.plot([x1, x2], [y1, y2], color = 'r', lw = 2)

def draw_h_tree(x0, y0, length, level, factor):
    if level == 0:
        return

    coord_c_x = x0 - length / 2.
    coord_c_y = y0
    coord_d_x = x0 + length / 2.
    coord_d_y = y0

    coord_a_x = x0 - length / 2.
    coord_a_y = y0 + length / 2.
    coord_e_x = x0 - length / 2.
    coord_e_y = y0 - length / 2.
    coord_b_x = x0 + length / 2.
    coord_b_y = y0 + length / 2.
    coord_f_x = x0 + length / 2.
    coord_f_y = y0 - length / 2.
    
    draw_line(coord_c_x, coord_c_y, coord_d_x, coord_d_y)
    draw_line(coord_a_x, coord_a_y, coord_e_x, coord_e_y)
    draw_line(coord_b_x, coord_b_y, coord_f_x, coord_f_y)

    length /= math.sqrt(factor)
    level -= 1
    draw_h_tree(coord_a_x, coord_a_y, length, level, factor)
    draw_h_tree(coord_b_x, coord_b_y, length, level, factor)
    draw_h_tree(coord_e_x, coord_e_y, length, level, factor)
    draw_h_tree(coord_f_x, coord_f_y, length, level, factor)

if __name__ == "__main__":
   draw_h_tree(0, 0, 2, 5, 4)
   plt.tight_layout()
   plt.show()
