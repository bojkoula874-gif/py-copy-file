def copy_file(task: str) -> None:
    paths_files = task.split(" ")
    if len(paths_files) != 3:
        return
    if paths_files[0] == "cp":
        try:
            with (open(paths_files[1], "r") as f1,
                  open(paths_files[-1], "w") as f2):
                for line in f1.readlines():
                    f2.write(line)
        except FileNotFoundError:
            return
