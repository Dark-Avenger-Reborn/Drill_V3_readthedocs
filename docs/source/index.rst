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
   shell
   remote_desktop
   webcam
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

Communication between DRILL V3 and agents are ecrypted both ways using a mix of both RSA and AES encryption preventing third parties from intercepting and decoding traffic.

Persistence
-----------

Persistence is implemented per operating system. At this time, DRILL supports:

- **Windows**: Startup registry modifications are used to ensure agents run on boot.
- **Linux**: The agent installs itself as a user-level systemd service.

There is currently no support for macOS agents in DRILL V3.

Post-Exploitation Modules (PEMs)
--------------------------------

DRILL V3 supports a flexible module system for post-exploitation tasks. These **Post-Exploitation Modules (PEMs)** allow operators to extend functionality beyond the built-in features by writing and integrating Python modules.

Modules are executed in-memory and on a seperate thread. PEMs can be used for a variety of tasks, including enumeration, lateral movement, or host-specific actions. They are easy to write and integrate, following a minimal interface standard.

For examples and templates, see the [post_exploitation.rst](post_exploitation.html) page.

Shell Access
------------

DRILL provides real-time shell access to agents through the UI. Operators can execute arbitrary commands on a target system and receive immediate responses. This feature behaves similarly to a traditional reverse shell but is wrapped within the secure, WebSocket-based communication channel used by DRILL.

More details and usage examples are available on the [shell.rst](shell.html) page.

Remote Desktop
--------------

DRILL V3 includes a remote desktop capability that allows operators to capture screenshots from the target machine. This provides visibility into the user’s active desktop session and can assist in visual reconnaissance.

Agent builds also support remote interaction, enabling limited control of the mouse and keyboard. These capabilities depend on the target platform and environment.

Refer to the [remote_desktop.rst](remote_desktop.html) page for supported features and usage instructions.

Webcam Access
-------------

Where supported, DRILL V3 agents can interface with connected webcams on the host machine. This allows the operator to view live camera feeds directly from the DRILL UI.

This feature works similarly to Remote Desktop as it uses screenshots to reconstruct a live video feed. Webcam access is particularly useful in physical reconnaissance during on-site red team assessments.

Setup detail and security implications are documented in [webcam.rst](webcam.html).

File Transfer
-------------

The framework supports bi-directional file transfer to and from agents. This includes:

- Uploading executables, scripts, and configuration files to agents.
- Downloading captured data, personal files, configurations, and log files.

Transfers can be initiated manually through the UI. The system supports transfers to multiple agents in parallel.

User Interface
--------------

DRILL's web-based UI is operator-centric, designed for clarity and speed. Through the dashboard, an operator can:

- Monitor connected agents and their statuses.
- Launch new commands or module-based operations.
- View screen captures or webcam streams.
- Browse transferred files.

The UI includes an optional login screen which can be enabled through the DRILL configuration file. Other configuration options include session timeouts, logging verbosity, and interface theme settings.

Security Considerations
-----------------------

DRILL is designed for use in authorized environments only, such as penetration testing and red teaming under valid legal agreements. Improper use may be illegal and unethical.

Operators should:

- Avoid exposing the teamserver to the internet without protection.
- Use strong authentication if enabling the login page.
- Monitor logs for anomalous activity.

It is also recommended to tunnel DRILL through services like Cloudflare and not proxies which can cause errors with IP discovery and geolocating.