# 🧠 Solving the N-Queens Problem with Exhaustive, Local, and Optimization Algorithms

This project implements and compares four different algorithmic approaches to solving the classic N-Queens problem. The goal of the N-Queens problem is to place N queens on an N×N chessboard such that no two queens attack each other.

## 📌 Algorithms Implemented

1. **Depth-First Search (DFS)**  
2. **Hill Climbing**  
3. **Simulated Annealing**  
4. **Genetic Algorithm (GA)**  

## 🧪 Tested Board Sizes

- N = 10
- N = 30
- N = 50
- N = 100
- N = 200

## 📊 Performance Metrics

Measured runtime, conflicts, and success status for each algorithm.

## 📁 Project Structure

```
📂 NQueens-Algorithms/
├── dfs_nqueens.py
├── hillclimbing_nqueens.py
├── simulatedannealing_nqueens.py
├── geneticalgorithm_nqueens.py
├── results/
│   ├── bfs_nqueens.txt
│   ├── hillclimbing_nqueens.txt
│   ├── simulatedanneling.txt
│   └── geneticalgorithm.txt
├── report/
│   ├── nqueens_report.pdf
│   ├── nqueens_runtime_comparison.png
│   └── main.tex
```

## 📖 Report

The PDF report includes:
- Algorithm descriptions
- Pseudocode
- Runtime table and chart
- Final conclusion

📝 Written in LaTeX, compiled using Overleaf or pdflatex.

## 👨‍💻 Author

**Sardor Samandarov**

## 📜 License

This project is open-source under the MIT License.

## 💬 How to Run

```bash
python dfs_nqueens.py
python hillclimbing_nqueens.py
python simulatedannealing_nqueens.py
python geneticalgorithm_nqueens.py
```
