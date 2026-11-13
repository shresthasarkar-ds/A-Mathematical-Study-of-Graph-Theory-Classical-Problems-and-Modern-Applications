# A Mathematical Study of Graph Theory: Classical Problems and Modern Applications

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![NetworkX](https://img.shields.io/badge/NetworkX-3.x-informational)
![License](https://img.shields.io/badge/code-MIT-green)

B.Sc. (Honours) Mathematics, Semester V project report, with the Python code used to check every worked example.

| | |
|---|---|
| **Author** | Shrestha Sarkar |
| **College / University** | Asansol Girls' College, Kazi Nazrul University |
| **Academic session** | 2019–2022 |
| **Under the guidance of** | Dr. Fahad Al Basir (HOD) and Assistant Prof. Chandan Kumar Adhak |

## About the project

Graph theory studies objects and the connections between them. This project builds the subject from the basic definitions up to its famous problems and its uses in mathematics, computer science and engineering. Theorems are proved, not only stated, and every numerical example in the report is re-computed in Python.

**Report in short (53 pages, 6 chapters).** The report keeps the theory short and concentrates on problems and applications.

| Chapter | Topic |
|---|---|
| 1 | Introduction, history, objectives and tools |
| 2 | Basic concepts and key results (only what the problems need): degrees, Euler and Hamilton graphs, trees, planar graphs, colouring, matching |
| 3 | **Classical problems with worked examples**: Königsberg bridges, Four Colour, Three Utilities, Travelling Salesman, Knight's Tour, Chinese Postman, Shortest Path, Minimum Spanning Tree, Maximum Flow, Assignment, and solved problems |
| 4 | Graph algorithms and computer-science applications: representations, BFS, DFS, Dijkstra, Floyd–Warshall, Prim/Kruskal, topological sort, Python demo |
| 5 | **Applications** in mathematics, electrical, communication and transportation engineering, operations research, chemistry, biology and economics, with two case studies (exam timetable, courier route) |
| 6 | Conclusion, limitations and future scope |

## Selected diagrams

Every figure in the report is drawn with **NetworkX** and **Matplotlib** by `src/make_figures.py`.

<table>
  <tr>
    <img width="1032" height="947" alt="Fig_3 1_konigsberg_bridges" src="https://github.com/user-attachments/assets/fcfbc9e6-f90a-444e-9e25-da632429c175" />
    <img width="970" height="883" alt="Fig_3 4_tsp_four_cities" src="https://github.com/user-attachments/assets/515ee076-e8b6-4c73-9368-d94514123ab7" />
    <img width="1125" height="848" alt="Fig_5 14_exam_timetable" src="https://github.com/user-attachments/assets/2afca510-998f-4c43-96c9-a2b2b40f2182" />
  </tr>
  <tr>
    <img width="815" height="986" alt="Fig_3 3_three_utilities_k33" src="https://github.com/user-attachments/assets/7319fcc9-d886-4e7e-ace5-f044a7a8c07c" />
    <img width="970" height="777" alt="Fig_3 6_chinese_postman" src="https://github.com/user-attachments/assets/0f2b5409-979a-4ee1-aa5f-4981870b73d3" />
    <img width="1260" height="1460" alt="Fig_4 8_prim_kruskal" src="https://github.com/user-attachments/assets/1c4d02a3-5fef-4db6-ab09-43b60784489e" />
  </tr>
  <tr>
    <img width="970" height="817" alt="Fig_5 9_max_flow_min_cut" src="https://github.com/user-attachments/assets/12c16558-41ec-47fa-9e9f-f8df4f40743d" />
    <img width="846" height="826" alt="Fig_4 10_deadlock_graph" src="https://github.com/user-attachments/assets/8ff84672-7c40-4ec2-bc73-977f623b4221" />
    <img width="1125" height="651" alt="Fig_5 10_pert_cpm" src="https://github.com/user-attachments/assets/2c2b93fc-5c0a-4cb4-a61c-fb1d09ce623a" />

  </tr>
</table>

## Repository structure

```
graph-theory-project/
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── report/
│   ├── Graph_Theory_Project.docx      # full project report (editable)
│   └── Graph_Theory_Project.pdf       # same report as PDF
├── notebooks/
│   └── graph_theory_verification.ipynb  # re-computes every worked example
├── src/
│   ├── graph_theory_demo.py             # Chapter 4 program (Appendix A)
│   └── make_figures.py                  # draws all 46 figures (NetworkX + Matplotlib)
├── outputs/
│   ├── demo_output.txt                  # output of graph_theory_demo.py
│   ├── notebook_output.txt              # output of the notebook code
│   └── shortest_path.png                # figure produced by the demo
├── figures/                             # 46 figures, drawn by src/make_figures.py
│   ├── chapter_1/   Fig_1.1 … Fig_1.4   (introduction)
│   ├── chapter_2/   Fig_2.1 … Fig_2.5   (basic concepts)
│   ├── chapter_3/   Fig_3.1 … Fig_3.10  (classical problems)
│   ├── chapter_4/   Fig_4.1 … Fig_4.13  (algorithms, computer science)
│   └── chapter_5/   Fig_5.1 … Fig_5.14  (applications, case studies)
└── data/
    └── references.bib                   # bibliography (BibTeX)
```

## Tools used

| Tool | Purpose |
|---|---|
| Python 3 with NetworkX | Building and drawing all the graphs; BFS, DFS, Dijkstra, Prim, Kruskal, maximum flow; checking all numerical examples |
| NumPy | Adjacency, incidence and Laplacian matrices; Floyd–Warshall; walk counting |
| Matplotlib | Rendering and saving the NetworkX drawings as figures |
| Jupyter Notebook / Google Colab | Running and documenting the code step by step |

## How to run

```bash
git clone https://github.com/<your-username>/graph-theory-project.git
cd graph-theory-project

python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python src/graph_theory_demo.py              # Chapter 4 demo
python src/make_figures.py                   # redraw all 46 figures into figures/
jupyter notebook notebooks/graph_theory_verification.ipynb
```

To use Google Colab instead, upload the notebook and run `!pip install networkx sympy` in the first cell.

## Results checked by the code

| Example in the report | Result |
|---|---|
| Handshaking Lemma, graph of Fig. 1.3 | degree sum 10 = 2 × 5 edges |
| Havel–Hakimi | (4,3,3,2,2) graphical; (3,3,3,1) not graphical |
| Königsberg bridges | degrees 3, 3, 3, 5 → no Euler trail |
| Travelling salesman, 4 cities | 3 distinct tours; optimal A–B–D–C–A = 80 |
| Dijkstra from A | A 0, C 2, B 3, D 8, E 10 (path A–C–B–D–E) |
| Minimum spanning tree | edges AC, BC, BD, DE; weight 10 |
| Floyd–Warshall (4-vertex digraph) | final matrix in Section 4.2.4 |
| Matrix-tree theorem | 3 spanning trees (Chapter 5 graph); K₄ has 16 = 4² |
| Maximum flow | 8 (Chapter 5 network) and 13 (Chapter 3 network) |
| Planarity | K₅ and K₃,₃ non-planar, K₄ planar |
| Chinese postman, weighted example | total 20 + repeat A–C (6) = 26 |
| Assignment problem (3 × 3) | W₁→Task 2, W₂→Task 1, W₃→Task 3, cost 6 |
| Case study 1: exam timetable | 3 time slots: {M, T}, {C, S}, {P, E} |
| Case study 2: courier route (5 stops) | optimum A–B–C–D–E–A = 64 km; nearest neighbour = 74 km |
| Chromatic polynomial of the diamond | x(x − 1)(x − 2)², so P(3) = 6 |
| BFS / DFS / topological order | A B C D E F / A B D E C F / A B C D E F |

## Figures

All 46 figures are generated from code, chapter by chapter, so they can be reproduced and edited. Each graph is built as a NetworkX object and drawn with Matplotlib. The script also checks the mathematics while drawing: for example it asserts that the colourings are proper, that the knight's tour moves are legal, that the maximum flow is 8, and that the shortest path is A–C–D–E.

## Academic note

This repository is shared for learning and reference. The report is the author's own work, based on the textbooks and papers listed in its bibliography (see `data/references.bib`). If you use ideas from it, please cite it and do not submit it as your own work.

## License

The code is released under the [MIT License](LICENSE). The report and figures are © Shrestha Sarkar; please contact the author before reusing them.
