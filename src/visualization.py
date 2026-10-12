import matplotlib.pyplot as plt

def show_grid(grid, path, start, goal):
    plt.figure()

    # show grid
    plt.imshow(grid, cmap='gray')

    # start point (green)
    plt.scatter(start[1], start[0], color='green', s=100, label='Start')

    # goal point (red)
    plt.scatter(goal[1], goal[0], color='red', s=100, label='Goal')

    # path line (blue)
    if path and len(path) > 0:
        x = [p[1] for p in path]
        y = [p[0] for p in path]
        plt.plot(x, y, color='blue', linewidth=2, label='Path')

    plt.title("AI-Based Autonomous Navigation System (A* Grid)")
    plt.legend()
    plt.show()