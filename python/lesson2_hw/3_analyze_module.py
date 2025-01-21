import inspect


def analyze_module(module_name: str):
    """
    Analyzes the given Python module by inspecting its functions and classes.
    """

    try:
        imported_module = __import__(module_name)
    except ImportError:
        print(f"Module with name {module_name} was not found")
        return

    print("Functions:")
    for name, member in inspect.getmembers(imported_module, inspect.isroutine):
        if not name.startswith("_"):
            try:
                signature = inspect.signature(member)
                formatted_signature = ", ".join(
                    param.name for param in signature.parameters.values()
                )
                print(f"- {name}({formatted_signature})")
            except ValueError:
                print(f"- {name}()")

    print("\nClasses:")
    class_found = False
    for name, member in inspect.getmembers(imported_module, inspect.isclass):
        if not name.startswith("_"):
            class_found = True
            try:
                init_method = getattr(member, "__init__", None)
                if init_method and callable(init_method):
                    signature = inspect.signature(init_method)
                    formatted_signature = ", ".join(
                        param.name for param in signature.parameters.values()
                        if param.name != "self"
                    )
                    print(f"- {name}({formatted_signature})")
                else:
                    print(f"- {name}()")
            except ValueError:
                print(f"- {name}()")
    if not class_found:
        print(f"- <There are no classes in module {module_name}>")


analyze_module("math")
