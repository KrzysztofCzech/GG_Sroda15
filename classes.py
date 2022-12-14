from dataclasses import dataclass
import enum

@dataclass
class Node:
    id : int
    label: str
    level: int = 0
    x: float = None
    y: float = None

    def graph_adapter(self):
        return (self.id, dict(label = self.label, x = self.x, y = self.y, level = self.level))

class Attr_MAP:
    x = "x"
    y = "y"
    label = "label"
    level = "level"
    