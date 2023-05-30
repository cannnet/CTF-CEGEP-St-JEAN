# Challenge Description
The Guess2 challenge requires participants to leverage the reverse engineering tool Ghidra to analyze the provided C program and find a way to retrieve the flag stored within the application, rather than solely focusing on guessing the secret number.

## Approach
To solve the Guess2 challenge, I followed these steps using the Ghidra reverse engineering tool:

1- Loaded the provided C program into Ghidra and performed a thorough analysis of its code and functionalities.
2- Examined the decompiled code to identify any references to the flag or mechanisms that would allow me to retrieve it.
3- Leveraged Ghidra's powerful analysis capabilities to identify a specific code section responsible for displaying the flag.
4- Once the memory address of the flag was identified, I developed a custom script or utilized Ghidra's scripting features to directly read and retrieve the flag value from memory.

## Findings and Solutions
By reverse engineering the provided C program using Ghidra and leveraging its scripting capabilities, I managed to retrieve the flag embedded within the application without relying solely on guessing the secret number.
