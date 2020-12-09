class KeyValueStorage:
    def __init__(self, file_name):
        self.__dict__["file_name"] = file_name
        with open(file_name, "r") as fi:
            file = fi.readlines()
            for line in file:
                key, value = line.strip().split("=")
                try:
                    value = int(value)
                except ValueError:
                    pass
                if not (self.__dict__.get(key) or str(key).startswith("__")):
                    self.__dict__.update({key: value})

    def __setattr__(self, key, value):
        if isinstance(key, (int, float)):
            raise ValueError("Key should be a hashable")
        if not (self.__dict__.get(key) or str(key).startswith("__")):
            self.__dict__.update({key: value})
            with open(self.file_name, "a") as fi:
                fi.writelines(f"{key}={value}\n")
