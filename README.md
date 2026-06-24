# The Geological Survey of South Australia (GSSA) SARIG Catalogue CSW

## Repository scope

This repository contains user-facing examples for the SARIG catalogue:

- `/home/runner/work/SARIG-Catalogue-CSW/SARIG-Catalogue-CSW/README.md`
- `/home/runner/work/SARIG-Catalogue-CSW/SARIG-Catalogue-CSW/Access SARIG CSW from Notebook.ipynb`
- `/home/runner/work/SARIG-Catalogue-CSW/SARIG-Catalogue-CSW/Search and Download CSW Data Example.ipynb`
- `/home/runner/work/SARIG-Catalogue-CSW/SARIG-Catalogue-CSW/Downloader Example for Professional User.py`

The examples cover two interfaces exposed by the SARIG catalogue:

- **OGC CSW** for catalogue metadata discovery
- **CKAN Action API** for package metadata and file-oriented workflows

## Verification status

- **Last reviewed:** 2026-06-24
- **Review scope:** in-repository fact check and context update across documentation, notebooks, and Python example code
- **Live endpoint verification:** not completed from this environment because `catalog.sarig.sa.gov.au` did not resolve during review
- **Current guidance:** treat exact service capabilities, limits, and availability as runtime-dependent; confirm them against the live endpoints before depending on them in production workflows

## CSW information

### What is CSW?

CSW is an Open Geospatial Consortium (OGC) standard that defines a common interface to discover, browse, and query metadata about geospatial data and services.

In simpler terms, it is a way to search for information about maps, datasets, and other geospatial resources. Geological surveys use CSW to publish metadata describing data such as maps, reports, and borehole information.

### Key concepts

- **Metadata:** data about data, such as title, description, extent, and keywords
- **OGC standards:** common standards that support interoperability between clients and servers
- **Core requests:** `GetCapabilities`, `DescribeRecord`, `GetDomain`, `GetRecords`, `GetRecordById`, `GetRepositoryItem`

## How to use the SARIG catalogue services

### CSW endpoint

- Base endpoint: `https://catalog.sarig.sa.gov.au/csw`
- Example stable capabilities request: `https://catalog.sarig.sa.gov.au/csw?service=CSW&request=GetCapabilities&version=2.0.2`
- Repository examples treat **CSW 2.0.2** as the default request version
- Any **CSW 3.0.0** references in this repository should be treated as evaluation or testing context unless re-verified

CSW responses are XML documents. If you call `GetCapabilities` or `GetDomain` from Python, handle the response as XML text or parse it with an XML library instead of expecting JSON.

### CKAN Action API endpoints

- Base endpoint: `https://catalog.sarig.sa.gov.au/api/3/action/`
- `package_search`: search package metadata
- `package_show`: retrieve one package and its resources
- `package_list`: list package identifiers
- `status_show`: retrieve CKAN instance status
- `recently_changed_packages_activity_list`: retrieve recent package activity metadata

The repository examples now use `/api/3/action/` consistently.

## Included examples

### `/home/runner/work/SARIG-Catalogue-CSW/SARIG-Catalogue-CSW/Access SARIG CSW from Notebook.ipynb`

Notebook examples for:

- retrieving CSW capabilities
- retrieving CSW domain values
- understanding CSW use cases

### `/home/runner/work/SARIG-Catalogue-CSW/SARIG-Catalogue-CSW/Search and Download CSW Data Example.ipynb`

Notebook examples for:

- searching CSW records with OWSLib
- searching CKAN packages by name
- retrieving package metadata and downloading a resource URL from `package_show`

### `/home/runner/work/SARIG-Catalogue-CSW/SARIG-Catalogue-CSW/Downloader Example for Professional User.py`

Python example for downloading **recent package activity metadata** from the CKAN Action API into CSV format.

## Requirements

Install the packages required by the examples you want to run:

- `owslib` for CSW notebook examples
- `requests` for HTTP requests
- `pandas` for CSV export in the downloader script

Example install command:

```bash
pip install owslib requests pandas
```

## Usage notes

1. Clone this repository.
2. Open the notebook or Python file you want to run.
3. Confirm the service endpoint and request version you intend to use.
4. Run the example.
5. If the live service behavior differs from the example assumptions, update the example before using it in an automated workflow.

## Fact-check notes applied in this update

- Removed stale operational notes about UAT links and temporary robots-based restrictions.
- Standardised CKAN examples on `/api/3/action/`.
- Clarified that CSW examples return XML, not JSON.
- Aligned download examples with CKAN `package_show` resource handling.
- Removed hard-coded capability constraints that were not re-verified against a live `GetCapabilities` response during this review.

## Re-validation checklist

Before future releases or example updates, re-check:

1. CSW base endpoint availability
2. Supported CSW versions and any production/testing distinction
3. `GetCapabilities` response structure and constraint values
4. CKAN Action API base path and action names
5. Example package identifiers such as `mesac12583` and `2018d036642`
6. Expected response shapes for `package_search`, `package_show`, and recent activity endpoints
7. Any network, authentication, proxy, or TLS assumptions documented in example code

## License

This repository content is described as Creative Commons Attribution 4.0 International (CC BY 4.0). Use the canonical license text here:

- <https://creativecommons.org/licenses/by/4.0/>

## Contacts

**South Australian Resource Information Gateway Team**

The Geological Survey of South Australia (GSSA)  
The Department for Energy and Mining (DEM)

Head office  
Level 4, 11 Waymouth Street  
Adelaide, South Australia 5000

<Dem.sarig@sa.gov.au>
