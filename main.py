def CIFRE(a, b, log=True, max_iterations=99999):
    """CIFOE (Chaotic Inverse Fractional Reverse Exponential). A chaotic two number generator"""
    if a == 0 or b == 0:
        raise ValueError("a and b must be non-zero values.")
    def show(text):
        if log:
            print(text)
        else:
            pass
    c = a * b
    T = 0
    show(f"Initial values: a = {a}, b = {b}, c = a * b = {c}")
    b2 = (a / b) ** (b / a)  
    a2 = 1 / b2
    T += a2  
    show(f"First calculation: b2 = (a / b) ^ (b / a) = {b2}")
    show(f"a2 = 1 / b2 = {a2}")
    show(f"T = {T}")
    iteration = 2
    while T <= c and iteration <= max_iterations:
        show(f"\nIteration {iteration}:")
        b2 = (a2 / b2) ** (b / a)  
        a2 = 1 / b2
        show(f"b2 = (a2 / b2) ^ (b / a) = {b2}")
        show(f"a2 = 1 / b2 = {a2}")
        T += a2 
        show(f"T = {T}")
        if T > c and round(T) == c:
            T_str = f"{T:.10f}"  
            fractional_part = T_str.split('.')[1][:3] 
            fractional_value = int(fractional_part)  
            if fractional_value != 0: 
                show(f"Rounded T is equal to C. Dividing T by {fractional_value}.")
                T /= fractional_value   
            break
        iteration += 1
    if iteration > max_iterations:
        show("Terminated due to reaching the maximum number of iterations.")
    
    return T

print(CIFRE(4,5, False))