
# Demo 1: Virtual Environments (week 2)

---

One of your labmates has shared a script with you, [`analyze.py`](./analyze.py).
Figure out how to run this script on your own machine.


**_Change to working directory for remainder of demo:_**

```shell
cd lectures/week02-reproducible-research-fundamentals
```


## Examine base environment

See what is in your base environment:

```shell
python --version
```
#### Output:

```text
Python 3.12.12
```

### Try to run the script:

```shell
python analyze.py
```

#### Output:

```text
Error: This script requires Python 3.13+.
No module named 'pandas'
Command 'which samtools' returned non-zero exit status 1.
Missing dependencies
```

## Create virtual environment

We will create a virtual environment with the following packages:

+ __python__ Need at least version 3.13
+ __pandas__ A python package for dataframes
+ __samtools__ A suite of CLI programs (written in C) for interacting with high-throughput sequencing data

```shell
mamba create -n week2-demo-1 python=3.13 pandas=2.2.3 bioconda::samtools
```
<details>
<summary>Top 7 Mamba Commands</summary>

### 📦 Top 7 Mamba Commands

#### Environments

```mamba create -n <myenv> python=3.10```

Creates a new isolated environment.

```mamba activate <myenv>```

Activates your specified environment.

```mamba info --envs```

List the environments mamba knows about

```mamba env remove -n <myenv>```

Remove an environment

#### Packages

```mamba install package_name```

Installs packages into your active environment.

```mamba search package_name```

Searches the repositories for available packages.

```mamba update --all```

Updates all packages in the current environment.

</details>

## Activate the environment

```shell
conda activate week2-demo-1
```

## Run the script

```shell
python analyze.py
```

#### Output:

```text
3.13.15 | packaged by conda-forge | (main, Aug 10 2026, 13:01:04) [Clang 19.1.7 ]

... [see full output below] ...

All dependencies installed!
```

<details>
<summary>Full Output</summary>

```text
3.13.15 | packaged by conda-forge | (main, Aug 10 2026, 13:01:04) [Clang 19.1.7 ]
pandas dataframe:
  Greeting Target
0    Hello  World
1  Bonjour  Monde
2     Hola  Mundo

samtools output:

Program: samtools (Tools for alignments in the SAM format)
Version: 1.24 (using htslib 1.24)

Usage:   samtools <command> [options]

Commands:
  -- Indexing
     dict           create a sequence dictionary file
     faidx          index/extract FASTA
     fqidx          index/extract FASTQ
     index          index alignment

  -- Editing
     calmd          recalculate MD/NM tags and '=' bases
     fixmate        fix mate information
     reheader       replace BAM header
     targetcut      cut fosmid regions (for fosmid pool only)
     addreplacerg   adds or replaces RG tags
     markdup        mark duplicates
     ampliconclip   clip oligos from the end of reads

  -- File operations
     collate        shuffle and group alignments by name
     cat            concatenate BAMs
     consensus      produce a consensus Pileup/FASTA/FASTQ
     merge          merge sorted alignments
     mpileup        multi-way pileup
     sort           sort alignment file
     split          splits a file by read group
     quickcheck     quickly check if SAM/BAM/CRAM file appears intact
     fastq          converts a BAM to a FASTQ
     fasta          converts a BAM to a FASTA
     import         Converts FASTA or FASTQ files to SAM/BAM/CRAM
     reference      Generates a reference from aligned data
     reset          Reverts aligner changes in reads

  -- Statistics
     bedcov         read depth per BED region
     coverage       alignment depth and percent coverage
     depth          compute the depth
     flagstat       simple stats
     idxstats       BAM index stats
     cram-size      list CRAM Content-ID and Data-Series sizes
     phase          phase heterozygotes
     stats          generate stats (former bamcheck)
     ampliconstats  generate amplicon specific stats
     checksum       produce order-agnostic checksums of sequence content

  -- Viewing
     flags          explain BAM flags
     head           header viewer
     tview          text alignment viewer
     view           SAM<->BAM<->CRAM conversion
     depad          convert padded BAM to unpadded BAM
     samples        list the samples in a set of SAM/BAM/CRAM files

  -- Misc
     help [cmd]     display this help message or help for [cmd]
     version        detailed version information



All dependencies installed!
```
</details>

## Export the environment

```shell
conda env export --from-history | grep -v '^prefix' > live-demo1.yml
```

