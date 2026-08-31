
# Demo 2: Virtual Environments (week 2)

**_Make sure you are in the correct directory:_**

```shell
cd lectures/week02-reproducible-research-fundamentals
```


## Dockerfile

The [Dockerfile](./Dockerfile) contains the following lines:

```dockerfile
FROM condaforge/miniforge3
WORKDIR /workspace
COPY live-demo1.yml environment.yml
COPY analyze.py .
RUN mamba env create -f environment.yml
```

+ Start with known base image [Base images](https://docs.docker.com/build/building/base-images/)
+ Set the working directory
+ Copy files into the image
  + In general: `COPY [src] [dest]`
  + Rename `live-demo1.yml` to `environment.yml`
  + `COPY . .` will copy all the files in the current directory
+ Create the environment using `RUN`
  + The miniforge3 image will already have `mamba`

### Optional: How to activate your environment by default?

<details>
<summary>Answer</summary>

Add the following line after `RUN`. This sets the path and activates the environment:

```dockerfile
ENV PATH=/opt/conda/envs/week2-demo-1/bin:$PATH
```

</details>

## docker build

Create a Docker image from a Dockerfile

```shell
docker build -t live-demo1 .   
```

<details>
<summary>Output</summary>

```text
[+] Building 9.6s (10/10) FINISHED                                                                                                                                                                                                           docker:orbstack
 => [internal] load build definition from Dockerfile                                                                                                                                                                                                    0.0s
 => => transferring dockerfile: 179B                                                                                                                                                                                                                    0.0s 
 => [internal] load metadata for docker.io/condaforge/miniforge3:latest                                                                                                                                                                                 0.1s 
 => [internal] load .dockerignore                                                                                                                                                                                                                       0.0s 
 => => transferring context: 2B                                                                                                                                                                                                                         0.0s 
 => [1/5] FROM docker.io/condaforge/miniforge3:latest@sha256:c7af1b9e9a2877b1aa7604fd250f8ad311876f6f0f52849acbff0a7011508eb7                                                                                                                           0.0s 
 => [internal] load build context                                                                                                                                                                                                                       0.0s 
 => => transferring context: 1.19kB                                                                                                                                                                                                                     0.0s 
 => CACHED [2/5] WORKDIR /workspace                                                                                                                                                                                                                     0.0s 
 => CACHED [3/5] COPY live-demo1.yml environment.yml                                                                                                                                                                                                    0.0s 
 => [4/5] COPY analyze.py .                                                                                                                                                                                                                             0.0s 
 => [5/5] RUN mamba env create -f environment.yml                                                                                                                                                                                                       7.2s 
 => exporting to image                                                                                                                                                                                                                                  2.2s 
 => => exporting layers                                                                                                                                                                                                                                 2.2s 
 => => writing image sha256:e9d9bd05ef3955acf2f2d3e4ae76cb70e3acf8c0fce869a267c5409d3424dfe7                                                                                                                                                            0.0s 
 => => naming to docker.io/library/live-demo1
```
</details>

## docker run

Use `docker run` to run commands inside the image

```shell
docker run --help
```

### Usage:

```text
Usage:  docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
```

### `OPTIONS`

+ `--rm` Automatically remove the container and its associated anonymous volumes when it exits
+ `-i, --interactive` Keep STDIN open even if not attached
+ `-t, --tty` Allocate a pseudo-TTY

### `IMAGE`

The name you gave in `docker build` (with option `-t`)

### `COMMAND`

The command(s) to run in the instance. Since we are trying to get a bash shell, this will be `/bin/bash`

### Full command:

```shell
docker run --rm -it live-demo1 /bin/bash
```

#### Result:

You should be dropped into a shell that is running within the image. Your prompt will change, something like:

```text
(base) root@76dbdffe1534:/workspace# 
```

This tells you that you are the `root` user, the "host" is a hash that will change in different sessions. 
You can also see that your current directory is `/workspace` and that you are using the `base` conda environment.

If you look around a bit using your linux commands (`ls`, `cd`, etc.), you will notice that
you are not in your local computer anymore - the files that are present are similar to what you might see
with a fresh install.

```shell
ls -la /   # list system root
ls /home   # list user homes
df -h      # list mounted filesystems
```


## Run analysis

Find the files we copied over in our Dockerfile:

```shell
ls
```

#### Output:

```text
analyze.py  environment.yml
```

Lets try running `analyze.py`:


```shell
python analyze.py
```

<details>
<summary>Result</summary>

What happened? I thought we created this image so we could run the analysis?

Our image begins with the miniforge3 image, so `conda` and `mamba` are installed,
and it creates the environment (`mamba env create -f environment.yml`).
But if we look back at demo1, we needed to activate the environment before 
using any of the dependencies.

</details>

First, lets check and see whether the conda environment was created:

```shell
conda info --envs
```

```text

# conda environments:
#
# * -> active
# + -> frozen
base                 *   /opt/conda
week2-demo-1             /opt/conda/envs/week2-demo-1

```

Great, we see that `week2-demo-1` was created.

### Activate the environment

```shell
conda activate week2-demo-1
```

Notice the change in your prompt.


### Run the script

```shell
python analyze.py
```

#### Output:

```text
3.13.15 | packaged by conda-forge | (main, Aug 10 2026, 13:04:21) [GCC 14.4.0]

... [see full output below] ...

All dependencies installed!
```

<details>
<summary>Full Output</summary>

```text
3.13.15 | packaged by conda-forge | (main, Aug 10 2026, 13:04:21) [GCC 14.4.0]
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



