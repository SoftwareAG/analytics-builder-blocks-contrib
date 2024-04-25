# analytics-builder-blocks-contrib
This repository contains non-productized blocks for Apaam Analytics Builder that have been contributed by the community.

## Installation
To add these blocks to a tenant, you will require:

* A copy of the [block-sdk](https://github.com/SoftwareAG/apama-analytics-builder-block-sdk) github repo
* A local install of Apama - from either the SoftwareAG suite installer or [Community edition - full version](http://www.apamacommunity.com/downloads/).
* A Cumulocity IoT tenant with a suitable apama-ctrl microservice subscribed (custom blocks are not supported with apama-ctrl-starter).

Installation Steps:

```
. $SAG_INSTALL/Apama/bin/apama_env
git clone https://github.com/SoftwareAG/apama-analytics-builder-block-sdk.git
git clone https://github.com/SoftwareAG/analytics-builder-blocks-contrib.git
./apama-analytics-builder-block-sdk/analytics_builder build extension \
      --input analytics-builder-blocks-contrib/blocks/  --name contrib-blocks\
      --cumulocity_url https://$TENANT/ \
      --username $USERNAME --password $PASSWORD --restart
```



## Licensing

This project is licensed under the Apache 2.0 license - see <https://www.apache.org/licenses/LICENSE-2.0>

______________________
These tools are provided as-is and without warranty or support. They do not constitute part of the Software AG product suite. Users are free to use, fork and modify them, subject to the license agreement. While Software AG welcomes contributions, we cannot guarantee to include every contribution in the master project.

Contact us at [TECHcommunity](mailto:technologycommunity@softwareag.com?subject=Github/SoftwareAG) if you have any questions.
______________________

