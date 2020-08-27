#!/usr/bin/env python

import os

class lineFile():
  def __init__(self, inArgs):
    """
    `get_line_file.py -h`
    """

    self.linesDir = inArgs['lines_path']
    self.pathStr = ['tape1_path', 'tape2_path', 'extra_params', \
      'xs_path', 'fscdxs']
    self.zRecID = inArgs['record_id']
  # end constructor

  def checkLineFile(self):
    """
    Check if line file dataset from Zenodo needs to be downloaded
    """

    # do we need to dowload the Line File Parameter Database?
    self.lfpdDL = True

    # it is assumed that if AER_Line_File exists, that everything
    # that is needed is underneath the directory
    if os.path.exists(self.modelDir):
      self.lfpdDL = False
      return
    # endif modelDir

    print('Generating list of Zenodo URLs')
    wgetList = 'line_file_list.txt'
    sub.call([self.zGet, str(self.zRecID), '-w', wgetList])
    files = open(wgetList).read().splitlines()

    # we archive a tarball and a license, just need tarball
    for file in files:
      base = os.path.basename(file)
      if '.tar.gz' not in base: continue
      if os.path.exists(base): self.lfpdDL = False
      self.tarBall = base

      # AER convention is that the tarball is just the line file
      # directory name with ".tar.gz" appended
      self.tarDir = base[:-7]
    # end file loop
  # end checkLineFile()

  def getLineFile(self):
    """
    Retrieve line file dataset from Zenodo, extract archive, then
    stage files as expected by LNFL and LBLRTM
    """

    import tarfile
    from zenodo_get.__main__ import zenodo_get as zget

    # what can be downloaded? should just be a tarball and license
    arcList = 'zenodo_archive_list.txt'
    zget([str(self.zRecID), '-w', arcList])
    files = open(arcList).read().splitlines()
    for file in files:
      base = os.path.basename(file)
      if '.tar.gz' not in base: continue
      if os.path.exists(base): self.lfpdDL = False
      self.tarBall = base

      # AER convention is that the tarball is just the line file
      # directory name with ".tar.gz" appended
      self.tarDir = base[:-7]
    # end file loop

    zget([str(self.zRecID)])

    if not os.path.exists(self.linesDir):
      if not os.path.exists(self.tarDir):
        # don't untar if it's not needed
        print('Extracting {}'.format(self.tarBall))
        with tarfile.open(self.tarBall) as tar: tar.extractall()
      # endif tar
      os.rename(self.tarDir, self.linesDir)
    else:
      print('{} already exists, using its Line File contents'.
        format(self.modelDir))
    # endif modelDir
  # end getLineFile()
# end lineFile class

if __name__ == '__main__':
  import argparse

  parser = argparse.ArgumentParser(\
    formatter_class=argparse.ArgumentDefaultsHelpFormatter, \
    description='Build LBLRTM and LNFL executables for usage in ' + \
    'e.g., ABSCO_config.ini and ABSCO_compute.py.')
  parser.add_argument('-lines', '--lines_path', \
    default='AER_Line_File', help='Top-level path of AER line file.')
  parser.add_argument('-record', '--record_id', type=int, \
    default=3837550, help='Zenodo record ID for the line file.')
  args = parser.parse_args()

  subObj = lineFile(vars(args))
  subObj.getLineFile()
# end main()
