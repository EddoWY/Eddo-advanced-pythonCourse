def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return f"__CONTENT_START__\n{content}\n__CONTENT_END__"
    except FileNotFoundError:
        return "__CONTENT_START__\n__NO_SUCH_FILE__\n__CONTENT_END__"
    except Exception as e:
        return f"__CONTENT_START__\n__ERROR__: {e}\n__CONTENT_END__"
    finally:
        print(f"Attempted to read file: {file_name}")


print(read_file("existing_file.txt"))
print(read_file("file_does_not_exist.txt"))
