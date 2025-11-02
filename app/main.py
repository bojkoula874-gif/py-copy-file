def copy_file(task: str) -> None:
    paths_files = task.split(" ")
    if paths_files[0] == "cp":
        with open(paths_files[1], "r") as f1, open(paths_files[-1], "w") as f2:
            for line in f1.readlines():
                f2.write(line + "\n")
