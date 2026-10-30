# Contributing to Open Source DFIR

From time to time someone asks how do I contribute to Open Source DFIR. This page contains relevant
tips and links from such conversations.

## First determine a scope in which you want to contribute

Open Source DFIR is combination of multiple very broad topics. First try to determine a scope. If
you are new to either open source or DFIR start we recommend to small, you and extend the scope at
any point in time.

Some questions that could help in determining a scope to start with:

* Any specific topics?
* Any specific technologies?
* Any tools/projects that you frequently use? What helps if you have ideas on how to improve these
  tools.

### Specific topics or technologies

What helps is to find a topic or technology that you are passionate about, find interesting, or
that is beneficial to your day-to-day work.

Consider:

* writing a [Forensics Wiki article](https://forensics.wiki/community/)
* writing a [blog post](https://osdfir.blogspot.com/)
* disussing it on [Open Source DFIR slack](https://github.com/open-source-dfir/slack)

### Tools/projects that you frequently use

* First learn as much as you can about the technologies the tools/project uses
* Learn about the development and/or maintenance processes of a project
* Learn about the contributors and/or community guidelines of a project
* Learn about the open source licenses and/or agreements a project uses and if you are able to
  contribute
* Reach out to the project maintainers to see what good starter projects are. It take a while to
  get to learn a code base.

## Second determine how you want to contribute

### Contribution by programming/software development

Programming and/or developing software you learn best by doing.

* **Start with small issues:** Look for issues labeled "good first issue" or "help wanted" to get
  familiar with the codebase.
* **Fix bugs or add features:** Help maintainers by resolving open bug reports or writing new
  parsers, plugins, or carvers.
* **Observe AI and coding agent constraints:** If you use coding agents to help write patches, tune
  down the output verbosity, rigidly follow project style guides, and double-check any speculations
  or claims made in your code descriptions.
* **Respect forensic integrity:** Ensure code modifications preserve forensic reproducibility and
  evaluate whether performance optimizations introduce adverse effects to data extraction accuracy.

### Contribution by testing

Tools cannot be trusted in investigations without rigorous validation.

* **Validate tool output:** Test tools against known public datasets or corpora (like CFReDS) and
  report any parsing inconsistencies, temporal errors, or data overflows.
* **Create synthetic test fixtures:** Contribute sanitized, safely licensed mock disk images,
  Windows Registry hives, or PCAP files to help maintainers run robust continuous integration (CI)
  tests.
* **Test across environments:** Run the software on different host operating systems (Windows,
  Linux, macOS) or unique edge-case setups and report compatibility bugs.
* **Submit factual bug reports:** When reporting bugs or vulnerabilities, keep your reports
  objective and backed strictly by evidence; avoid speculating about the hypothetical worst-case or
  theoretical business impact.

### Contribution by research

Forensic tools constantly lag behind new operating system artifacts and threat actor techniques.

* **Analyze new artifacts:** Research undocumented Windows Registry keys, log formats, or
  application behaviors and share your findings.
* **Create mapping rules:** Write or update detection signatures, such as YARA rules, Sigma rules,
  or SQL queries for forensic search engines.
* **Reverse engineer malware:** Provide the community with detailed technical breakdowns of
  emerging malware behaviors that tools will need to parse.

### Contribution by documentation

Good code is useless if an investigator cannot figure out how to use it under pressure.

* **Improve user guides:** Write clear installation steps, command-line usage examples, and
  troubleshooting guides.
* **Document forensic edge cases:** Write documentation explaining how a tool interprets complex or
  ambiguous timeline entries.
* **Translate material:** Help internationalize the tool by translating documentation or localized
  strings into other languages to support investigators worldwide.

### Contribution by supporting other users

A strong community takes the burden off a handful of core maintainers.

* **Answer community questions:** Monitor the project's GitHub Issues, Discussions, or Slack
  channels to help triage problems for other users.
* **Share use cases:** Write up walkthroughs or case studies showcasing how you successfully
  leveraged the tool in an investigation.
* **Review community pull requests:** Help maintainers review code or documentation submissions
  from other contributors to ensure they meet project standards.
