Pwgen RPM Spec
==============

Tested on
---------

* Sailfish OS SDK Beta 1502, Sailfish OS 1.1.2.16


Building the Source RPM
-----------------------

* Download the sources mentioned in `pwgen.spec` to your `SOURCES` directory
  (e.g. `~/rpmbuild/SOURCES`).
* Build the source RPM right under the `mersdk` account:

          rpmbuild -bs pwgen.spec

  Doing so with Scratchbox2 would result in *Bad owner/group* errors from
  `rpmbuild` because this environmnt has no account information for the user
  `mersdk`.


Building the RPM
----------------

* Build the RPM from the source RPM using Scratchbox2:

          sb2 rpmbuild --rebuild ~/rpmbuild/SRPMS/pwgen-VERSION-RELEASE.src.rpm
