

def print_info(obj_name: str, var: object, operation: str) -> None:
    print('=' * 79)
    print(f"{obj_name} -> Type: {type(var)}, ID: {id(var)}, Value: {var} <--- After {operation}")

def mutability_test(immutable_var: int, mutable_var: list) -> None:
    immutable_var += 1
    mutable_var.append(5)
    print(f"   immutable_var = {immutable_var}, mutable_var = {mutable_var}")

if __name__ == "__main__":

    ##### IMMUTABLE ############################################################
    print("/" * 79)
    print("IMMUTABLE - INT")
    print("/" * 79)

    i = 1
    print_info("i", i, "i = 1")

    i = i + 1 # <--- i points to a new object
    print_info("i", i, "i = i + 1")

    j = i  # <--- J points to same object as i
    print_info("j", j, "j = i")

    i = i + 1
    print_info("i", i, "i = i + 1")

    print_info("j", j, "No operation on j")  # <--- j points to the object of value 2

    print('=' * 79)

    ##### MUTABLE ############################################################
    print()
    print("/" * 79)
    print("MUTABLE - LIST")
    print("/" * 79)

    i = [1]
    print_info("i", i, "i = [1]")

    i.append(2) # <--- i points to same object
    print_info("i", i, "i.append(2)")

    j = i  # <--- j points to same object as i
    print_info("j", j, "j = i")

    i.append(3) # <--- i points to same object
    print_info("i", i, "i.append(3)")

    print_info("j", j, "No operation on j") # j points to the same object as i

    print('=' * 79)

    ##### (IM)MUTABLE TEST ####################################################
    print()

    immutable_var = 1
    mutable_var = [1, 2, 3]
    
    print("=" * 79)
    print("BEFORE mutability_test")
    print("=" * 79)
    print(f"   immutable_var = {immutable_var}, mutable_var = {mutable_var}")
    print()

    print("=" * 79)
    print("IN mutability_test")
    print("=" * 79)
    mutability_test(immutable_var, mutable_var)
    print()

    print("=" * 79)
    print("AFTER mutability_test")
    print("=" * 79)
    print(f"   immutable_var = {immutable_var}, mutable_var = {mutable_var}")
    print()
    