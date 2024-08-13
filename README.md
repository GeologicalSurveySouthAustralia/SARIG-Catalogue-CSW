# Draft GSSA SARIG catalogue

## NEW SARIG catalogue and CSW API, JULY 2024
The Geological Survey of South Australia’s SA Geodata database (the back end to SARIG: https://map.sarig.sa.gov.au/) is the primary repository for geoscientific information in South Australia. SARIG now has the opportunity to release a range of reports that were previously embargoed to the public. The SARIG Catalogue is a comprehensive online resource providing access to a vast collection of the Department for Energy and Mining (DEM) publications. This platform enables users to efficiently search and discover relevant departmental publications, mineral exploration company reports, and data sets. By leveraging advanced search functionality, users can refine their queries based on keywords, geographic location, time period, and data type. The SARIG Catalogue adheres to OGC standard protocols, ensuring seamless interaction between users and the system.

For those who want to access and download all reports in one space, we offer a customised Python script and the required accompanying CSV file. These two files are available on this page, in the files listed above.

## UAT links for NEW SARIG catalogue
https://catalog.uat.sarig.sa.gov.au/
- https://catalog.uat.sarig.sa.gov.au/csw?Request=GetCapabilities&service=CSW&version=2.0.2&
- https://catalog.uat.sarig.sa.gov.au/api/3/action/status_show

> **Note:** This is the UAT link for catalogue, pleaase delete "uat." on hoperlink if it has already go alive.


## What is new?  
The SARIG Catalogue has undergone significant enhancements to improve user experience and accessibility. The traditional envelope system has been removed, allowing users to directly select and add desired documents to a virtual cart. Please note that there may be limitations on cart size, which will be clearly indicated. Importantly, the catalogue has transitioned to Persistent Identifier (PID) URLs, replacing previous links. As a result, existing links will no longer function. Users are advised to update their bookmarks and references accordingly. 


## Frequent Asked Question for SARIG catalogue

### Can I preview the contents of a document or zip file before I download?
Yes, you can. If a record contains downloadable documents or zip files, clicking on the file name will open a new window with an embedded file viewer.

### How to search for my tenement?
*Instructions to be added.*

### How to search for report book?
Multiple data sets from 1892 are incorporated into the catalogue. However, data before 2000 may not be available in digital format due to the short timeline of data formats. GSSA runs legacy data programs to fill in gaps in data.

### How do I search for the latest publications?
You can filter by publication date on the filter panel.
### IMAGE
### IMAGE

### I would like to download all mineral company reports
Please refer to the link to our GitHub page for API connection details.

### What web browser should I use?
*Information to be added.*

### What tools/software are required to visualise data?
SARIG supports multiple file types that may require specialist software (GIS).

### How can I understand the new acronyms?
We include a table of old terms and new terms to explain new acronyms. Please refer to the "Voc prez / universal terms" section.

### What did Pre-Update SARIG Open Data and Product Catalogue provide?
SARIG Open Data and Product Catalogue is a platform that utilizes the metadata profile of ISO19115 to enable users to discover and query metadata related to South Australian resources. This includes links to associated resources like web services, maps, publications, or data downloads.

### What are the changes in the updated SARIG catalogue?
The updated SARIG catalogue now includes additional keywords related to various fields such as geosciences, earth sciences, geology, mining, and archaeology. It supports both 2.0.2 and 3.0.0 versions of the OGC CSW standard protocol and provides a direct link to the Department for Energy and Mining website. Moreover, it specifies that there are no access constraints.

### Where can I access the updated SARIG catalogue?
You can access the updated SARIG catalogue through the following link: 
(NEW SARIG catalogue)

### What are the benefits of using OGC CSW?
OGC CSW ensures interoperability between different systems, simplifies metadata discovery processes, and promotes standardization in the geospatial domain.

### What are the key features of the updated SARIG catalogue?
The updated SARIG catalogue allows users to query metadata based on various criteria such as keywords, spatial extent, temporal coverage, and data format. It also follows a standardized interface for consistent communication between clients and servers.

### What operations can I perform with SARIG catalogue?
You can perform operations such as GetCapabilities, DescribeRecord, GetDomain, GetRecords, GetRecordById, and GetRepositoryItem.

### What are the constraints associated with SARIG catalogue?
The constraints include MaxRecordDefault set to 10, PostEncoding options of XML and SOAP, and XPathQueryables allowed.

### What capabilities does SARIG catalogue offer?
In terms of spatial and scalar capabilities, SARIG catalogue offers various spatial operators and operands for filtering.

### What scalar capabilities does SARIG catalogue offer?
SARIG catalogue offers logical and comparison operators, as well as arithmetic functions for filtering.

### What are the Id capabilities of SARIG catalogue?
SARIG catalogue supports EID (Entity Identifier) and FID (Feature Identifier) for identification purposes.

### What query syntax can I use?
Catalog queries are based on Solr syntax to create complex search queries. Extensive resources can be found online.
