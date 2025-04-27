.. DRILL V3 documentation master file

Welcome to DRILL V3's documentation!
====================================

Contents:

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   install
   usage
   architecture
   communication
   persistence
   post_exploitation
   file_transfer
   ui
   security

Overview
--------

DRILL V3 (Distributable Remote Integrated Lightweight Link) is a modern and modular Command and Control (C2) framework tailored for stealthy post-exploitation operations. It offers a flexible architecture, real-time bidirectional communication, and support for a wide range of features that aid in maintaining and expanding access within a target environment.

This documentation provides a detailed look into the DRILL V3 framework, its components, how it operates, and how it can be configured and deployed effectively. While DRILL is still evolving, it already includes a mature feature set suitable for internal security assessments and research.

Architecture
------------

DRILL V3 is organized around three major components:

- **Agent**: A lightweight implant that connects back to the teamserver and executes commands. It maintains persistence and executes post-exploitation tasks.
- **Teamserver**: The backend core of the operation, responsible for receiving agent connections, distributing commands, and storing results.
- **Client Interface**: A web-based UI for interacting with agents, issuing commands, managing modules, and viewing data returned from endpoints.

The design emphasizes modularity, enabling easy development of new features or modification of existing ones.

Communication
-------------

DRILL V3 uses WebSockets over HTTP/HTTPS to establish agent communication. This allows real-time, bidirectional data flow between the teamserver and the agent, improving responsiveness compared to traditional polling methods.

Although DRILL does not include built-in support for tunneling through services like Cloudflare Tunnel, it is fully compatible and can be used with such infrastructure to enhance traffic obfuscation and bypass network restrictions.

All agent traffic runs over a single configurable port, simplifying deployment and making it easier to disguise C2 traffic as normal web activity.

Persistence
-----------

Persistence is implemented per operating system. At this time, DRILL supports:

- **Windows**: Startup registry modifications are used to ensure agents run on boot.
- **Linux**: The agent installs itself as a user-level systemd service.

There is currently no support for macOS agents in DRILL V3.

Post-Exploitation Features
--------------------------

DRILL V3 includes several native post-exploitation features. These can be extended via a module system, allowing operators to customize their workflow. Built-in functionality includes:

- **Shell Command Execution**: Operators can run arbitrary shell commands on any connected agent.
- **Remote Desktop**: Agents can capture the screen allowing the operator to view and interact with the target in near real-time.
- **Webcam Access**: If available on the host, the agent can stream webcam video to the operator.
- **Scripting Support**: The system supports scripting via modules that can execute predefined tasks.

More advanced operations can be implemented via custom modules developed in Python and integrated into the system.

File Transfer
-------------

The framework supports bi-directional file transfer to and from agents. This includes:

- Uploading executables, scripts, and configuration files to agents.
- Downloading captured data, screenshots, webcam footage, or log files.

Transfers can be initiated through the UI. The system supports transfers to and from multiple agents in parallel.

User Interface
--------------

DRILL's web-based UI is operator-centric, designed for clarity and speed. Through the dashboard, an operator can:

- Monitor connected agents and their statuses.
- Launch new commands or module-based operations.
- View screen captures or webcam streams.
- Browse transferred files and session logs.

Additionally, the UI includes an optional login page that can be enabled or disabled via the configuration file. The same file can also be used to configure other interface behaviors such as streaming quality, UI themes, and modules.

Security Considerations
-----------------------

DRILL is designed for use in authorized environments only, such as penetration testing and red teaming under valid legal agreements. Improper use may be illegal and unethical.

Operators should:

- Avoid exposing the teamserver to the internet without protection.
- Use strong authentication if enabling the login page.
- Monitor logs for anomalous activity.
- Secure agent binaries to prevent unauthorized distribution.

It is also recommended to tunnel DRILL through services like Cloudflare or NGROK and not proxys as it can cause errors when locating clients geographically.

