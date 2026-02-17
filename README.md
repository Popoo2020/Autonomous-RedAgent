# Autonomous‑RedAgent

**AI‑driven offensive security agent for reconnaissance and payload generation**

## Overview
Autonomous‑RedAgent is a Python‑based tool that automates reconnaissance and exploit preparation. It leverages Nmap via Python wrappers to perform network scans, consumes CVE feeds to map detected services to known vulnerabilities, and uses an LLM to summarise and prioritise attack vectors. The goal is to augment red‑team efficiency and provide actionable insights without manual sifting through long vulnerability lists.

### Features
* **Automated Reconnaissance:** Uses Nmap to discover hosts, open ports and service versions. Results are parsed into structured objects.
* **CVE Mapping:** Downloads and parses CVE feeds; correlates discovered services with relevant CVEs and severity information.
* **LLM Summarisation:** An AI model prioritises vulnerabilities based on exploitability and business impact.
* **Payload Generation:** Generates custom scripts or payload templates for exploitation testing (never used against production without authorisation).
* **Extensible:** Designed to integrate additional modules such as Shodan lookups, OSINT or malware analysis.

### Repository Structure

```
Autonomous-RedAgent/
├── README.md
├── requirements.txt
├── src/
│   ├── recon.py          # Nmap scanning and result parsing
│   ├── cve.py            # Fetch and parse CVE feeds
│   ├── llm.py            # AI summarisation and prioritisation
│   ├── payloads.py       # Payload template generation
│   └── utils.py
└── reports/              # Generated reconnaissance and CVE reports
```

### Usage
1. Install dependencies: `pip install -r requirements.txt`.
2. Populate `.env` with API keys (e.g., for CVE feeds or LLM services).
3. Run `python src/recon.py --target <IP/CIDR>` to perform a scan and generate an attack surface report.
4. Use `python src/cve.py --input reports/scan_results.json` to map services to vulnerabilities.
5. Generate payload templates with `python src/payloads.py`.

### Disclaimer
This tool is intended for authorised penetration testing and educational purposes only. Improper use may violate laws and ethical guidelines.
