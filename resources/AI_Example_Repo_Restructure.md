# Restructuring a Git Repository Directory

[https://gemini.google.com/app/d7feb68fe234cf31](https://gemini.google.com/app/d7feb68fe234cf31)

> ### User prompt: 
> I created this repository, but the instructor wants the directory structure to look like this 
> (refer to https://github.com/gwcbi/applied-computing-HDS/blob/main/labs/lab1-reproducible-setup/README.md). 
> Explain how I can get my local copy of the repo to look like this and give me the commands to run in my terminal 
> to have this directory structure.

### Response:

To restructure your local repository so that all the main contents are grouped cleanly inside a repro-demo subfolder—matching the standard layout from the [applied-computing-HDS repository](https://github.com/gwcbi/applied-computing-HDS/blob/main/labs/lab1-reproducible-setup/README.md)—you will need to move patients.csv and any hidden/configuration files into repro-demo using Git tracking so your project history stays intact.

### Steps to Reorganize the Directory

**1. Navigate to Repository Root**

Terminal

Open your terminal and change directory into your local hds-practical repository folder.

`cd path/to/hds-practical`

*Verification:* Run pwd to ensure you are at the root of the hds-practical directory.

**2. Move Files into repro-demo**

Git File Operation

Move tracked files like patients.csv into the existing repro-demo subfolder using git mv.

`git mv patients.csv repro-demo/`

*Verification:* Run ls \-la repro-demo/ to confirm patients.csv is now inside repro-demo.

**3. Handle Hidden or Untracked Files**

Optional File Movement

If you have top-level configuration files (like .gitignore or Docker files) that need to live inside repro-demo according to your lab specification, move them as well:

`git mv .gitignore repro-demo/ 2>/dev/null || mv .gitignore repro-demo/`

*Verification:* Run ls \-a repro-demo/ to ensure all necessary files are inside the folder.

**4. Commit and Push Changes**

Git Version Control

Stage, commit, and push your restructured directory layout to GitHub.

`git add .`  
`git commit -m "Restructure repository files into repro-demo folder"`  
`git push origin main`

*Verification:* Refresh your [sofiafeiranz/hds-practical repository page](https://github.com/sofiafeiranz/hds-practical) in the browser to verify the root only contains the required repro-demo folder (and root-level configuration files if required by your instructor).

---

> ### User prompt: 
> I don't actually want this to be structured like that repo, I want to have the directory structure described in the README.md.
>
> Tasks:
> - Read "https://github.com/gwcbi/applied-computing-HDS/blob/main/labs/lab1-reproducible-setup/README.md" The directory structure described in the README is my target.
> - Examine my repository. The required files are in the \`repro-demo\` subdirectory and further nested in \`conda-version\`, \`renv-version\`, and \`uv-version\` \- Assume I have this repo cloned locally at \`\~/Development/hds-practical\`. 
> - Give me the commands in one block that I could cut and paste in order to refactor my repository

### Response:

To move all your files out of the nested repro-demo directory and place them directly at the root level of your repository—matching the exact structure defined in your [README.md](https://github.com/sofiafeiranz/hds-practical/blob/main/repro-demo/README.md)—run the following commands in your terminal:

`cd ~/Development/hds-practical`

`# Move all files and subdirectories out of repro-demo into the root directory`  
`git mv repro-demo/* .`  
`git mv repro-demo/.* . 2>/dev/null || true`

`# Remove the now-empty repro-demo directory`  
`rmdir repro-demo`

`# Stage, commit, and push the changes to GitHub`  
`git add -A`  
`git commit -m "Refactor directory structure to match README layout at repo root"`  
`git push origin main`

**What this does:**

> * git mv moves tracked files (conda-version/, renv-version/, uv-version/, patients.csv, AI\_USAGE.md, README.md, etc.) directly into \~/Development/hds-practical/ so Git tracks the move as a file relocation rather than a deletion/re-addition.  
> * The hidden files move attempt ensures setup files like .gitignore are transferred cleanly to the root.  
> * rmdir repro-demo cleans up the empty folder once everything has been extracted.

---

