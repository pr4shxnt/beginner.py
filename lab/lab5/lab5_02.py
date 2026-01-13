import math

origin = (0, 0)

def get_next_point(step):
    """Get the next point coordinates from user input."""
    x = int(input(f"x{step}: "))
    y = int(input(f"y{step}: "))
    return (x, y)

def cal_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    x1, y1 = p1
    x2, y2 = p2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def main():
    """Run the robot program."""
    print("------ Robot Program ------")
    
    current_point = origin
    step = 1
    
    while True:
        print(f" ---------- Step {step} ----------")
        next_point = get_next_point(step)
        
        if next_point == (999, 999):
            print("Robot reached destination (999, 999). Program ended.")
            break
        
        distance = cal_distance(current_point, next_point)
        print(f"Distance moved: {distance:.2f}")
        
        current_point = next_point
        step += 1

if __name__ == "__main__":
    main()
