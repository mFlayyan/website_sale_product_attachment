Technotrading Odoo 9.0 code
===========================

When migrating, respect the following rules:

- migrate in order of dependencies
- where not already done, create new modules with `ttr_` as prefix for the core module this module modifies: When adapting stuff for product, create a module called ``ttr_product``
- before migrating anything, comment all includes and imports, this makes it simpler to migrate file per file
- before migrating anything, move files around to conform the [OCA directory structure](https://github.com/OCA/maintainer-tools/blob/master/CONTRIBUTING.md#directories) and file names
- while migrating, migrate to the v8 api and follow the [OCA coding style](https://github.com/OCA/maintainer-tools/blob/master/CONTRIBUTING.md#python)
- don't migrate blindly. Always think back if there's already a module doing what's done there or similar, and rather use those when available
- adapt license headers to match the [OCA default](https://github.com/OCA/maintainer-tools/blob/master/template/module/__init__.py#L1), but also include existing copyrights if applicable
- if not technically impossible, create one MR per module
