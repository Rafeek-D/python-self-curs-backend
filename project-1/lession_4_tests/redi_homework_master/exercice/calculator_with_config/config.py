import pathlib
import configparser

class Config:
    def __init__(self):
        self.load_cwd()

    def __repr__(self) -> str:
        return f"Config(prompt={self.prompt!r})"

    def load(self, path: pathlib.Path) -> None:
        parser = configparser.ConfigParser()
        parser.read(path)
        self.prompt = parser["rpncalc"]["prompt"]

    def save(self, path: pathlib.Path) -> None:
        parser = configparser.ConfigParser()
        parser["rpncalc"] = {"prompt": self.prompt}
        with path.open("w") as f:
            parser.write(f)

    def load_cwd(self) -> bool:
        ini = pathlib.Path.cwd() / "rpncalc.ini"
        if ini.exists():
            self.load(ini)
            return True
        return False
    def get_prompt(self) -> str:
        return self.prompt
if __name__ == '__main__':
    config = Config()
    print(config.prompt)
    config.load_cwd()
    print(config.prompt)