
## **Homework Assignment: Implementing a CI/CD Pipeline for a Flask App**


### **Objective**  
Implement a CI/CD pipeline for a Python Flask app to check for linting issues, dependency vulnerabilities, and code security flaws. Use GitHub Actions to automate this process.

---

### **Provided Resources**
1. A basic Flask app (`app.py`) that includes a `/` and `/health` endpoint.
2. A `requirements.txt` file listing the app's dependencies.
3. An overview of the pipeline components you need to implement.

---

### **Your Task**  
You need to create a GitHub Actions workflow file (`.github/workflows/python-ci.yml`) that does the following:

1. **Check out the code**: Ensure the pipeline works with the latest version of the code in the `main` branch.
2. **Set up Python**: Use Python 3.9 for the pipeline.
3. **Install dependencies**: Install all dependencies listed in `requirements.txt`.
4. **Linting**: Add a step to ensure the code is clean by running the `flake8` linter.
5. **Dependency Security Check**: Use `Safety` to check for known vulnerabilities in the app’s dependencies.
6. **Code Security Scan**: Use `Bandit` to identify potential security issues in the app's code.

---

### **Step-by-Step Guide**

#### **1. Initialize the Workflow**
- Create a `.github/workflows` directory in your project.
- Inside the directory, create a file called `python-ci.yml`.

#### **2. Set the Workflow Trigger**
- Ensure the pipeline runs whenever changes are pushed to the `main` branch.

#### **3. Add the Linter**
- Include a step to install and run the `flake8` linter to ensure the code follows Python style guidelines.
- **HINT**: Packages are normally installed via python using `pip install <package name>`. Do some research into the basic usage of `flake8` and how you can execute it (should be simple).

#### **4. Add a Dependency Vulnerability Scanner**
- Use the `safety` tool to analyze the `requirements.txt` file for vulnerabilities in the app’s dependencies.
- **HINT**: Packages are normally installed via python using `pip install <package name>`. Do some research into the basic usage of `safety` and how you can execute it (should be simple).

#### **5. Add a Code Security Scanner**
- Integrate the `bandit` tool to scan Python files for common security vulnerabilities.
- **HINT**: Packages are normally installed via python using `pip install <package name>`. Do some research into the basic usage of `bandit` and how you can execute it (should be simple). Make sure to use `-r` option for recursive.

#### **6. Run the Workflow**
- Push your changes to `main` and observe the workflow running on GitHub.

---

### **Deliverables**

1. **Working Pipeline**:
   A functional `.github/workflows/python-ci.yml` file that automates linting, security checks, and dependency scanning.

2. **Write-Up**:
   Submit a short document explaining:
   - How you set up the pipeline.
   - What each tool (Flake8, Bandit, and Safety) does.
   - Any issues you faced and how you resolved them.

   **IMPORTANT**: Make sure to include a link to your pipeline, the most recent run of your pipeline should be green.

---

### **Additional Instructions**

- Avoid hardcoding paths or settings where possible to ensure flexibility.
- Make sure your workflow is clean and modular, with logical step names for clarity.

---

