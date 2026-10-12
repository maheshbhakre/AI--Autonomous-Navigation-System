from src.simulation import create_grid
from src.path_planning import astar
from src.visualization import show_grid

def main():
    # Step 1: Create environment
    grid, start, goal = create_grid(size=20, obstacle_ratio=0.2)

    # Step 2: Run path planning
    path = astar(grid, start, goal)

    # Step 3: Debug info (important for proof)
    print("Start:", start)
    print("Goal:", goal)
    print("Path Length:", len(path))

    # Step 4: Visualization
    show_grid(grid, path, start, goal)

if __name__ == "__main__":
    main()