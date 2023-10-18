<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">

 <a href="https://github.com/github_username/repo_name">
    <img src="/images/storm.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">California Weather Analysis</h3>

  <p align="center">
    Data infrastructure for analysis of California Weather
    <br />
    <a href="https://github.com/JackDoyleIRE/node-chat-app"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/JackDoyleIRE/node-chat-app">View Demo</a>
    ·
    <a href="https://github.com/JackDoyleIRE/node-chat-app/issues">Report Bug</a>
    ·
    <a href="https://github.com/JackDoyleIRE/node-chat-app/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

California has been experiencing some wild weather in 2023. The shift from extreme drought conditions with wildfires to extreme cold and massive storms and rainfall has seemed dramatic based on the news coverage. But how extreme has the recent weather actually been?

This project collects data from multiple Californian government online data sources. It then stores them in Google Big Query for multiple analysis use cases.

Check out how this code can be addapted to use Apache Airflow here:

https://github.com/JackDoyleIRE/airflow-pipelines

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
* ![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the app and how to install them (mac only).
* python
  ```sh
  brew install python
  ```

### Installation

2. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
3. Install anaconada
   ```sh
   brew install anaconda
   ```
4. Run the main current ulitiy file
   ```sh
   python utils/fetch_stations.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

App currently in development.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Grab the rainfall stations and rivers from 
    - [ ] Store the stations in a Big Query table
- [ ] Use the API to collect rainfall data for each station
    - [ ] Store in another Big Query table
- [ ] Create inital Tableau Public dashboard for trends
- [ ] Create a React dashboard to view the data

See the [open issues](https://github.com/JackDoyleIRE/cali-weather/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[product-screenshot]: public/images/screenshot.png




