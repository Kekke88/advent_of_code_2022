from dataclasses import dataclass, field

@dataclass
class Terminal:
    tree: dict = field(default_factory=dict)
    cwd: str = "/"
    TOTAL_DISKSPACE: int = 70000000
    UPDATE_SIZE: int = 30000000

    def go(self, dir: str):
        if dir == "..":
            for i in range(len(self.cwd)-2, -1, -1):
                if self.cwd[i] == "/":
                    self.cwd = self.cwd[:i+1]
                    if self.cwd == "": self.cwd = "/"
                    break
        elif dir == "/":
            self.cwd = "/"
        else:
            self.cwd += f"{dir}/"

    def add_size_to_previous_folders(self, file_size: int):
        cwd = self.cwd
        while cwd != "/":
            for i in range(len(cwd)-2, -1, -1):
                if cwd[i] == "/":
                    cwd = cwd[:i+1]
                    if not cwd in self.tree:
                        self.tree[cwd] = 0
                    self.tree[cwd] += file_size
                    if cwd == "": cwd = "/"
                    break

    def index_file(self, file_size: int):
        if not self.cwd in self.tree:
            self.tree[self.cwd] = 0
        self.tree[self.cwd] += file_size
        self.add_size_to_previous_folders(file_size)

    def parse(self, line: str):
        if line[0] == "$":
            command = line.split(" ")

            if command[1] == "cd":
                self.go(command[2])
        else:
            content = line.split(" ")
            if content[0] != "dir":
                self.index_file(int(content[0]))

    def get_disk_space(self) -> int:
        return self.TOTAL_DISKSPACE - self.tree["/"]

    def get_deletion_size(self) -> int:
        available = list()
        needed_space = self.UPDATE_SIZE - self.get_disk_space()

        for folder_size in self.tree.values():
            if folder_size >= needed_space:
               available.append(folder_size)

        return sorted(available)[0]

    def get_total_sum(self, treshold: int = 100000) -> int:
        sum = 0

        for folder_size in self.tree.values():
            if folder_size <= treshold:
                sum += folder_size

        return sum