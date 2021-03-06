# Copyright (C) 2013  The Debsources developers <info@sources.debian.net>.
# See the AUTHORS file at the top-level directory of this distribution and at
# https://anonscm.debian.org/gitweb/?p=qa/debsources.git;a=blob;f=AUTHORS;hb=HEAD
#
# This file is part of Debsources. Debsources is free software: you can
# redistribute it and/or modify it under the terms of the GNU Affero General
# Public License as published by the Free Software Foundation, either version 3
# of the License, or (at your option) any later version.  For more information
# see the COPYING file at the top-level directory of this distribution and at
# https://anonscm.debian.org/gitweb/?p=qa/debsources.git;a=blob;f=COPYING;hb=HEAD


class InvalidPackageOrVersionError(ValueError):
    """The package or the version doesn't exist in the DB"""
    pass


class FileOrFolderNotFound(Exception):
    """The Folder or File doesn't exist in the disk"""
    pass


class Http500Error(Exception):
    pass


class Http404Error(Exception):
    pass


class Http404ErrorSuggestions(Http404Error):
    def __init__(self, package, version, path):
        self.package = package
        self.version = version
        self.path = path
        super(Http404ErrorSuggestions, self).__init__()


class Http403Error(Exception):
    pass
