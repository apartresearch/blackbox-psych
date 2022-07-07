"""
Creates a dataset of unsolved questions (from wikipedia)
"""
import sys

sys.path.append("../")
import src.format_questions as format_questions
import pandas as pd

OPTIONS = [" Yes", " No", " Unknown"]
QUESTIONS = [
    "Do black holes have an internal structure?",
    "Does a firewall exist around a black hole?",
    "Is dark matter a particle?",
    "Given an arbitrary compact gauge group, does a non-trivial quantum Yang–Mills theory with a finite mass gap exist?",
    "Did particles that carry 'magnetic charge' exist in some past, higher-energy epoch?",
    "Can integer factorization be done in polynomial time on a classical (non-quantum) computer?",
    "Can the shortest vector of a lattice be computed in polynomial time on a classical or quantum computer?",
    "Can clustered planar drawings be found in polynomial time?",
    "Can the graph isomorphism problem be solved in polynomial time?",
    "Can leaf powers and k-leaf powers be recognized in polynomial time?",
    "Can parity games be solved in polynomial time?",
    "Can the rotation distance between two binary trees be computed in polynomial time?",
    "Can graphs of bounded clique-width be recognized in polynomial time?",
    "Can one find a simple closed quasigeodesic on a convex polyhedron in polynomial time?",
    "Can a simultaneous embedding with fixed edges for two given graphs be found in polynomial time?",
]


def main():
    formatted_questions = [
        format_questions.format_question(question, OPTIONS) for question in QUESTIONS
    ]
    correct_index = 2
    result_df = format_questions.create_df(formatted_questions, OPTIONS, correct_index)
    result_df.to_csv("unsolved_questions.csv", index=False)


if __name__ == "__main__":
    main()
