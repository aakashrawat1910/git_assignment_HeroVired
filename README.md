# Git Assignment: Hero Vired

## Title: CalculatorPlus & GeometryCalculator

### Description:
This repository contains two Python applications:
1. **CalculatorPlus**: A simple calculator that supports basic arithmetic operations and square root calculations.
2. **GeometryCalculator**: A utility to calculate areas of circles and rectangles.

Both applications demonstrate branching, merging, and stashing techniques in Git along with Git LFS usage for large binary files.

---

### Features:
- **CalculatorPlus**:
  - Addition
  - Subtraction
  - Multiplication
  - Division with error handling
  - Square root calculation
  
- **GeometryCalculator**:
  - Calculate the area of a circle
  - Calculate the area of a rectangle
  
- **Git Techniques**:
  - Branching
  - Merging
  - Stashing
  - Git LFS for large file storage

---

### Prerequisites:
- Python 3.x installed.
- Git installed.
- GitHub account with access to create private repositories.
- Git LFS installed.

---

### Requirements:
- Python Libraries:
  - `math` (standard Python library)
- GitHub CLI (optional for easy GitHub operations).

---

## Using the Program:

### **1. CalculatorPlus**

#### Commands:
```bash
# Clone the repository
git clone <repository-link>
cd git_assignment_HeroVired

# Switch to dev branch
git checkout dev

# Run the CalculatorPlus app
python CalculatorPlus.py
```

#### Sample Input & Output:
```python
16 + 4 = 20
16 - 4 = 12
16 * 4 = 64
16 / 4 = 4.0
The square root of 25 = 5.0
```

---

### **2. GeometryCalculator**

#### Commands:
```bash
# Switch to geometry-calculator branch
git checkout geometry-calculator

# Run the GeometryCalculator app
python GeometryCalculator.py
```

#### Sample Input & Output:
```python
The area of the circle with radius 5 = 78.54
The area of the rectangle with length 10 and width 6 = 60
```

---

### Git Workflow:

#### 1. Create Repository and Branches:
```bash
git init
git remote add origin <repository-link>
git checkout -b dev
```

#### 2. Add and Commit Files:
```bash
git add .
git commit -m "Initial commit for CalculatorPlus"
```

#### 3. Create and Merge Feature Branch:
```bash
git checkout -b feature/sqrt
# Implement and commit square root feature
git add CalculatorPlus.py
git commit -m "Added square root functionality"
git checkout dev
git merge feature/sqrt
```

#### 4. Bug Fix in Division:
```bash
git checkout -b hotfix/divide
# Fix divide by zero error
git add CalculatorPlus.py
git commit -m "Fixed division by zero bug"
git checkout dev
git merge hotfix/divide
```

#### 5. Use Git LFS:
```bash
git lfs install
git checkout -b lfs
git lfs track "*.mkv"
git commit -m "Added large file with Git LFS"
git push origin lfs
```

#### 6. Use Git Stash:
```bash
# Stash Circle Feature
git checkout -b feature/circle-area
git stash

# Start Rectangle Feature
git checkout -b feature/rectangle-area
git stash apply
```

---
