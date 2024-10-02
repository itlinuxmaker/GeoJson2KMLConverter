# GeoJson2KML Converter

GeoJson2KML Converter is a Python script that can be used to convert GeoJSON files - especially those exported from Google Maps - into KML format. The KML data is split from the raw data of the Google Maps timeline into individual files in order to filter certain time periods. These KML files are specially prepared for use in Google Earth and are also used to back up your own timeline on local systems. In this way, the data in the Google Maps account can be regularly deleted if you first organize regular downloads of the JSON files via "https://takeout.google.com/". This way, the timeline is always backed up, even if it is regularly deleted.

## Installation and Requirements on Linux
#### 1. Requirements

Make sure that the following requirements are met on your system.
* Python 3.x is installed. Check this with the command:
```bash    
python3 --version
```
If Python is not installed, you can install it on a Debian-based system (such as Ubuntu) using the following command:
```bash
sudo apt update
sudo apt install python3 python3-pip
```
* **pip** (Python package manager) must be installed:
```bash  
sudo apt install python3-pip  
```
* **Virtual environment** (optional but recommended): To have a clean and isolated environment for your project, set up a virtual environment:
```bash  
sudo apt install python3-venv  
```
#### 2. Clone project repository
Clone the project from GitHub to your system:
```bash  
git clone https://github.com/itlinuxmaker/GeoJson2KMLConverter.git
cd GeoJson2KMLConverter  
```
#### 3. Set up virtual environment (optional, but recommended)
Create and activate a virtual environment:
```bash  
python3 -m venv venv
source venv/bin/activate  
```
#### 4. Install dependencies
Install the necessary Python packages. If there is a requirements.txt, use this command:
```python  
pip install -r requirements.txt  
```
With these steps you can install and use GeoJson2KML Converter on a Linux system.

## Installation and requirements on Windows
#### 1. Prerequisites

* Python 3.x is installed. You can check this by opening the command line (CMD) and entering the following command:
```bash  
python --version
```
If Python is not installed, you can download and install it from the official website: https://www.python.org/downloads/. Make sure to enable the "Add Python to PATH" option during installation.

* **pip** (Python package manager) should already be installed with Python. Check this with:  
```bash  
pip --version
```
#### 2. Download project from GitHub

Copy the repository from GitHub. You can either install Git and clone the repository, or download the ZIP archive directly from GitHub:

* **Method 1: Clone repository** (if Git is installed):
	* Install Git from https://git-scm.com/
	* Open the command line and enter the following command:
	```bash  
	git clone https://github.com/itlinuxmaker/GeoJson2KMLConverter.git  
	cd GeoJson2KMLConverter  
	```
* **Method 2: Download ZIP archive:**
	* Go to https://github.com/itlinuxmaker/GeoJson2KMLConverter and click the "Code" button, then select "Download ZIP".
	* 	Extract the archive to a desired location on your computer.
#### 3. Set up a virtual environment (optional but recommended)

It is recommended to use a virtual environment to install the dependencies in an isolated environment.
1. Open the command line and navigate to the project directory:  
```bash  
cd Path\to\GeoJson2KMLConverter  
```
2. Create a virtual environment:
```bash  
python3 -m venv venv  
```
3. Activate the virtual environment:
```bash  
source venv\Scripts\activate  
```
You should see that your prompt now starts with (venv), indicating that the virtual environment is active.
#### 4. Install dependencies
Once the virtual environment is enabled (or without a virtual environment), install the required Python dependencies using pip:
```bash  
pip install -r requirements.txt  
```

This guide will help you install and use the GeoJson2KML Converter on Windows. The steps to set up the virtual environment are optional but helpful to create an isolated environment for your project.

## Utilization
1. After you have downloaded the product **"Maps - your settings and personal places in Maps"** (only this product, no others!) to your computer via Google Takeout as a ZIP or TAR.GZ archive, unpack the archive.
Then change to the directory in which the year folders (e.g. 2023, 2024) are located. By default, this directory is located in the path:
```bash
Takeout/Location History (Timeline)/Semantic Location History  
```
Alternatively, you can copy or move the year folders to another location and navigate to that directory.

2. Start the script:

*    For Linux/macOS:
```Bash
python3 /path/to/your/geoJson2Kml.py
```
* For Windows:
```Bash
python \path\to\your\geoJson2Kml.py      
```
3. Inputs:

    Enter the start date and end date in the format YYYY-MM-DD.
Choose whether you also want to add the routes (lines).

#### Output
The script creates a KML file in the current directory. The file name contains the start and end date of the period. 
  
  This allows you to optimally and individually save your timelines from Google Maps on your own storage media and display them in external tools.