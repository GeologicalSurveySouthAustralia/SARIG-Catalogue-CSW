# (Draft Under review Nov 2024) GSSA SARIG Catalogue CSW

## NEW SARIG catalogue and CSW API
The SARIG Catalogue is a comprehensive online resource providing access to a vast collection of the Department for Energy and Mining (DEM) publications. This platform enables users to efficiently search and discover relevant departmental publications, mineral exploration company reports, and data sets. By leveraging advanced search functionality, users can refine their queries based on keywords, geographic location, time period, and data type. The SARIG Catalogue adheres to OGC standard protocols, ensuring seamless interaction between users and the system.

For those who want to use APIs to fetch data in one space, we offer customised Python notebooks and Python files. These files are available on this page, in the files listed above.

# ( Draft Oct 2024) SARIG Catalogue CSW URL
- CSW v2.0.2:  https://catalog.uat.sarig.sa.gov.au/csw?Request=GetCapabilities&service=CSW&version=2.0.2&
- CSW v3.0.0:  https://catalog.uat.sarig.sa.gov.au/csw?Request=GetCapabilities&service=CSW&version=3.0.0&
- URL links to capabilities document for a Catalogue Service for the Web (CSW), which is a standard for exposing a catalogue of geospatial records in XML.

## ( Draft Oct 2024) CKAN API endpoint query examples
### 1. Package Search by Organisation
- **URL**: [Package Search by Organisation](https://catalog.uat.sarig.sa.gov.au/api/action/package_search?fq=organization:department-for-energy-and-mining)
- **Description**: This endpoint searches for datasets within the "department-for-energy-and-mining" organisation.

### 2. Package Search by Name
- **URL**: [Package Search by Name](https://catalog.uat.sarig.sa.gov.au/api/action/package_search?fq=name:mesac12583)
- **Description**: This endpoint searches for a specific dataset by its name, in this case, "mesac12583".

### 3. Package List
- **URL**: [Package List](https://catalog.uat.sarig.sa.gov.au/api/action/package_list)
- **Description**: This endpoint retrieves a list of all available datasets.

### 4. Recently Changed Packages Activity List
- **URL**: [Recently Changed Packages Activity List](https://catalog.uat.sarig.sa.gov.au/api/3/action/recently_changed_packages_activity_list)
- **Description**: This endpoint provides a list of recently changed datasets, showing the latest updates and modifications.

### 5. Status Show
- **URL**: [Status Show](https://catalog.uat.sarig.sa.gov.au/api/3/action/status_show)
- **Description**: This endpoint returns the current status of the CKAN instance, including information about the system's health and configuration.


> **Note:** This is the test link for catalogue, pleaase delete "uat." on hiperlink if it has already go alive.


## ( Draft Oct 2024) What is new?  
The SARIG Catalogue CSW has undergone significant enhancements to improve user experience and accessibility. CSW now supports both 2.0.2 and 3.0.0 versions of the OGC CSW (Catalogue Service for the Web) standard protocol. Benefits: 
- **Interoperability**: Ensures seamless operation between different systems by adhering to the same protocol.
- **Metadata Discovery**: Simplifies the process of discovering relevant geospatial datasets and services.
- **Standardisation**: Part of the suite of OGC standards promoting consistency and compatibility in the geospatial domain.

![image](https://github.com/user-attachments/assets/46fdafec-c626-4bc7-a106-8621755a5ed1)
> **Note:** Functions disabled temporarily <https://catalog.uat.sarig.sa.gov.au/robots.txt>, please use browser before CSW activated. 


### Key Features
- **Metadata Querying**: Users are allowed to query metadata based on various criteria such as keywords, spatial extent, temporal coverage, and data format.
- **Standardised Interface**: Follows a standardised interface for consistent communication between clients (such as web applications) and servers (where metadata is stored). Users can find links to other OGC protocols (such as WMS, WFS) to view and download the actual geospatial data.

### Operations
- **Operations**: GetCapabilities, DescribeRecord, GetDomain, GetRecords, GetRecordById, GetRepositoryItem
- **Service and Version**: CSW 2.0.2, 3.0.0
- **Constraints**: MaxRecordDefault: 10, PostEncoding: XML, SOAP, XPathQueryables: allowed
- **Id Capabilities**: EID, FID

## How to execute API requests with Python?
- An API call consists of three components: the API endpoint, the requested action, and any filters applied to the returned data.
- To get started, please refer to the Jupyter notebook provided below.
- You can use the notebook at this link:  <https://github.com/GeologicalSurveySouthAustralia/SARIG-Catalogue-CSW/blob/194f46b18ea6665695522dd1600d4b3eb894b6dc/Access%20SARIG%20CSW%20from%20Notebook.ipynb>
- You can run this python script: <https://github.com/GeologicalSurveySouthAustralia/SARIG-Catalogue-CSW/blob/main/Downloader%20Example%20for%20Professional%20User.py>


## Requirements

To run this notebook, you need to have the following Python packages installed:

- `owslib`: For interacting with OGC web services, including CSW.
- `requests`: For making HTTP requests.
- `pandas`: For data manipulation and analysis.
- `numpy`: For numerical operations.

You can install these packages using pip:
````python
!pip install owslib requests pandas numpy
````

## Usage

1. **Clone the Repository**: Download or clone the repository containing the notebook to your local machine.
   ```bash
   git clone <https://github.com/GeologicalSurveySouthAustralia/SARIG-Catalogue-CSW>
2. **Open the Notebook** : Launch Jupyter Notebook and open the SARIG_CSW_Notebook.ipynb file.
3. **Run Notebook on terminal** :jupyter notebook SARIG_CSW_Notebook.ipynb
4. **Configure the CSW Server URL**: In the notebook, specify the URL of the SARIG CSW server.
5. **Run the Notebook Cells**: Execute the cells in the notebook to connect to the SARIG CSW server, perform queries, and handle the results.

## Frequent Asked Question for CSW

### 1. What are the changes in the updated SARIG catalogue?
The updated SARIG catalogue now includes additional keywords related to various fields such as geosciences, earth sciences, geology, mining, and archaeology. It supports both 2.0.2 and 3.0.0 versions of the OGC CSW standard protocol and provides a direct link to the Department for Energy and Mining website. Moreover, it specifies that there are no access constraints.

### 2. Where can I access the updated SARIG catalogue?
You can access the updated SARIG catalogue through the following link: 
(NEW SARIG catalogue)

### 3. What are the benefits of using OGC CSW?
OGC CSW ensures interoperability between different systems, simplifies metadata discovery processes in the geospatial domain.

### 4. What are the key features of the updated SARIG catalogue?
The updated SARIG catalogue allows users to query metadata based on various criteria such as keywords, spatial extent, temporal coverage, and data format. It also follows a standardised interface for consistent communication between clients and servers.

### 5. What operations can I perform with SARIG catalogue CSW?
You can perform operations such as GetCapabilities, DescribeRecord, GetDomain, GetRecords, GetRecordById, and GetRepositoryItem.

### 6. What are the constraints associated with SARIG catalogue CSW?
The constraints include MaxRecordDefault set to 10, PostEncoding options of XML and SOAP, and XPathQueryables allowed.

### 7. What scalar capabilities does SARIG catalogue CSW offer?
SARIG catalogue offers logical and comparison operators, as well as arithmetic functions for filtering.

### 8. What are the ID capabilities of SARIG catalogue CSW?
SARIG catalogue supports EID (Entity Identifier) and FID (Feature Identifier) for identification purposes.


## License
This code repository's content are licensed under the [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/), the deed of which is stored in this repository here: [LICENSE](LICENSE).


## Contacts
**South Australian Resource Information Gateway Team**,

The Geological Survey of South Australia (GSSA),

The Department for Energy and Mining (DEM)

Head office
Level 4, 11 Waymouth Street, 
Adelaide, South Australia 5000

<Dem.sarig@sa.gov.au>

