filename = {
    16: "Largest Divisible Subset.py",
    17: "Find Subsequence of Length K With the Largest Sum.py",
    18: "Amount of Time for Binary Tree to Be Infected.py",
    19: "K-diff Pairs in an Array.py",
    20: "Count the Number of Square-Free Subsets.py",
    21: "Rotate Function.py",
    22: "Get Equal Substrings Within Budget.py",
    23: "Friends Of Appropriate Ages.py",
    24: "Maximum Length of Repeated Subarray.py",
    25: "Verify Preorder Serialization of a Binary Tree.py",
    26: "Top K Frequent Words.py",
    27: "Battleships in a Board.py",
    28: "Sort Characters By Frequency.py",
    29: "Word Break.py",
    30: "Extra Characters in a String.py",
}

def create_python_files():
    for i in range(16, 31):
        file_name = filename[i]
        file_content = ''
        with open(file_name, "w") as file:
            file.write(file_content)

if __name__ == "__main__":
    create_python_files()
