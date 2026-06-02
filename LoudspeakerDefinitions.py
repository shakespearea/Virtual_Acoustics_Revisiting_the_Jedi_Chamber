from dataclasses import dataclass
@dataclass
class Bandwidth:
    min: int
    max: int

@dataclass
class Dimensions:
    w: int
    h: int
    d: int

@dataclass
class Loudspeaker: 
    SPL_max: int
    bw: Bandwidth
    d: Dimensions

l1 = Loudspeaker(SPL_max = 160,
                 bw = Bandwidth(min = 35, max = 20000),
                 d = Dimensions(w = 1500, h = 1005, d = 750)
                 )
