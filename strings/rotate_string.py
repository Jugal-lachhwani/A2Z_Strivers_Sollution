def rotateString(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False  
    doubled_s = s + s  # Concatenate s with itself
    return goal in doubled_s  # Check if goal is a substring of s + s
        
print(rotateString("rotation", "tionrota"))
