# Hub9 AI Customer Support & Package Sorting

This repository contains two distinct components:
1. `app.py`: A Streamlit-based customer support agent that leverages the OpenAI API to answer questions about Hub9 AI's automation agents, using a predefined dataset.
2. `task.c++`: A C++ program that categorizes packages based on their dimensions and mass.

## Overview
1. app.py
  - Purpose:
      Provides an interactive web interface for answering customer queries about Hub9 AI's agents.
  - Functionality:
      - Uses Streamlit to create the UI.
      - Calls the OpenAI API to generate responses based on a predefined JSON dataset included in the system message.
      - Supports case-insensitive queries, ensuring that inputs like "how does the phil work?" are correctly handled.

2. task.c++
  - Purpose:
      Categorizes packages into three types: "REJECTED", "SPECIAL", or "STANDARD" based on their dimensions (width, height, length) and mass.
  - Functionality:
      - Computes the volume of the package.
      - Uses specific conditions to determine the appropriate category:
        - A package is considered bulky if its volume (Width × Height × Length) is greater than or equal to 1,000,000 cm³ or if any of its dimensions (width, height, or length) is greater than or equal to 150 cm.
        - A package is considered heavy if its mass is greater than or equal to 20 kg.
        - Must dispatch the packages into the following stacks:
            - STANDARD: Standard packages (those that are neither bulky nor heavy) can be handled normally.
            - SPECIAL: Packages that are either bulky or heavy (but not both) require special handling.
            - REJECTED: Packages that are both bulky and heavy are rejected and cannot be processed.
