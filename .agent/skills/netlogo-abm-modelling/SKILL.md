---
name: netlogo-abm-modeling
description: Generates, optimizes, and documents NetLogo 7 Agent-Based Models (ABMs). Use when a user asks to "build a NetLogo model," "optimize NetLogo code," or "write an ODD protocol." Do NOT use for other agent-based frameworks like Mesa or Repast.
metadata:
version: 0.2.0
tags: \[netlogo, abm, odd-protocol, simulation, netlogo-7\]
---

# **NetLogo Agent-Based Modeling Skill**

Follow these steps and guidelines when assisting with NetLogo 7 model development, optimization, or documentation.

## **Workflow Steps**

When a user requests a new NetLogo model or module, execute the following steps:

1. **Analyze the Requirements:** Identify the core research question, agents (turtles/patches/links), and environmental scale.
2. **Draft the ODD Protocol:** Outline the Overview, Design concepts, and Details (ODD) to establish scientific rigor. Format the ODD directly in the NetLogo Info Tab using Markdown.1 For highly complex models, utilize nested ODDs for submodels.2
3. **Establish Enterprise Folder Structure:** Propose a standard directory layout: /data/ for inputs, /src/ for external scripts, /models/ for the main .nlogox and .nls files, /docs/, and /experiments/ for BehaviorSpace setups.
4. **Scaffold the Code:** Write the initialization (setup) and execution (go) procedures. Adhere to Lisp-derived orthography by using kebab-case for identifiers and terminating boolean variables with a question mark. Always declare both plural and singular forms for breed definitions.3
5. **Optimize the Code:** Review the logic to ensure high computational efficiency using the NetLogo Profiler and optimize spatial queries.4

## **uardrails**

- **Do not** write monolithic go procedures. Break agent behaviors into distinct sub-procedures, strictly using nouns for reporters and verbs for commands.5
- **Do not** use \= to assign values to variables; strictly use the set command.6
- **Do not** use strings evaluated via run for dynamic execution. Strictly utilize anonymous procedures (lambdas) denoted by the \-\> operator for reliable scoping and performance.7
- **Do not** assign stationary state variables to turtles; use patches-own for environmental factors.
- **Do not** invent NetLogo primitives. Strictly adhere to the official NetLogo 7 Dictionary syntax.

## **If/Then Rules**

Apply these decision logic rules to optimize and structure code:

- **If** the codebase exceeds 500 lines or involves highly distinct components, **Then** use the \_\_includes \["file.nls"\] primitive to modularize the code into separate files.3
- **If** you need to filter agents based on both spatial proximity and a property condition, **Then** strictly invoke the in-radius primitive _before_ applying the property filter (e.g., patches in-radius 3 with \[pcolor \= green\]) to leverage spatial hashing.
- **If** a complex query or calculation is used multiple times in a procedure to produce the same subset of agents, **Then** calculate it once and cache it using let.4
- **If** integrating the model into a continuous integration (CI) pipeline, **Then** utilize GitHub Actions like LogoActions (check-netlogo) to automatically verify that BehaviorSpace experiments run without errors.

## **Resource Links**

Reference the following locations for model validation and code snippets (assume paths relative to project root or web sources):

- **Local Data:** /data/ for GIS (.shp) or CSV initialization files.
- **Documentation:** Info tab in the .nlogox file.
- **External Snippets:** Search the _NetLogo Models Library_, _CoMSES Net_, or _Modeling Commons_ for peer-reviewed agent logic.
