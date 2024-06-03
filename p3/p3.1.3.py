def raise_stop_iteration():
    iterator = iter([])
    next(iterator)

def raise_zero_division_error():
    result = 1 / 0

def raise_assertion_error():
    assert False, "This is an AssertionError"

def raise_import_error():
    import non_existent_module

def raise_key_error():
    my_dict = {}
    value = my_dict['non_existent_key']

def raise_syntax_error():
    eval('x === x')

def raise_indentation_error():
    if True:
    print("This will cause IndentationError")


def raise_type_error():
    result = 'string' + 5

# Test the functions
try:
    raise_stop_iteration()
except StopIteration as e:
    print(f"Caught an exception: {e}")

try:
    raise_zero_division_error()
except ZeroDivisionError as e:
    print(f"Caught an exception: {e}")

try:
    raise_assertion_error()
except AssertionError as e:
    print(f"Caught an exception: {e}")

try:
    raise_import_error()
except ImportError as e:
    print(f"Caught an exception: {e}")

try:
    raise_key_error()
except KeyError as e:
    print(f"Caught an exception: {e}")

try:
    raise_syntax_error()
except SyntaxError as e:
    print(f"Caught an exception: {e}")

try:
    raise_indentation_error()
except IndentationError as e:
    print(f"Caught an exception: {e}")

try:
    raise_type_error()
except TypeError as e:
    print(f"Caught an exception: {e}")