# Uploading New Line File to Zenodo

Since DOIs are associated with each record and version, some caution needs to be taken when updating the Line File dataset in the Zenodo repository. Once versions are published, one cannot remove, add, or modify any of the files -- **Zenodo Publications are permanent**. Users should ensure that only the necessary files -- `aer_v_*.*` and `LICENSE` are in a release on Zenodo. If we keep just adding the new releases (in tarball form), the repository will become unnecessarily large since previous releases are preserved in their respective versions.

Additionally, two versions of a Zenodo record cannot have the exact same file upload names. This means that no two versions of the AER Line File can have an, e.g., `aer_v_3.7` file and a `LICENSE` file, even if the content of each is different.

`LICENSE` should not need to be edited more than once a year, and the only edit should be the copyright year.

For users new to Zenodo, it is recommended that "practice runs" of releasing new versions be first performed in the [AER Line File Sandbox](https://sandbox.zenodo.org/record/667626). If everything looks OK, they can proceed to the [official Zenodo release](https://zenodo.org/record/4019086). Note that if newer versions for the links provided exist, a banner at the top of the Zenodo page will notify the user of where to go. The steps for releasing a new version are:

1. Follow the link to either the Sandbox or official repository
2. Click on the green "New version" button
3. *Delete* the tarball for the previous release (e.g., `aer_v_3.7.tar.gz`)
4. Click on "Choose files" and select the new release (e.g., `aer_v_3.8.tar.gz`)
5. Click on green "Start upload" button
6. Scroll down to the "Basic Information" section and edit the "Version" field (to, e.g., `v3.8`); "Publication Date" and "Authors" and any other fields can also be edited as necessary
7. Scroll back to the top of the page and ensure file uploads are complete, then click "Save", then the blue "Publish" buttons
8. Change any references to the previous releases (e.g., "https://zenodo.org/record/4019086" or "https://zenodo.org/record/4019086/files/aer_v_3.8.tar.gz?download=1") in the following documents:
   - https://github.com/AER-RC/AER_Line_File/blob/master/README.md
   - https://github.com/AER-RC/AER_Line_File/wiki
   - https://github.com/AER-RC/LBLRTM/blob/master/README.md
   - https://github.com/AER-RC/LBLRTM/wiki
   - https://github.com/AER-RC/MT_CKD/blob/master/README.md
   - https://github.com/AER-RC/cross-sections
