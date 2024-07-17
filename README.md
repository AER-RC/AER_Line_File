# AER_Line_File

The AER Line File starts with HITRAN parameters, then modifies them with observed parameters (e.g., through radiation closure studies). It is publicly available on [on Zenodo](https://zenodo.org/record/5120012). This repository does **not** contain this database, because it is a very large set of files. Rather, we provide a simple script that leverages the [Zenodo Python API](https://pypi.org/project/zenodo-get/) to download the file. While the user is free to download the Line File on their own, this repository will also serve as reference, since it will contain documentation in this README and in the [Wiki Pages](https://github.com/AER-RC/AER_Line_File/wiki).

[LBLRTM](https://github.com/AER-RC/LBLRTM) uses the line parameters and [MT_CKD continuum](https://github.com/AER-RC/MT_CKD) in its calculations. The models and data are thus linked. For the latest release, the relationships are:

| LBLRTM Release | MT_CKD Release | Line File |
| :---: | :---: | :---: |
| [v12.11](https://github.com/AER-RC/LBLRTM/releases/tag/v12.17) | [v4.3](https://github.com/AER-RC/MT_CKD/releases/tag/v4.3) | [v3.8.1](https://zenodo.org/record/5120012/files/aer_v_3.8.1.tar.gz?download=1) |

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

Note that we install `v1.3.0` of the package, which was released in February 2020. The code in this repository is currently incompatible with `v1.3.2`.

# Downloading and Staging the Line File

Assuming the user has `cd`'d into `AER_Line_File`, they can download and untar the AER Line File package with:

```
./get_line_file.py
```

Currently, the tarball is downloaded as `aer_v_3.8.1.tar.gz`, extracted, then renamed `AER_Line_File`. Under this directory is the familiar directory structure:

```
% ls AER_Line_File/
extra_brd_params        RELEASE_NOTES_aer_linefile  xs_files
line_file               spd_dep
line_files_By_Molecule  spectral_lines_for_MonoRTM
```

Users will likely want to use `AER_Line_File/line_file/aer_v_?.?` with [LNFL](https://github.com/AER-RC/LNFL).
