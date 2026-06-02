# Secure Coding Review Report
## CodeAlpha Cyber Security Internship - Task 3

### 1. Application Audited
**Language**: Python  
**Framework**: Flask  
**File**: vulnerable_app.py

### 2. Vulnerabilities Found by Bandit

| # | Vulnerability | Severity | CWE | Location |
| --- | --- | --- | --- | --- |
| 1 | Flask Debug Mode Enabled | High | CWE-94 | Line 35 |
| 2 | Hardcoded Password String | Low | CWE-259 | Line 7 |
| 3 | SQL Injection | Medium | CWE-89 | Line 14 |

### 3. Manual Review Findings
1. **Sensitive Data Exposure**: Line 20 returns user password in response
2. **Cross-Site Scripting (XSS)**: Line 26 renders user input without escaping

### 4. Recommendations & Remediation

**1. Flask Debug Mode**  
**Risk**: Exposes Werkzeug debugger allowing arbitrary code execution  
**Fix**: `app.run(debug=False)` for production

**2. Hardcoded Credentials**  
**Risk**: Password visible in source code/Git history  
**Fix**: Use environment variables: `os.environ.get("DB_PASS")`

**3. SQL Injection**  
**Risk**: Attacker can manipulate database queries  
**Fix**: Use parameterized queries: `cursor.execute("SELECT * FROM users WHERE username=?", (username,))`

**4. Sensitive Data Exposure**  
**Fix**: Never return passwords. Return JWT tokens instead

**5. XSS**  
**Fix**: Use `from markupsafe import escape` and `escape(query)`

### 5. Tools Used
1. **Bandit v1.9.4** - Static analysis for Python
2. **Manual Code Review** - Line by line audit

### 6. Conclusion
The application contains 5 critical vulnerabilities. All fixes documented above must be implemented before deployment.