"""Draws every figure of the project report with NetworkX + Matplotlib.
Run from the repository root:  python src/make_figures.py
Output: figures/chapter_1 ... figures/chapter_5  (files named Fig_<chapter>.<number>_<key>.png)"""
import os, itertools
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx

OUT = "figures"
BLUE, NAVY, ORANGE, GREEN, RED, GREY, PINK, PURPLE = "#dbe9f6", "#1f4e79", "#fde9d4", "#d9ead3", "#c00000", "#9aa9b5", "#f4b6b6", "#e6d9f2"
COL = {0: "#f4b6b6", 1: "#b7dca8", 2: "#a9c8ee", 3: "#fff3b0"}

def canvas(w=6, h=4, title=None, n=1, m=1):
    f, axs = plt.subplots(m, n, figsize=(w, h))
    axs = [axs] if n * m == 1 else list(axs.flatten())
    for a in axs:
        a.axis("off"); a.margins(0.12)
    if title and n * m == 1: axs[0].set_title(title, fontsize=13, pad=8)
    return f, (axs[0] if n * m == 1 else axs)

def draw(ax, G, pos, nc=BLUE, nec=NAVY, ns=900, fs=12, labels=None, edgelist=None, ecol="#455a6b", ew=2.4,
         directed=False, rad=0.0, style="solid", elabels=None, elp=0.5, efs=11, nodelist=None, lcol="black"):
    nx.draw_networkx_nodes(G, pos, ax=ax, nodelist=nodelist, node_color=nc, edgecolors=nec, node_size=ns, linewidths=2)
    nx.draw_networkx_edges(G, pos, ax=ax, edgelist=edgelist, edge_color=ecol, width=ew, style=style, node_size=ns,
                           arrows=True, arrowstyle="-|>" if directed else "-", arrowsize=18,
                           connectionstyle=f"arc3,rad={rad}")
    nx.draw_networkx_labels(G, pos, ax=ax, labels=labels, font_size=fs, font_weight="bold", font_color=lcol)
    if elabels:
        nx.draw_networkx_edge_labels(G, pos, ax=ax, edge_labels=elabels, label_pos=elp, font_size=efs,
                                     rotate=False, connectionstyle=f"arc3,rad={rad}",
                                     bbox=dict(fc="white", ec="none", pad=0.8))

def note(ax, x, y, t, fs=10, **k): ax.text(x, y, t, ha="center", va="center", fontsize=fs, **k)

def save(f, ch, num, key):
    d = os.path.join(OUT, f"chapter_{ch}"); os.makedirs(d, exist_ok=True)
    f.savefig(os.path.join(d, f"Fig_{ch}.{num}_{key}.png"), dpi=200, bbox_inches="tight", facecolor="white"); plt.close(f)

WG = nx.Graph(); WG.add_weighted_edges_from([("A","B",4),("A","C",2),("B","C",1),("B","D",5),("C","D",8),("C","E",10),("D","E",2)])
WPOS = {"A": (0, 1), "B": (2, 2.4), "C": (2, -0.4), "D": (4, 2.4), "E": (5.4, 0.4)}
WLAB = {(u, v): d["weight"] for u, v, d in WG.edges(data=True)}
FIGS = []
def fig(ch, key):
    def deco(fn): FIGS.append((ch, key, fn)); return fn
    return deco

# ------------------------------------------------------------------ Chapter 1
@fig(1, "graph_vs_coordinate")
def _():
    f, (a, b) = canvas(8, 3.4, n=2)
    G = nx.Graph([(1,2),(1,3),(2,3),(3,4)]); draw(a, G, {1:(0,1),2:(2,1),3:(1,-0.2),4:(3,-0.2)})
    a.set_title("Graph-theory graph", fontsize=11); note(a, 1.5, -1.1, "Vertices and edges show connections")
    b.axis("on"); xs = [-2,-1,0,1,2]; b.plot(xs, [x*x for x in xs], "o-", color="#b04a4a"); b.grid(alpha=.3)
    b.set_title("Coordinate graph  y = x²", fontsize=11); b.set_xlabel("x"); b.set_ylabel("y")
    return f
@fig(1, "history_timeline")
def _():
    yrs = [("1736", "Euler solves the\nKönigsberg bridges"), ("1847", "Kirchhoff: graphs\nin circuits"), ("1852", "Four Colour\nProblem posed"),
           ("1930", "Kuratowski: planar\ngraphs"), ("1976", "Four Colour Theorem\nproved by computer"), ("Today", "Networks, AI and\ndata science")]
    G = nx.path_graph([y for y, _ in yrs]); pos = {y: (i, 0) for i, (y, _) in enumerate(yrs)}
    f, a = canvas(9, 2.8); draw(a, G, pos, ns=1500, fs=9)
    for i, (y, t) in enumerate(yrs): a.text(i, 0.55 if i % 2 == 0 else -0.55, t, ha="center", va="center", fontsize=9)
    a.set_ylim(-1, 1); return f
@fig(1, "simple_graph")
def _():
    G = nx.Graph([("A","B"),("A","C"),("B","C"),("C","D"),("D","E")]); pos = {"A":(0,2),"B":(2,2),"C":(1,0),"D":(3,0),"E":(5,0)}
    f, a = canvas(6, 3.6, "A simple graph G = (V, E)"); draw(a, G, pos)
    note(a, 2.5, -1.1, "V = {A, B, C, D, E}      E = {AB, AC, BC, CD, DE}", 11); return f
@fig(1, "application_areas")
def _():
    areas = ["Mathematics", "Computer\nscience", "Engineering", "Communication", "Transportation", "Social\nnetworks"]
    G = nx.star_graph(6); pos = nx.circular_layout(G); pos[0] = (0, 0)
    f, a = canvas(7.4, 5.4, "Applications of graph theory")
    nx.draw_networkx_edges(G, pos, ax=a, edge_color=GREY, width=2)
    nx.draw_networkx_nodes(G, pos, nodelist=[0], ax=a, node_color=ORANGE, edgecolors="#9c5a00", node_size=6200, linewidths=2)
    nx.draw_networkx_nodes(G, pos, nodelist=range(1, 7), ax=a, node_color=BLUE, edgecolors=NAVY, node_size=5600, linewidths=2)
    nx.draw_networkx_labels(G, pos, labels={0: "GRAPH\nTHEORY", **{i + 1: t for i, t in enumerate(areas)}}, ax=a, font_size=8, font_weight="bold")
    return f

# ------------------------------------------------------------------ Chapter 2
@fig(2, "basic_terminology")
def _():
    G = nx.Graph([("A","B"),("A","C"),("B","C"),("C","D")]); G.add_node("E")
    pos = {"A":(0,2),"B":(2,2),"C":(1,0.4),"D":(3,0),"E":(4,1.6)}
    f, a = canvas(6, 3.6, "Basic terminology"); draw(a, G, pos)
    note(a, 1, -0.6, "deg(C) = 3", 10, color="#7a5200"); note(a, 3.2, -0.6, "D: pendant vertex", 10, color="#6a1b9a")
    note(a, 4, 1.0, "E: isolated", 10, color="#c00000"); note(a, 2, -1.3, "A and B are adjacent (edge AB)", 10, color="#2e7d32"); return f
@fig(2, "walk_trail_path_cycle")
def _():
    f, ax = canvas(8, 5.2, n=2, m=2)
    def panel(a, G, pos, edges_num, title):
        draw(a, G, pos, ns=700, fs=10); nx.draw_networkx_edge_labels(G, pos, ax=a, edge_labels=edges_num, font_size=9, font_color=RED, rotate=False, bbox=dict(fc="white", ec="none", pad=.5))
        a.set_title(title, fontsize=10)
    panel(ax[0], nx.Graph([("A","B"),("B","C"),("B","D")]), {"A":(0,0),"B":(1,0),"C":(2,.8),"D":(2,-.8)}, {("A","B"):"1", ("B","C"):"2, 3", ("B","D"):"4"}, "Walk A–B–C–B–D (edge BC repeated)")
    panel(ax[1], nx.Graph([("A","B"),("B","C"),("C","D"),("D","B")]), {"A":(0,0),"B":(1,0),"C":(2,.8),"D":(2,-.8)}, {("A","B"):"1", ("B","C"):"2", ("C","D"):"3", ("D","B"):"4"}, "Trail A–B–C–D–B (no repeated edge)")
    panel(ax[2], nx.path_graph(["A","B","C","D"]), {"A":(0,0),"B":(1,0),"C":(2,0),"D":(3,0)}, {("A","B"):"1", ("B","C"):"2", ("C","D"):"3"}, "Path A–B–C–D (no repeated vertex)")
    panel(ax[3], nx.cycle_graph(["A","B","C","D"]), {"A":(0,0),"B":(1.4,0),"C":(1.4,1.4),"D":(0,1.4)}, {("A","B"):"1", ("B","C"):"2", ("C","D"):"3", ("D","A"):"4"}, "Cycle A–B–C–D–A")
    f.tight_layout(); return f
@fig(2, "euler_trail_circuit")
def _():
    f, (a, b) = canvas(9, 3.6, n=2)
    G = nx.Graph([("A","B"),("A","D"),("A","C"),("B","C"),("D","C")]); pos = {"A":(0,2),"B":(2,2),"D":(0,0),"C":(2,0)}
    draw(a, G, pos, nc=[PINK if v in "AC" else BLUE for v in G], nec=NAVY)
    nx.draw_networkx_edge_labels(G, pos, ax=a, edge_labels={("A","B"):"1",("B","C"):"2",("D","C"):"3",("A","D"):"4",("A","C"):"5"}, font_color=RED, font_size=10, bbox=dict(fc="white", ec="none", pad=.5), rotate=False)
    a.set_title("Euler trail A–B–C–D–A–C\n(odd vertices A, C in red)", fontsize=10)
    H = nx.Graph([("A","B"),("B","O"),("O","A"),("O","C"),("C","D"),("D","O")]); hp = {"A":(0,1),"B":(0,-1),"O":(1.5,0),"C":(3,1),"D":(3,-1)}
    draw(b, H, hp, nc=[ORANGE if v == "O" else BLUE for v in H])
    nx.draw_networkx_edge_labels(H, hp, ax=b, edge_labels={("A","B"):"1",("B","O"):"2",("O","C"):"3",("C","D"):"4",("D","O"):"5",("O","A"):"6"}, font_color=RED, font_size=10, bbox=dict(fc="white", ec="none", pad=.5), rotate=False)
    b.set_title("Euler circuit A–B–O–C–D–O–A\n(all degrees even)", fontsize=10); return f
@fig(2, "tree")
def _():
    G = nx.Graph([("A","B"),("A","C"),("B","D"),("B","E"),("C","F")]); pos = {"A":(2,2),"B":(1,1),"C":(3,1),"D":(0.4,0),"E":(1.6,0),"F":(3,0)}
    f, a = canvas(4.6, 3.6, "A tree: 6 vertices, 5 edges"); draw(a, G, pos); return f
@fig(2, "plane_graph_faces")
def _():
    G = nx.Graph([(0,1),(1,2),(2,3),(3,0),(0,2)]); pos = {0:(0,2),1:(3,2),2:(3,0),3:(0,0)}
    f, a = canvas(5, 3.8, "Plane graph: V = 4, E = 5, F = 3"); draw(a, G, pos, nc="#fff3d1", nec="#b8860b")
    note(a, 2.2, 1.45, "F₁", 12, weight="bold"); note(a, 0.8, 0.55, "F₂", 12, weight="bold"); note(a, 1.5, -0.9, "F₃ = outer face;  4 − 5 + 3 = 2", 10); return f

# ------------------------------------------------------------------ Chapter 3
@fig(3, "konigsberg_bridges")
def _():
    G = nx.MultiGraph(); pos = {"A":(0,2.4),"B":(0,-2.4),"C":(3.6,0),"D":(-1.6,0)}
    f, a = canvas(6.4, 5, "Königsberg: graph model of the seven bridges")
    nx.draw_networkx_nodes(nx.Graph([("A","B"),("C","D")]), pos, ax=a, node_color=[ORANGE,ORANGE,ORANGE,BLUE], edgecolors=NAVY, node_size=1000, linewidths=2, nodelist=["A","B","C","D"])
    nx.draw_networkx_labels(nx.Graph([("A","B"),("C","D")]), pos, ax=a, font_size=13, font_weight="bold")
    E = [("A","D",0.35,"b₁"),("A","D",-0.35,"b₂"),("B","D",-0.35,"b₃"),("B","D",0.35,"b₄"),("A","C",0,"b₅"),("B","C",0,"b₆"),("D","C",0,"b₇")]
    for u, v, r, l in E:
        g = nx.Graph([(u, v)])
        nx.draw_networkx_edges(g, pos, ax=a, width=2.4, edge_color="#455a6b", arrows=True, arrowstyle="-", node_size=1000, connectionstyle=f"arc3,rad={r}")
        nx.draw_networkx_edge_labels(g, pos, ax=a, edge_labels={(u, v): l}, font_size=10, connectionstyle=f"arc3,rad={r}", bbox=dict(fc="white", ec="none", pad=.6), rotate=False)
    note(a, 0, -3.5, "A north bank, B south bank, C east region, D island\ndeg(A) = deg(B) = deg(C) = 3, deg(D) = 5", 10); return f
@fig(3, "map_adjacency_graph")
def _():
    G = nx.Graph([("1","2"),("1","3"),("1","4"),("2","3"),("3","4"),("2","5"),("3","5"),("4","6"),("3","6"),("5","6")])
    assert nx.check_planarity(G)[0]
    pos = {"1":(0,1.5),"2":(1.6,3),"3":(2.2,1.2),"4":(1.6,-0.4),"5":(4,2.2),"6":(4,0.2)}
    cols = nx.coloring.greedy_color(G, strategy="largest_first"); assert all(cols[u] != cols[v] for u, v in G.edges())
    f, a = canvas(5.4, 4, f"Six map regions as a planar graph, {len(set(cols.values()))} colours"); draw(a, G, pos, nc=[COL[cols[v]] for v in G], nec="#333", ns=1000); return f
@fig(3, "three_utilities_k33")
def _():
    G = nx.complete_bipartite_graph(3, 3); pos = {**{i: (0, 2 - i) for i in range(3)}, **{i + 3: (3, 2 - i) for i in range(3)}}
    lab = {0:"H₁",1:"H₂",2:"H₃",3:"W",4:"E",5:"G"}
    f, a = canvas(5, 4, "Three Utilities Problem: K₃,₃"); draw(a, G, pos, nc=[BLUE]*3 + [ORANGE]*3, labels=lab, ns=900); note(a, 1.5, -1.5, "6 vertices, 9 edges", 10); return f
@fig(3, "tsp_four_cities")
def _():
    G = nx.complete_graph(["A","B","C","D"]); pos = {"A":(0,3),"B":(4,3),"D":(0,0),"C":(4,0)}
    d = {("A","B"):10,("A","C"):15,("A","D"):20,("B","C"):35,("B","D"):25,("C","D"):30}
    tour = [("A","B"),("B","D"),("D","C"),("C","A")]
    f, a = canvas(6, 4.6, "Travelling Salesman Problem: four cities")
    on = [e for e in G.edges() if e in tour or e[::-1] in tour]; off = [e for e in G.edges() if e not in on]
    draw(a, G, pos, nc="#fff3d1", nec="#b8860b", edgelist=off, ecol=GREY, ew=2); nx.draw_networkx_edges(G, pos, ax=a, edgelist=on, edge_color=RED, width=4, node_size=900)
    for e, lp in [(("A","B"),.5),(("C","D"),.5),(("A","D"),.5),(("B","C"),.5),(("A","C"),.28),(("B","D"),.28)]:
        nx.draw_networkx_edge_labels(G, pos, ax=a, edge_labels={e: d[e]}, label_pos=lp, font_size=11, bbox=dict(fc="white", ec="none", pad=.6), rotate=False)
    note(a, 2, -0.9, "Optimal tour A–B–D–C–A: 10 + 25 + 30 + 15 = 80", 10); return f
@fig(3, "knights_tour_5x5")
def _():
    rc = [(0,0),(2,1),(4,0),(3,2),(4,4),(2,3),(0,4),(1,2),(3,3),(1,4),(0,2),(1,0),(3,1),(4,3),(2,4),(0,3),(1,1),(3,0),(4,2),(3,4),(1,3),(0,1),(2,2),(4,1),(2,0)]
    for (r1,c1),(r2,c2) in zip(rc, rc[1:]): assert sorted((abs(r1-r2),abs(c1-c2))) == [1,2]
    G = nx.path_graph(range(1, 26)); pos = {i + 1: (c, -r) for i, (r, c) in enumerate(rc)}
    f, a = canvas(5, 5, "Knight's tour of a 5 × 5 board")
    for r in range(5):
        for c in range(5): a.add_patch(plt.Rectangle((c-.5, -r-.5), 1, 1, fc="#f0dab5" if (r+c) % 2 == 0 else "#b58863", ec="white", zorder=0))
    draw(a, G, pos, nc="white", nec=NAVY, ns=330, fs=8, ecol=NAVY, ew=1.6); a.set_xlim(-.6, 4.6); a.set_ylim(-4.6, .6); return f
@fig(3, "chinese_postman")
def _():
    G = nx.Graph([("A","B"),("A","D"),("A","C"),("B","C"),("D","C"),("C","E")]); pos = {"A":(0,2),"B":(2.5,2),"D":(0,0),"C":(2.5,0),"E":(5,0)}
    f, a = canvas(6, 3.6, "Chinese Postman: odd vertices A and E")
    draw(a, G, pos, nc=[PINK if v in "AE" else GREEN for v in G], nec="#555")
    nx.draw_networkx_edges(G, pos, ax=a, edgelist=[("A","C"),("C","E")], edge_color=RED, width=3, style="dashed", node_size=900)
    note(a, 2.5, -0.9, "Repeat A–C and C–E (dashed): closed route of length 6 + 2 = 8", 10); return f
@fig(3, "shortest_path")
def _():
    f, a = canvas(6.2, 4, "Shortest path from A to E"); p = nx.dijkstra_path(WG, "A", "E"); pe = list(zip(p, p[1:]))
    draw(a, WG, WPOS, elabels=WLAB, ecol=GREY, ew=2)
    nx.draw_networkx_edges(WG, WPOS, ax=a, edgelist=pe, edge_color=RED, width=4, node_size=900)
    nx.draw_networkx_edge_labels(WG, WPOS, ax=a, edge_labels=WLAB, font_size=11, bbox=dict(fc="white", ec="none", pad=.8), rotate=False); note(a, 2.7, -1.3, "A–C–B–D–E: 2 + 1 + 5 + 2 = 10", 10); return f
@fig(3, "minimum_spanning_tree")
def _():
    G = WG.copy(); G.add_edge("B", "E", weight=7); lab = {(u, v): d["weight"] for u, v, d in G.edges(data=True)}
    t = nx.minimum_spanning_tree(G); f, a = canvas(6.2, 4, "Minimum spanning tree")
    draw(a, G, WPOS, nc="#fff3d1", nec="#b8860b", elabels=lab, ecol=GREY, ew=2)
    nx.draw_networkx_edges(G, WPOS, ax=a, edgelist=list(t.edges()), edge_color="#38761d", width=4.5, node_size=900)
    nx.draw_networkx_edge_labels(G, WPOS, ax=a, edge_labels=lab, font_size=11, bbox=dict(fc="white", ec="none", pad=.8), rotate=False); note(a, 2.7, -1.3, "Tree weight 2 + 1 + 5 + 2 = 10", 10); return f
@fig(3, "flow_network")
def _():
    G = nx.DiGraph(); cap = {("S","A"):8,("S","B"):5,("A","B"):3,("A","T"):5,("B","T"):8}; G.add_edges_from(cap)
    pos = {"S":(0,1),"A":(2,2),"B":(2,0),"T":(4,1)}; f, a = canvas(6, 3.8, "Flow network: capacities on arcs")
    draw(a, G, pos, nc=ORANGE, nec="#9c5a00", directed=True, elabels=cap, ns=1000); note(a, 2, -0.9, "Maximum flow = 13 (cut {SA, SB} = 8 + 5)", 10); return f
@fig(3, "perfect_matching")
def _():
    G = nx.Graph([("S1","P1"),("S1","P2"),("S2","P2"),("S2","P3"),("S3","P1"),("S3","P3")]); pos = {**{f"S{i}": (0, 3 - i) for i in (1,2,3)}, **{f"P{i}": (3, 3 - i) for i in (1,2,3)}}
    m = [("S1","P2"),("S2","P3"),("S3","P1")]; f, a = canvas(5, 3.8, "Perfect matching: students and projects")
    draw(a, G, pos, nc=[BLUE]*3 + [ORANGE]*3, nodelist=list(G), ecol=GREY, ew=1.8); nx.draw_networkx_edges(G, pos, ax=a, edgelist=m, edge_color="#38761d", width=4.5, node_size=900); return f

# ------------------------------------------------------------------ Chapter 4
def matrix_text(a, M, x, y, title):
    a.text(x, y + 0.9, title, ha="center", fontsize=10)
    a.text(x, y, "\n".join("[ " + "  ".join(str(v) for v in row) + " ]" for row in M), ha="center", va="center", family="monospace", fontsize=12)
@fig(4, "adjacency_matrix")
def _():
    f, (a, b) = canvas(7.4, 3.2, n=2); G = nx.complete_graph(["A","B","C"]); draw(a, G, {"A":(0,2),"B":(2,2),"C":(1,0.3)}); a.set_title("K₃", fontsize=11)
    A = nx.to_numpy_array(G, dtype=int); matrix_text(b, A.tolist(), 0, 0, "Adjacency matrix (rows A, B, C)"); b.set_xlim(-2, 2); b.set_ylim(-1.5, 1.5); return f
@fig(4, "incidence_matrix")
def _():
    f, (a, b) = canvas(7.4, 3.2, n=2); G = nx.Graph(); G.add_edges_from([("A","B"),("A","C"),("B","C")]); draw(a, G, {"A":(0,2),"B":(2,2),"C":(1,0.3)})
    nx.draw_networkx_edge_labels(G, {"A":(0,2),"B":(2,2),"C":(1,0.3)}, ax=a, edge_labels={("A","B"):"e₁",("A","C"):"e₂",("B","C"):"e₃"}, font_size=10, rotate=False)
    a.set_title("Triangle with edges e₁ = AB, e₂ = AC, e₃ = BC", fontsize=9)
    M = nx.incidence_matrix(G, edgelist=[("A","B"),("A","C"),("B","C")], nodelist=["A","B","C"]).toarray().astype(int).tolist()
    matrix_text(b, M, 0, 0, "Incidence matrix (rows A, B, C; columns e₁, e₂, e₃)"); b.set_xlim(-2, 2); b.set_ylim(-1.5, 1.5); return f
TREE = nx.Graph([("A","B"),("A","C"),("B","D"),("B","E"),("C","F")]); TPOS = {"A":(2,2),"B":(1,1),"C":(3,1),"D":(0.4,0),"E":(1.6,0),"F":(3,0)}
@fig(4, "adjacency_list")
def _():
    f, (a, b) = canvas(7.6, 3.4, n=2); draw(a, TREE, TPOS)
    b.text(0, 0, "\n".join(f"{v} → {', '.join(sorted(TREE[v]))}" for v in sorted(TREE)), ha="center", va="center", family="monospace", fontsize=12, bbox=dict(fc="#f2f6fa", ec=GREY, boxstyle="round")); b.set_title("Adjacency list", fontsize=10); return f
@fig(4, "bfs_order")
def _():
    order = ["A"] + [v for u, v in nx.bfs_edges(TREE, "A")]; f, a = canvas(5.2, 3.8, "Breadth-first search from A")
    draw(a, TREE, TPOS, labels={v: f"{v}" for v in TREE}, nc=[BLUE]*6)
    for i, v in enumerate(order): a.text(TPOS[v][0] + .3, TPOS[v][1] + .28, str(i + 1), color=RED, fontsize=11, fontweight="bold")
    note(a, 2, -0.9, "Visiting order: " + ", ".join(order), 10); return f
@fig(4, "dfs_order")
def _():
    order = ["A"] + [v for u, v in nx.dfs_edges(TREE, "A")]; f, a = canvas(5.2, 3.8, "Depth-first search from A")
    draw(a, TREE, TPOS, nc=ORANGE, nec="#9c5a00")
    for i, v in enumerate(order): a.text(TPOS[v][0] + .3, TPOS[v][1] + .28, str(i + 1), color=RED, fontsize=11, fontweight="bold")
    note(a, 2, -0.9, "Visiting order: " + ", ".join(order), 10); return f
@fig(4, "dijkstra_distances")
def _():
    dist = nx.single_source_dijkstra_path_length(WG, "A"); p = nx.dijkstra_path(WG, "A", "E"); f, a = canvas(6.2, 4, "Dijkstra from A: final distances")
    draw(a, WG, WPOS, labels={v: f"{v}\n{dist[v]}" for v in WG}, ns=1300, fs=10, elabels=WLAB, ecol=GREY, ew=2, nc="#fff3d1", nec="#b8860b")
    nx.draw_networkx_edges(WG, WPOS, ax=a, edgelist=list(zip(p, p[1:])), edge_color=RED, width=4, node_size=1300); nx.draw_networkx_edge_labels(WG, WPOS, ax=a, edge_labels=WLAB, font_size=11, bbox=dict(fc="white", ec="none", pad=.8), rotate=False); return f
@fig(4, "floyd_warshall_digraph")
def _():
    G = nx.DiGraph(); w = {(1,2):3,(1,4):7,(2,1):8,(2,3):2,(3,1):5,(3,4):1,(4,1):2}; G.add_edges_from(w)
    pos = {1:(0,2),2:(3,2),3:(3,0),4:(0,0)}; f, a = canvas(5.6, 4, "Digraph for Floyd–Warshall")
    draw(a, G, pos, directed=True, rad=0.18, elabels=w, elp=0.5, ns=900); return f
@fig(4, "prim_kruskal")
def _():
    G = WG.copy(); G.add_edge("B", "E", weight=7); lab = {(u, v): d["weight"] for u, v, d in G.edges(data=True)}
    f, (a, b) = canvas(6.4, 7.4, n=1, m=2)
    for ax, order, t in [(a, [("B","C"),("A","C"),("D","E"),("B","D")], "Kruskal: edges accepted in order"), (b, [("A","C"),("C","B"),("B","D"),("D","E")], "Prim from A: edges added in order")]:
        draw(ax, G, WPOS, nc="#fff3d1", nec="#b8860b", ecol=GREY, ew=1.8, elabels=lab, efs=10)
        nx.draw_networkx_edges(G, WPOS, ax=ax, edgelist=order, edge_color="#38761d", width=4.5, node_size=900); nx.draw_networkx_edge_labels(G, WPOS, ax=ax, edge_labels=lab, font_size=9, bbox=dict(fc="white", ec="none", pad=.6), rotate=False)
        for i, (u, v) in enumerate(order): ax.text((WPOS[u][0]+WPOS[v][0])/2, (WPOS[u][1]+WPOS[v][1])/2 + .32, f"({i+1})", color="#38761d", fontsize=10, fontweight="bold", ha="center")
        ax.set_title(t, fontsize=11)
    f.tight_layout(); return f
@fig(4, "topological_sort")
def _():
    G = nx.DiGraph([("A","C"),("B","C"),("C","D"),("C","E"),("D","F"),("E","F")]); pos = {"A":(0,1.6),"B":(0,0),"C":(2,0.8),"D":(4,1.6),"E":(4,0),"F":(6,0.8)}
    f, a = canvas(6.4, 3.4, "Topological order: A, B, C, D, E, F"); draw(a, G, pos, directed=True, nc=PURPLE, nec="#6a3d9a", ns=900); return f
@fig(4, "deadlock_graph")
def _():
    G = nx.DiGraph([("P1","R1"),("R1","P2"),("P2","R2"),("R2","P1")]); pos = {"P1":(0,2),"R1":(3,2),"P2":(3,0),"R2":(0,0)}
    f, a = canvas(5.2, 4, "Deadlock: a cycle in the resource graph"); draw(a, G, pos, directed=True, nc=[BLUE if v[0]=="P" else ORANGE for v in G], rad=0.15, ns=1000)
    note(a, 1.5, -0.8, "P₁ holds R₂ and requests R₁;  P₂ holds R₁ and requests R₂", 9); return f
@fig(4, "register_interference_graph")
def _():
    G = nx.Graph([("t1","t2"),("t2","t3"),("t1","t3"),("t2","t4"),("t3","t4")]); pos = {"t1":(0,1),"t2":(2,2.2),"t3":(2,-0.2),"t4":(4,1)}
    c = nx.coloring.greedy_color(G, strategy="smallest_last"); assert all(c[u] != c[v] for u, v in G.edges()); assert len(set(c.values())) == 3
    f, a = canvas(5.2, 3.6, "Register allocation: interference graph, 3 colours"); draw(a, G, pos, nc=[COL[c[v]] for v in G], nec="#333", ns=1000); return f
@fig(4, "social_network")
def _():
    G = nx.Graph([("A","B"),("B","C"),("A","C"),("C","D"),("D","E"),("E","F"),("D","F")]); pos = {"A":(0,1.6),"B":(0,0),"C":(1.6,0.8),"D":(3.4,0.8),"E":(5,1.6),"F":(5,0)}
    f, a = canvas(6.4, 3.6, "Two communities joined by a bridge (CD)"); draw(a, G, pos, nc=[BLUE]*3 + [ORANGE]*3, nodelist=["A","B","C","D","E","F"]); return f
@fig(4, "networkx_shortest_path_drawing")
def _():
    pos = nx.spring_layout(WG, seed=7); p = nx.dijkstra_path(WG, "A", "E"); f, a = canvas(5.6, 4, "NetworkX drawing with the shortest route highlighted")
    draw(a, WG, pos, ecol=GREY, ew=2, elabels=WLAB); nx.draw_networkx_edges(WG, pos, ax=a, edgelist=list(zip(p, p[1:])), edge_color=RED, width=4, node_size=900); nx.draw_networkx_edge_labels(WG, pos, ax=a, edge_labels=WLAB, font_size=11, bbox=dict(fc="white", ec="none", pad=.8), rotate=False); return f

# ------------------------------------------------------------------ Chapter 5
@fig(5, "graphs_on_three_vertices")
def _():
    f, ax = canvas(8, 2.4, n=4); pos = {"A":(0,1.4),"B":(2,1.4),"C":(1,0)}
    for a, edges, t in zip(ax, [[], [("A","B")], [("A","B"),("B","C")], [("A","B"),("B","C"),("A","C")]], ["No edge", "One edge", "Path P₃", "Triangle K₃"]):
        G = nx.Graph(); G.add_nodes_from("ABC"); G.add_edges_from(edges); draw(a, G, pos, ns=800, fs=11); a.set_xlim(-.7, 2.7); a.set_ylim(-.7, 2.1); a.set_title(t, fontsize=11)
    f.tight_layout(); return f
@fig(5, "laplacian_matrix")
def _():
    G = nx.Graph([("A","B"),("A","C"),("B","C"),("C","D")]); L = nx.laplacian_matrix(G, nodelist=list("ABCD")).toarray().astype(int).tolist()
    f, (a, b) = canvas(7.8, 3.4, n=2); draw(a, G, {"A":(0,1.6),"B":(0,0),"C":(1.6,0.8),"D":(3.2,0.8)}); matrix_text(b, L, 0, 0, "Laplacian L = D − A  (order A, B, C, D)"); b.set_xlim(-2.2, 2.2); b.set_ylim(-1.6, 1.6); return f
@fig(5, "electrical_network_kcl")
def _():
    f, (a, b) = canvas(8.6, 3.6, n=2); G = nx.Graph([("N1","N2"),("N1","N3"),("N2","N3"),("N2","N4"),("N3","N4")]); pos = {"N1":(0,1),"N2":(1.6,2),"N3":(1.6,0),"N4":(3.2,1)}
    draw(a, G, pos, nc="#fff3d1", nec="#b8860b", ns=900, fs=9); a.set_title("Nodes and branches", fontsize=10)
    H = nx.DiGraph([("x","N"),("y","N"),("N","z")]); hp = {"x":(0,1.2),"y":(0,-0.2),"N":(1.6,0.5),"z":(3.2,0.5)}
    nx.draw_networkx_nodes(H, hp, nodelist=["N"], ax=b, node_color="#fff3d1", edgecolors="#b8860b", node_size=1000, linewidths=2); nx.draw_networkx_labels(H, hp, labels={"N":"N"}, ax=b, font_weight="bold")
    nx.draw_networkx_edges(H, hp, ax=b, node_size=300, arrows=True, arrowstyle="-|>", arrowsize=20, edge_color=NAVY, width=2.2)
    for xy, t in [((0.6,1.2),"5 A in"),((0.6,-0.1),"3 A in"),((2.4,0.8),"8 A out")]: b.text(*xy, t, fontsize=10, ha="center")
    b.set_title("KCL at node N: 5 + 3 = 8", fontsize=10); return f
@fig(5, "kvl_loop")
def _():
    G = nx.Graph([("a","b"),("b","c"),("c","a")]); pos = {"a":(0,0),"b":(3,0),"c":(1.5,2.4)}
    f, a = canvas(5.4, 3.8, "Kirchhoff's Voltage Law around a loop"); draw(a, G, pos, ns=500, fs=10, elabels={("a","b"):"+12 V (source)",("b","c"):"−5 V (R₁)",("a","c"):"−7 V (R₂)"}, efs=10)
    note(a, 1.5, -0.8, "+12 − 5 − 7 = 0", 11); return f
@fig(5, "network_topologies")
def _():
    f, ax = canvas(6.4, 5.6, n=2, m=2)
    for a, (G, t) in zip(ax, [(nx.star_graph(5), "Star"), (nx.cycle_graph(6), "Ring"), (nx.complete_graph(5), "Full mesh"), (nx.balanced_tree(2, 2), "Tree")]):
        pos = nx.kamada_kawai_layout(G) if t != "Tree" else {0:(0,2),1:(-1.2,1),2:(1.2,1),3:(-1.8,0),4:(-0.6,0),5:(0.6,0),6:(1.8,0)}
        if t == "Star": pos = nx.shell_layout(G, nlist=[[0], list(range(1, 6))])
        draw(a, G, pos, ns=420, labels={v: "" for v in G}, ew=1.8); a.set_title(t, fontsize=11)
    f.tight_layout(); return f
@fig(5, "routing_least_cost")
def _():
    G = nx.Graph(); G.add_weighted_edges_from([("A","B",4),("B","D",3),("A","C",2),("C","D",2),("D","E",1),("C","E",5)])
    pos = {"A":(0,1),"B":(1.6,2.4),"C":(1.6,-0.4),"D":(3.4,1),"E":(5,-0.2)}; lab = {(u, v): d["weight"] for u, v, d in G.edges(data=True)}
    p = nx.dijkstra_path(G, "A", "E"); assert p == ["A","C","D","E"]; f, a = canvas(6, 3.8, "Least-cost route A → E"); draw(a, G, pos, elabels=lab, ecol=GREY, ew=2)
    nx.draw_networkx_edges(G, pos, ax=a, edgelist=list(zip(p, p[1:])), edge_color=RED, width=4, node_size=900); nx.draw_networkx_edge_labels(G, pos, ax=a, edge_labels=lab, font_size=11, bbox=dict(fc="white", ec="none", pad=.8), rotate=False); note(a, 2.5, -1.1, "A–C–D–E: 2 + 2 + 1 = 5", 10); return f
@fig(5, "city_network")
def _():
    G = nx.Graph(); G.add_weighted_edges_from([("Bengaluru","Hyderabad",570),("Hyderabad","Mumbai",710),("Hyderabad","Chennai",630),("Bengaluru","Chennai",350),("Bengaluru","Mysuru",145),("Mysuru","Chennai",480)])
    pos = {"Bengaluru":(0,1),"Hyderabad":(2.5,2.4),"Mumbai":(5,2.4),"Chennai":(2.5,-0.6),"Mysuru":(-0.4,-0.6)}; lab = {(u, v): d["weight"] for u, v, d in G.edges(data=True)}
    f, a = canvas(7, 4, "Illustrative city network (approximate km)"); draw(a, G, pos, nc=GREEN, nec="#38761d", ns=2600, fs=8, elabels=lab, ecol=GREY, ew=2); return f
@fig(5, "traffic_flow")
def _():
    G = nx.DiGraph(); w = {("A","B"):"400 veh/h",("A","C"):"300 veh/h",("B","D"):"400 veh/h",("C","D"):"300 veh/h"}; G.add_edges_from(w)
    pos = {"A":(0,1.5),"B":(2.5,3),"C":(2.5,0),"D":(5,1.5)}; f, a = canvas(6.4, 4, "Traffic flow modelled as a directed network")
    draw(a, G, pos, nc="#fff3d1", nec="#b8860b", directed=True, elabels=w, efs=9); note(a, 2.5, -0.8, "Inflow = outflow at B (400) and C (300)", 10); return f
@fig(5, "max_flow_min_cut")
def _():
    G = nx.DiGraph(); cap = {("s","a"):5,("s","b"):4,("a","b"):2,("a","t"):3,("b","t"):5}; fl = {("s","a"):4,("s","b"):4,("a","b"):1,("a","t"):3,("b","t"):5}; G.add_edges_from(cap)
    assert nx.maximum_flow_value(nx.DiGraph([(u, v, {"capacity": c}) for (u, v), c in cap.items()]), "s", "t") == 8
    pos = {"s":(0,1),"a":(2,2.2),"b":(2,-0.2),"t":(4,1)}; f, a = canvas(6, 4, "Maximum flow 8 (flow / capacity)")
    draw(a, G, pos, directed=True, elabels={e: f"{fl[e]}/{cap[e]}" for e in cap}, ecol="#455a6b", ns=800)
    nx.draw_networkx_edges(G, pos, ax=a, edgelist=[("a","t"),("b","t")], edge_color=RED, width=4, arrows=True, node_size=800)
    nx.draw_networkx_edge_labels(G, pos, ax=a, edge_labels={e: f"{fl[e]}/{cap[e]}" for e in cap}, font_size=11, bbox=dict(fc="white", ec="none", pad=.8), rotate=False); note(a, 2, -1.1, "Minimum cut {at, bt} (red) has capacity 3 + 5 = 8", 10); return f
@fig(5, "pert_cpm")
def _():
    G = nx.DiGraph([("Start","A"),("Start","B"),("A","C"),("B","C"),("C","Finish")]); pos = {"Start":(0,1),"A":(2,2),"B":(2,0),"C":(4,1),"Finish":(6,1)}
    f, a = canvas(7, 3.6, "Project network: critical path Start–B–C–Finish = 9 days")
    draw(a, G, pos, directed=True, nc=PURPLE, nec="#6a3d9a", ns=1600, fs=9, labels={"Start":"Start","A":"A\n3 d","B":"B\n5 d","C":"C\n4 d","Finish":"Finish"}, ecol=GREY)
    nx.draw_networkx_edges(G, pos, ax=a, edgelist=[("Start","B"),("B","C"),("C","Finish")], edge_color=RED, width=3.5, arrows=True, node_size=1600); return f
@fig(5, "molecular_graphs")
def _():
    f, (a, b) = canvas(7.6, 3.2, n=2); W2 = nx.Graph([("H₁","O"),("O","H₂")]); draw(a, W2, {"H₁":(0,0),"O":(1.2,0),"H₂":(2.4,0)}, nc=[BLUE,"#f4b6b6",BLUE], nodelist=["H₁","O","H₂"], ns=800); a.set_title("Water (H₂O)", fontsize=10)
    M = nx.Graph([("C","H₁"),("C","H₂"),("C","H₃"),("C","H₄")]); draw(b, M, {"C":(0,0),"H₁":(-1.2,1),"H₂":(1.2,1),"H₃":(-1.2,-1),"H₄":(1.2,-1)}, nc=["#cfcfcf"] + [BLUE]*4, nodelist=["C","H₁","H₂","H₃","H₄"], ns=800); b.set_title("Methane (CH₄)", fontsize=10); return f
@fig(5, "food_web")
def _():
    G = nx.DiGraph([("Grass","Grasshopper"),("Grasshopper","Frog"),("Frog","Snake"),("Snake","Eagle"),("Grass","Rabbit"),("Rabbit","Fox"),("Fox","Eagle")])
    pos = {"Grass":(0,1),"Grasshopper":(1.8,2),"Frog":(3.8,2),"Snake":(5.8,2),"Rabbit":(1.8,0),"Fox":(3.8,0),"Eagle":(7.6,1)}
    f, a = canvas(8.6, 3.8, "Food web: arrows show energy transfer"); draw(a, G, pos, directed=True, nc=GREEN, nec="#38761d", ns=3300, fs=7); return f
@fig(5, "supply_chain")
def _():
    G = nx.path_graph(["Supplier","Factory","Warehouse","Retailer","Customer"], create_using=nx.DiGraph); pos = {v: (i * 1.8, 0) for i, v in enumerate(G)}
    f, a = canvas(9.6, 2.4, "Supply chain as a directed network"); draw(a, G, pos, directed=True, nc="#fff3d1", nec="#b8860b", ns=3600, fs=7.5); return f
@fig(5, "exam_timetable")
def _():
    G = nx.Graph([("M","P"),("M","C"),("P","C"),("M","S"),("C","T"),("E","S"),("E","T")]); pos = {"M":(0,3),"P":(0,0),"C":(3,1.5),"S":(6,3),"T":(6,0),"E":(9,1.5)}
    c = nx.coloring.greedy_color(G, strategy="largest_first"); assert all(c[u] != c[v] for u, v in G.edges()) and len(set(c.values())) == 3
    f, a = canvas(7, 4.2, "Exam timetable: conflict graph coloured by slot"); draw(a, G, pos, nc=[COL[c[v]] for v in G], nec="#333", ns=1000)
    slots = {s: sorted(v for v in c if c[v] == s) for s in sorted(set(c.values()))}
    note(a, 4.5, -1.1, "   ".join(f"Slot {s+1}: {', '.join(v)}" for s, v in slots.items()), 10); return f

if __name__ == "__main__":
    count = {}
    for ch, key, fn in FIGS:
        count[ch] = count.get(ch, 0) + 1
        save(fn(), ch, count[ch], key)
    print("figures written:", sum(count.values()), count)
