<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
<div align="center">
  
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Twitter][twitter-shield]][twitter-url] 

</div>

<h3 align="center">eBay Price Checker</h3>

  <p align="center">
    Quickly check the median recent sale price of any number of items on eBay in the country you specify.
    <br />
    <br />
    <a href="https://github.com/keatonrproud/eBay_price_check/issues">Report Bug</a>
    ·
    <a href="https://github.com/keatonrproud/eBay_price_check/issues">Request Feature</a>
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
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a small tool I use to review prices of items sold through eBay in the last few days. You can price estimates of items before buying or selling them yourself.


### Built With

[![Python][python-shield]][python-url]
[![Selenium][selenium-shield]][selenium-url]
[![PyCharm][pycharm-shield]][pycharm-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Clone the repo, install the required scripts, and get to price checking:

1) View the sample_output file to see what your output will look like.
2) Replace the items in search_list.csv with your own eBay searches. The more specific your search, the more accurately the price will reflect your search.
3) Run the script and view your median search prices in the new output.

### Prerequisites

You'll need to install [selenium][selenium-url], [chromedriver-autoinstaller](https://github.com/yeongbin-jo/python-chromedriver-autoinstaller), and [Google Chrome](https://www.google.com/chrome/) to get going with the script.

The chromedriver version should automatically update based on your version of Chrome. If you have issues with the script, it would be worth ensuring your version of Chrome matches the chromedriver installed locally.


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/keatonrproud/eBay_price_check.git
   ```
2. Install any missing packages
   ```sh
   pip install missing_package
   ```
3. Ensure you have Google Chrome installed

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

If you have a suggestion, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". All feedback is appreciated!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Selenium Docs](https://www.selenium.dev/documentation/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Keaton Proud - [Twitter](https://twitter.com/keatonrproud) - [LinkedIn](https://linkedin.com/in/keatonrproud)- keatonrproud@gmail.com

Project Link: [https://github.com/keatonrproud/eBay_price_check](https://github.com/keatonrproud/eBay_price_check)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/keatonrproud/eBay_price_check.svg?style=for-the-badge
[contributors-url]: https://github.com/keatonrproud/eBay_price_check/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/keatonrproud/eBay_price_check.svg?style=for-the-badge
[forks-url]: https://github.com/keatonrproud/eBay_price_check/network/members
[stars-shield]: https://img.shields.io/github/stars/keatonrproud/eBay_price_check.svg?style=for-the-badge
[stars-url]: https://github.com/keatonrproud/eBay_price_check/stargazers
[issues-shield]: https://img.shields.io/github/issues/keatonrproud/eBay_price_check.svg?style=for-the-badge
[issues-url]: https://github.com/keatonrproud/eBay_price_check/issues
[license-shield]: https://img.shields.io/github/license/keatonrproud/eBay_price_check.svg?style=for-the-badge
[license-url]: https://github.com/keatonrproud/eBay_price_check/blob/main/license
[linkedin-shield]: https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin-url]: https://linkedin.com/in/keatonrproud
[twitter-shield]: https://img.shields.io/badge/Twitter-%231DA1F2.svg?style=for-the-badge&logo=Twitter&logoColor=white
[twitter-url]: https://twitter.com/keatonrproud
[python-shield]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[python-url]: https://python.org/
[selenium-shield]: https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white
[selenium-url]: https://www.selenium.dev/
[pycharm-shield]: https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green
[pycharm-url]: [https://jupyter.org/](https://www.jetbrains.com/pycharm/)
