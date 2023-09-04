from dataclasses import dataclass

from app.flow.node import Node


@dataclass
class Flow:
    id: str
    nodes: [Node]
