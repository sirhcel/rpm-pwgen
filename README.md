Pwgen RPM Spec
==============

Tested on
---------

* Sailfish OS SDK Beta 1502, Sailfish OS 1.1.2.16


Building the Source RPM
-----------------------

* Download the sources mentioned in `pwgen.spec` to your `SOURCES` directory
  (e.g. `~/rpmbuild/SOURCES`)
* Get account information on Mer build engine right (Sailfish OS SDK Beta 1502)
    * User *mersdk* (UID 1001, GID 100000) has no corresponding user
      information within the *SailfishOS-armv7hl* target environment
    * This results in *Bad owner/group* errors when attempting to build the
      source RPM
    * Group 100000 is already present for the target as *nemo*
    * Add user *mersdk* as

              mersdk:x:1001:100001::/home/nemo:/bin/bash

      to `/parentroot/srv/mer/targets/SailfishOS-armv7hl/etc/passwd`
* Run

          sb2 rpmbuild -bs pwgen.spec

  to build the source RPM.


Building the RPM
----------------

* Build the RPM from the source RPM using

          sb2 rpmbuild --rebuild ~/rpmbuild/SRPMS/pwgen-VERSION-RELEASE.src.rpm
