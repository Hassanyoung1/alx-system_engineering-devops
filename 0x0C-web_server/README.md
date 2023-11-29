# Project Overview

In this project, tasks will be evaluated based on two key aspects:

1. **Web-01 Server Configuration:**
   - Is your web-01 server configured according to requirements?

2. **Bash Script Automation:**
   - Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (without any human intervention)?

For instance, if a task involves creating a file /tmp/test containing the string hello world and modifying the Nginx configuration to listen on port 8080 instead of 80, the solution should be automated in a Bash script rather than relying on manual intervention.

Here's an example Bash script:

\`\`\`bash
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
\`\`\`

Note: The script is designed for automation and does not involve manual steps using tools like emacs.

This exercise emphasizes the importance of automating tasks to enhance efficiency. Automating repetitive tasks allows professionals to focus on more interesting and complex aspects of their work. For System Reliability Engineers (SREs), automation is crucial when managing a large number of servers.

### Key Points:

- The checker will execute your script as the root user; there is no need for the sudo command.

- Remember: A good Software Engineer is a lazy Software Engineer.

### Testing Your Bash Script:

Feel free to reproduce the checker environment for testing:
1. Start an Ubuntu 16.04 sandbox.
2. Run your script on it.
3. Observe its behavior.

---

# Learning Objectives

At the end of this project, you are expected to be able to explain, without the help of Google, the following concepts:

## General
- **Main Role of a Web Server**
- **Child Process**
- **Reasons for Web Servers Having Parent and Child Processes**
- **Main HTTP Requests**

## DNS
- **What DNS Stands For**
- **DNS Main Role**
- **DNS Record Types:**
  - A
  - CNAME
  - TXT
  - MX

---

**Author: Hassan Olaoluwa**
EOF

