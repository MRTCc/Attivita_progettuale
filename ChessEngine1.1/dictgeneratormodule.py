import movemodule as mvm
import algebraicnotationmodule as alg
from algebraicnotationmodule import (a8, b8, c8, d8, e8, f8, g8, h8,
                                     a7, b7, c7, d7, e7, f7, g7, h7,
                                     a6, b6, c6, d6, e6, f6, g6, h6,
                                     a5, b5, c5, d5, e5, f5, g5, h5,
                                     a4, b4, c4, d4, e4, f4, g4, h4,
                                     a3, b3, c3, d3, e3, f3, g3, h3,
                                     a2, b2, c2, d2, e2, f2, g2, h2,
                                     a1, b1, c1, d1, e1, f1, g1, h1)


class OccupationException(Exception):
    pass


class AllyOccupationException(OccupationException):
    pass


occupiedcells = []
whiteoccupiedcells = []
blackoccupiedcells = []
whitepawns = []
blackpawns = []
promotioncells = [a8, b8, c8, d8, e8, f8, g8, h8, a1, b1, c1, d1, e1, f1, g1, h1]
whiterooks = []
blackrooks = []
whiteknights = []
blackknights = []
whitebishops = []
blackbishops = []
whitequeen = []
blackqueen = []
whiteking = []
blackking = []
enpassantcells = []
whitecastlingrights = {'wk': True, 'wq': True}
castling = {'wk': [True, True], 'wq': [True, True], 'bk': [True, True],
            'bq': [True, True]}
blackcastlingrights = {'bk': True, 'bq': True}


whitepawnonestep = {a7: a8, b7: b8, c7: c8, d7: d8, e7: e8, f7: f8, g7: g8, h7: h8,
                    a6: a7, b6: b7, c6: c7, d6: d7, e6: e7, f6: f7, g6: g7, h6: h7,
                    a5: a6, b5: b6, c5: c6, d5: d6, e5: e6, f5: f6, g5: g6, h5: h6,
                    a4: a5, b4: b5, c4: c5, d4: d5, e4: e5, f4: f5, g4: g5, h4: h5,
                    a3: a4, b3: b4, c3: c4, d3: d4, e3: e4, f3: f4, g3: g4, h3: h4,
                    a2: a3, b2: b3, c2: c3, d2: d3, e2: e3, f2: f3, g2: g3, h2: h3}

whitepawntwostep = {a2: a4, b2: b4, c2: c4, d2: d4, e2: e4, f2: f4, g2: g4, h2: h4}

whitepawncapture = {a7: (None, b8), b7: (a8, c8), c7: (b8, d8), d7: (c8, e8), e7: (d8, f8), f7: (e8, g8), g7: (f8, h8),
                    h7: (g8, None),
                    a6: (None, b7), b6: (a7, c7), c6: (b7, d7), d6: (c7, e7), e6: (d7, f7), f6: (e7, g7), g6: (f7, h7),
                    h6: (g7, None),
                    a5: (None, b6), b5: (a6, c6), c5: (b6, d6), d5: (c6, e6), e5: (d6, f6), f5: (e6, g6), g5: (f6, h6),
                    h5: (g6, None),
                    a4: (None, b5), b4: (a5, c5), c4: (b5, d5), d4: (c5, e5), e4: (d5, f5), f4: (e5, g5), g4: (f5, h5),
                    h4: (g5, None),
                    a3: (None, b4), b3: (a4, c4), c3: (b4, d4), d3: (c4, e4), e3: (d4, f4), f3: (e4, g4), g3: (f4, h4),
                    h3: (g4, None),
                    a2: (None, b3), b2: (a3, c3), c2: (b3, d3), d2: (c3, e3), e2: (d3, f3), f2: (e3, g3), g2: (f3, h3),
                    h2: (g3, None)}

whitekingpawnrange = {a7: (None, b8), b7: (a8, c8), c7: (b8, d8), d7: (c8, e8), e7: (d8, f8), f7: (e8, g8),
                      g7: (f8, h8), h7: (g8, None),
                      a6: (None, b7), b6: (a7, c7), c6: (b7, d7), d6: (c7, e7), e6: (d7, f7), f6: (e7, g7),
                      g6: (f7, h7), h6: (g7, None),
                      a5: (None, b6), b5: (a6, c6), c5: (b6, d6), d5: (c6, e6), e5: (d6, f6), f5: (e6, g6),
                      g5: (f6, h6), h5: (g6, None),
                      a4: (None, b5), b4: (a5, c5), c4: (b5, d5), d4: (c5, e5), e4: (d5, f5), f4: (e5, g5),
                      g4: (f5, h5), h4: (g5, None),
                      a3: (None, b4), b3: (a4, c4), c3: (b4, d4), d3: (c4, e4), e3: (d4, f4), f3: (e4, g4),
                      g3: (f4, h4), h3: (g4, None),
                      a2: (None, b3), b2: (a3, c3), c2: (b3, d3), d2: (c3, e3), e2: (d3, f3), f2: (e3, g3),
                      g2: (f3, h3), h2: (g3, None),
                      a1: (None, b2), b1: (a2, c2), c1: (b2, d2), d1: (c2, e2), e1: (d2, f2), f1: (e2, g2),
                      g1: (f2, h2), h1: (g2, None)}

blackpawnonestep = {a7: a6, b7: b6, c7: c6, d7: d6, e7: e6, f7: f6, g7: g6, h7: h6,
                    a6: a5, b6: b5, c6: c5, d6: d5, e6: e5, f6: f5, g6: g5, h6: h5,
                    a5: a4, b5: b4, c5: c4, d5: d4, e5: e4, f5: f4, g5: g4, h5: h4,
                    a4: a3, b4: b3, c4: c3, d4: d3, e4: e3, f4: f3, g4: g3, h4: h3,
                    a3: a2, b3: b2, c3: c2, d3: d2, e3: e2, f3: f2, g3: g2, h3: h2,
                    a2: a1, b2: b1, c2: c1, d2: d1, e2: e1, f2: f1, g2: g1, h2: h1}

blackpawntwostep = {a7: a5, b7: b5, c7: c5, d7: d5, e7: e5, f7: f5, g7: g5, h7: h5}

blackpawncapture = {a7: (None, b6), b7: (a6, c6), c7: (b6, d6), d7: (c6, e6), e7: (d6, f6), f7: (e6, g6), g7: (f6, h6),
                    h7: (g6, None),
                    a6: (None, b5), b6: (a5, c5), c6: (b5, d5), d6: (c5, e5), e6: (d5, f5), f6: (e5, g5), g6: (f5, h5),
                    h6: (g5, None),
                    a5: (None, b4), b5: (a4, c4), c5: (b4, d4), d5: (c4, e4), e5: (d4, f4), f5: (e4, g4), g5: (f4, h4),
                    h5: (g4, None),
                    a4: (None, b3), b4: (a3, c3), c4: (b3, d3), d4: (c3, e3), e4: (d3, f3), f4: (e3, g3), g4: (f3, h3),
                    h4: (g3, None),
                    a3: (None, b2), b3: (a2, c2), c3: (b2, d2), d3: (c2, e2), e3: (d2, f2), f3: (e2, g2), g3: (f2, h2),
                    h3: (g2, None),
                    a2: (None, b1), b2: (a1, c1), c2: (b1, d1), d2: (c1, e1), e2: (d1, f1), f2: (e1, g1), g2: (f1, h1),
                    h2: (g1, None)}

blackkingpawnrange = {a8: (None, b7), b8: (a7, c7), c8: (b7, d7), d8: (c7, e7), e8: (d7, f7), f8: (e7, g7),
                      g8: (f7, h7), h8: (g7, None),
                      a7: (None, b6), b7: (a6, c6), c7: (b6, d6), d7: (c6, e6), e7: (d6, f6), f7: (e6, g6),
                      g7: (f6, h6), h7: (g6, None),
                      a6: (None, b5), b6: (a5, c5), c6: (b5, d5), d6: (c5, e5), e6: (d5, f5), f6: (e5, g5),
                      g6: (f5, h5), h6: (g5, None),
                      a5: (None, b4), b5: (a4, c4), c5: (b4, d4), d5: (c4, e4), e5: (d4, f4), f5: (e4, g4),
                      g5: (f4, h4), h5: (g4, None),
                      a4: (None, b3), b4: (a3, c3), c4: (b3, d3), d4: (c3, e3), e4: (d3, f3), f4: (e3, g3),
                      g4: (f3, h3), h4: (g3, None),
                      a3: (None, b2), b3: (a2, c2), c3: (b2, d2), d3: (c2, e2), e3: (d2, f2), f3: (e2, g2),
                      g3: (f2, h2), h3: (g2, None),
                      a2: (None, b1), b2: (a1, c1), c2: (b1, d1), d2: (c1, e1), e2: (d1, f1), f2: (e1, g1),
                      g2: (f1, h1), h2: (g1, None)}

knightstep = {a8: (c7, b6), b8: (d7, c6, a6), c8: (e7, d6, b6, a7), d8: (f7, e6, c6, b7), e8: (g7, f6, d6, c7),
              f8: (h7, g6, e6, d7), g8: (h6, f6, e7), h8: (g6, f7), a7: (c8, c6, b5), b7: (d8, d6, c5, a5),
              c7: (e8, e6, d5, b5, a8, a6), d7: (f8, f6, e5, c5, b8, b6), e7: (g8, g6, f5, d5, c8, c6),
              f7: (h8, h6, g5, e5, d8, d6), g7: (h5, f5, e8, e6), h7: (g5, f8, f6), a6: (b8, c7, c5, b4),
              b6: (a8, c8, d7, d5, c4, a4), c6: (b8, d8, e7, e5, d4, b4, a7, a5), d6: (c8, e8, f7, f5, e4, c4, b7, b5),
              e6: (d8, f8, g7, g5, f4, d4, c7, c5), f6: (e8, g8, h7, h5, g4, e4, d7, d5), g6: (f8, h8, h4, f4, e7, e5),
              h6: (g8, g4, f7, f5), a5: (b7, c6, c4, b3), b5: (a7, c7, d6, d4, c3, a3),
              c5: (b7, d7, e6, e4, d3, b3, a6, a4), d5: (c7, e7, f6, f4, e3, c3, b6, b4),
              e5: (d7, f7, g6, g4, f3, d3, c6, c4), f5: (e7, g7, h6, h4, g3, e3, d6, d4), g5: (f7, h7, h3, f3, e6, e4),
              h5: (g7, g3, f6, f4), a4: (b6, c5, c3, b2), b4: (a6, c6, d5, d3, c2, a2),
              c4: (b6, d6, e5, e3, d2, b2, a5, a3), d4: (c6, e6, f5, f3, e2, c2, b5, b3),
              e4: (d6, f6, g5, g3, f2, d2, c5, c3), f4: (e6, g6, h5, h3, g2, e2, d5, d3), g4: (f6, h6, h2, f2, e5, e3),
              h4: (g6, g2, f5, f3), a3: (b5, c4, c2, b1), b3: (a5, c5, d4, d2, c1, a1),
              c3: (b5, d5, e4, e2, d1, b1, a4, a2), d3: (c5, e5, f4, f2, e1, c1, b4, b2),
              e3: (d5, f5, g4, g2, f1, d1, c4, c2), f3: (e5, g5, h4, h2, g1, e1, d4, d2), g3: (f5, h5, h1, f1, e4, e2),
              h3: (g5, g1, f4, f2), a2: (b4, c3, c1), b2: (a4, c4, d3, d1), c2: (b4, d4, e3, e1, a3, a1),
              d2: (c4, e4, f3, f1, b3, b1), e2: (d4, f4, g3, g1, c3, c1), f2: (e4, g4, h3, h1, d3, d1),
              g2: (f4, h4, e3, e1), h2: (g4, f3, f1), a1: (b3, c2), b1: (a3, c3, d2), c1: (b3, d3, e2, a2),
              d1: (c3, e3, f2, b2), e1: (d3, f3, g2, c2), f1: (e3, g3, h2, d2), g1: (f3, h3, e2), h1: (g3, f2)}

kingstep = {a8: (b8, b7, a7), b8: (c8, c7, b7, a7, a8), c8: (d8, d7, c7, b7, b8), d8: (e8, e7, d7, c7, c8),
            e8: (f8, f7, e7, d7, d8), f8: (g8, g7, f7, e7, e8), g8: (h8, h7, g7, f7, f8), h8: (h7, g7, g8),
            a7: (a8, b8, b7, b6, a6), b7: (a8, b8, c8, c7, c6, b6, a6, a7), c7: (b8, c8, d8, d7, d6, c6, b6, b7),
            d7: (c8, d8, e8, e7, e6, d6, c6, c7), e7: (d8, e8, f8, f7, f6, e6, d6, d7),
            f7: (e8, f8, g8, g7, g6, f6, e6, e7), g7: (f8, g8, h8, h7, h6, g6, f6, f7), h7: (g8, h8, h6, g6, g7),
            a6: (a7, b7, b6, b5, a5), b6: (a7, b7, c7, c6, c5, b5, a5, a6), c6: (b7, c7, d7, d6, d5, c5, b5, b6),
            d6: (c7, d7, e7, e6, e5, d5, c5, c6), e6: (d7, e7, f7, f6, f5, e5, d5, d6),
            f6: (e7, f7, g7, g6, g5, f5, e5, e6), g6: (f7, g7, h7, h6, h5, g5, f5, f6), h6: (g7, h7, h5, g5, g6),
            a5: (a6, b6, b5, b4, a4), b5: (a6, b6, c6, c5, c4, b4, a4, a5), c5: (b6, c6, d6, d5, d4, c4, b4, b5),
            d5: (c6, d6, e6, e5, e4, d4, c4, c5), e5: (d6, e6, f6, f5, f4, e4, d4, d5),
            f5: (e6, f6, g6, g5, g4, f4, e4, e5), g5: (f6, g6, h6, h5, h4, g4, f4, f5), h5: (g6, h6, h4, g4, g5),
            a4: (a5, b5, b4, b3, a3), b4: (a5, b5, c5, c4, c3, b3, a3, a4), c4: (b5, c5, d5, d4, d3, c3, b3, b4),
            d4: (c5, d5, e5, e4, e3, d3, c3, c4), e4: (d5, e5, f5, f4, f3, e3, d3, d4),
            f4: (e5, f5, g5, g4, g3, f3, e3, e4), g4: (f5, g5, h5, h4, h3, g3, f3, f4), h4: (g5, h5, h3, g3, g4),
            a3: (a4, b4, b3, b2, a2), b3: (a4, b4, c4, c3, c2, b2, a2, a3), c3: (b4, c4, d4, d3, d2, c2, b2, b3),
            d3: (c4, d4, e4, e3, e2, d2, c2, c3), e3: (d4, e4, f4, f3, f2, e2, d2, d3),
            f3: (e4, f4, g4, g3, g2, f2, e2, e3), g3: (f4, g4, h4, h3, h2, g2, f2, f3), h3: (g4, h4, h2, g2, g3),
            a2: (a3, b3, b2, b1, a1), b2: (a3, b3, c3, c2, c1, b1, a1, a2), c2: (b3, c3, d3, d2, d1, c1, b1, b2),
            d2: (c3, d3, e3, e2, e1, d1, c1, c2), e2: (d3, e3, f3, f2, f1, e1, d1, d2),
            f2: (e3, f3, g3, g2, g1, f1, e1, e2), g2: (f3, g3, h3, h2, h1, g1, f1, f2), h2: (g3, h3, h1, g1, g2),
            a1: (a2, b2, b1), b1: (a2, b2, c2, c1, a1), c1: (b2, c2, d2, d1, b1), d1: (c2, d2, e2, e1, c1),
            e1: (d2, e2, f2, f1, d1), f1: (e2, f2, g2, g1, e1), g1: (f2, g2, h2, h1, f1), h1: (g2, h2, g1), }

rookstep = {a8: ((), (b8, c8, d8, e8, f8, g8, h8), (a7, a6, a5, a4, a3, a2, a1), ()),
            b8: ((), (c8, d8, e8, f8, g8, h8), (b7, b6, b5, b4, b3, b2, b1), (a8,)),
            c8: ((), (d8, e8, f8, g8, h8), (c7, c6, c5, c4, c3, c2, c1), (b8, a8)),
            d8: ((), (e8, f8, g8, h8), (d7, d6, d5, d4, d3, d2, d1), (c8, b8, a8)),
            e8: ((), (f8, g8, h8), (e7, e6, e5, e4, e3, e2, e1), (d8, c8, b8, a8)),
            f8: ((), (g8, h8), (f7, f6, f5, f4, f3, f2, f1), (e8, d8, c8, b8, a8)),
            g8: ((), (h8,), (g7, g6, g5, g4, g3, g2, g1), (f8, e8, d8, c8, b8, a8)),
            h8: ((), (), (h7, h6, h5, h4, h3, h2, h1), (g8, f8, e8, d8, c8, b8, a8)),
            a7: ((a8,), (b7, c7, d7, e7, f7, g7, h7), (a6, a5, a4, a3, a2, a1), ()),
            b7: ((b8,), (c7, d7, e7, f7, g7, h7), (b6, b5, b4, b3, b2, b1), (a7,)),
            c7: ((c8,), (d7, e7, f7, g7, h7), (c6, c5, c4, c3, c2, c1), (b7, a7)),
            d7: ((d8,), (e7, f7, g7, h7), (d6, d5, d4, d3, d2, d1), (c7, b7, a7)),
            e7: ((e8,), (f7, g7, h7), (e6, e5, e4, e3, e2, e1), (d7, c7, b7, a7)),
            f7: ((f8,), (g7, h7), (f6, f5, f4, f3, f2, f1), (e7, d7, c7, b7, a7)),
            g7: ((g8,), (h7,), (g6, g5, g4, g3, g2, g1), (f7, e7, d7, c7, b7, a7)),
            h7: ((h8,), (), (h6, h5, h4, h3, h2, h1), (g7, f7, e7, d7, c7, b7, a7)),
            a6: ((a7, a8), (b6, c6, d6, e6, f6, g6, h6), (a5, a4, a3, a2, a1), ()),
            b6: ((b7, b8), (c6, d6, e6, f6, g6, h6), (b5, b4, b3, b2, b1), (a6,)),
            c6: ((c7, c8), (d6, e6, f6, g6, h6), (c5, c4, c3, c2, c1), (b6, a6)),
            d6: ((d7, d8), (e6, f6, g6, h6), (d5, d4, d3, d2, d1), (c6, b6, a6)),
            e6: ((e7, e8), (f6, g6, h6), (e5, e4, e3, e2, e1), (d6, c6, b6, a6)),
            f6: ((f7, f8), (g6, h6), (f5, f4, f3, f2, f1), (e6, d6, c6, b6, a6)),
            g6: ((g7, g8), (h6,), (g5, g4, g3, g2, g1), (f6, e6, d6, c6, b6, a6)),
            h6: ((h7, h8), (), (h5, h4, h3, h2, h1), (g6, f6, e6, d6, c6, b6, a6)),
            a5: ((a6, a7, a8), (b5, c5, d5, e5, f5, g5, h5), (a4, a3, a2, a1), ()),
            b5: ((b6, b7, b8), (c5, d5, e5, f5, g5, h5), (b4, b3, b2, b1), (a5,)),
            c5: ((c6, c7, c8), (d5, e5, f5, g5, h5), (c4, c3, c2, c1), (b5, a5)),
            d5: ((d6, d7, d8), (e5, f5, g5, h5), (d4, d3, d2, d1), (c5, b5, a5)),
            e5: ((e6, e7, e8), (f5, g5, h5), (e4, e3, e2, e1), (d5, c5, b5, a5)),
            f5: ((f6, f7, f8), (g5, h5), (f4, f3, f2, f1), (e5, d5, c5, b5, a5)),
            g5: ((g6, g7, g8), (h5,), (g4, g3, g2, g1), (f5, e5, d5, c5, b5, a5)),
            h5: ((h6, h7, h8), (), (h4, h3, h2, h1), (g5, f5, e5, d5, c5, b5, a5)),
            a4: ((a5, a6, a7, a8), (b4, c4, d4, e4, f4, g4, h4), (a3, a2, a1), ()),
            b4: ((b5, b6, b7, b8), (c4, d4, e4, f4, g4, h4), (b3, b2, b1), (a4,)),
            c4: ((c5, c6, c7, c8), (d4, e4, f4, g4, h4), (c3, c2, c1), (b4, a4)),
            d4: ((d5, d6, d7, d8), (e4, f4, g4, h4), (d3, d2, d1), (c4, b4, a4)),
            e4: ((e5, e6, e7, e8), (f4, g4, h4), (e3, e2, e1), (d4, c4, b4, a4)),
            f4: ((f5, f6, f7, f8), (g4, h4), (f3, f2, f1), (e4, d4, c4, b4, a4)),
            g4: ((g5, g6, g7, g8), (h4,), (g3, g2, g1), (f4, e4, d4, c4, b4, a4)),
            h4: ((h5, h6, h7, h8), (), (h3, h2, h1), (g4, f4, e4, d4, c4, b4, a4)),
            a3: ((a4, a5, a6, a7, a8), (b3, c3, d3, e3, f3, g3, h3), (a2, a1), ()),
            b3: ((b4, b5, b6, b7, b8), (c3, d3, e3, f3, g3, h3), (b2, b1), (a3,)),
            c3: ((c4, c5, c6, c7, c8), (d3, e3, f3, g3, h3), (c2, c1), (b3, a3)),
            d3: ((d4, d5, d6, d7, d8), (e3, f3, g3, h3), (d2, d1), (c3, b3, a3)),
            e3: ((e4, e5, e6, e7, e8), (f3, g3, h3), (e2, e1), (d3, c3, b3, a3)),
            f3: ((f4, f5, f6, f7, f8), (g3, h3), (f2, f1), (e3, d3, c3, b3, a3)),
            g3: ((g4, g5, g6, g7, g8), (h3,), (g2, g1), (f3, e3, d3, c3, b3, a3)),
            h3: ((h4, h5, h6, h7, h8), (), (h2, h1), (g3, f3, e3, d3, c3, b3, a3)),
            a2: ((a3, a4, a5, a6, a7, a8), (b2, c2, d2, e2, f2, g2, h2), (a1,), ()),
            b2: ((b3, b4, b5, b6, b7, b8), (c2, d2, e2, f2, g2, h2), (b1,), (a2,)),
            c2: ((c3, c4, c5, c6, c7, c8), (d2, e2, f2, g2, h2), (c1,), (b2, a2)),
            d2: ((d3, d4, d5, d6, d7, d8), (e2, f2, g2, h2), (d1,), (c2, b2, a2)),
            e2: ((e3, e4, e5, e6, e7, e8), (f2, g2, h2), (e1,), (d2, c2, b2, a2)),
            f2: ((f3, f4, f5, f6, f7, f8), (g2, h2), (f1,), (e2, d2, c2, b2, a2)),
            g2: ((g3, g4, g5, g6, g7, g8), (h2,), (g1,), (f2, e2, d2, c2, b2, a2)),
            h2: ((h3, h4, h5, h6, h7, h8), (), (h1,), (g2, f2, e2, d2, c2, b2, a2)),
            a1: ((a2, a3, a4, a5, a6, a7, a8), (b1, c1, d1, e1, f1, g1, h1), (), ()),
            b1: ((b2, b3, b4, b5, b6, b7, b8), (c1, d1, e1, f1, g1, h1), (), (a1,)),
            c1: ((c2, c3, c4, c5, c6, c7, c8), (d1, e1, f1, g1, h1), (), (b1, a1)),
            d1: ((d2, d3, d4, d5, d6, d7, d8), (e1, f1, g1, h1), (), (c1, b1, a1)),
            e1: ((e2, e3, e4, e5, e6, e7, e8), (f1, g1, h1), (), (d1, c1, b1, a1)),
            f1: ((f2, f3, f4, f5, f6, f7, f8), (g1, h1), (), (e1, d1, c1, b1, a1)),
            g1: ((g2, g3, g4, g5, g6, g7, g8), (h1,), (), (f1, e1, d1, c1, b1, a1)),
            h1: ((h2, h3, h4, h5, h6, h7, h8), (), (), (g1, f1, e1, d1, c1, b1, a1))}

bishopstep = {a8: ((), (), (b7, c6, d5, e4, f3, g2, h1), ()),
              b8: ((), (), (c7, d6, e5, f4, g3, h2), (a7,)),
              c8: ((), (), (d7, e6, f5, g4, h3), (b7, a6)),
              d8: ((), (), (e7, f6, g5, h4), (c7, b6, a5)),
              e8: ((), (), (f7, g6, h5), (d7, c6, b5, a4)),
              f8: ((), (), (g7, h6), (e7, d6, c5, b4, a3)),
              g8: ((), (), (h7,), (f7, e6, d5, c4, b3, a2)),
              h8: ((), (), (), (g7, f6, e5, d4, c3, b2, a1)),
              a7: ((), (b8,), (b6, c5, d4, e3, f2, g1), ()),
              b7: ((a8,), (c8,), (c6, d5, e4, f3, g2, h1), (a6,)),
              c7: ((b8,), (d8,), (d6, e5, f4, g3, h2), (b6, a5)),
              d7: ((c8,), (e8,), (e6, f5, g4, h3), (c6, b5, a4)),
              e7: ((d8,), (f8,), (f6, g5, h4), (d6, c5, b4, a3)),
              f7: ((e8,), (g8,), (g6, h5), (e6, d5, c4, b3, a2)),
              g7: ((f8,), (h8,), (h6,), (f6, e5, d4, c3, b2, a1)),
              h7: ((g8,), (), (), (g6, f5, e4, d3, c2, b1)),
              a6: ((), (b7, c8), (b5, c4, d3, e2, f1), ()),
              b6: ((a7,), (c7, d8), (c5, d4, e3, f2, g1), (a5,)),
              c6: ((b7, a8), (d7, e8), (d5, e4, f3, g2, h1), (b5, a4)),
              d6: ((c7, b8), (e7, f8), (e5, f4, g3, h2), (c5, b4, a3)),
              e6: ((d7, c8), (f7, g8), (f5, g4, h3), (d5, c4, b3, a2)),
              f6: ((e7, d8), (g7, h8), (g5, h4), (e5, d4, c3, b2, a1)),
              g6: ((f7, e8), (h7,), (h5,), (f5, e4, d3, c2, b1)),
              h6: ((g7, f8), (), (), (g5, f4, e3, d2, c1)),
              a5: ((), (b6, c7, d8), (b4, c3, d2, e1), ()),
              b5: ((a6,), (c6, d7, e8), (c4, d3, e2, f1), (a4,)),
              c5: ((b6, a7), (d6, e7, f8), (d4, e3, f2, g1), (b4, a3)),
              d5: ((c6, b7, a8), (e6, f7, g8), (e4, f3, g2, h1), (c4, b3, a2)),
              e5: ((d6, c7, b8), (f6, g7, h8), (f4, g3, h2), (d4, c3, b2, a1)),
              f5: ((e6, d7, c8), (g6, h7), (g4, h3), (e4, d3, c2, b1)),
              g5: ((f6, e7, d8), (h6,), (h4,), (f4, e3, d2, c1)),
              h5: ((g6, f7, e8), (), (), (g4, f3, e2, d1)),
              a4: ((), (b5, c6, d7, e8), (b3, c2, d1), ()),
              b4: ((a5,), (c5, d6, e7, f8), (c3, d2, e1), (a3,)),
              c4: ((b5, a6), (d5, e6, f7, g8), (d3, e2, f1), (b3, a2)),
              d4: ((c5, b6, a7), (e5, f6, g7, h8), (e3, f2, g1), (c3, b2, a1)),
              e4: ((d5, c6, b7, a8), (f5, g6, h7), (f3, g2, h1), (d3, c2, b1)),
              f4: ((e5, d6, c7, b8), (g5, h6), (g3, h2), (e3, d2, c1)),
              g4: ((f5, e6, d7, c8), (h5,), (h3,), (f3, e2, d1)),
              h4: ((g5, f6, e7, d8), (), (), (g3, f2, e1)),
              a3: ((), (b4, c5, d6, e7, f8), (b2, c1), ()),
              b3: ((a4,), (c4, d5, e6, f7, g8), (c2, d1), (a2,)),
              c3: ((b4, a5), (d4, e5, f6, g7, h8), (d2, e1), (b2, a1)),
              d3: ((c4, b5, a6), (e4, f5, g6, h7), (e2, f1), (c2, b1)),
              e3: ((d4, c5, b6, a7), (f4, g5, h6), (f2, g1), (d2, c1)),
              f3: ((e4, d5, c6, b7, a8), (g4, h5), (g2, h1), (e2, d1)),
              g3: ((f4, e5, d6, c7, b8), (h4,), (h2,), (f2, e1)),
              h3: ((g4, f5, e6, d7, c8), (), (), (g2, f1)),
              a2: ((), (b3, c4, d5, e6, f7, g8), (b1,), ()),
              b2: ((a3,), (c3, d4, e5, f6, g7, h8), (c1,), (a1,)),
              c2: ((b3, a4), (d3, e4, f5, g6, h7), (d1,), (b1,)),
              d2: ((c3, b4, a5), (e3, f4, g5, h6), (e1,), (c1,)),
              e2: ((d3, c4, b5, a6), (f3, g4, h5), (f1,), (d1,)),
              f2: ((e3, d4, c5, b6, a7), (g3, h4), (g1,), (e1,)),
              g2: ((f3, e4, d5, c6, b7, a8), (h3,), (h1,), (f1,)),
              h2: ((g3, f4, e5, d6, c7, b8), (), (), (g1,)),
              a1: ((), (b2, c3, d4, e5, f6, g7, h8), (), ()),
              b1: ((a2,), (c2, d3, e4, f5, g6, h7), (), ()),
              c1: ((b2, a3), (d2, e3, f4, g5, h6), (), ()),
              d1: ((c2, b3, a4), (e2, f3, g4, h5), (), ()),
              e1: ((d2, c3, b4, a5), (f2, g3, h4), (), ()),
              f1: ((e2, d3, c4, b5, a6), (g2, h3), (), ()),
              g1: ((f2, e3, d4, c5, b6, a7), (h2,), (), ()),
              h1: ((g2, f3, e4, d5, c6, b7, a8), (), (), ())}


def white_pawn_generator(fromcell):
    try:
        onestep = whitepawnonestep[fromcell]
        if onestep in occupiedcells:
            raise OccupationException
    except (KeyError, OccupationException):
        onestep = None
        # print("No one step move for white pawn in ", fromcell)
    try:
        if onestep is None:
            raise OccupationException
        twostep = whitepawntwostep[fromcell]
        if twostep in occupiedcells:
            raise OccupationException
    except (KeyError, OccupationException):
        twostep = None
        # print("No two step move for white pawn in ", fromcell)
    try:
        capturesx, capturedx = whitepawncapture[fromcell]
        if capturesx not in blackoccupiedcells:
            capturesx = None
        if capturedx not in blackoccupiedcells:
            capturedx = None
    except KeyError:
        capturesx, capturedx = (None, None)
        # print("No captures possible for white pawn from ", fromcell)
    if capturesx in enpassantcells:
        enpassantsx = capturesx
    else:
        enpassantsx = None
    if capturedx in enpassantcells:
        enpassantdx = capturedx
    else:
        enpassantdx = None
    destinationlist = [tocell for tocell in (onestep, twostep, capturesx, capturedx, enpassantsx, enpassantdx)
                       if tocell is not None]
    return destinationlist


def black_pawn_generator(fromcell):
    try:
        onestep = blackpawnonestep[fromcell]
        if onestep in occupiedcells:
            raise OccupationException
    except (KeyError, OccupationException):
        onestep = None
        # print("No one step move for black pawn in ", fromcell)
    try:
        if onestep is None:
            raise OccupationException
        twostep = blackpawntwostep[fromcell]
        if twostep in occupiedcells:
            raise OccupationException
    except (KeyError, OccupationException):
        twostep = None
        # print("No two step move for black pawn in ", fromcell)
    try:
        capturesx, capturedx = blackpawncapture[fromcell]
        if capturesx not in whiteoccupiedcells:
            capturesx = None
        if capturedx not in whiteoccupiedcells:
            capturedx = None
    except KeyError:
        capturesx, capturedx = (None, None)
        # print("No captures possible for black pawn from ", fromcell)
    if capturesx in enpassantcells:
        enpassantsx = capturesx
    else:
        enpassantsx = None
    if capturedx in enpassantcells:
        enpassantdx = capturedx
    else:
        enpassantdx = None
    destinationlist = [tocell for tocell in (onestep, twostep, capturesx, capturedx, enpassantsx, enpassantdx)
                       if tocell is not None]
    return destinationlist


def white_knight_generator(fromcell):
    tocells = knightstep[fromcell]
    destination = [tocell for tocell in tocells if tocell not in whiteoccupiedcells]
    return destination


def black_knight_generator(fromcell):
    tocells = knightstep[fromcell]
    destination = [tocell for tocell in tocells if tocell not in blackoccupiedcells]
    return destination


def white_king_generator(fromcell):
    try:
        tocells = kingstep[fromcell]
    except KeyError:
        tocells = None
        # print("No entry for king in ", fromcell)
    destination = [tocell for tocell in tocells if tocell not in whiteoccupiedcells]
    return destination


def black_king_generator(fromcell):
    try:
        tocells = kingstep[fromcell]
    except KeyError:
        tocells = None
        # print("No entry for king in ", fromcell)
    destination = [tocell for tocell in tocells if tocell not in blackoccupiedcells]
    return destination


def white_rook_generator(fromcell):
    deltas = rookstep[fromcell]
    destination = []
    for delta in deltas:
        for tocell in delta:
            if tocell in whiteoccupiedcells:
                break
            destination.append(tocell)
            if tocell in blackoccupiedcells:
                break
    return destination


def black_rook_generator(fromcell):
    deltas = rookstep[fromcell]
    destination = []
    for delta in deltas:
        for tocell in delta:
            if tocell in blackoccupiedcells:
                break
            destination.append(tocell)
            if tocell in whiteoccupiedcells:
                break
    return destination


def white_bishop_generator(fromcell):
    deltas = bishopstep[fromcell]
    destination = []
    for delta in deltas:
        for tocell in delta:
            if tocell in whiteoccupiedcells:
                break
            destination.append(tocell)
            if tocell in blackoccupiedcells:
                break
    return destination


def black_bishop_generator(fromcell):
    deltas = bishopstep[fromcell]
    destination = []
    for delta in deltas:
        for tocell in delta:
            if tocell in blackoccupiedcells:
                break
            destination.append(tocell)
            if tocell in whiteoccupiedcells:
                break
    return destination


def white_queen_generator(fromcell):
    destinationrook = white_rook_generator(fromcell)
    destinationbishop = white_bishop_generator(fromcell)
    return destinationrook + destinationbishop


def black_queen_generator(fromcell):
    destinationrook = black_rook_generator(fromcell)
    destinationbishop = black_bishop_generator(fromcell)
    return destinationrook + destinationbishop


def get_black_captured_piece(tocell):
    if tocell in blackpawns:
        return 'bP'
    if tocell in blackrooks:
        return 'bR'
    if tocell in blackknights:
        return 'bN'
    if tocell in blackbishops:
        return 'bB'
    if tocell in blackqueen:
        return 'bQ'
    if tocell in blackking:
        return 'bK'
    return None


def get_white_captured_piece(tocell):
    if tocell in whitepawns:
        return 'wP'
    if tocell in whiterooks:
        return 'wR'
    if tocell in whiteknights:
        return 'wN'
    if tocell in whitebishops:
        return 'wB'
    if tocell in whitequeen:
        return 'wQ'
    if tocell in whiteking:
        return 'wK'
    return None


def white_pawn_move_factory(fromcell, tocell):
    capturedpiece = get_black_captured_piece(tocell)
    if tocell in promotioncells:
        promotionto = 'wQ'
    else:
        promotionto = None
    if tocell.absfiledifference(fromcell) == 2:
        isenpassant = True
    else:
        isenpassant = False
    return mvm.Move('wP', fromcell, tocell, True, capturedpiece, False, False, promotionto, isenpassant, False)


def white_piece_move_factory(fromcell, tocell, piece):
    capturedpiece = get_black_captured_piece(tocell)
    return mvm.Move(piece, fromcell, tocell, True, capturedpiece, False, False, None, False, False)


def black_pawn_move_factory(fromcell, tocell):
    capturedpiece = get_white_captured_piece(tocell)
    if tocell in promotioncells:
        promotionto = 'bQ'
    else:
        promotionto = None
    if tocell.absfiledifference(fromcell) == 2:
        isenpassant = True
    else:
        isenpassant = False
    return mvm.Move('bP', fromcell, tocell, False, capturedpiece, False, False, promotionto, isenpassant, False)


def black_piece_move_factory(fromcell, tocell, piece):
    capturedpiece = get_white_captured_piece(tocell)
    return mvm.Move(piece, fromcell, tocell, False, capturedpiece, False, False, None, False, False)


def king_castling_move_factory(iswhiteturn):
    return mvm.Move(None, None, None, iswhiteturn, None, True, False, None, False, False)


def queen_castling_move_factory(iswhiteturn):
    return mvm.Move(None, None, None, iswhiteturn, None, False, True, None, False, False)


def white_generator_moves():
    for fromcell in whitepawns:
        destinationlist = white_pawn_generator(fromcell)
        for tocell in destinationlist:
            yield white_pawn_move_factory(fromcell, tocell)
    for fromcell in whiteknights:
        destinationlist = white_knight_generator(fromcell)
        for tocell in destinationlist:
            yield white_piece_move_factory(fromcell, tocell, 'wN')
    for fromcell in whiterooks:
        destinationlist = white_rook_generator(fromcell)
        for tocell in destinationlist:
            yield white_piece_move_factory(fromcell, tocell, 'wR')
    for fromcell in whitebishops:
        destinationlist = white_bishop_generator(fromcell)
        for tocell in destinationlist:
            yield white_piece_move_factory(fromcell, tocell, 'wB')
    for fromcell in whitequeen:
        destinationlist = white_queen_generator(fromcell)
        for tocell in destinationlist:
            yield white_piece_move_factory(fromcell, tocell, 'wQ')
    for fromcell in whiteking:
        destinationlist = white_king_generator(fromcell)
        for tocell in destinationlist:
            yield white_piece_move_factory(fromcell, tocell, 'wK')
    if whitecastlingrights['wk']:
        yield king_castling_move_factory(iswhiteturn=True)
    if whitecastlingrights['wq']:
        yield queen_castling_move_factory(iswhiteturn=True)


def black_generator_moves():
    for fromcell in blackpawns:
        destinationlist = black_pawn_generator(fromcell)
        for tocell in destinationlist:
            yield black_pawn_move_factory(fromcell, tocell)
    for fromcell in blackknights:
        destinationlist = black_knight_generator(fromcell)
        for tocell in destinationlist:
            yield black_piece_move_factory(fromcell, tocell, 'bN')
    for fromcell in blackrooks:
        destinationlist = black_rook_generator(fromcell)
        for tocell in destinationlist:
            yield black_piece_move_factory(fromcell, tocell, 'bR')
    for fromcell in blackbishops:
        destinationlist = black_bishop_generator(fromcell)
        for tocell in destinationlist:
            yield black_piece_move_factory(fromcell, tocell, 'bB')
    for fromcell in blackqueen:
        destinationlist = black_queen_generator(fromcell)
        for tocell in destinationlist:
            yield black_piece_move_factory(fromcell, tocell, 'bQ')
    for fromcell in blackking:
        destinationlist = black_king_generator(fromcell)
        for tocell in destinationlist:
            yield black_piece_move_factory(fromcell, tocell, 'bK')
    if blackcastlingrights['bk']:
        yield king_castling_move_factory(iswhiteturn=False)
    if blackcastlingrights['bq']:
        yield queen_castling_move_factory(iswhiteturn=False)


def list_piece_factory(hashgenerator=None):
    if hashgenerator is None:
        return ListPiece()
    else:
        return ListPieceHashValue(hashgenerator)


class ListPiece:
    def __init__(self):
        self.moves = []
        self.castlingrights = []
        self.castlings = []
        self.enpassants = []
        global occupiedcells, whiteoccupiedcells, blackoccupiedcells, whitepawns, blackpawns, whiterooks, blackrooks
        global whiteknights, blackknights, whitebishops, blackbishops, whitequeen, blackqueen, whiteking, blackking
        global enpassantcells, whitecastlingrights, blackcastlingrights, castling
        occupiedcells = []
        whiteoccupiedcells = []
        blackoccupiedcells = []
        whitepawns = []
        blackpawns = []
        whiterooks = []
        blackrooks = []
        whiteknights = []
        blackknights = []
        whitebishops = []
        blackbishops = []
        whitequeen = []
        blackqueen = []
        whiteking = []
        blackking = []
        enpassantcells = []
        whitecastlingrights = {'wk': False, 'wq': False}
        blackcastlingrights = {'bk': False, 'bq': False}
        castling = {'wk': [True, True], 'wq': [True, True], 'bk': [True, True],
                    'bq': [True, True]}

    @staticmethod
    def set_castlingrights(whitekingside=None, whitequeenside=None, blackkingside=None, blackqueenside=None):
        if whitekingside is True:
            whitecastlingrights['wk'] = True
        else:
            whitecastlingrights['wk'] = False
            castling['wk'] = [False, False, False, False]
        if whitequeenside is True:
            whitecastlingrights['wq'] = True
        else:
            whitecastlingrights['wq'] = False
            castling['wq'] = [False, False, False, False, False]
        if blackkingside is True:
            blackcastlingrights['bk'] = True
        else:
            blackcastlingrights['bk'] = False
            castling['bk'] = [False, False, False, False]
        if blackqueenside is True:
            blackcastlingrights['bq'] = True
        else:
            blackcastlingrights['bq'] = False
            castling['bq'] = [False, False, False, False, False]

    def update_white_king_castling_rights(self):
        if castling['wk'][0] is False or castling['wk'][1] is False:
            whitecastlingrights['wk'] = False
            castling['wk'] = [False, False]
            return
        if h1 not in whiterooks:
            whitecastlingrights['wk'] = False
            castling['wk'] = [False, False]
            return
        if self.is_white_king_in_check():
            whitecastlingrights['wk'] = False
            return
        if f1 in occupiedcells:
            whitecastlingrights['wk'] = False
            return
        global whiteking
        whiteking.pop(-1)
        whiteking.append(f1)
        occupiedcells.remove(e1)
        occupiedcells.append(f1)
        whiteoccupiedcells.remove(e1)
        whiteoccupiedcells.append(f1)
        if self.is_white_king_in_check():
            whitecastlingrights['wk'] = False
            whiteking.pop(-1)
            whiteking.append(e1)
            occupiedcells.remove(f1)
            occupiedcells.append(e1)
            whiteoccupiedcells.remove(f1)
            whiteoccupiedcells.append(e1)
            return
        if g1 in occupiedcells:
            whitecastlingrights['wk'] = False
            whiteking.pop(-1)
            whiteking.append(e1)
            occupiedcells.remove(f1)
            occupiedcells.append(e1)
            whiteoccupiedcells.remove(f1)
            whiteoccupiedcells.append(e1)
            return
        whiteking.pop(-1)
        whiteking.append(g1)
        occupiedcells.remove(f1)
        occupiedcells.append(g1)
        whiteoccupiedcells.remove(f1)
        whiteoccupiedcells.append(g1)
        if self.is_white_king_in_check():
            whitecastlingrights['wk'] = False
            whiteking.pop(-1)
            whiteking.append(e1)
            occupiedcells.remove(g1)
            occupiedcells.append(e1)
            whiteoccupiedcells.remove(g1)
            whiteoccupiedcells.append(e1)
            return
        whiteking.pop(-1)
        whiteking.append(e1)
        occupiedcells.remove(g1)
        occupiedcells.append(e1)
        whiteoccupiedcells.remove(g1)
        whiteoccupiedcells.append(e1)
        whitecastlingrights['wk'] = True

    def update_white_queen_castling_rights(self):
        if castling['wq'][0] is False or castling['wq'][1] is False:
            whitecastlingrights['wq'] = False
            castling['wq'] = [False, False]
            return
        if a1 not in whiterooks:
            whitecastlingrights['wq'] = False
            castling['wq'] = [False, False]
            return
        if self.is_white_king_in_check():
            whitecastlingrights['wq'] = False
            return
        if d1 in occupiedcells:
            whitecastlingrights['wq'] = False
            return
        global whiteking
        whiteking.pop(-1)
        whiteking.append(d1)
        occupiedcells.remove(e1)
        occupiedcells.append(d1)
        whiteoccupiedcells.remove(e1)
        whiteoccupiedcells.append(d1)
        if self.is_white_king_in_check():
            whitecastlingrights['wq'] = False
            whiteking.pop(-1)
            whiteking.append(e1)
            occupiedcells.remove(d1)
            occupiedcells.append(e1)
            whiteoccupiedcells.remove(d1)
            whiteoccupiedcells.append(e1)
            return
        if c1 in occupiedcells:
            whitecastlingrights['wq'] = False
            whiteking.pop(-1)
            whiteking.append(e1)
            occupiedcells.remove(d1)
            occupiedcells.append(e1)
            whiteoccupiedcells.remove(d1)
            whiteoccupiedcells.append(e1)
            return
        whiteking.pop(-1)
        whiteking.append(c1)
        occupiedcells.remove(d1)
        occupiedcells.append(c1)
        whiteoccupiedcells.remove(d1)
        whiteoccupiedcells.append(c1)
        if self.is_white_king_in_check():
            whitecastlingrights['wq'] = False
            whiteking.pop(-1)
            whiteking.append(e1)
            occupiedcells.remove(c1)
            occupiedcells.append(e1)
            whiteoccupiedcells.remove(c1)
            whiteoccupiedcells.append(e1)
            return
        if b1 in occupiedcells:
            whitecastlingrights['wq'] = False
            whiteking.pop(-1)
            whiteking.append(e1)
            occupiedcells.remove(c1)
            occupiedcells.append(e1)
            whiteoccupiedcells.remove(c1)
            whiteoccupiedcells.append(e1)
            return
        whiteking.pop(-1)
        whiteking.append(b1)
        occupiedcells.remove(c1)
        occupiedcells.append(b1)
        whiteoccupiedcells.remove(c1)
        whiteoccupiedcells.append(b1)
        if self.is_white_king_in_check():
            whitecastlingrights['wq'] = False
            whiteking.pop(-1)
            whiteking.append(e1)
            occupiedcells.remove(b1)
            occupiedcells.append(e1)
            whiteoccupiedcells.remove(b1)
            whiteoccupiedcells.append(e1)
            return
        whiteking.pop(-1)
        whiteking.append(e1)
        occupiedcells.remove(b1)
        occupiedcells.append(e1)
        whiteoccupiedcells.remove(b1)
        whiteoccupiedcells.append(e1)
        whitecastlingrights['wq'] = True

    def update_black_king_castling_rights(self):
        if castling['bk'][0] is False or castling['bk'][1] is False:
            blackcastlingrights['bk'] = False
            castling['bk'] = [False, False]
            return
        if h8 not in blackrooks:
            blackcastlingrights['bk'] = False
            castling['bk'] = [False, False]
            return
        if self.is_black_king_in_check():
            blackcastlingrights['bk'] = False
            return
        if f1 in occupiedcells:
            blackcastlingrights['bk'] = False
            return
        global blackking
        blackking.pop(-1)
        blackking.append(f8)
        occupiedcells.remove(e8)
        occupiedcells.append(f8)
        blackoccupiedcells.remove(e8)
        blackoccupiedcells.append(f8)
        if self.is_black_king_in_check():
            blackcastlingrights['bk'] = False
            blackking.pop(-1)
            blackking.append(e8)
            occupiedcells.remove(f8)
            occupiedcells.append(e8)
            blackoccupiedcells.remove(f8)
            blackoccupiedcells.append(e8)
            return
        if g1 in occupiedcells:
            blackcastlingrights['bk'] = False
            blackking.pop(-1)
            blackking.append(e8)
            occupiedcells.remove(f8)
            occupiedcells.append(e8)
            blackoccupiedcells.remove(f8)
            blackoccupiedcells.append(e8)
            return
        blackking.pop(-1)
        blackking.append(g8)
        occupiedcells.remove(f8)
        occupiedcells.append(g8)
        blackoccupiedcells.remove(f8)
        blackoccupiedcells.append(g8)
        if self.is_black_king_in_check():
            blackcastlingrights['bk'] = False
            blackking.pop(-1)
            blackking.append(e8)
            occupiedcells.remove(g8)
            occupiedcells.append(e8)
            blackoccupiedcells.remove(g8)
            blackoccupiedcells.append(e8)
            return
        blackking.pop(-1)
        blackking.append(e8)
        occupiedcells.remove(g8)
        occupiedcells.append(e8)
        blackoccupiedcells.remove(g8)
        blackoccupiedcells.append(e8)
        blackcastlingrights['bk'] = True

    def update_black_queen_castling_rights(self):
        if castling['bq'][0] is False or castling['bq'][1] is False:
            blackcastlingrights['bq'] = False
            castling['bq'] = [False, False]
            return
        if a8 not in blackrooks:
            blackcastlingrights['bk'] = False
            castling['bk'] = [False, False]
            return
        if self.is_black_king_in_check():
            blackcastlingrights['bq'] = False
            return
        if d1 in occupiedcells:
            blackcastlingrights['bq'] = False
            return
        global blackking
        blackking.pop(-1)
        blackking.append(d8)
        occupiedcells.remove(e8)
        occupiedcells.append(d8)
        blackoccupiedcells.remove(e8)
        blackoccupiedcells.append(d8)
        if self.is_black_king_in_check():
            blackcastlingrights['bq'] = False
            blackking.pop(-1)
            blackking.append(e8)
            occupiedcells.remove(d8)
            occupiedcells.append(e8)
            blackoccupiedcells.remove(d8)
            blackoccupiedcells.append(e8)
            return
        if c1 in occupiedcells:
            blackcastlingrights['bq'] = False
            blackking.pop(-1)
            blackking.append(e8)
            occupiedcells.remove(d8)
            occupiedcells.append(e8)
            blackoccupiedcells.remove(d8)
            blackoccupiedcells.append(e8)
            return
        blackking.pop(-1)
        blackking.append(c8)
        occupiedcells.remove(d8)
        occupiedcells.append(c8)
        blackoccupiedcells.remove(d8)
        blackoccupiedcells.append(c8)
        if self.is_black_king_in_check():
            blackcastlingrights['bq'] = False
            blackking.pop(-1)
            blackking.append(e8)
            occupiedcells.remove(c8)
            occupiedcells.append(e8)
            blackoccupiedcells.remove(c8)
            blackoccupiedcells.append(e8)
            return
        if b1 in occupiedcells:
            blackcastlingrights['bq'] = False
            blackking.pop(-1)
            blackking.append(e8)
            occupiedcells.remove(c8)
            occupiedcells.append(e8)
            blackoccupiedcells.remove(c8)
            blackoccupiedcells.append(e8)
            return
        blackking.pop(-1)
        blackking.append(b1)
        occupiedcells.remove(c8)
        occupiedcells.append(b8)
        blackoccupiedcells.remove(c8)
        blackoccupiedcells.append(b8)
        if self.is_black_king_in_check():
            blackcastlingrights['bq'] = False
            blackking.pop(-1)
            blackking.append(e8)
            occupiedcells.remove(b8)
            occupiedcells.append(e8)
            blackoccupiedcells.remove(b8)
            blackoccupiedcells.append(e8)
            return
        blackking.pop(-1)
        blackking.append(e8)
        occupiedcells.remove(b8)
        occupiedcells.append(e8)
        blackoccupiedcells.remove(b8)
        blackoccupiedcells.append(e8)
        blackcastlingrights['bq'] = True

    def update_castling_rights(self):
        self.update_white_king_castling_rights()
        self.update_white_queen_castling_rights()
        self.update_black_king_castling_rights()
        self.update_black_queen_castling_rights()

    @staticmethod
    def add_white_pawn(cell):
        whitepawns.append(cell)
        whiteoccupiedcells.append(cell)
        occupiedcells.append(cell)

    @staticmethod
    def add_black_pawn(cell):
        blackpawns.append(cell)
        blackoccupiedcells.append(cell)
        occupiedcells.append(cell)

    @staticmethod
    def add_white_rook(cell):
        whiterooks.append(cell)
        whiteoccupiedcells.append(cell)
        occupiedcells.append(cell)

    @staticmethod
    def add_black_rook(cell):
        blackrooks.append(cell)
        blackoccupiedcells.append(cell)
        occupiedcells.append(cell)

    @staticmethod
    def add_white_knight(cell):
        whiteknights.append(cell)
        whiteoccupiedcells.append(cell)
        occupiedcells.append(cell)

    @staticmethod
    def add_black_knight(cell):
        blackknights.append(cell)
        blackoccupiedcells.append(cell)
        occupiedcells.append(cell)

    @staticmethod
    def add_white_bishop(cell):
        whitebishops.append(cell)
        whiteoccupiedcells.append(cell)
        occupiedcells.append(cell)

    @staticmethod
    def add_black_bishop(cell):
        blackbishops.append(cell)
        blackoccupiedcells.append(cell)
        occupiedcells.append(cell)

    @staticmethod
    def add_white_queen(cell):
        whitequeen.append(cell)
        whiteoccupiedcells.append(cell)
        occupiedcells.append(cell)

    @staticmethod
    def add_black_queen(cell):
        blackqueen.append(cell)
        blackoccupiedcells.append(cell)
        occupiedcells.append(cell)

    @staticmethod
    def add_white_king(cell):
        whiteking.append(cell)
        whiteoccupiedcells.append(cell)
        occupiedcells.append(cell)

    @staticmethod
    def add_black_king(cell):
        blackking.append(cell)
        blackoccupiedcells.append(cell)
        occupiedcells.append(cell)

    @staticmethod
    def set_enpassant(cell):
        enpassantcells.append(cell)

    @staticmethod
    def get_piece_by_cell(cell):
        if cell in whiteoccupiedcells:
            if cell in whitepawns:
                return 'wP'
            elif cell in whiterooks:
                return 'wR'
            elif cell in whiteknights:
                return 'wN'
            elif cell in whitebishops:
                return 'wB'
            elif cell in whitequeen:
                return 'wQ'
            elif cell in whiteking:
                return 'wK'
            else:
                raise ValueError("dictgeneratormodule.py : Listpiece.get_piece_by_cell --> board not consistent!!!")
        elif cell in blackoccupiedcells:
            if cell in blackpawns:
                return 'bP'
            elif cell in blackrooks:
                return 'bR'
            elif cell in blackknights:
                return 'bN'
            elif cell in blackbishops:
                return 'bB'
            elif cell in blackqueen:
                return 'bQ'
            elif cell in blackking:
                return 'bK'
            else:
                raise ValueError("dictgeneratormodule.py : Listpiece.get_piece_by_cell --> board not consistent!!!")
        else:
            return None

    @staticmethod
    def get_promoted_piece(piece, tocell):
        if piece is 'wP' and tocell in promotioncells:
            return 'wQ'
        if piece is 'bP' and tocell in promotioncells:
            return 'bQ'
        return None

    @staticmethod
    def _get_active_occupied_list(iswhiteturn):
        if iswhiteturn:
            return whiteoccupiedcells, blackoccupiedcells
        else:
            return blackoccupiedcells, whiteoccupiedcells

    @staticmethod
    def _get_list_by_piece(piece):
        listbypiece = {'wP': whitepawns, 'wR': whiterooks, 'wN': whiteknights, 'wB': whitebishops, 'wQ': whitequeen,
                       'wK': whiteking,
                       'bP': blackpawns, 'bR': blackrooks, 'bN': blackknights, 'bB': blackbishops, 'bQ': blackqueen,
                       'bK': blackking}
        try:
            lookup = listbypiece[piece]
        except KeyError:
            lookup = None
        return lookup

    def applymove(self, move):
        self.moves.append(move)
        global castling, enpassantcells
        self.castlingrights.append([whitecastlingrights, blackcastlingrights])
        self.castlings.append(castling)
        self.enpassants.append(enpassantcells)
        enpassantcells = []
        activeoccupiedlist, enemyoccupiedlist = self._get_active_occupied_list(move.iswhiteturn)
        activepiecelist = self._get_list_by_piece(move.piece)
        capturedpiecelist = self._get_list_by_piece(move.capturedpiece)
        promotionlist = self._get_list_by_piece(move.promotionto)
        if move.piece is not None:
            try:
                occupiedcells.remove(move.fromcell)
            except ValueError as e:
                print(self)
                e.args += (str(move),)
                raise e
            activeoccupiedlist.remove(move.fromcell)
            activepiecelist.remove(move.fromcell)
            if capturedpiecelist is not None:
                if move.tocell in enpassantcells:
                    if move.iswhiteturn:
                        hitcell = move.tocell.sumcoordinate(0, -1)
                    else:
                        hitcell = move.tocell.sumcoordinate(0, +1)
                else:
                    hitcell = move.tocell
                occupiedcells.remove(hitcell)
                enemyoccupiedlist.remove(hitcell)
                capturedpiecelist.remove(hitcell)
            if promotionlist is not None:
                promotionlist.append(move.tocell)
            else:
                activepiecelist.append(move.tocell)
            activeoccupiedlist.append(move.tocell)
            occupiedcells.append(move.tocell)
            if move.piece is 'wP' and move.fromcell.absfiledifference(move.tocell):
                enpassantcells.append(move.tocell.sumcoordinate(0, -1))
            if move.piece is 'bP' and move.fromcell.absfiledifference(move.tocell):
                enpassantcells.append(move.tocell.sumcoordinate(0, 1))
            if move.iswhiteturn:
                if move.piece == 'wK':
                    castling['wk'] = [False, False]
                    castling['wq'] = [False, False]
                if move.piece == 'wR':
                    if move.fromcell == h1:
                        castling['wk'] = [False, False]
                    elif move.fromcell == a1:
                        castling['wq'] = [False, False]
            else:
                if move.piece == 'bK':
                    castling['bk'] = [False, False]
                    castling['bq'] = [False, False]
                if move.piece == 'bR':
                    if move.fromcell == h8:
                        castling['bk'] = [False, False]
                    elif move.fromcell == a8:
                        castling['bq'] = [False, False]
        else:
            if move.iswhiteturn:
                if move.iskingcastling:
                    occupiedcells.remove(e1)
                    whiteoccupiedcells.remove(e1)
                    whiteking.remove(e1)
                    occupiedcells.append(g1)
                    whiteoccupiedcells.append(g1)
                    whiteking.append(g1)
                    occupiedcells.remove(h1)
                    whiteoccupiedcells.remove(h1)
                    whiterooks.remove(h1)
                    occupiedcells.append(f1)
                    whiteoccupiedcells.append(f1)
                    whiterooks.append(f1)
                    castling['wk'] = [False, False]
                if move.isqueencastling:
                    occupiedcells.remove(e1)
                    whiteoccupiedcells.remove(e1)
                    whiteking.remove(e1)
                    occupiedcells.append(c1)
                    whiteoccupiedcells.append(c1)
                    whiteking.append(c1)
                    occupiedcells.remove(a1)
                    whiteoccupiedcells.remove(a1)
                    whiterooks.remove(a1)
                    occupiedcells.append(d1)
                    whiteoccupiedcells.append(d1)
                    whiterooks.append(d1)
                    castling['wq'] = [False, False]
            else:
                if move.iskingcastling:
                    occupiedcells.remove(e8)
                    blackoccupiedcells.remove(e8)
                    blackking.remove(e8)
                    occupiedcells.append(g8)
                    blackoccupiedcells.append(g8)
                    blackking.append(g8)
                    occupiedcells.remove(h8)
                    blackoccupiedcells.remove(h8)
                    blackrooks.remove(h8)
                    occupiedcells.append(f8)
                    blackoccupiedcells.append(f8)
                    blackrooks.append(f8)
                    castling['bk'] = [False, False]
                if move.isqueencastling:
                    occupiedcells.remove(e8)
                    blackoccupiedcells.remove(e8)
                    blackking.remove(e8)
                    occupiedcells.append(c8)
                    blackoccupiedcells.append(c8)
                    blackking.append(c8)
                    occupiedcells.remove(a8)
                    blackoccupiedcells.remove(a8)
                    blackrooks.remove(a8)
                    occupiedcells.append(d8)
                    blackoccupiedcells.append(d8)
                    blackrooks.append(d8)
                    castling['bq'] = [False, False]
        self.update_castling_rights()

    def undomove(self, move):
        global castling, enpassantcells, whitecastlingrights, blackcastlingrights
        activeoccupiedlist, enemyoccupiedlist = self._get_active_occupied_list(move.iswhiteturn)
        activepiecelist = self._get_list_by_piece(move.piece)
        capturedpiecelist = self._get_list_by_piece(move.capturedpiece)
        promotionlist = self._get_list_by_piece(move.promotionto)
        if activepiecelist is not None:
            occupiedcells.remove(move.tocell)
            activeoccupiedlist.remove(move.tocell)
            if promotionlist is not None:
                promotionlist.remove(move.tocell)
            else:
                activepiecelist.remove(move.tocell)
            if capturedpiecelist is not None:
                if move.isenpassant:
                    sumcoor = {True: (0, -1), False: (0, 1)}
                    hitcell = move.tocell.sumcoordinate(sumcoor[move.iswhiteturn])
                else:
                    hitcell = move.tocell
                occupiedcells.append(hitcell)
                enemyoccupiedlist.append(hitcell)
                capturedpiecelist.append(hitcell)
            occupiedcells.append(move.fromcell)
            activeoccupiedlist.append(move.fromcell)
            activepiecelist.append(move.fromcell)
        else:
            if move.iswhiteturn:
                if move.iskingcastling:
                    occupiedcells.remove(g1)
                    whiteoccupiedcells.remove(g1)
                    whiteking.remove(g1)
                    occupiedcells.append(e1)
                    whiteoccupiedcells.append(e1)
                    whiteking.append(e1)
                    occupiedcells.remove(f1)
                    whiteoccupiedcells.remove(f1)
                    whiterooks.remove(f1)
                    occupiedcells.append(h1)
                    whiteoccupiedcells.append(h1)
                    whiterooks.append(h1)
                    whitecastlingrights['wk'] = True
                if move.isqueencastling:
                    occupiedcells.remove(c1)
                    whiteoccupiedcells.remove(c1)
                    whiteking.remove(c1)
                    occupiedcells.append(e1)
                    whiteoccupiedcells.append(e1)
                    whiteking.append(e1)
                    occupiedcells.remove(d1)
                    whiteoccupiedcells.remove(d1)
                    whiterooks.remove(d1)
                    occupiedcells.append(a1)
                    whiteoccupiedcells.append(a1)
                    whiterooks.append(a1)
                    whitecastlingrights['wq'] = True
            else:
                if move.iskingcastling:
                    occupiedcells.remove(g8)
                    blackoccupiedcells.remove(g8)
                    blackking.remove(g8)
                    occupiedcells.append(e8)
                    blackoccupiedcells.append(e8)
                    blackking.append(e8)
                    occupiedcells.remove(f8)
                    blackoccupiedcells.remove(f8)
                    blackrooks.remove(f8)
                    occupiedcells.append(h8)
                    blackoccupiedcells.append(h8)
                    blackrooks.append(h8)
                    blackcastlingrights['bk'] = True
                if move.isqueencastling:
                    occupiedcells.remove(c8)
                    blackoccupiedcells.remove(c8)
                    blackking.remove(c8)
                    occupiedcells.append(e8)
                    blackoccupiedcells.append(e8)
                    blackking.append(e8)
                    occupiedcells.remove(d8)
                    blackoccupiedcells.remove(d8)
                    blackrooks.remove(d8)
                    occupiedcells.append(a8)
                    blackoccupiedcells.append(a8)
                    blackrooks.append(a8)
                    blackcastlingrights['bq'] = True
        castling = self.castlings.pop(-1)
        whitecastlingrights, blackcastlingrights = self.castlingrights.pop(-1)
        enpassantcells = self.enpassants.pop(-1)
        self.moves.remove(move)

    @staticmethod
    def isboardvalid():
        if len(whiteking) != 1:
            return False
        if len(blackking) != 1:
            return False
        for enp in enpassantcells:
            if enp not in alg.enpassantlist:
                return False
        return True

    @staticmethod
    def is_white_king_in_check():
        kingcell = whiteking[0]
        try:
            targetlist = whitekingpawnrange[kingcell]
            for cell in targetlist:
                if cell in blackpawns:
                    return True
        except KeyError:
            pass
        targetlist = kingstep[kingcell]
        for cell in targetlist:
            if cell in blackking:
                return True
        targetlist = knightstep[kingcell]
        for cell in targetlist:
            if cell in blackknights:
                return True
        targetsuperlist = rookstep[kingcell]
        for targetlist in targetsuperlist:
            for cell in targetlist:
                if cell in whiteoccupiedcells:
                    break
                if cell in blackrooks or cell in blackqueen:
                    return True
        targetsuperlist = bishopstep[kingcell]
        for targetlist in targetsuperlist:
            for cell in targetlist:
                if cell in whiteoccupiedcells:
                    break
                if cell in blackbishops or cell in blackqueen:
                    return True
        return False

    @staticmethod
    def is_black_king_in_check():
        kingcell = blackking[0]
        try:
            targetlist = blackkingpawnrange[kingcell]
            for cell in targetlist:
                if cell in whitepawns:
                    return True
        except KeyError:
            pass
        targetlist = kingstep[kingcell]
        for cell in targetlist:
            if cell in whiteking:
                return True
        targetlist = knightstep[kingcell]
        for cell in targetlist:
            if cell in whiteknights:
                return True
        targetsuperlist = rookstep[kingcell]
        for targetlist in targetsuperlist:
            for cell in targetlist:
                if cell in blackoccupiedcells:
                    break
                if cell in whiterooks or cell in whitequeen:
                    return True
        targetsuperlist = bishopstep[kingcell]
        for targetlist in targetsuperlist:
            for cell in targetlist:
                if cell in blackoccupiedcells:
                    break
                if cell in whitebishops or cell in whitequeen:
                    return True
        return False

    @staticmethod
    def is_stalemate():
        if len(whitepawns) > 0 or len(blackpawns) > 0:
            return False
        whitequeencount = len(whitequeen)
        blackqueencount = len(blackqueen)
        whiterookcount = len(whiterooks)
        blackrookcount = len(blackrooks)
        whiteknightcount = len(whiteknights)
        blackknightcount = len(blackknights)
        whitebishopcount = len(whitebishops)
        blackbishopcount = len(blackbishops)
        insufficientmaterialtables = [(1, 1, 0, 0, 0, 0, 0, 0), (0, 0, 1, 1, 0, 0, 0, 0), (0, 0, 0, 0, 2, 0, 0, 0),
                                      (0, 0, 0, 0, 0, 2, 0, 0), (0, 0, 0, 0, 0, 0, 1, 1), (0, 0, 0, 0, 0, 0, 1, 0),
                                      (0, 0, 0, 0, 0, 0, 0, 1), (0, 0, 0, 0, 1, 0, 0, 0), (0, 0, 0, 0, 0, 1, 0, 0),
                                      (0, 0, 0, 0, 0, 0, 0, 0)]
        if (whitequeencount, blackqueencount, whiterookcount, blackrookcount, whiteknightcount, blackknightcount,
                whitebishopcount, blackbishopcount) in insufficientmaterialtables:
            return True
        else:
            return False

    @staticmethod
    def count_doubled_pawns():
        whitecount = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0}
        blackcount = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0}
        for cell in whitepawns:
            whitecount[cell.getrank()] += 1
        for cell in blackpawns:
            blackcount[cell.getrank()] += 1
        whitedoubled = 0
        blackdoubled = 0
        for count in whitecount.values():
            if count > 1:
                whitedoubled += 1
        for count in blackcount.values():
            if count > 1:
                blackdoubled += 1
        return whitedoubled, blackdoubled

    @staticmethod
    def count_blocked_pawns():
        whiteblocked = 0
        blackblocked = 0
        for cell in whitepawns:
            tocell = cell.sumcoordinate(0, 1)
            if tocell in occupiedcells:
                whiteblocked += 1
        for cell in blackpawns:
            tocell = cell.sumcoordinate(0, -1)
            if tocell in occupiedcells:
                blackblocked += 1
        return whiteblocked, blackblocked

    @staticmethod
    def count_isolated_pawns():
        check = {'a': ('b',), 'b': ('a', 'c'), 'c': ('b', 'd'), 'd': ('c', 'e'), 'e': ('d', 'f'), 'f': ('e', 'g'),
                 'g': ('f', 'h'), 'h': ('g',)}
        ranklist = []
        whiteisolated = 0
        for cell in whitepawns:
            ranklist.append(cell.getrank())
        for rank in ranklist:
            isolated = True
            for ranktocheck in check[rank]:
                if ranktocheck in ranklist:
                    isolated = False
                    break
            if isolated:
                whiteisolated += 1
        ranklist = []
        blackisolated = 0
        for cell in blackpawns:
            ranklist.append(cell.getrank())
        for rank in ranklist:
            isolated = True
            for ranktocheck in check[rank]:
                if ranktocheck in ranklist:
                    isolated = False
            if isolated:
                blackisolated += 1
        return whiteisolated, blackisolated

    @staticmethod
    def get_white_pieces():
        for cell in whitepawns:
            yield 'wP', cell
        for cell in whiterooks:
            yield 'wR', cell
        for cell in whiteknights:
            yield 'wR', cell
        for cell in whitebishops:
            yield 'wB', cell
        for cell in whitequeen:
            yield 'wQ', cell
        for cell in whiteking:
            yield 'wK', cell

    @staticmethod
    def get_black_pieces():
        for cell in blackpawns:
            yield 'bP', cell
        for cell in blackrooks:
            yield 'bR', cell
        for cell in blackknights:
            yield 'bR', cell
        for cell in blackbishops:
            yield 'bB', cell
        for cell in blackqueen:
            yield 'bQ', cell
        for cell in blackking:
            yield 'bK', cell

    @staticmethod
    def get_white_castling_rights():
        return whitecastlingrights

    @staticmethod
    def get_black_castling_rights():
        return blackcastlingrights

    @staticmethod
    def get_enpassant_cells():
        return enpassantcells

    def __str__(self):
        # solo per debug
        # print("occupiedcells: ", occupiedcells)
        # print("whiteoccupiedcells: ", whiteoccupiedcells)
        # print("blackoccupiedcells: ", blackoccupiedcells)
        # print("whitepawns: ", whitepawns)
        # print("blackpawns: ", blackpawns)
        # print("promotioncells: ", promotioncells)
        # print("whiterooks: ", whiterooks)
        # print("blackrooks: ", blackrooks)
        # print("whiteknights: ", whiteknights)
        # print("blackknights: ", blackknights)
        # print("whitebishops: ", whitebishops)
        # print("blackbishops: ", blackbishops)
        # print("whitequeen: ", whitequeen)
        # print("blackqueen: ", blackqueen)
        # print("whiteking: ", whiteking)
        # print("blackking: ", blackking)
        # print("enpassantcells: ", enpassantcells)
        # print("whitecastlingrights: ", whitecastlingrights)
        # print("blackcastlingrights: ", blackcastlingrights)

        board = {}
        for cell in alg.celllist:
            if cell in whitepawns:
                board[cell] = 'wP'
            elif cell in blackpawns:
                board[cell] = 'bP'
            elif cell in whiteknights:
                board[cell] = 'wN'
            elif cell in blackknights:
                board[cell] = 'bN'
            elif cell in whitebishops:
                board[cell] = 'wB'
            elif cell in blackbishops:
                board[cell] = 'bB'
            elif cell in whiterooks:
                board[cell] = 'wR'
            elif cell in blackrooks:
                board[cell] = 'bR'
            elif cell in whitequeen:
                board[cell] = 'wQ'
            elif cell in blackqueen:
                board[cell] = 'bQ'
            elif cell in whiteking:
                board[cell] = 'wK'
            elif cell in blackking:
                board[cell] = 'bK'
            else:
                board[cell] = '--'
        strlist = [str(board[coordinate]) for coordinate in alg.celllist]
        result = ("|%s|%s|%s|%s|%s|%s|%s|%s|\n" +
                  "|%s|%s|%s|%s|%s|%s|%s|%s|\n" +
                  "|%s|%s|%s|%s|%s|%s|%s|%s|\n" +
                  "|%s|%s|%s|%s|%s|%s|%s|%s|\n" +
                  "|%s|%s|%s|%s|%s|%s|%s|%s|\n" +
                  "|%s|%s|%s|%s|%s|%s|%s|%s|\n" +
                  "|%s|%s|%s|%s|%s|%s|%s|%s|\n" +
                  "|%s|%s|%s|%s|%s|%s|%s|%s|\n") % tuple(strlist)

        return result


class ListPieceHashValue(ListPiece):
    def __init__(self, hashgenerator):
        super().__init__()
        self.hashgenerator = hashgenerator
        self.originhashvalue = None
        self.hashvalues = []
        self.changedcastling = []
        self.changedenpassant = []

    def set_origin_hash_value(self, activecolor):
        self.originhashvalue = self.hashgenerator.gethashkey(self, activecolor)

    def gethashkey(self):
        if len(self.moves) <= 1:
            return self.originhashvalue
        else:
            return self.hashvalues[-1]

    def applymove(self, move):
        super().applymove(move)
        self.update_castling_rights()
        self.changedcastling = [False, False, False, False]
        self.changedenpassant = [False, False, False, False, False, False, False, False]
        lastwhitecastlingright, lastblackcastlingright = self.castlingrights[-1]
        if whitecastlingrights['wk'] != lastwhitecastlingright['wk']:
            self.changedcastling[0] = True
        if whitecastlingrights['wq'] != lastwhitecastlingright['wq']:
            self.changedcastling[1] = True
        if blackcastlingrights['bk'] != lastblackcastlingright['bk']:
            self.changedcastling[2] = True
        if blackcastlingrights['bq'] != lastblackcastlingright['bq']:
            self.changedcastling[3] = True
        lastenpassantcells = self.enpassants[-1]
        tmp = []
        for cell in enpassantcells:
            if cell not in lastenpassantcells:
                tmp.append(cell)
        for cell in tmp:
            index = cell.getrankvalue() - 1
            self.changedenpassant[index] = True
        activecolor = not self.moves[-1].iswhiteturn
        newhashvalue = self.hashgenerator.updatehashkey(self.gethashkey(), self, activecolor)
        self.hashvalues.append(newhashvalue)

    def undomove(self, move):
        super().undomove(move)
        self.hashvalues.pop(-1)


if __name__ == '__main__':
    l = ListPiece()
    l.add_white_king(e1)
    l.add_black_king(e8)
    print(l)
    print(l.is_stalemate())

    """
    for move in black_generator_moves():
        print(move)
    """
    """
    knightstep = {}
    deltas = ((-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, 1), (-2, -1))
    for fromcell in alg.celllist:
        destination = []
        for delta in deltas:
            try:
                tocell = fromcell.sumcoordinate(delta[0], delta[1])
                destination.append(tocell)
            except alg.CoordinateException:
                pass
        knightstep[fromcell] = tuple(destination)
    for key, value in knightstep.items():
        line = str(key) + ": ("
        for cell in value:
            if cell == value[-1]:
                line += str(cell) + ")"
            else:
                line += str(cell) + ", "
        line += ","
        print(line)
    """
    """
    kingstep = {}
    deltas = ((-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0))
    for fromcell in alg.celllist:
        destination = []
        for delta in deltas:
            try:
                tocell = fromcell.sumcoordinate(delta[0], delta[1])
                destination.append(tocell)
            except alg.CoordinateException:
                pass
        kingstep[fromcell] = tuple(destination)
    msg = ""
    for key, value in kingstep.items():
        line = str(key) + ": ("
        for cell in value:
            if cell == value[-1]:
                line += str(cell) + ")"
            else:
                line += str(cell) + ", "
        line += ", "
        msg += line
    print(msg)
    """
    """
    rookstep = {}
    deltas = ((0, 1), (1, 0), (0, -1), (-1, 0))     # rook
    # deltas = ((-1, 1), (1, 1), (1, -1), (-1, -1))   # bishop
    for fromcell in alg.celllist:
        destination = []
        for delta in deltas:
            subdestination = []
            for slide in range(1, 8):
                try:
                    tocell = fromcell.sumcoordinate(delta[0] * slide, delta[1] * slide)
                    subdestination.append(tocell)
                except alg.CoordinateException:
                    pass
            destination.append(tuple(subdestination))
        rookstep[fromcell] = tuple(destination)
    msg = "{ "
    isfirstkey = True
    for key, superlist in rookstep.items():
        if isfirstkey:
            line = str(key) + ": ("
            isfirstkey = False
        else:
            line = ", " + str(key) + ": ("
        isfirstsublist = True
        for sublist in superlist:
            if isfirstsublist:
                line += "("
                isfirstsublist = False
            else:
                line += ", ("
            isfirstcell = True
            for cell in sublist:
                if isfirstcell:
                    line += str(cell)
                    isfirstcell = False
                else:
                    line += ", " + str(cell)
            line += ")"
        line += ')'
        msg += line
    msg += "}"
    print(msg)
    """