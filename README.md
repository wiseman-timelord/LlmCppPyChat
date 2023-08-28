# Llama2Robot
Status: Beta, Currently upgrading, Prompt and key, logic. The factors are...
1) Need to logically analyze, "summarize" and "consolidate", functions in "model.py".
2) Need to implement, "Instruct" model for text processing and "Chat" model for chatting to the user, intended currently for '2 x 7b' models, essentially tuned for their tasks, has got to be faster, but may also possibly be better overall, than using 1 x llama2 13b chat model for both tasks. 
* It is hard to find the Llama2 8bit instruct uncensored GGML, literally files disappear infront of my face on huggingface. will be using the "Llama-2-7B-GGML" censored version for now, however, this 32k instruct version could be epic later on when there is, file reading or websearch, code. will have to, test and compare, "32k instruct" and "and 8k instruct", the 32k one could wildly hallucinate for all I know.
* auto-model-detection feature would be a bit iffy, as most of the llama 2 instruct models do not have "instruct" written on them, however, all instruct models are named llama-2 models that but not have chat in the filename. so its doable.
* we will be only testing with 8 bit version of the GGML models
 
### GPT4 DESCRIPTION:
Llama2Robot uses the Llama 2 language model for conversation and YAML files for state management. The main.py script is the entry point and orchestrates the flow, calling functions from interface.py for UI, model.py for model interactions, and utility.py for utility functions like YAML operations and response shifting. The program is designed to be interactive, allowing users to chat with the model in real-time.

### HUMAN DESCRIPTION:
This is a, Llama 2 language model and llama-cpp, based chatbot framework, it uses, python scripts and prompts and a '.yaml', to produce context aware conversations. Producing a framework for creation of other future Llama 2 based projects such as, personal managers or automated agent, this is intended to be through forks. You have an idea for a fork, then create a fork, you may inadvertantly, inspire my own creations or save me some time. Llama2Robot uses ".yaml" files, so the Llama 2 model should be more than compitent at the task of, reading and creating, multi-line output to be used in forks for other purposes, such as complex, commands and operations.

### FUTURE PLANS:
1) Implement 2 models, 1 for text processing "Llama-2-7B-32K-Instruct-GGML" and 1 for chat "llama2_7b_chat_uncensored-GGML". 
1) Get scripts working 100% as intended, currently there are some, response parsing and pompt logic, issues.
2) implement optimizations for each
3 Implement  a --logs switch to enable printout of complete, input and output, during the session to file "debug.log", that are cleared on run.
4) Implement text to speach utilizing built in OS simulated voice for current response from model, in both, linux and windows, 
4) size of Llama 2 GGML based models, eg, 7b, 13b, 30b, 70b, etc.
5) Consider tuning temperatures.
6) Multi-model support, so as, to be using, faster model for simpler things and larger model for complex things,
7) At the time of writing the developers of Llama 2 are still holding back the 30b, so at some point later will have to test it works.
8) Implement "llama-cpp-python", thus enabling ClBlas through option in "Install.bat", to install brand specific version of Blas.
9) Introduce more critical fork shared theme features, but stop somewhere before it becomes significantly customised.
10) develop interface, possibly progress to multi-panel, will have to re-visit limitations on WSL with, curses or tkinter, even consider webserver. 

### FEATURES:
* Dynamic Model Initialization, seamlessly initializes the Llama language model with optimal thread settings.
* Interactive User Loop, features a continuous loop for real-time user interaction.
* Intelligent Response Generation, utilizes predefined prompts to generate contextually relevant and coherent responses.
* YAML State Management, manages session state, user preferences, and more through YAML file operations.
* User-Friendly Chat Interface, offers a clean and intuitive chat interface, complete with ASCII art and dialogue history.
* Customizable Model Selection, allows users to select from a list of available Llama 2 models in "./models".


### INTERFACE:
Interface is under development...
```
=======================================================================================
                                    Dialogue Display
=======================================================================================
 Human
---------------------------------------------------------------------------------------
Hello Llama, I am having a productive day, I am upgrading my python scripts.


=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
 Llama
---------------------------------------------------------------------------------------
Human, please elaborate on your statement. What exactly is it that you are upgrading? Do you require any assistance from me?


=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
 History:
---------------------------------------------------------------------------------------
Empty
The session history is now: Empty. Recent conversation between, Llama and Human, is:
Llama said, "Please elaborate on your statement. What exactly are you upgrading? Do you require any assistance from me?"
Human replied, "I am upgrading my computer system to improve its performance."
The session history now reads as follows: Empty. Recent conversation between Llama and Human is:
Llama said, "Please elaborate on your statement. What exactly are you upgrading? Do you require any assistance from me?"
Human replied, "I am upgrading my computer system to improve its performance."
The session history now reads as follows: Empty. Recent conversation between Llama and Human is:
Llama said, "Please elaborate on your statement. What exactly are you upgrading? Do you require any assistance from me?"
Human Human, please elaborate on your statement. What exactly is it that you are upgrading? Do you require any assistance from me? Hello Llama, I am having a productive day, I am upgrading my python scripts.


=======================================================================================
You:
```
```
=======================================================================================
                                    Model Selection
=======================================================================================

                 1. llama2_13b_chat_uncensored.ggmlv3.q8_0.bin
                 2. llama2_7b_chat_uncensored.ggmlv3.q4_0.bin
                 3. llama2_7b_chat_uncensored.ggmlv3.q8_0.bin
                 4. None
                 5. None
                 6. None
                 7. None
                 8. None
                 9. None

---------------------------------------------------------------------------------------

 Select a model from 1-9: 2

 Loading model, be patient...
llama.cpp: loading model from ./models/llama2_7b_chat_uncensored.ggmlv3.q4_0.bin
llama_model_load_internal: format     = ggjt v3 (latest)
llama_model_load_internal: n_vocab    = 32000
llama_model_load_internal: n_ctx      = 4096
llama_model_load_internal: n_embd     = 4096
llama_model_load_internal: n_mult     = 256
llama_model_load_internal: n_head     = 32
llama_model_load_internal: n_layer    = 32
llama_model_load_internal: n_rot      = 128
llama_model_load_internal: ftype      = 2 (mostly Q4_0)
llama_model_load_internal: n_ff       = 11008
llama_model_load_internal: n_parts    = 1
llama_model_load_internal: model size = 7B
llama_model_load_internal: ggml ctx size =    0.07 MB
llama_model_load_internal: mem required  = 5407.71 MB (+ 1026.00 MB per state)

```
### USAGE: (including linux)
1) Download the package, extract somewhere on drive, to its own folder, then open folder in, explorer on Admin account or shell with Admin rights.
2) Download models such as "https://huggingface.co/TheBloke/llama2_7b_chat_uncensored-GGML". (note: proposed instruct model for later implementation "https://huggingface.co/TheBloke/Llama-2-7B-32K-Instruct-GGML").
3) For Windows users, install requirements by double clicking `WinInstall.bat` or run `wsl pip install -r requirements.txt`. (For Linux users run `pip install -r requirements.txt`.)
4) Copy Llama 2 GGML bsed model with the "*.bin" extention into the "models" folder, eg `llama2_7b_chat_uncensored.ggmlv3.q4_0.bin`, the required "config.json" is already present.)
5) For Windows users, double click the `Llama2Robot.bat` or run `wsl python3 main.py`. ( For Linux users, run `python3 main.py` and ensure to use 85 columns for the window ) .

### REQUIREMENTS:
Windows with WSL (later also linux)

### NOTES:
* This program is designed to be run on Windows/WSL/Python, it will not work in Windows/Python without WSL, this is because of the use of, `jaxlib` and `jax[cpu]`. 

### DISCLAIMER:
* This program is in no way affiliated with the Llama 2 developers, it merely is a Chatbot that runs through the use of Llama 2 GGML based. models. The Llama 2 model has been chosen because it is the only local language model that has been reviewed on YouTube to my knowing at the time of, inception and creation, that are able to correctly write a ".json" file, if this were the case with MPT, it would be called MPTRobot. 
