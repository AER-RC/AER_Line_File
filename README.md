# AER_Line_File

The AER Line File starts with HITRAN parameters, then modifies them with observed parameters (e.g., through radiation closure studies). It is publicly available on [on Zenodo](https://zenodo.org/record/3837550). This repository does **not** contain this database, because it is a very large set of files. Rather, we provide a simple script that leverages the [Zenodo Python API](https://pypi.org/project/zenodo-get/) to download the file. While the user is free to download the Line File on their own, this repository will also serve as reference, since it will contain documentation in this README and in the [Wiki Pages](https://github.com/AER-RC/AER_Line_File/wiki).

# Cloning the Repository

Cloning of this repository can be done with a simple:

```
git clone git@github.com:AER-RC/AER_Line_File.git
```

The repository is downloaded into a subdirectory called `AER_Line_File` in the working directory of the user.

# Dependencies

Before running the download script, the user will need to install the Zenodo Python API, which can be done with:

```
pip install -r requirements.txt
```

# Downloading and Staging the Line File

Assuming the user has `cd`'d into `AER_Line_File`, they can download and untar the AER Line File package with:

```
./get_line_file.py
```
