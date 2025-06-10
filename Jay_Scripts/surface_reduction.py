import numpy as np

def create_simple_cylinder_stl(radius=0.5, height=1.0, num_segments=20, filename="valid_cylinder.stl"):
    """
    Create a simple cylinder STL file with the given dimensions.
    """
    # Create vertices for top and bottom circles
    theta = np.linspace(0, 2*np.pi, num_segments, endpoint=False)
    
    # Points on bottom circle
    bottom_circle = np.zeros((num_segments, 3))
    bottom_circle[:, 0] = radius * np.cos(theta)
    bottom_circle[:, 1] = radius * np.sin(theta)
    bottom_circle[:, 2] = 0
    
    # Points on top circle
    top_circle = np.zeros((num_segments, 3))
    top_circle[:, 0] = radius * np.cos(theta)
    top_circle[:, 1] = radius * np.sin(theta)
    top_circle[:, 2] = height
    
    # Create STL file
    with open(filename, 'w') as f:
        f.write("solid SimpleCylinder\n")
        
        # Create bottom cap
        for i in range(num_segments):
            i_next = (i + 1) % num_segments
            f.write("  facet normal 0 0 -1\n")
            f.write("    outer loop\n")
            f.write(f"      vertex 0 0 0\n")
            f.write(f"      vertex {bottom_circle[i_next, 0]} {bottom_circle[i_next, 1]} {bottom_circle[i_next, 2]}\n")
            f.write(f"      vertex {bottom_circle[i, 0]} {bottom_circle[i, 1]} {bottom_circle[i, 2]}\n")
            f.write("    endloop\n")
            f.write("  endfacet\n")
        
        # Create cylinder wall
        for i in range(num_segments):
            i_next = (i + 1) % num_segments
            normal_x = np.cos(theta[i] + np.pi/num_segments)
            normal_y = np.sin(theta[i] + np.pi/num_segments)
            
            f.write(f"  facet normal {normal_x} {normal_y} 0\n")
            f.write("    outer loop\n")
            f.write(f"      vertex {bottom_circle[i, 0]} {bottom_circle[i, 1]} {bottom_circle[i, 2]}\n")
            f.write(f"      vertex {bottom_circle[i_next, 0]} {bottom_circle[i_next, 1]} {bottom_circle[i_next, 2]}\n")
            f.write(f"      vertex {top_circle[i_next, 0]} {top_circle[i_next, 1]} {top_circle[i_next, 2]}\n")
            f.write("    endloop\n")
            f.write("  endfacet\n")
            
            f.write(f"  facet normal {normal_x} {normal_y} 0\n")
            f.write("    outer loop\n")
            f.write(f"      vertex {bottom_circle[i, 0]} {bottom_circle[i, 1]} {bottom_circle[i, 2]}\n")
            f.write(f"      vertex {top_circle[i_next, 0]} {top_circle[i_next, 1]} {top_circle[i_next, 2]}\n")
            f.write(f"      vertex {top_circle[i, 0]} {top_circle[i, 1]} {top_circle[i, 2]}\n")
            f.write("    endloop\n")
            f.write("  endfacet\n")
        
        # Create top cap
        for i in range(num_segments):
            i_next = (i + 1) % num_segments
            f.write("  facet normal 0 0 1\n")
            f.write("    outer loop\n")
            f.write(f"      vertex 0 0 {height}\n")
            f.write(f"      vertex {top_circle[i, 0]} {top_circle[i, 1]} {top_circle[i, 2]}\n")
            f.write(f"      vertex {top_circle[i_next, 0]} {top_circle[i_next, 1]} {top_circle[i_next, 2]}\n")
            f.write("    endloop\n")
            f.write("  endfacet\n")
        
        f.write("endsolid SimpleCylinder")
    
    print(f"Created cylinder STL file with {num_segments*4} faces at: {filename}")
    return filename

if __name__ == '__main__':
    # Create a cylinder with 20 segments (80 faces total)
    create_simple_cylinder_stl(radius=0.5, height=1.0, num_segments=20, filename="valid_cylinder.stl")